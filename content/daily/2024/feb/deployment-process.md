---
title: Streamlining my deployment process
tags:  ["daily"]
date: 2024-02-07T22:43:46.372-05:00
---


I've been hosting my website over on GH Pages for a long time now. Honestly I don't have too many problems with it or the process. But I was skeptical when I first started.. and as such I wanted to actually commit the build artifacts to a separate repo so that I could inspect them and not rely too much on GH Actions. I feel like I'm finally at the point where I'm ok with things so I took some time to rework my process a bit.

Now when I commit and push to github, I'm utilizing GitHub Actions to build and publish the build directly to GH Pages. Literally just lifted the configuration that [hugo publishes](https://gohugo.io/hosting-and-deployment/hosting-on-github/) because I didn't care to spend time figuring it out myself and did a bit of re-work on my repo.

I know eventually I'll have to change some of this as I'd like to add some more functionality to my site to support some [IndieWeb](https://indieweb.org) functionality like [WebMentions](https://www.w3.org/TR/webmention/). In order to do that I need to run various server components to be able to receive mentions and (Perhaps directly through Caddy) and serve up [WebFinger](https://webfinger.net/).






    