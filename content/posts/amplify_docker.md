---
title:  Amplify docker limitations
summary:  Amplify has some odd docker limitations it doesn't want to fix
tags:  ["aws", "docker", "amplify"]
date: 2023-12-05T05:16:29.288-05:00
---


I've recently had the chance to do some work wtih Amplify in AWS and I'm surprised how simultaneously feature rich and half baked it is. It seems if you're in to click-ops you'll be fine in Amplify until you hit a problem.

If you're deploying through amplify you'll eventually hit this problem:

```[BUILD_CONTAINER_UNABLE_TO_PULL_IMAGE: Unable to pull customer's container image. CannotPullContainerError: Error response from daemon: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit]```

Which seems perfectly reasonable at first glance. Nowhere in your project setup did you really define credentials for your docker account.

But if you dig a bit it gets weird: You actually can't define credentials for a docker account.. and the limits for the free tier are high enough that you probably wouldn't hit them with a small team - 100 pulls every 6 hours per IP.

Turns out you actually share a build pool with other users in amplify - which makes sense. But that in turn means that every so often your build pool will hit the limits for pulling containers from docker hub. And since there's no way to set credentials for your pull.. you're just kinda left hoping that if you retry things will work. There's probably a large enough build pool that it works sometimes, but there are reports of it taking up to an hour or so.

So you think: Oh yeah, no worries -> I'll just set up ECR, and configure Amplify to grab my image from that repo instead. But ECR is a non-starter. It turns out that you can't assign any kind of roles to amplify to allow authentication against an ECR.. so if you're hosting your image in ECR, you have to make the entire repo publicly accessible.

If you're using customized images unfortunately this is really the only way to go. You have to build and deploy to ECR and make the repo publicly available.

If you're using pre-built images, amazon actually has their own public replica of popular docker images [https://gallery.ecr.aws/](https://gallery.ecr.aws/). If you can find your image on there then you can reference it in the build params for your Amplify project.










    