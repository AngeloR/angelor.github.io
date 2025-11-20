---
date: Wed, 13 Aug 2025 13:56:08 GMT
draft: false
medium_link: https://xangelo.medium.com/the-fallacies-of-management-the-network-is-reliable-89cd2c958f6c?source=rss-d5a790d38792------2
slug: the-fallacies-of-management--the-network-is-reliable
summary: 'Turns out management is closer to engineering than we let on'
title: The Fallacies of Management — The Network is Reliable
---

> Turns out management is closer to engineering than we let on.

For your entire IC career you’ll hear that management is not a “promotion” — it’s an entirely separate discipline. You’ll be told that the skills you learned as an engineer don’t translate well to being a manager and often are a hinderance.

This is only half of the truth.

The rest of it is that if you’re a truly good engineer, you don’t think in code — you think in systems. You understand that the feature you’re adding to your product is just one of many that need to interact with each other to produce something usable. This same skillset can help you if you find yourself in management — it can give you a firm base on which you can build.

Here’s a list of the fallacies of distributed computing that we’ll cover — each post will be about a different fallacy and, hopefully, help you connect what you know about distributed computing to people.

1. The Network is Reliable
2. Latency is Zero
3. Bandwidth is Infinite
4. The Network is Secure
5. Topology Doesn’t Change
6. There is One Administrator

### The Network is Reliable

Fallacy: Messages always get delivered

When you’re a new manager, you think communication is easy: People mostly want to do a good job, so you just need to say the thing and people will do the thing.

But somewhere between your all-hands presentation, your carefully worded Slack update, and the actual code shipped two weeks later… something got lost.

You thought the network was reliable.

In distributed systems the assumption is “messages always arrive”.

Managers often fall for the same trap. We say something in a meeting, or we write it in an email. We slack it. And we assume it was received, interpreted how we intended, and then acted upon in the expected manner.

In a distributed system, a message is a single structured payload comprising of explicit information. In management, that message is squishier. It’s actually two messages masquerading as one:

* The words you say
* The meaning that’s reconstructed

And they are almost never the same.

Not only is the network unreliable — but it turns out that in management, even if the message is received you can’t believe that it was received as intended.

You might say: “Let’s keep this sprint focused.”

One person hears: “No experiments allowed.”

Another hears: “Just don’t miss your estimates again.”

A third… doesn’t hear it at all. They’re still thinking about yesterday’s architecture review.

To borrow from Shannon’s information theory, a message is just noise until the receiver has the right *context* — the shared encoding and decoding protocol. In other words: people don’t understand what you say — they understand what they *think* you meant.

Being understood is not a matter of merely reproducing what someone else says, but of interpreting what is said in one’s own way.

This is the philosophical underpinning of hermeneutics, the study of interpretation. And it’s why repeating the same words rarely helps. If someone didn’t “get it” the first time, saying it again verbatim just gives them another chance to misinterpret it the same way — and enforce their alternative understanding.

Another way to think about this process is as follows:

* The words arrive
* Meaning is constructed by the individual
* There’s no guarantee that your intent survived

This means that a key component of effective management is repeating your idea with different words every time. In the same way that GPS requires multiple data satellite data points for triangulation, your ideas need multiple routes to your team.

In distributed systems you use retries, acknowledgements, and idempotency.

In teams you use 1:1s, Slack posts, Email Newsletters, and Town Halls. Each repitition is a new signal allowing your team to converge on your true intent.

This is all about redundancy and delivery in a high-failure network.

### The People Factor

Once you understand that your message is actually two parts, it turns out that as a manager the “second” part is most important and relevant to your work. The part about “meaning being constructed locally”

See that’s the crux of being a manager and what makes an organization so much more complicated than a distributed system.

Each person is the some of their experiences. Everyone had a different path to get to where they were right at this moment. Not just their lives, but in their day. Someone might be married. Someone might have just got a dog. Someone might have lost a loved one. Someone might have gotten into an argument.

All of these are pieces of the whole and are represented in the person at this moment — and they can change in the very next.

This is the context that they are using the decipher your messaging.

Did they have a less-than-stellar performance review? Well maybe your message is taken a bit more critically.

Was it a great one? Maybe they think the message isn’t for them.

When I was younger I used to work at a Milestones — a restaurant chain without a kids section on the menu. I worked in the kitchen and I spent my morning shifts doing prep work. My job was everything from making mashed potatoes for the lunch shift, to portioning pastas for the line cooks.

As part of prepping mashed potatoes, one of the first steps is cutting mashed potatoes.

Months into the role, I managed to cut my finger pretty badly. Enough to warrant heading to the hospital and filling out workplace safety documentation. It was no ones fault but my own, I knew better, but I still positioned my fingers incorrectly. The resulting blood loss was enough that, coupled with my relatively low blood pressure, I passed out.

The following week we had a “kitchen all hands” where we went over different new menu items and over issues that the head chef was seeing. There were also mini-tutorials on things… and one of the tutorials was on proper knife safety.

It was pretty pointedly at me, and deservedly so. Word of my misadventure had no doubt gotten out. Kitchens are tough environments socially — there was probably going to be some good-natured ribbing. And some bad natured ribbing too. I’d probably get some kind of nickname. I resolved to pay closer attention to the tutorial so this never happened again.

After the tutorial I think I made some kind of comment to the head chef about how I appreciated the tutorial and it wouldn’t happen again. I did feel a bit called out by it, but clearly there was a need.

She heard my words — and also understood the intent behind them.

She said “This tutorial isn’t because of what happened — you’re not that important. We need to go over this at least twice a year.”

The message I had heard was simple: You did it wrong, here’s the right way to do it. We’re going to cover it because there can’t be another mistake like this.

But it was wrong — I brought all of my insecurities and problems to interpreting what was actually going on.

Chef repeated the message and clarified: This is not about calling you out — this is about safety first.

See the only message there was “here is information about knife safety”.

I brought all of my context and interpreted it as “You are bad and you should feel bad. Now I have to do this tutorial for everyone.”

She repeated: “This is not about you, this is about knife safety”.

The second time around, it landed as intended.

### TL;DR:

In distributed systems, we assume messages might be lost — so we plan for retries and acknowledgements.

In management, assume the same. You’re not transmitting truth. You’re helping others rebuild it.

If it’s important, say it again. Say it differently. Say it until it’s reflected back to you in action.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=89cd2c958f6c)

---

This was originally published on Medium - https://xangelo.medium.com/the-fallacies-of-management-the-network-is-reliable-89cd2c958f6c?source=rss-d5a790d38792------2
