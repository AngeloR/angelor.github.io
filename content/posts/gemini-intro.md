---
title: Gemini, an HTTP alternative
date: 2021-06-21T17:11:57-04:00
tags:
  - gemini
  - upkeep
  - publish
summary: An HTTP alternative
lastmod: 2024-12-12T05:25:23.255Z
---
For the last few months now I've started embracing my weird love for text and text-related user interfaces. From email to irc, I'm moving more and more of my social interactions away from traditional websites/apps and over to my terminal. A big part of this move is a step back from 3rd party applications to things that I have a bit more control over - but there are many reasons.

* Privacy: Text only platforms make it very hard for trackers. Most email nowdays include "tracking pixels" that allow the sender to know when you opened the email and to gather information about the device what opened the email itself.
* No ads: When everything is text, there's 0 need to include the ability to deal with images. As such advertisements just can't happen in a traditional format. The closest you can get is what you think of when you look at global chat in MMOs - people just spamming whatever they want. As a result it makes it easier to deal with (blocking).
* Faster: As we've added more and more compute power to devices, the tools and applications that we use have just gotten larger and less efficient. It's very common for websites loaded to be 1mb in size - that's kinda terrible. By moving to a text-only interface, you lose the ability to include a bunch of extra things and you end up with what matters - Just The Content.
* Interoperability: When everything is text, it's much easier to wire up multiple tools together. Think of the unix interface philosophy. Every tool does one thing well, and the input/output is text. So you have the ability to wire up a chain of tools that the original authors don't need to know/care about.

The hard part is that you need to find alternatives to a lot of traditional apps that you have come to rely on. For some things (email for example) it's very easy. For others, like web browsers, it's basically impossible. There are things like [lynx](https://lynx.invisible-island.net/) that you can utilize, but it's just not the same. So many websites now days are designed around the fact that the user is going to have a full GUI browser. And, honestly, that's a very reasonable expectation.

But I still found myself looking for an alternative. And I found Gemini.

## What is Gemini

[Gemini](https://gemini.circumlunar.space) is an alternative to the HTTP protocol. It's definitely not going to replace HTTP, nor does it want to. Instead it aims to operate alongside. It's a very stripped down subset of markdown to enable easy implementations of parsing. A lot of the complexity of modern browser systems is around parsing HTML/CSS effectively and gemini just does away with that whole idea.

This means that documents in Gemini are very light-weight, and are readable without any parsing. You could just read the raw text that makes up a gemini doc (called gemtext) and be just fine. Any styling choices are entirely up to the renderer (browser mostly) and are irrelevant to the document itself. There is no way to view images in-line, there is no JS, there is nothing but text.

I really recommend you check out the gemini home page and do a bit of reading up on it.

## Accessing Gemini

Since gemini is a completely different protocol you can't access it with a regular web-browser that deals in HTTP. Instead you have to find an alternative browser that deals with the gemini:// protocol. There are [numerous](https://gemini.circumlunar.space/software/) owing to the simplicitly of the parser implementation. The one I've been using most is a terminal based one called [amfora](https://github.com/makeworld-the-better-one/amfora), but if you're looking for something graphical I highly recommend [Lagrange](https://gmi.skyjake.fi/lagrange/) which is wonderful.

Obviously this is just a browser, so you need to go somewhere. I recommend starting at [geminispace.info](gemini://geminispace.info).

One thing I should caution you - don't expect a full replacement for what you consider "the internet". Gemini is very simplistic and focuses on ease of content consumption. It doesn't make content creation hard, but because of the focus on content itself, "interactions" are minimal. Some capsules (the gemini equivalent of a website) have "comment" sections, which harken back to the guestbooks of the 90s.

## Why I'm interested in Gemini

The thing that attracts me to Gemini is the same thing that attracts me to most projects: putting data privacy/ownership above all else.

Getting technical, Gemini foces TLS connections. Nothing is transmitted un-encrypted. It also brings to the forefront client certificates in SSL. The original spec for certs already supports this and it's crazy that it never took off. It honestly resolves the whole account identification/password problem in a really neat way.

### A sidenote on SSL and Authentication

This is, I think, one of my favourite features of gemini. SSL certs have two sides, and most people are only familiar with one. Servers generate certs to identify themselves. But since anyone can just generate a cert, there is really no way of knowing that the server you are connecting to is who they say they are. That is, I can generate a cert for duckduckgo.com, and you would have no way of knowing I'm NOT the actual owner of that site. One way that we currently resolve this problem is "Certificate Authorities".

Certificate Authorities (CA) are just a collection of companies that at SOME POINT were declared trustworthy. You had no say in that process, and despite numerous hacks of the CAs, they're still considered "trustworthy". You pay these companies to certify that you are who you say you are. There are various levels of "validation" that you can do, but the end goal is that your browser trusts a bunch of these CAs. When they see a cert from your website signed by a CA, they trust it.

Don't get me wrong, trust in certs is a hard problem to solve and one that has been around for a long time.

Gemini utilizies the idea of "Trust on First Use (TOFU)". The idea is similar to how ssh manages your known hosts. The first time you visit a site in gemini that provides you a key, you just believe that they are who they say they are and record the key/site pair. Next time you visit, they simply match the cert recieved with what they have stored.

This is naive. The rational is, once you connect to a site you'll won't be able to connect to anyone else impersonating that site unless you forget the original key/site mapping. Of course, the reverse is also true -> if you connect to a site that is already impersonating a different one, you'll need to forget the original mapping before you can navigate to the actual site.

On the server side, it definitely feels a bit weird. But this works wonderfully for the client!

As a user, you can generate a single certificate that's YOU. You can then provide the public key for that cert to the server to identify it as you. If the server implements TOFU (which is how every authentication system ever works) then you are mapped to that cert on that server. Going to another server? Provide the same signature. Nothing to remember. You just need to keep your private key safe.

The "certification generation" part is the tricky part and is why this never caught on for authentication on the web. But in Gemini, which is currentyly a more technical audience, it's a bit more feasible as a solution. What it means is, as a user, I can generate a single "account" and reuse it everywhere.

## Updating Hugo to output Gemini valid content

I'm interested enough in Gemini to put some time into modifying my website to output docs in gemtext so that I can serve my site over gemini as well as http. There are a few steps here (including getting off github pages so that both domains can be served over the xangelo.ca root) but that's ok.

The first thing I had to do was figure out how to get my content into gemtext. The easiest way was just to utilize hugo and add a new gemini output. There are a couple resources on this, but the two that were the most helpful were [this article by Sylvain Durand](https://sylvaindurand.org/gemini-and-hugo/) and [this one by Wouter Groenveld](https://brainbaking.com/post/2021/04/using-hugo-to-launch-a-gemini-capsule/). I won't re-hash what these are but the final configurations for my site can be found here:

* [config.toml](https://github.com/AngeloR/xangelo.ca/blob/88c61cd88bd2228dc7f2e46871f5e5ea6e2fcfdc/config.toml#L36): The config file to declare the gemini output
* [index.gmi](https://github.com/AngeloR/xangelo.ca/blob/88c61cd88bd2228dc7f2e46871f5e5ea6e2fcfdc/layouts/index.gmi) - The layout file for the main page
* [single.gmi](https://github.com/AngeloR/xangelo.ca/blob/88c61cd88bd2228dc7f2e46871f5e5ea6e2fcfdc/layouts/_default/single.gmi) - The layout file for a single post

I'm including them because I mostly cannibalized Wouter/Sylvain's docs. Wouter made the decision to get off Gemini due to the earlyness of the protocol (it is very early) and as such dropped the original config links that he had up. I just went through git history and found them and made a few tweaks and put them up in my repo.

At the moment I'm mostly doing what Wouter is - a "build" on my site involves me generating some hugo and usign scp to move it over to my gemini server. I'm then running [agate](https://github.com/mbrubeck/agate) a bit manually while testing. This command just starts agate, tells it where my content folder is located, the addresses to bind to, and the hostname and language.

Agate will happily generate the keys for you on first run, or you can provide them yourself.

```bash to start agate
 ./agate.x86_64-unknown-linux-gnu --content ./gemini/ --addr [::]:1965 --addr 0.0.0.0:1965 --hostname gemini.xangelo.ca --lang en-US
```

For now, scp is fine - but I'll probably just set up a gemini submodule/repo and deploy that to my server instead. That way I don't have to worry too much about transferring the entirety of the site.

## Conclusion

Overall, I'm pretty excited about Gemini. The ease of getting into the ecosystem as a consumer and publisher is amazing. There are some awesome projects to really ease that gap. But there's also plenty of room for growth and a small enough community that you can get involved in. The best place to get into it is [gemini space](gemini://gemini.circumlunar.space). I think the thing that excites me most about it is just the fact that there's such a big focus on privacy and small contributors. I think that's something that's missing from the web today, that we used to have at some point.
