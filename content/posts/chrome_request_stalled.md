---
title:  Chrome HTTP Request stuck in "Stalled" State
summary:  Chrome reports that a request is stuck in a "stalled" state and I try and figure out why
tags:  ["chrome" ,"iis", "investigation", "explanation"]
draft:  true
date: 2023-05-30T11:24:48.041-04:00
---


I got the chance to investigate a really odd bug where randomly network requests in Chrome would just hang. This would only occurr in our test environments at work and not in production. The request would hang for some long amount of time.. and then eventually complete successfully. The bug has been occurring for some time, but has been getting worse in Chrome. It got so bad that it was guaranteed that if you were using Chrome it was going to happen to you. Eventually it started happening in Firefox as well.. during an investor demo (what good is a demo if it doesn't go up in flames?). That's when I got roped in.

The first thing I did was attempt to replicate it and capture a `.har` file that I could share with anyone else that was interested. This part was easy - just popping open the network tab, navigating to the app on a test env, and then clicking every link that would trigger a network request. After about 30-40 seconds I had replicated the event

LINK TO TIMING WHERE IT SHOES THE QUEUE

So we can clearly see here that the request took 2 minutes and the entirety of that time the connection was stuck in the `stalled` state. That indicates one of two things:

1. Chrome never attempted to make the network request at all. Perhaps the priority on the request was dropped, maybe there were too many connections open to that FQDN already.&nbsp;

1. In some situations chrome actually merges the CORS preflight requests into what it reports as `stalled`. So it's possible that there was a problem in the preflight request that caused the delay before the actual request happened.

I did a bit more testing to figure out the scope of the issue. On/Off VPN with multiple browsers would all replicate the problem just fine. In this particular situation the fact that we could replicate it across EVERYTHING made it pretty clear that it was something related to our server.. but what? If the request never actually hits the server what could be going on?

### Chrome Network Log

One tool that chrome has to diagnose networking issues is hidden away at `chrome://net-export`. It generates a very VERY detailed log of everything network related that chrome is aware of.&nbsp;

IMAGE OF CHROME CAPTURE NETWORK LOG

I unchecked the `strip private information` option and told it to include cookies + credentials and started logging it to disk. Then I swapped back to my tab and replicated the issue. Waited a few seconds, and then went back and ended the captuer session.

Once you get that capture file, you have to head over to https://netlog-viewer.appspot.com and import it. There's a TON of information here, and honestly I didn't even look at half of it. The only two things I cared about were the "Events" and "Timeline" sections. The Timeline really makes no sense until you have a idea of when your actual network event happened, so we can skip that and jump right over to Events

There will likely be a lot of events. The "filter" at the top never worked for me given the sheer size of the events.. but scrolling through them all was just fine and eventually I found the URL request that caused the issue. If you click on the event it will display a bunch of debug information about the request.&nbsp;

IMAGE OF EVENT 169281

As you can see.. suddenly there's a HUGE jump in time from `66807` to `187631`. We've confirmed now that this is a problem that's occurring within the CORS preflight request specifically, and it's just getting rolled into the `stalled` state. The log viewer makes it trivial to dig down into the events and if you click on the details of the `HTTP_STREAM_JOB_CONTROLLER` event you can see some more details.&nbsp;

IMAGE OF EVENT 169283

Here again, we see that there is a definitely delay when it attempts to call `HTTP_STREAM_REQUEST_STARTED_JOB`&nbsp;

IMAGE OF EVENT 169284

And now we can easily see the problem: `SOCKET_POOL_STALLED_MAX_SOCKETS_PER_GROUP`

For some reason, the socket pool dedicated to this particular group (in this case grouped by FQDN) is filled up and so it can't actually make the next request. So it just sits there.. until suddenly a socket is available (2 minutes later) and it is able to complete the rest of the request as expected.

We can dig even further! Since we know that this is happening on an HTTP2 call, we can filter our events to only show us the http2 connections and that paints a more serious picture!&nbsp;

Every since one of our http2 sockets is getting set a `GOAWAY` frame by the server.. but notice that it says `NO_ERROR`. Some quick research shows us that this is actually part of the "graceful shutdown" strategy. The server tells the client to `GOAWAY` but there's `NO_ERROR`. This is the clients indication to wrap up its work because the server is going to officially disconnect soon. Except that final disconnect frame is never sent. So as far as chrome is concerned, we're still happily connected so it returns the connection to the pool. But the server has disconnected.












    