---
title: "Serverless with CloudFlare Workers"
Description: Building LootCap with CloudFlare Workers
date: 2020-05-07T17:31:57-04:00
draft: false
tags: ["architecture", "lootcap"]
---

## What is LootCap?

Last week we ([Adam Cochran](https://twitter.com/AdamScochran) and myself) launched [LootCap](https://lootcap.com). The goal is to provide tracking on a new class of tokens called [Loot](https://medium.com/@adamscochran/what-are-loot-tokens-understanding-an-emerging-asset-class-380b0cc38749). It's been a few years since I used to work at Vault of Satoshi and since that time I fell a bit out of Crypto Currencies. I always felt that most of the buzz around them was focused on the tech or the coin itself. It never provided any value. It felt like most coins out there were focused on trying to re-create the trajectory of Bitcoin rather than trying to DO anything. Ethereum was different. It was different enough to force me to pay attention. It allows you to run [Smart Contracts](https://github.com/ethereumbook/ethereumbook/blob/develop/07smart-contracts-solidity.asciidoc#what-is-a-smart-contract). In recent years you've likely seen "Tokens" suddenly gain popularity. Well those are primarily powered by Ethereum. Again, however, it felt like tokens were just trying to recreate the Bitcoin boom. 

Recently however, Loot tokens have become a thing. To condense Adam's [article](https://medium.com/@adamscochran/what-are-loot-tokens-understanding-an-emerging-asset-class-380b0cc38749) (which you should read if you're interested in this stuff) 

> Loot tokens are earned by contributing to communities.

What that means is, instead of you buying the token, the community you belong to gives you the token because your contributions to the community have some merit. It's a way to reward content creators for utilizing your community platform. 

When Adam first approached me about the idea for [LootCap](https://lootcap.com) I was on board - this was the first timssse I saw a use for Crypto that wasn't being sold as "Well it's crypto so it's just better!". My task was to build a simple Market Cap site targeting a select number of these tokens that actually qualify as "Loot".

## Planning

The first step in any project is to have a plan. This doesn't mean that I have some giant design document sitting on my computer, or is it scrawled on a napkit. It varies for every project. In this case, a markdown document with some relatively simple diagrams via mermaidjs was more than enough. In fact, the goal of the site could be expressed in a single sentence.

>  Display relevant market-cap information quickly to everyone

I'm also a firm believer in starting application development from the data side of things. The data is the only constant in your application. Everything is just abstracting away queries for your users to display the data in ways that make sense. So that's where I begin.

### Database Design

Whenever I start a project I do the same thing, from the technical side. 

1. What will be UI look like?
2. What data do I need to make this happen?
3. How do I store the data?

Weird right? The hard thing about database design, traditionally, is that the original wisdom is normalization. That is, data should be split apart into smaller isolated pieces. This idea is one that we use in software development all the time - Don't Repeat Yourself (DRY). By splitting the data into smaller units we're not storing more data than we need to store. When your databases start getting to the 10s of millions of rows storing unnecessary data can get expensive. Expensive because it's a lot of work to keep the same piece of data updated across different tables, but also expensive because storage is expensive.

I've always believed that the reason that normalization existed is two fold

1. Resources were expensive. Going from 8GB to 16GB HDDs were a huge financial leap. 
2. Development was segmented. DBAs worked in isolation, and often against, developers. 

As a database designer, you already know all the normalization rules. So take a look at how the application is being designed. What pieces if information are always shown together. What is important and what isn't? These questions can help you better shape your database design. 

With these things in mind, I took a look at my UI, drawing inspiration from the many market-cap sites devoted to crypto currencies. After all, while Tokens aren't Coins, they're treated quite similarly. This wasn't something I did in isolation - Adam has been a part of the crypto community for much longer than I have and I heavily relied on his expertise in defining what data we want to showcase.

Knowing what data I had to display for a first pass, and how my data was organized I opted to skip a database entirely. 

See it turns out I can assemble most of the information I need from various 3rd parties, cache it in memory, and when that cache expires, grab the information from the sources and assemble it again. 

This worked because the scope of the initial launch is small. I only need to display fairly static data (may change every few minutes) that's simultaneously general. I don't need real-time precision at the moment. This means that I had a lot more flexibility in my architecture design, but also it meant that apart from the cache load/reload events, serving this data would be as fast as I can possible make it.

### Application Architecture

#### API

When designing any application I always start with my API. It allows me to define my endpoints and figure out how I'm going to breaking up the data so that I can return the most relevant data for an endpoint. That is, now that I've broken down how I'm going to store my data, what's the best way to create my endpoints so that I have the flexibility to compose the UI that I have envisioned, but also allows me to change that front end as necessary. 

It's a tough nut to craft. If you pop open your console on [LootCap](https://lootcap.com) you'll see that we make requests to 2 different endpoints:

```
/api/v1/contracts/[contract-address]/price

/api/v1/coin/ethereum/price
```

For us, that's enough to render the entire first page and also preload some data so that if you click on any Token for more information, that data is already loaded and ready for you. I also made sure to version the end-points. The reason for this is to differentiate between deployment/releases. We can roll out new functionality to the API endpoints and test them to our hearts content before releasing front-end changes and deprecating the old API versions. We can also split test UI designs if we are interested in such a thing. Versioning your API endpoints is vital. 

In original dev versions, you could actually supply multiple contract addresses, comma separated, and it would return all the data at once. It was a way to reduce 7 or 8 calls to load the page into 2.

Obviously that's not what happened in production, but we'lll get to that later. 

#### Front end

The front-end for the app is actually just a SPA. We load some minimal HTML and dynamically populate the data as soon as we can. The idea behind this is that once we hit production, we can cache the static content for much longer periods of time improving response times which would help us achieve our original goal of Displaying relevant market-cap information quickly for everyone. 

We are using a two different 3rd party libraries on the front-end.

- Mvp.css - https://andybrewer.github.io/mvp/ - because we wanted a simple, classless, css framework as a base
- BigNumber - https://mikemcl.github.io/bignumber.js - because dealing with crypto numbers in JS can be challenging.

We aren't using React, and so for the times where we have to update the Dom we're using this function and interacting directly with the Element nodes.

```javascript
const $ = (selector, root) => {
    root = root || document;
    return root.querySelectorAll(selector);
}
```

We're also relying on `fetch` since all our endpoints are very simple `GET` based requests.

We are also using a very rudimentary SPA router that relies on css classes to define routes. We're only able to do this because we have 2 routes. 

```javascript
function route() {
    const routeTable = [
        {name: 'route-name', route: REGEX_MATCH, handler: fn}
    ];
    $('.route.active')[0].classList.remove('active');
    const requestedRoute = window.location.hash.split('#')[1] || '/';

    if(!routeTable.some(route => {
        if(route.route.test(requestedRoute)) {
            if(route.handler)
                route.handler(route.route.exec(requestedRoute));
            $(`#route-${route.name}`)[0].classList.add('active');
            return true;
        }
    })) {
        // clear the info page
        $('#route-info')[0].innerHTML = '';
        $('.route.default')[0].classList.add('active');
    }
}
```

## Going Live

### Heroku

Once I had a copy working locally it was time to deploy it. [Heroku](https://heroku.com) has long been my dpeloyment strategy of choice for projects that are undergoing rapid development. I always use git, but I don't always use a git hosting provider (GitLab/GitHub). Since heroku supports deploying from git, so I'm able to deploy from my dev env to share.

If you haven't had a chance to mess with Heroku for yourself, I high recommend you do. It's a wonderful service that allows you virtually unlimited free applications, and you can easily build your PoC without concern. 

They also offer numerous paid plans that you can use to take your service from PoC to live by clicking a few buttons. My initial thoughts on architecture were pretty standard. Perhaps two "dynos" or servers+load-balancer would be more than enough. We have no state, just in-mem caches, I don't care if the caches are repliced for eahc node. Base price like 20$ a month easy.

### Serverless?

However this is somethign we're launching for fun. While spending 20$ for infrastructure (bandwidth might cause some overage) is certainly doable.. is it the best option for us? 

For one thing, with any cloud provider, if I'm running a container or vm, I'm stuck to a paricular data-center. That's not very helpful if someone in Japan wants to take a look at my site. Remember, our goal was to provide this information quickly for everyone. 

So maybe we look at **SERVERLESS**

The idea behind server less infrastructure is simply: You write apps that are designed as "functions". These functions are deployed and spun up/down as necessary. Scale becomes pretty straight-forward. The infrastructure is available, it's just a matter of

- How much do you want to pay?
- What's the cold-start time on your app?

The payment is pretty straight foward. Since these serverless tends to be small apps that cater well to "bursty" applications in terms of requests, they tend to be cheaper to run. 

Most of these providers will take your app out of the pool if you don't get any requests for a preset amount of time. This is to free up compute space for other apps. The time to start for an app NOT currently pre-loaded is what's refered to as "cold start". That varies, mostly reliant on the size of the application you're starting, but there is a baseline cost regardless.

And of course, all "Serverless" is really server-based. They just abstract that away from you. That means I'm still on the hook for running these in multiple data centers around the world to hit my goals.

### CloudFlare Workers and KV

Then I ran across CloudFlare Workers. I remember seeing the announcement post some time back, and thought "hey that's neat" but quickly pushed it out of my mind. I returned to CloudFlare workers and did some more investigation. 

Oh My. I think CloudFlare Workers are the only TRUE serverless mechanism out there. 

CloudFlare workers are essentially serverless functions.. except they run at every CloudFlare Point-of-Presence (PoP). They have milliseconds of cold-start time, and they run globally. They do have way more restrictions than traditional serverless offerings

- 1MB compressed filesize
- 50ms CPU time
- max 30 workers
- < 50 subrequests per worker (redirects count!)

But I felt that if we COULD work within their limits, it would bring us closest to what we needed. They also offered an eventually consistent KV store that was accessible from the workers. Since our data was cached anyway, we didn't care about the eventual consistency - worst case we served stale data for a minute more than we expected.

After a couple of days of fiddling with their tooling and documentation, I was able to convert our regular API into a bunch of "serverless" functions that worked with the KV store and were deployed to all CloudFlare PoP. 

Today, when you load [LootCap](https://lootcap.com) you're loading data from 3 different workers

1. Two running API endpoints
2. 1 Running a static site
