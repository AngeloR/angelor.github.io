---
title: "DEVLOG: NewsRiver Updates"
date: 2020-11-10T09:43:04-05:00
---

## What is News River?
[News River](https://newsriver.xangelo.ca) is an auto-updating stream of news that doesn't need to clutter up your RSS feeds. It was based off ideas from [Dave Winer](https://scripting.com). There are some sites that you don't necessarily CARE about reading every single update. Sometimes you just want to see the most recent stuff and move on. Sites like [HackerNews](https://news.ycombinator.com) and some subreddits ([/r/devops](https://reddit.com/r/devops) or [/r/aws](https://reddit.com/r/aws)) are things that I'm curious about more recent things that get up there, but I don't necessarily want to read every single item. Normally I'm just skimming for interesting titles. 

I used to have these things synced up to my RSS reader, but the sheer number of updates to them caused me to go insane. There's no reasonable way to keep up with all of that stuff. So I had to pull them and then just.. remember to go there. Eventually I got tired of that and wrote the first News River system. You provide a list of sources (RSS or RedditJSON) and it will periodically scan them, download the items, save them, and serve them up for you to see in a simple little auto-updating front-end. 

It was a pretty handy tool that was written in Node.js and relied on Redis as the backend storage, with everything hosted on Heroku. It was written at a time when I was really digging into various Redis use cases and the free-form nature was a useful thing when trying to figure out the project. However, due to the nature of Redis I had to jump through quite a few loops to "optimize" queries. It had a strange bucketing system for the keys that allowed me to query all updates in the last 10 minutes by grouping all updates into sets where the key was in 5 minute intervals. It was a crazy system and honestly most of the code was handling the bucketing+tests for it.

## Sqlite3

The latest version of NewsRiver actually rips out Redis and replaces it with Sqlite3. The crazy bucketing system no longer exists since I can just sort by rounded date values. By utilizing sqlite3 instead of Redis I was able to move the entire system over to a small VPS that I ran and eliminate the heroku requirement for running it. The move to sqlite3 was really pushed by the need to simplify the code base. 

NewsRiver is not a project I want to keep tinkering with. I'd like it to be complete and to be able to use it daily without making a bunch of tweaks. But the date code had become unwieldy and as a result I spent most of time reviewing it to make sure I wasn't breaking it when fixing things. Moving to sqlite3 allowed me to drop that whole system, delete a ton of code, and just move to something that didn't really require a lot of explanation/documentation. 

Eventually we can replace the sqlite3 only setup by utilizing something like `knex` to allow for a swappable data storage layer.

