---
title: Git Branching Strategies
date: 2021-07-16T16:14:40-04:00
tags:
  - git
  - development
  - dev workflow
  - engineering processes
  - publish
summary: A topic that every developer in the world has an opinion about
lastmod: 2024-12-12T05:25:42.443Z
---
In a [previous](/posts/git-workflows/) post, I talked about git workflows and I outlined the two big problems I see with git workflows:

* Pull Requests/Reviews
* Branching Strategies

I took the easy route at the time and just talked about Pull Requests/Reviews. But I was requested to throw some thoughts out around branching strategies and how they should work.

The reason I think branching strategies are such a complicated topic is because it touches more than just git. As an industry we've mostly settled on the idea of Continuous Integration and Continuous Deployment (CI/CD). These processes tend to tie directly into git and have deep ties to your branching strategies. In addition branching strategies tend to reflect the testing architecture and experience level of the engineering organization itself. It's not the simple strategy that workflows like GitHub Flow like to pretend it is. Whether you like it or not, your git branching strategy is already embedded in your organiztion and reflected in your development process. It's your job to discover what that is and then decide if it's even worth it to change. Sometimes, unfortunately, even though it may not be what you consider ideal, the strategy the team is currently using is MOSTLY one that works for them. At that point it's just a matter of uncovering bottlenecks (oh don't worry, the engineers will tell you what those are) and mitigating them.

The two main branching strategies people tend to advocate for are "Environment Branching" and "Feature Branching" so lets talk about the strategy itself, and then see how it affects your org.

## Environment Branching

Environment branching models the fact that the software at your org has some kind of "release cycle" where a series of patches (in the git sense) are first in a "development" environment where the developers involved can work on the feature without impacting others. We then merge the dev branch into a "staging"/"testing"/"integration" environment where a patch or series of patches are released for other people in the org to test. Often this involves a QA team looking at the changes and validating that there aren't any regression tests. Finally once everyone is happy we merge staging into production and deploy it.

```Environment branching example
┌┬──────┐    ┌┬───────┐    ┌┬──────┐
││ Dev  │    ││ Stage │    ││ Prod │
└┴──┬───┘    └┴──┬────┘    └┴──┬───┘
    │            │             │
   ┌┼┐           │             │
   └┼┴───────────┤             │
    │            │             │
   ┌┼┐          ┌┼┐            │
   └┼┘          └┼┘            │
    │            │             │
   ┌┼┐           ▼             │
   └┼┴───────────┐             │
    │            │             │
   ┌┼┐          ┌▼┐            │
   └┴┘          └─┴────────────┤
    ▼                          │
                              ┌┼┐
                              └─┘
```

Note that not every commit to the dev branch results in an equivalent merge to the staging branch. Infact sometimes there'll be plenty of back/forth on the dev branch. Finally a set of features is selected and deployed to staging. Once it's been debugged, it goes off to production. Of course, this is when everything goes smoothly. Most times you'll have hotfixes that you'll need to make to prod to fix additional bugs.

Different orgs deal with that differently. Sometimes we'll have "hotfixes", which bypass the branching model entirely. It allows us to take whatever is it prod, branch from it to fi xa bug and merge it straight back into prod without going through the other branches. That hotfix is then ported back to development.

This model, of course, has its pros/cons. But if it works for your org then it's right for your org. I've outlined  some caveats and things to think about if you decide to go with the environment branching model.

### It forces a release cadence

When you have a single team working in this model it's very easy. It also maps so cleanly to traditional engineering pipelines that it doesn't require a lot of explanation or documentation. But this requires that each team working has its own "dev" branch/environment to ensure that they're not impacting others testing. But this is expensive, so there's a tradeoff. Often you'll find "shared" dev environments, which are really just a very broken integration environment where you can't really trust what's happening, and a less broken integration environment. Just the inclusion of an environment that's considering "integration" requires scheduled releases.

You need to ensure that your features aren't impacting other developers and so you need to coordinate between internal teams. This takes time. It means while your changes can be tested in tandem in "dev", eventually you'll need to settle on what's going out to production adn only those patches get moved into staging. Those patches get tested on for some time and then move into production. There you have a release cadence. Your cadence might be a day, or it might be two weeks. It doesn't matter - that is your cadence. That is the minimal amount of time, on average, that it takes for a change to make it to production.

There are always ways to mitigate this problem, but I'd argue that it isn't a real problem. Having a release cadence is perfectly fine once you have a product that has paying users. It ensures that releases can happen during low-volume traffic times and doesn't impact as many users. It also ensures that users know when they can expect new features.

* Have dedicated dev environments for each team with no shared resources to speed up the development time. Keep the "staging"/"integration" environment the only place where multiple features/bug-fixes are tested in tandem.
* Declare your cadence officially so that everyone knows when the cutoff for a release is. Stick to this. No last minute sneaking in of changes allowed. This allows internal/external expectations for when new features will be rolled out.
* Understand that there is a difference between deploying a change and releasing it to users.

### It's very easy for the branches to get out of sync

Since you now have multiple teams working it's easy for features that everyone thinks is ready to make it to integration.. only to discover that they are quite broken. So we need to pull them out so that they're not impacting anything else. But how do you do that? You can't just muck with staging directly since merges from dev->staging will then break. So you need to actually back the change out in dev, then merge dev->staging to remove the change. But are you using squash+merge or rebase functionality? That can affect the method of resolution you decide on. Regardless, you can expect dev/staging/prod branches to get out of sync and you'll need to manually intervene to sort that nonsense out.

### It's easy for broken things to get out

The dev environment will probably be mostly broken - with working state only conveyed via some internal communication among devs. Merging that right into staging will cause unexpected bugs or broken features to make it out. The best way to deal with this is to have each team working on a single feature/code-base and having dedicated development environments for each team. This way you ensure that a team is able to test what they are working on in isolation. Once they're sure it's working they'll be able to merge their fixes into the integration environment. This is suspiciously close to the other model of branching.

### Conclusion

I'm really not a fan of environment branching, but I do concur that when there are processes/releases cadences already in place that are immovable (imagine you have a 3rd party group that needs to do testing on releases before they go out) then this can be a good way to handle dependencies. Personally I think environment branching is easy for SREs/devops teams to think about and they map very cleanly to how software orgs traditionally worked. It provides the lowest barrier to adoption - but it has enough problems that it can seem like the new process doesn't work as well as the old one.

I would be wary about moving an org TO this model as there's just a lot of things that can go wrong that will result in certain individuals spending time rectifying process problems rather than business ones.

## Feature Branches

This is the other model of branching that I think attempts to tackle some of the major problems with environment branching (while offering up a few of its own). In feature branches you don't have a single dev branch.. instead every thing you work on gets its own "dev" branch. It's expected that while you're working on your thing your feature branch is probably in a "broken" state. You keep adding commits to it and eventually when you're happy you merge it to your integration environment branch. Once it's tested, the integration environment gets deployed to production.

Feature branches aim to solve the problem of environment branches by integrating the "staging" and "production" branches. Devs work on feature branches, and then merge their features into "integration" environments. When people are happy with that, the features get moved into production environments. There's a lot less moving parts (on the surface) and so this is normally the process that people go with.

## Branching Strategies Affect Everything

These branching strategies sound great - but branching strategies aren't an isolated problem that can be solved without affecting anything else. Environment branches require you to have multiple environments for your code. It requires you to have "development" and "staging" and "production" environments. All branching strategies require you to differentiate between "code" and "build artifacts" which are actually what you should be deploying.
