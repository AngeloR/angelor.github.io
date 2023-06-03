---
title: "Running a Git Server"
date: 2022-03-30T11:08:53-04:00
draft: true
---

# Running your own Git server
Following this theme of owning your digital space I wanted to do a quick post on what it takes to run your own git server. There are a bunch of services out there like that will host your git repositories for free (I personally recommend [sourcehut](https://sourcehut.org/)), but you can get a most of what they offer for free with [gitweb](https://xangelo.ca/posts/gitweb/). 

## Why would you want to do this?
Honestly it's not as complicated as you would think to run your own git server and get almost all the same functionality from popular forges. Running your own git server doesn't mean you can't use something like GitHub or GitLab - it's not a one or the other choice. You can host all your repos on your own VPS while still pushing to GitHub/GitLab to ensure that you can still take advantage of their social networks.

For me the biggest precursor to hosting my own repos was just to get more familiar with git. I've been using git for a number of years, but it was only in the last year or so that I really started digging into all the functionality that it offers.

In addition to that there's a huge difference in complexity between running your own server, and running a service for millions of others to consume. As GitHub grows (both in size and in feature set) the likelihood of any one piece of it being down also grows. If we look at the [Incident History](https://www.githubstatus.com/history) of GitHub from Jan 2022  to March 2022 we can see that some piece of it has been dozens of incidents and outages. Using git allows you to bypass a lot of those problems, but centralizing on any hosted forge will always come with these inherent risks. It's much better to use hosted forges as secondary locations and just host your own git repos. 

## What do you need?
1. Server - You need somewhere to host your git server. Personally I use [Digital Ocean]() but you are free to use anything that gives you ssh access and an IP address.
1. You'll need root access to that server

That's it. Those are the minimum requirements to actually host your git repos elsewhere. Everything else on top of that is just extra functionality and we'll talk about those later.

### A Server
The easiest thing to do would be to spin up a brand new server on a cloud platform like [DigitalOcean](https://digitalocean.com). It costs approx 5$ CAD and is probably one of the cheaper shared hosts you can find. You don't need anything fancy because the git repos actually do nothing the majority of the time. There's only activity on them when you push/pull. 

If you spin up a droplet (server) in Digital Ocean it will provide you the ability to set up your root credentials. Personally I'd suggest using an SSH key! It's a heck of a lot easier than typing in your password every time you try and connect.

#### ssh-keygen
