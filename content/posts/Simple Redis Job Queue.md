---
summary: A naive redis job queue implementation
tags:
  - redis
  - architecture
  - publish
date: 2023-05-25T00:15:53.362-04:00
title: Simple Redis Job Queue
lastmod: 2024-12-10T19:48:22.826Z
---

A common pattern in most software projects is the "queue". You'll throw some stuff on there and eventually get around to sorting it all out. In some cases, you may not even really care about that.

I recent ran into a situation in node.js where I needed to offload some CPU intensive out of the main http request handling process. Originally I thought about just forking the process, but I due to the fact that this endpoint is public facing (albeit authenticated and paid for), I was wary. Instead I figured I'd rope in a quick job queue.

### Caveats:

- The jobs have an easy "deduplication key". An ID that is the same given the same inputs.<br>

- If we don't complete a job for any reason, that's fine, another one will likely show up again in a few minutes

We were also using redis so here's a real simple pattern that can handle this kind of workload.

1. Whenever we get a new job we calculate its deduplication ID. We'll call this the `jobId` moving forward.

2. We call `set job:[jobId] value NX EX 10`. This sets the key `job:[jobId]` to some value we provide only if the key does not already exist. It also sets a 10s expiration time. We're using `NX` to provide some additional deduplication and we're using `EX` to ensure that if for some reason our job doesn't complete in 10s.. just allow another job to be inserted with the same key. You can tune `EX` as necessary, or leave it off entirely if you never want this job re-processed again until you flush your cache.

3. We use `rpush [queueName] [jobId]` to add the job Id to the list of jobs that need to be processed.

4. If we have any additional information about the job we want to pass on, we can use `hset jobDetails:[jobId] k1 v1 k2 v2...` and store it in there.

Your "worker" is just a process that runs `lrange [queueName] 0 0`. That will retrieve the oldest `jobId` in your queue. You can grab any further information from the `jobDetails:[jobId]` hash set and do whatever work you need. When you're done you can call `ltrim [queueName] 0 0` which will remove the job from the queue.

An interesting fact about this setup is that all your calls are `O(1)` and you can pipeline the initial `set`/`rpush`/`hset` calls so that things are even faster.
