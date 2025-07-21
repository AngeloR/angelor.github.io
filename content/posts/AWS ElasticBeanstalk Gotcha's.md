---
tags:
  - publish
  - aws
  - elasticbeanstalk
  - guide
summary: Funky ElasticBeanstalk behaviours
title: AWS ElasticBeanstalk Gotcha's
date: 2024-12-09T16:29:52.051Z
lastmod: 2024-12-12T05:45:27.752Z
---

I've been lucky and unlucky enough to work with AWS ElasticBeanstalk for a number of years and here's a list of footguns.

## Degraded on 4xx Errors

If your app is doing any kind of authentication you're going to run into an eventual issue where every time someone incorrectly authenticates you run the risk of the environment moving into a "degraded" state. This is because ElasticBeanstalk counts 4xx errors as "application" errors and if you have too many of them it thinks your app is in a degraded state and will attempt to redeploy.

You can fix it two ways:

1. There's an option in the UI for you to check
2. A custom ConfigDocument

### UI option

You can find this section under Health monitoring rule customization for the environment.\
![Disable 4xx health monitoring via UI](https://i.sstatic.net/m6fvY.png)

### Config Document

This is displayed as you would for TypeScript based CDK, but I think it's pretty straight forward to convert?

```js
  {
        namespace: 'aws:elasticbeanstalk:healthreporting:system',
        optionName: 'ConfigDocument',
        value: JSON.stringify({
          Rules: {
            Environment: {
              Application: {
                ApplicationRequests4xx: {
                  Enabled: false
                }
              }
            }
          },
          Version: 1
        })
      },
```

## Deployment Options

EB is great for getting started - but as you start getting users you'll start running into outages as you deploy your application. That's because, by default, ElasticBeanstalk uses "All at Once" as a deployment mode. This means it goes through your list of instances, sets up the new version, then restarts the proxy which means downtime on each instance.

Depending on your load, and application start time, you can see periodic downtime for a good chunk of your deployment. This is no-bueno. Your best bet is to swap to either:\
\- Rolling with an additional batch\
\- Immutable

### Rolling with an Additional Batch

In this scenario, EB will launch a new set of instances with the new application, and then cycle through the old instances updating as it goes (similar to the rolling method). By spinning up the new batch of instances first, EB can ensure that your application maintains its availability/throughput during the deployment.

### Immutable

In this scenario, EB will spin up an entirely new set of instances and do a hard swap from the old ones. This takes the longest amount of time, depending on the number of instances you're running simultaneously.
