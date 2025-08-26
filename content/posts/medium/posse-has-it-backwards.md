---
date: Mon, 21 Jul 2025 17:52:35 GMT
draft: false
medium_link: https://xangelo.medium.com/posse-has-it-backwards-ca9ab4d5b529?source=rss-d5a790d38792------2
slug: posse-has-it-backwards
summary: The Presentation of Self in Every Blog post
title: POSSE Has it Backwards
---

I’ve been blogging for a number of years now, even though my website makes it seem like I stopped. You can check the wayback machine and see posts from [2011](https://web.archive.org/web/20110507234835/http://xangelo.ca) before composer was a thing in the PHP world, or you can jump back to [2005](https://web.archive.org/web/20050415040309/http://www.xangelo.com/) when I was more focused on the design of the website than the content itself. I’ve tried almost every blogging platform out there, and a few that never made it off my hard-drive.

A few years ago I moved over to Hugo and static sites and decided to set up something a bit more barebones, but intentional. I bought in to the concepts behind POSSE (Publish (on your) Own Site, Syndicate Everywhere) and worked to make sure that my content would survive first. I wrote in markdown, published to my own git server (and GitHub as well) so that I could invoke GH Actions to actually build my website. You can check it out the behind the scenes [here](https://github.com/AngeloR/angelor.github.io). I actually really like this process, but I realized something.

POSSE and the IndieWeb would have you believe that your site should be the starting point for your content — I’ve come to believe that that’s the furthest thing from the truth.

### The Masks We Wear

The truth is that you are not experienced homogeneously.

The truth is that just as you are the sum of your parts, you present those parts in various amounts. Each room you enter calls for a different mix of your many selves.

I am not the same person I am on X as I am on LinkedIn.

I am not the same person I am on Facebook as I am on Mastodon.

I am not the same person I am on Instagram as I am on Twitch.

The truth is that I shift tone and intention in every room I am in, based on the room itself. Erving Goffman talks about this extensively in his book “***The Presentation of Self in Everyday Life”;*** As the backdrop of our stage changes we present different sides of ourselves. This isn’t wrong or incorrect, and it isn’t being “fake”. This is the truth of who we are as people.

The sorts of comments I leave on a LinkedIn post are vastly different from what I leave on X. They’re both facets of who I am, but they exist within the bounds of those systems. The systems inform how I interact with them.

In that way, the POSSE mentality of “writing on your own site first” trades true authenticity for self-erasure.

A bold claim, to be sure, but the truth is that social platforms have become mirrors of facets of self. In the same way that the language you use when you text an older relative is different from the language used when you text a younger one.

### So what does this have to do with POSSE?

By writing first on your own site, you miss tapping into the zeitgeist of the platform. When you are on LinkedIn, the type of content you see changes the way you interact with the platform. But it goes further than that — the WAY you even construct your post is different.

When X limits your count to a couple hundred characters, not only does it force you to to be brief and adjust language, but the very textbox to enter your tweet lends itself to the style and format of message. In the same way that the long form editor of Medium lends itself to larger posts.

POSSE ignores all of this and, instead, implicitly enforces a single-voice on what you write.

By writing on your own site first, you are forcing yourself to engage with different audiences in a way that doesn’t match their expectations. Long form posts on X are different from long form on Medium and are different from long form on LinkedIn — forcing a single writing interface over them doesn’t do them justice.

### From POSSE to EPOSS

I’m proposing a shift in direction of POSSE, while maintaining the original goals: Engage Platforms, Own Site Syndication

Instead of writing on your own website and pushing to other platforms, I suggest the opposite. Write on the platforms that are meant for that style of writing. Engage with your audience where they are in a manner they are expecting. Syndicate back to your own website as a way of archiving and gathering the different parts of yourself in one location. If someone wants all of those, they can still get it — but you allow yourself the freedom to express yourself differently.

IndieWeb and POSSE is about control and ownership, but it does this at the cost of contextual expression and implicitly imposed homogenous authenticity. POSSE targets digital attrition, but ignores the benefits on the platforms entirely — a mechanism to express a facet of yourself wholly. You are a spectrum and foil of your environment, and that’s just as true in the digital world. By engaging with platforms FIRST, you start from where your context already lives. You speak in the language of the room you’re in. The backdrop matches the persona you are displaying in its fullness. Then you archive that.

Instead of syndicating one voice everywhere, EPOSS seeks to collect all of your voices in one place. If a platform disappears, it disappears. The content and interactions are still collected in your archive. And the community moves to the next place.

Your website isn’t the orgin, it’s the destination. It’s a museum and collection of all your selves across the internet.

### Technically Practical

The same tools that power POSSE can power EPOSS, you just need to point them the other way.

For example, this post, even though it shows up on Medium, also appears on my website (<https://xangelo.ca/posts/medium/posse-has-it-backwards/>). It does this because Medium supports RSS and I can use that RSS feed to generate a post in markdown and feed it back to Hugo. This particular script looks at the RSS feed defined at RSS\_URL and writes markdown versions of it to content/posts/medium so that I can track which posts are being imported: <https://github.com/AngeloR/angelor.github.io/blob/main/.github/scripts/medium_to_hugo.py>

<https://medium.com/media/c7634bd7099d8b4a3c68e75789d29869/href>

I’ve connected this to my github actions to run this script every 30 minutes to pull in new content from medium.

EPOSS isn’t the antithesis of POSSE, it’s an evoluion.



---

This was originally published on Medium - https://xangelo.medium.com/posse-has-it-backwards-ca9ab4d5b529?source=rss-d5a790d38792------2