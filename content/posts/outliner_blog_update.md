---
title: Now Powered by Outlines
tags:  ["outliner", "blog", "project"]
date: 2023-05-21T23:29:45.732-04:00
summary: An update to how I publish new posts
---


One of the things that I do every so often is completely re-write the backend of my blog. I've mostly hit upon a UI that I like, but I've swapped out the backend over the years between various custom iterations, wordpress, ghost, and now finally Hugo. This time, I've swapped out how I write my blog posts - but kept everything else the same.

The current system allows me to write markdown in vim. I'm normally running `hugo serve -w` at the same time so I can watch the rendered version of what I'm doing as I go. It's sort of like a hacked-together live preview. It works well enough.

However, for the last 10 years (maybe more?) I've been a huge fan of outliners. I original started with various projects by [Dave Winer](https://scripting.com) and I used almost everything he's written around them for a number of years. I've also tried tooling like [Workflowy](https://workflowy.com) and almost every other infinite-bullet-list tool that came after them. They were all.. fine? I had no real problems with them except that they never really stuck around for very long. They were in a tab in my browser, and my browser has like 100 tabs open at any given time.&nbsp;

For the last 6 months or so, however, I've been working on my own outliner. It started as an in-browser tool... and I quickly moved it to an offline-first desktop app via [Tauri](https://tauri.app). Having it offline first meant a few big things.

1. All the syncing tools just work. Dropbox, rsync, backblaze, s3 as a filesystem. Whatever. It works. All nodes in the outliner are individual json files on your computer. There's an "outline" file that stitches the nodes together into a tree. &nbsp;<br>

2. Building desktop first allowed me to bypass the need for user accounts and passwords. It allowed me to skip out on the complexities of providing reliable encrypted storage to users. I don't need to run a collection of servers and databases and object stores to power this thing.

Since I use this tool across operating systems all day long it slowly ended up being where most of my thoughts for blog ideas end up. And so what I hope to be the final feature of this project was realized: I'd love to be able to write my whole blog post in here, and then hit a button to have it publish to my hugo deploy.

This first iteration uses a lot of hard-coded stuff.. and I'll probably take some time to iron out some of the edge cases around rendering.. but it honestly came together pretty quickly. Since every node in the outliner is markdown it was trivial to put it together. As of right now, I can write my blog post in my outliner, press `shift+p` and have it write out a markdown file to my local hugo instance.

For now, I do some manual reviewing before officially publishing it. For now there's a few more usability things that need to be added like&nbsp;

- differentiating which posts are published vs. un-published

- being able to 'unpublish' a node

But honestly? I'm kind of enjoying this right now.






    
