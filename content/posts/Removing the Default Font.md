---
title: Removing the Default Font
date: 2022-03-31T00:07:57-04:00
tags:
  - upkeep
  - fonts
  - publish
summary: Where I spend too long talking about why I removed the default font temporarily
lastmod: 2024-12-10T19:49:17.644Z
---

This is a small change that I've made to the site that I've actually been thinking about for quite some time. I've always had a monospaced font configured in my CSS, forcing all text into whatever the default monospace font on your system is.

Personally I like monospaced fonts - but then again, I spend a lot of my time looking at them so it's only inevitable.

However, monospaced fonts arose to solve a technical problem that original typesetters had long since solved.

## Monospaced Font

A monospaced font is a font that has a "fixed with". When you look at a word in a monospaced font, it's not that each character is the same size, but rather the area that contains each character is the same size.

![Font Spaces](/img/monospace.png)

In this image we can see how a monospace font is "set". Whenever a character appears on the screen, these "boxes" surrounding them denote their bounds. In a monospace'f font, the bounding box for each character is the same size. The size of the character and its placement within the box may vary - but by standardizing on the bounding box size it will appear that each character is the same "width".

This is very cool stuff.

Since each character has a bounding box that's the same size as every other character we actually run into a very specific instance of a cool typography side-effect known as [Rivers](<https://en.wikipedia.org/wiki/River_(typography)>). Each character aligns itself perfectly with the character above and below it, creating a giant grid of characters on your screen.

But this isn't always the best for reading.

## Proportional Font

A proportional font is one that allows the bounding box for any individual character to vary. This has the side-effect of allowing for much narrow kerning (the space between letters) and does 100% lead to improved legibility (see [this study here](https://journals.sagepub.com/doi/pdf/10.1177/001872088302500303)).

![Proportional Font](/img/proportional.png)

By varying the kerning and allowing each character to use as much space as it needs, font designers can really tweak the legibility of the font.

## Why does any of this matter?

We know that monospaced fonts improve the legibility of text in SOME cases, like reading code or if the reader has a disability like dyslexia. In all other cases, proportional fonts improve legibility. Serifs in generally tend to be chosen by popular type users (newspapers for example) because of their legibility.

All of this means that... me setting the default font to be a monospace font is actually a problem for legibility. By leaving this setting blank and using the browser defaults, I can ensure that you are reading the content of this site how you would best consume it. I've taken a lot of time to ensure that things like dark/light modes respect user settings. I've spent longer than I would have liked getting the right shades of blue/purple (the default unvisited/visited link colors) so that they are the same in dark/light modes. The only thing I didn't do was think about the font - I just set it to monospaced since I like it and went about my day.

I've since decided to remove that setting, allowing your browser/system defaults to set the primary font on the site. After all, what matters on this site is the content and you should be able to view that as you'd like.

## Appendix

The study linked looks specifically at fixed vs. variable letter width (monospace vs. proportional) for televised text. This is particularly relevant since we're talking about screens rather than print. The differences cited are also quite marginal - but that's the point of this font change. To the majority of users it won't make a difference, but to a small few it will matter a lot.
