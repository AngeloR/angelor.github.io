---
title: Code Reviews Are Failure
date: 2022-02-24T11:05:34-05:00
tags:
  - git
  - development
  - engineering processes
  - publish
summary: Code Reviews are nothing more than a half-hearted attempt to avoid planning
lastmod: 2024-12-10T19:49:29.025Z
---

As a new startup with one or two engineers on staff, you're very likely not doing code reviews. Engineers at this stage have a very deep understanding of the code - after all, they've probably written most of it. When it's time for a new feature, these initial developers know exactly how they're going to implement it given the architecture of their code base. Chances are, they keep their own work in a branch, and open a Pull Request or Merge Request, but they aren't asking someone to take a look at it. Instead they're making sure their changes work and they're merging it in themselves. Often they'll do this many times a day as they crank out features and bug fixes.

At some point things are going better than they were and this small group of engineers start adding more! Now you have 5 or 6 engineers, all with varying familiarity of your code base. This is generally the first time Code Reviews come about - and normally for good reason. Often someone has pushed some code to production that has broken things and the developers take a step back and realize that maybe before they push code, it's best if they have others review it. Perhaps bugs like this can be caught next time. And so they come up with rules and reasons for why they need Code Reviews. Non technical managers think "Ah, this won't happen again - we're instituting code reviews now!"

We've all seen the reasons for Code Reviews:

- Find bugs further downstream
- Propagation of Knowledge
- Team Ownership
- Double check functionality/architecture

These are nonsense - Code Reviews in isolation almost always end up with the following results:

- Reviews languishing in a "Ready for Review" state
- Drastic code architecture changes
- Being "Approved" based on social standing of the developer opening the request

Code Reviews are often seen as some kind of magic bullet to catching errors before they get merged into code bases. The ideal is that a developer gets a ticket, makes some code changes, and then shares those changes with everyone else on the team for feedback. The idea is that other developers, with perhaps more context, can catch potential issues or side-effects in the code that the developer doing the work may not have even known about.

Why the heck are you waiting until things are "Ready for Review" before you share you knowledge and context with the developer doing the task? Why are you telling them to "open a draft request as they go" so that you can share with them little tidbits of knowledge along the way.

Why do Code Reviews fail? Because it moves in-depth planning to the end of the development process once someone is already "done" mentally with a task.

## The Opposite of Code Reviews

The opposite of Code Reviews isn't NO code reviews.

The opposite of Code Reviews is Planning!

Let me regale you with tales of how development works in the Open Source world. I specifically pick the Open Source community because they operate the opposite way of most startups. Both have no budget, but OS communities have much longer (almost.. undefined in some cases) delivery times for new features. But not just any Open Source community - I'm specifically going to target communities that were around before 2008. Old Open Source. I'm doing this specifically to highlight not just the mechanisms that were used, but also how they contributed to this default of Planning over Code Reviews.

When a new feature was proposed - it didn't just appear on an issue board somewhere. Instead someone had to find the mailing list for a piece of software, get ON that mailing list, and then send an email to the development group explaining in detail what your feature was. If you were not clear, chances are you'd simply receive a short email asking for more explanation about a certain part, or possibly just outright dismissal of your idea. In either case, you'd end up needing to explain yourself further.

At some point someone on the development team might agree that your idea should be a feature. At this point, they start digging into the code. They probably aren't making the changes you need for your feature, but they're validating how they would go about implementing it. A followup email you may receive would actually include code snippets, specific files/line-numbers to reference, and links to external documentation.

This all happens in public. Other developers that see that email may realize that they have more context, and will chime in with additional edge cases, more documentation, maybe more code! This will likely go on for a while. Days is obscenely fast. Weeks is more reasonable. Eventually what will happen is that you'll end up with an email that details the goals for the feature, and a flurry of emails outlining the best way to go about it - complete with links to documentation, code, and even code snippets to implement the feature.

The goal for this email activity isn't to code the feature - it's to get it to the point that anyone can pick up this email chain and implement the feature based on the knowledge shared up front.

Once that's done, the developer may still run into cases they didn't think about and may message the group again. But often, things are planned out enough that the developer implementing the feature can solve the problem. This completed code is sent back to the group/maintainer for Integration. The "Code Review" at this stage is simply to make sure that things are happening as expected, to do one last check of the code, and to actually merge the changes in and test things.

Now, there's plenty of problems with this process - but the Code Review is rarely one of them.

## The Advent of Code Reviews

I want to place the blame squarely on GitHub for enabling and promoting Code Reviews, via mostly circumstantial evidence.

Prior to GitHub contributing to an Open Source project required you to get involved in the developer community for the project before submitting code. After GitHub anyone can stumble across a repo and open a Pull Request with code changes - without discussing anything at all.

That mentality has premeated current development processes everywhere. Now when you start work on a task, instead of having all the information/discussion up front the developer is expected to seek it out. They're expected to not just figure out that they may be missing information, but also figure out the best person to ask to find out what they're missing. The developer is immediately set up for failure unless they already know the codebase well. At any sufficiently large enough project, that is very unlikely to be the case.

Instead you end up open a code review that sits in review for days while engineers chime in with little fixes, slightly better ways of going about things, while you scramble to implement them and get your code reviewed again and again. Of course, some places recognize this problem and simply outlaw large scale architecture changes at this stage even if they are completely warranted.

See the problem isn't that the Code Review is bad - it's that the Code Review is the first time anyone has actually looked at the code related to the problem.

## The Solution to Code Reviews

There isnt one.

All planning up front without a deadline isn't helpful. All work without planning is pointless. But where your team draws the line between planning that's "good enough" and the length of time attributed to feature development changes frequently. It changes based on team composition, it changes based on the company state, it changes based on the market your company operates in. The only thing that's certain is that the amount of planning from feature to feature will be different.

You have to be able to make a call at some point that the planning is enough. But if your planning doesn't include pseudo code and links to code in the project, chances are it's not enough planning.

Planning should not be a single person event either. The whole team that would participate in the code review should be participating in the planning process as well.

Once the planning is done and a developer completes the code change, the Code Review needs to happen. At this point generally it's about testing change rather than re-architecting how the change is made. When we're at this stage, there's even more tools at our disposal!

Unit tests, Integration Tests, Synthetic/BlackBox Tests - all of these can help ease the time code spends stuck in code reviews. By minimizing the time spent in code reviews, and maximizing the time spent in planning instead we can achieve things like:

- Actually find bugs further downstream and upstream
- Propagation of Knowledge throughout the team
- Team Ownership of a feature
- Double check functionality/architecture

How fun.

## Notes

- This was originally published on Medium - https://xangelo.medium.com/code-reviews-are-a-failure-36b72a659de4
