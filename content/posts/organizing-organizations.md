---
title:  Organizing Organizations
summary:  A walk through various organizational structures
tags:  ["engineering org"]
draft: true
date: 2024-06-01T23:29:09.966-05:00
---

> A lot of what I'll be waxing poetic on will be focused around the tech industry, and smaller companies in general. But the truth is all small companies think they're large, and large companies get so large that they have small companies within them. The real truth then is that you are stuck in a never ending cycle - a wheel of workplace - to borrow and then bastardize from Buddhism. But rather than be disheartened, the repetition is required because the collective you is always changing and the new change is never quite the same because of it.

I was lucky that early in my career I got the chance to really dig into organizational structures. It happened at a time when I didn't really have a lot of obligations outside of work. The startup that I had co-founded had been doing well, I had naively thought, and so I could devote the little free time I had to figure out how to scale this inevitable behemoth of a company.

## The Tribes model
A few years after that crashed and burned, I got the opportunity to put my knowledge into practice. Spotify had just published their "tribes" model - which is a matrix org with jazz hands. It took the SaaS world by storm. Cross functional teams centered around a particular system. In spotify's world, for example, search was a "tribe". There was a group of people devoted to just search - they could really focus on it. The tribes model was a "matrix" because it offloaded your functional growth among a lateral management line. 
![The spotify tribes matrix](/img/tribes-model.png)

In this example, each line of business has its own team needs. There could be any number of these individuals organized around the business need. This allowed them to iterate and become SMEs in their area of focus. This is hugely important to the line of business. Having a long running team that you can take through all stages (Forming, Storming, Norming, Performing) meant that you could really optimize that line of business.

The problem with this, is the exact same as any matrix organization. The person that owns your line of business may have very little understanding of what you do actually do. Imagine a team focused around search. The lead for the team could really be focused on the user experience.. but there's a deep technical aspect to real-time search. If they don't understand it, it can be hard to gauge how well individuals are working. 

Another inherent issue is isolation. Front end engineers within a line of business do not get to interact with other front end engineers. Things become inefficient as multiple teams work through similar classes of problems and each of them come away with a slightly different method that works for them. 

Traditionally in a matrix org you report to two individuals - your direct manger, who ran the particular team. And then a functional lead, who was the expert in what you did. These two often clash as the functional lead rarely has control over what you do day-to-day, and then business lead has no interest in larger scale functional changes.

This is true of all matrix organizations. 

The truth is what Spotify had found is that by providing purpose to a diverse group you could achieve great things. 

## It's always Maslow

![Maslows Hierarchy of Corporate Needs](/img/maslow.png)

This Maslow guy was no slouch it turns out. In the context of a job, they are ideally taking care of the first two levels (Bottom up). They hope that you feel a sense of connection and belonging because then you are "aligned" with the companies vision. Once you have those things, we introduce a performance review and bam - now you know about yourself and where you stand. You can understand your unique skillset and the areas you still need to grow. It helps you identify those areas in others and fosters a natural respect within the company. Everyone knows that one guy who you go to when things explode. 

When viewed through this lens, all organizational changes attempt to change three things:  

    - Your sense of connection to your team
    - Your self esteem and confidence within the team
    - What your team is responsible for.

## Matrix: Reloaded

Armed with this knowledge, we can revisit the tribes model with a little more insight. All re-orgs come with the risk of severing your sense of connection to your team. The tribes model hopes that by providing a shared purpose, the sense of connection to your team will grow. 

A standard growth cycle of a team through the Forming, Storming, Norming, and Performance phases takes care of the self-esteem portion. Coupled with performance reviews. And your purpose has already been given to you. 

But what actually happens is that it severs your connections with other individuals within your discipline. You do form closer bonds with your team, but you lose sight of the larger actions being taken upon by your function and so your career can stagnate, without looking like it. What can (and does) end up happening is that your team is focused on your immediate manager and the goals of the Business Unit. Often the thing that suffers is your growth within your function. Backend engineers don't really progress in skillset from jr -> mid -> sr, but instead get stuck in a state where they aren't aware they may be falling behind. The truth is there are known knowns, and there are known unknowns. But there are also unknown unknowns (I don't know why I'm obsessed with this phrasing by Rumsfeld). And the scope of your unknown unknowns is limited by your exposure to your function. 

Some people can find this growth in communities outside work. Some people can't. It's not wrong one way or another - but it is important that re-orgs that jump to matrix's understand this. You are trading overall growth for specific growth. Now that also isn't wrong - infact, I'd argue this is precisely what a PhD is. The important thing is that we make these decisions explicitly. The only things that bite you in the butt are implicit decisions.

## The two-to-three Legged Stool

A nother model that is favoured because of the way it implicitly arises is the two-to-three legged stool. In this system you have 2 or 3 major divisions in your team:  

    - Engineering, lead by an engineering manager
    - Product Manager, lead by some kind of VP of Product
    - Designer, lead by some kind of VP of Design

Occasionally the designer is folded into the product org under the guise (maybe appropriately) of "user experience". 

This model does have some benefits, but the truth is this is model is never an explicit decision - it arises from natural growth. You have some engineers and a Product Manager working together. As the team grows you add more engineers, eventually you have enough engineers that a "tech lead" isn't enough -> so one of them becomes an Engineering Manager. Bobs your uncle. 2 legged stool. 

I dislike this model because it splits things unevenly. The PM is being judged on their ability to deliver, but that is being controlled by a different entity - the engineering manager. Often the two have to work together and you get plenty of arguments like "we are supposed to get a sprint to work on tech debt" or "we said 20% of our time could be focused on these devex tasks." 

I find this often ends up happening when you have a large dichotomy higher up in the company that is resolved through collaboration. What happens is that you have two individuals who work well together - one on product, and one on engineering. Each one is comfortable staying out of the others domain and they've hit some kind of equilibrium on how they work together. They're given full control of the down-stream org and they implicitly replicate their relationship without any of the history. 

It's not that I don't like this model, it's that I don't like the implicit nature of this model. When it works, it works amazingly well. Engineering managers can carve out time for their team to not just deliver on the product, but also make time to improve the developer experience. But it separates the workload in "things we have to do" and "things we'd like to do" - which is not a good place to be in.

## Random Thoughts
  - I often send around rough drafts of these and one of the questions I got was "what about the STO model". The truth is the STO model is nothing more than a matrix org where the business unit leader is given a few more powers. Depending on how high up the STO is defined really just changes who reports to them - but the org remains matrix'd. 
  - At around the same time the [OKR Video]([https://www.youtube.com/watch?v=mJB83EZtAjc](https://www.youtube.com/watch?v=mJB83EZtAjc)) at Google started to make the rounds and they seemed to go hand in hand. Taking your cross functional team, and giving them a single area of focus, allows for specialization. The long running team facilitated experimentation which fits perfectly into the realm of OKRs. This worked even better when viewed under the umbrella of agile. 

