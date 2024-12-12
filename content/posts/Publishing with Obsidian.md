---
date: 2024-12-09
tags:
  - publish
  - blog
  - hugo
  - obsidian
authors:
  - angelor
title: Publishing with Obsidian
summary: Blogging with Obsidian
lastmod: 2024-12-09T21:19:10.953Z
---
# Publishing with Obsidian

For the last couple years I've been been trending toward the idea that tools like https://remotestorage.io and https://5apps.com/ are actually not any better for owning your content than everything they purport to replace. Instead the true bastion of content owners is the lowly file that exists on their computer. While tools like RemoteStorage (and I'm definitely picking on them for no good reason) talk about freedom, really they're just pushing their vision of freedom on users. Freedom is really about making informed choices.

As I came to terms with the idea, I started working on software that.. wrote actual files. My https://github.com/angelor/outliner that I've used for a while now writes everything locally. There's no network requests necessary. That means if you want, you can go in, grab all those files, and just.. put them wherever you want: Dropbox, RemoteStorage, your NAS. That's freedom. That's really giving users control.

I recently stumbled across a blog post by Steph Anjo called [File over app](https://stephango.com/file-over-app) which really resonated with me. As a result, I kind of dropped everything and moved to Obsidian as my primary note taking tool.

It sounds impulsive, but the truth is - the output of Obsidian is just markdown. An open protocol with hundreds of implementations across almost every programming language. Obsidian is a good enough note-taking tool - but one day it too will be gone. Likely replaced by something better with more features I haven't thought of. But that's ok, it'll probably import my Markdown files just fine.

## Setup

My existing deployment process has been:

1. Write my blog posts in my outliner
2. Export the outline-based notes to markdown (I wrote a small parser that flattened my outlines)
3. Import those to my hugo-based blog repo locally
4. Commit the changes and deploy to GitHub
5. GitHub workflows builds my site and publishes it for me

The only thing that's going to change is that

1. I'm going to utilize Obsidian to write my posts
2. I'm going to export them, to my hugo-based blog repo locally

## FrontMatter

I'm using Obsidian's built in Template system to create a basic FrontMatter that gets applied whenever I want to convert something into a post.

```
---
date: {{date}}
tags: [publish]
authors:
  - angelor
title: {{title}}
---

```

For me, specifically, I add the "publish" tag to denote "published" blog posts vs. things I'm still working on. This gets formatted with some Hugo specifics (like the current date and title), and inserted verbatim into the post.

## Compiling

The default vault format for Obsidian would be good enough for me, except I like to keep all my notes in a single vault. Sometimes things start off as memo's to myself, and slowly morph into actual blog posts. Other times as I build up an understanding of a topic, I update my notes, and those slowly become blog posts. As a result, I want a way of differentiating between notes that are "blog posts" and those that are just regular notes.

I use a Community Plugin called [Hugo Publish](https://github.com/kirito41dd/obsidian-hugo-publish) that does this part for me.

![Screenshot 2024-12-09 at 4.12.32 PM.png](/Screenshot%202024-12-09%20at%204.12.32%20PM.png)

My settings are pretty straight forward - that "publish" tag that I mentioned earlier is what selects a post for "compilation". It doesn't really do too much, just rewrites some links and moves the uploaded images to the right folder in my hugo setup - and then it copies the compiled files over.

## Thoughts

I think overall I'm pretty pleased with this process - one of the things that I've really struggled with is that writing a blog post is a very involved process right now using a custom editor. Using Obsidian this can happen much easier, and I get the added benefit of being able to sync the files across different platforms in a variety of ways. I'll have to play around with this a bit more - but so far I'm liking it.
