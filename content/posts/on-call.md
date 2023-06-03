---
title: "Designing On-Call"
date: 2022-09-21T22:36:23-04:00
tags: ["engineering", "engineering org", "engineering processes"]
summary: How to implement a successful on-call process for the first time
---
On-call is one of those things that all developers end up doing at some point. My goal isn't to discuss the merit of on-call, but rather what the point of on-call is and how to go about designing what “on-call” means at your company. I'm going to start at the very beginning because chances are you're already doing it wrong. I should also note that I'm looking at this specifically from a SaaS point of view.

## Why do devs go on-call?
The point of on-call is simple: People use your app 24/7 relative to you. They may be using it from Italy or Australia or Thailand while you're tucked up in bed in Wisconsin. But for them, it's working hours and they expect your site to be available. But, of course, that's not always possible. Things happen that will inevitably take your project down. In these situations "on-call" is vital for several reasons: The least of which is solving the problem.

Normally you go on-call because your founders or manager or a customer noticed that your service was offline when it wasn't supposed to be. People start complaining, it makes some rounds internally, and then eventually ends up at the desks of whoever deployed it. Often that ends up being some kind of "infrastructure" team (You probably call them DevOps or SREs - why that's wrong is an issue for another time). These folk hear about it, fix the problem, and then go about setting up some alerts to let them know when the issue happens again. Bam, you've just enabled on-call without any of the good parts. You can all but guarantee that your on-call team is going to end up angry and upset about on-call which will manifest in the worst ways possible.

## Let's walk through the standard on-call process
Let's walk through a very high-level on-call process and then we can break it down.

1. Something breaks
2. You find out that something is broken
3. You bash at your keyboard until it works again
4. You put in some metrics so that if "thing" happens again, you'll know

It's wrong. 

Ok, it's not wrong - it's just a subset of what "on-call" really is. 

See the thing that you're REALLY missing is that nowhere in this process have you actually figured out what's going on. Sure you solved a symptom - maybe that symptom is synonymous with the cause. But you don't know, because your process doesn't encompass that. 

To have a good on-call process you have to understand a fundamental truth of on-call: on-call isn't just about engineering. on-call is the culmination of a bunch of different business, product, and culture decisions. 

Here's the truth of each step in your process

### Something breaks
#### Something
The first thing we need to define is what "something" is. The easiest thing to do is to take a look at your code repositories. If you’ve broken things down into services, you likely have one repo/service. That’s an easy way to define the boundaries of “something”. But it’s also probably wrong. 

If you have a monolithic codebase in a single repository this is a much harder step for you, and you’ll probably do a better job.

It’s very easy to define “something” by engineering components - but this isn’t always answering “what” broke, but “how” and “why”. A user doesn’t care that your lambda was opening too many connections to RDS causing a spike in memory which caused your API to lag. They care that they weren’t able to send a cat picture. 

When defining your “something” start with user flows. Look at your application and define “core” actions that your user can take. From there, simplify until you have a handful of actions that you want a user to be able to do All the Time. 

#### Broke
Defining the "something" is relatively easy compared to defining "broken". We know a thing is broken if it's not starting, but:

- What if it works but 1% of the requests are resulting in an error?
- What if it works but 1% of the time it crashes and restarts?
- What if it works but is very slow?
- What if it works, is not slow, and doesn't crash, but your API docs don't match what the endpoint is returning?
- What if it works, but your database is being crushed by a sudden increase in traffic?

Defining our “something” first is important because it helps us to set bounds on what we consider “broke” and what is “degraded” and what is “fine”. 

Perhaps we don't care if 1% of requests fail.. maybe we don't care if 0.1% of requests fail. Defining these thresholds is tough because it requires realistically looking at our application and deciding what is "acceptable" and what is not. Sometimes we have to make difficult choices here. Maybe we want 0.1% to be considered broken.. but actually, 1% is broken. This is where we impact your actual application.

Deciding 0.1% of errors is "broken" where your application is currently sitting at 1% may seem like a good thing. 0.1% is where we want to be and so letting devs know when that isn't the case is good. We can work toward 0.1%. But this involves much larger product considerations. 

- When these alerts happen overnight - are devs tasked with a complete resolution during work hours?
- Does that mean feature work will suffer?
- How will you buffer your sprint to make time for these interruptions?
- Do you have the ability to buffer your sprint given product launch dates?
- What happens when a dev is up all night dealing with issues, do they take the next day off?
- Do you offload the task to a different team (Ops/Infra/SRE) since feature work is so important?
- What happens when those teams get burnt out and leave?

On the flip side setting your alerts at 1% is accepting that this is the current state.. but now it becomes a decision on whether or not a 0.1% error rate is more important than the next feature you're supposed to get out.

Defining the state of "broken" is hard because it is the intersection of the current and future state of our application, while simultaneously being the fulcrum that will help tip the scales between "acceptable" and "unacceptable".

There's no right answer here - just an answer for your team, for right now. Whatever you decide today, the most important thing is that you re-evaluate it and allow those that are on-call to provide feedback on if this was a reasonable level of "broken".

#### Service Level Objectives
By defining what broken means you've now set a baseline stat for your systems. You've defined your first Service Level Objective (SLO). Yay! 

In the nutshell, SLOs form the baseline for your Service Level Agreements (SLA) with customers. Your SLA can't be better than your SLO or you're going to have to sacrifice on feature development to bring them up to speed. Now we can talk about all kinds of marketing tricks you can do (mainly playing with the measurement period) but the truth is if your SLO defines a particular flow as "broken" it sets the floor for your SLA. You can only promise less than that until you invest in improving that SLO.

Let's move on to the 2<sup>nd</sup> step.

### You find out that something is broken 
#### What's on first?
Ok. something is definitely broken. How do you find out?

This is probably the most technically straightforward piece, but the one that has the most impact on people. 

When something is broken, an alert is generated you get notified. 

The first step is figuring out how you get data out of your system into a place that can perform some analysis and generate these alerts. The two big products here are Datadog and NewRelic. These are all-in-one solutions that allow you to instrument your application and gather metrics+logs+events and put them somewhere you can visualize them. These systems also allow you to create “alerts” that get generated based on the data you’ve been feeding it. 

Given that you now know what you consider critical user flows your goal is to go through your application and ensure that everything that supports these flows is properly instrumented. This is where we start looking at the different infrastructure components. This is where we learn how/why our system broke. This is an important step - it's easy to think that devs should just "go through and instrument everything", but that makes things harder to reason about. You're increasing your "noise" and when you're looking at a Signal vs. Noise ratio, you want to keep your noise to a minimum.

Take a look at your SLOs -> and then define your Service Level Indicators (SLI).

#### Service Level Indicators
These are the metrics that you can look at to identify that you're meeting your SLOs. They're often aggregate metrics. If your objective is a 1% error rate, your SLI will likely ensure that you are getting an accurate count of errors vs. successful requests across your system. That will involve you going through various systems and making sure that your code base is sending appropriate logs. It'll also be going through your monitoring tooling and creating dashboards/alerts so you can view your SLI and all the subcomponents that make up your SLI easily.

Now that we have these metrics, and we know what we consider “broken” we can tune our alarms. When one of these components is in a state that impacts our user flow - thats an alert. 

That alert is going to be sent to whomever is on-call. 

#### Who’s on first?
Everyone in Engineering that is responsible for writing code that could end up affecting a user.

Bam. Easiest decision ever. 

But you'll likely face some pushback from teams that don't normally see themselves as "needing to be in rotation". Doesn't matter - at some point you have to make a decision and this is one hill you must die on as a manager.

Traditionally on-call was reserved for infrastructure/devops/sre groups and developers weren't required to be on-call. This is a silly separation of concerns. The people who wrote the code that likely resulted in user impacts are often not from your infrastructure/platform team -> they're likely from the application team. This should be your first tier of on-call when thinking about SLOs from the product.

Often you'll end up with a rotation of engineers, probably daily, with multiple tiers.

1. The primary: They're the first ones to get alerted about an issue
2. The secondary: If alerts to the primary don't get acknowledged, it goes to this person
3. The backup: If primary AND secondary are not responding -> this person is here.

You may decide to have different schedules for weekdays/weekends but in the end the goal is to cycle through all developers without making it feel like anyones "job" is to be on-call.

Now that you have your schedule, you must know that  
1. Everyone should feel empowered to schedule alternates if they're busy. If I'm scheduled tomorrow night and something comes up - I should feel comfortable addressing the engineering team as a whole and asking someone to trade with me. Likewise, you should feel comfortable saying no.
1. No one should treat on-call as being stuck at the computer. This does end up personal preference for engineers, but if you're on-call you should be able to take your laptop/phone with you where you go. If your company is not technically ready for this, then you better be compensating your employees well for tying them to their homes outside of work hours.

### You bash at your keyboard until it works again
Alright. It's 3 am, something broke, you were paged. You hop on your computer, bleary-eyed and upset because it's chillier than you expected because you forgot your pants in the rush to deal with this situation.

Relax.

Your job is not to solve the problem - your job is to ensure that your application is performing as expected.

Solving the problem is a task that is best left to those on full nights of sleep. When it's 3 am and you finally manage to log into your laptop, "solving" the problem should be the furthest thing from your mind. The goal is to mitigate the outage and restore acceptable functionality based on your SLOs.

In some cases simply restarting a process is enough to get things back to working. Sometimes you may need to upsize a database.

What you should NOT be required to do, is:  
- figure out where your application code is crashing
- optimize that weird nested join that you're supposed to tackle next sprint

Your job at 3 am is problem mitigation. Maybe nothing can be done except throw on a status message so that users know what's happening.

Perhaps this alert is fine, this level of error is acceptable.. so you can just adjust your alerting and call it a night.

Don't attempt to be smart at 3 am because when you get paged at 6 am you'll be much worse off trying to decipher what you did.

This is often where we run into issues. Engineers like to solve problems. When we get an alert we dig in. We want to fully understand what's happening because we can easily over/under complicate an issue. Oh is CPU on the DB at 100%? Do we need to just upsize the database? Are we locking something? Is there some periodic system running? 

Sometimes the problem is obvious and fixing the symptom is the same as fixing the problem. It's much harder when the problem isn't obvious. Rememeber that while you're "digging in" this is impacting users - otherwise it wouldn't be alerting you right? As unnatural and silly as it seems, at 3 am -> solve the symptom for immediate relief. Then when you're not stressed, solve the problem.

Again: Solving the problem at 3 am is not your job.

Once you fix the symptom causing the alert and verify that things are working again - leave notes in a public place. Explain what you did and why. The why is the most important part. This is that when you or whomever else logs in the following day and looks over what happened "on-call" you can easily decipher your thought process and areas that you should begin looking to resolve the underlying problem.

### You put in some metrics so that if "thing" happens again, you'll know
This is the easiest part: Once you identify the "root cause" of your problem, get some metrics/logs in place so that you know. Don't forget to include the metric in any SLI calculations that you might need.

## Compensation
Your propensity for compensation is entirely dependent on your org and the legalities of where you reside. In some situations you will have to pay engineers overtime for on-call. In some you can get away it.

Don't be a jerk.

Whatever you decide to do understand that your team will leave if they think they're getting a bad deal. on-call is requesting something of your team outside of normal working hours. It doesn't matter if you put it in a contract, it doesn't matter if it was on the job description. You are requesting something of your team that is above their work day.

If an on-call night was rough, let them take the following day off. If they've been having a bad week personally, remind them that its' ok if they want to move their on-call. 

## Your On-Call Process
Finally, you've ready all that and are ready to implement a real "on-call" process. Here's what it should look like: 

1. Identify your SLOs
1. Identify your SLIs
1. Work to track metrics/logs that relate to your SLIs
1. Create an on-call rotation
1. Something breaks
2. You find out that something is broken
3. You mitigate the problem
4. You put in some metrics so that if "thing" happens again, you'll know
1. You revisit the alert the morning after to figure out root cause
1. You resolve the actual problem.


## Your On-Call Process in Practice
The truth is, there's a huge difference from the "ideal" process and what you end up with in practice. So much of this is up to the people involved and the culture of the workplace. Chances are you already have some of this implemented and it kinda works for you mostly.

That's ok.

The goal here is that you understand ideal, and you understand where you are. And now you have the information to be able to make trade-offs. Expending your entire development capital on the first 3 items on this process before getting to the next is silly.

Instead this process is more of a "Flow". If you understand ther flow, you can understand how each thing feeds into the next. When you know that you can better break down your approach. 

You probably have Service Level Agreements (SLAs) with your customers. And you likely have some rough SLOs/SLIs that track that. Solidify them. Make them available to the team on demand and make sure that they're accurate. 

The on-call process is a larger movement within your engineering organization that pushes the whole team toward excellence: Both technical in being able to understand the inner-workings of your application and all the components, but also of your product. If your SLAs are at 99% uptime, but you're sitting at 99.9% uptime -> that's an excellent way to upsell. Likewise, if your uptime is actually at 98% you now know exactly the area your team will need to focus on next.

## Final Thoughts

Understand that no matter your best efforts, pages will be missed. Bugs will go undetected. Users will be upset. But these are short-term issues. You can fix bugs. You can explain to users. You can tell your devs that this push is temporary.

Do understand the difference between pages being missed and pages being ignored - call your team out on it however you need. Missing a page isn't just letting customers down, it's letting your team down. If it happens frequently enough the team will either think that the alert isn't important or that an individual is above the on-call rotation. It'll foster all kinds of interpersonal problems.

Don't treat on-call as the solution to your stability and reliability issues. Reacting is not being proactive. When alerts happen overnight, ensure that there is SOME mechanism to address the root cause reasonably.

If you are running into issues with this, reach out - I'd love to chat. I've been doing this for a long time and I love to help out. I set aside a few hours a week to donate to help companies and individuals make sense of these kinds of larger scale engineering problems. My email is at the bottom of every page.
