---
title: "Git Workflows Suck"
date: 2021-07-15T12:16:45-04:00
tags: ["git", "development", "engineering processes"]
summary: Common pitfalls with everyones "git process"
---

I'm tired of all the git workflows. I'm tired of talking about the best way to craft commit messages. I'm tired of how people pile on the best way to do PRs. I'm sick of people picking apart architectural decisions in a PR. I'm tired of opening PRs only to have no one look at them for days while I continue to harass people into reviews. I'm over the fact that I don't think I've ever seen a single person clone a PR locally and actually verify that it does what it says it does.

And I don't think I'm alone in these problems. Almost every engineering team I've ever worked with has their own slightly customized git workflow that "works" for them. And every one has had the same problems I mentioned above. Honestly I think it's just cause no one uses git properly.

The problem, of course, is not "using git". The problem is from all the interconnected bits around it. Writing a commit message is easy. Writing a commit message on code that no one at your company knows anything about, where you're pretty sure it does what you want, is much harder. In order to even talk about "using git properly" there's so much background that needs to be talked about.

## What is git?
Git has this as the first sentence on it's site:  
> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 

Git is a free and open source *distributed version control system*.

That's git. Distributed version control system (DVCS).

Traditional Version Control Systems (VCS) tended to be centralized. That is you had a "server" where your code resided. Developers would "check out" the files that they wanted to work on. Do the work locally, and then re-upload them to this central server. git changed that model. EVERYONE has a copy of the code. You make your changes locally, and you can push to anyone else you'd like! You could make a change, and then send that code to a friend directly from git USING git. Push to their repo. They could do the same to you. Instead of having one central server that contains all the code, people work with each other.

## What are Forges?
Of course, that works really well when you're a small group that's making changes. When things get larger, it can be a bit more difficult. There are inherent problems with having copies of your code scattered around. Who has the most recent version? Who has the authority to merge changes in? How do you communicate these changes to everyone? 

These problems are what propelled tooling like GitHub, GitLab, and BitBucket into the spotlight (known as a Forge). They became these central repositories for your code that allows you to not have to think about that. They allow you a central location where you push/pull your code. They provided an interface for Pull Requests. The ability to track issues and correlate them with code changes. They provided a service that filled a gap in git tooling. They even started publishing general "workflows" on how best to use git that are all slight variations on this:  

* clone from remote
* create a new branch from master
* make your changes
* commit your changes
* push your changes in your branch to the remote
* create a PR in the UI
* Ping some reviewers (maybe they're automatically assigned)
* Back/Forth on review/code changes
* Merge the approved branch into master

Note that the "workflow" is only a small portion of what your actual workflow will look like at your company. It literally is just "how do I interact with git and get this change approved". There are many steps before/after.

There are variations, as always. [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) talks about conventions for branch naming/merging processes. [GitHub Flow](https://guides.github.com/introduction/flow/) and [GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) do the same, but with a focus on their tooling instead of general git level instructions.

## The Big Git Workflow Problem
The problems people have with git workflows tend to stem from two areas: Pull Requests and Branching Strategies. I'm going to avoid chatting about branching strategies here because there is a lot more to consider than just naming conventions. A lot of companies have a lot of additional tooling that is very integrated into the git branching styles used. Things like CI/CD that use environment branches, merging to master auto-deploying to certain environments - all these things force additional constraints on the branching strategies decided upon. Often it's very hard to change these things and you're left in an in-between state indefinitely that is much worse than the original. 

Instead I'm going to focus on Pull Requests and the processes around it: Commits, Pull Request Reviews, Merging Strategies.


### Commits
The smallest unit of the PR is the commit. Now, even at this stage, there's lots of argument on how to proceed but there's at least one "agreement": A commit should be one thing.

Of course, that's much easier said than done. A lot of the time you'll be in your code and then you may see some small bit of logging or metrics that could be improved. It's only a one line change? May as well make it now to improve things for everything. Sometimes the changes you're making end up really being two indepedent changes that COULD work separately, but only together do they make a whole feature.. is that one commit or two? 

Once you figure out what's going to be IN your commit, then you get to figure out what message you to leave your future self.

I used to think that [https://chris.beams.io/posts/git-commit/](https://chris.beams.io/posts/git-commit/) was a great example on how to write commit messages. I've since changed my mind a bit to be less prescriptive about process and more descriptive about outcome.

The goal for a final commit message is that when you look at this message in a year, what's the best way for you to recontruct the context that you had when you came up with your solution. In order to do this you need to have:  
* A good summary sentence, as short as possible and no shorter (the hardest part, I always write this last)
* A good explanation of what your single change is. Go as in-depth as you want, but if you find yourself writing multiple paragraphs, put that in a separate document and then add it to the references section.
* A References section with links to ticket/issue/tasks related, any documentation you used to come up with your solution (possibly links to other repos if you used a particular pattern that you found elsewhere)

As long as you have those 3 things, you're free to do whatever you'd like.

But note that this is for your FINAL commit. That's very different from the active commits that are happening that people use as "save points" on their work. Commits with messages like "fix typo", "does this work?", "how about now?" are normally used by devs while they're working on things. These are what I call "active" commits. That is, you're actively working on something and using git as a bit of a save point for you to go back if you want, or not. Maybe you're wroking on something and just need to get someone else to take a look so you make a random commit, push it to your forge, and send someone a link to review unofficially. These are important steps in the development process.

These types of active commits are fine, but once you're DONE and you're happy with what you did, it's time to REBASE your branch. Rebasing seems like a bit of an ambiguous word, but what we are going to be doing is taking a look at the git commit history you've created, and then squashing them all up into a single commit or maybe a couple if you tried to do multiple things. I don't want to go into all the details about this, because there are plenty of instructions for how to accomplish what you want [this website being one of the better ones](https://git-rebase.io/) I've run into.

Rebase allows you to see all the commits between two different commits, and allows you to decide what to do with them. So if you made 10 commits that were "fix this typo" and one that had the actual implementation, you could choose to squash all those commits in a single one just by telling git "squash this commit" and choose to "pick" the commit that you want to remain as a commit. Git even gives you a nice little interactive interface that allows you to do this (it is a text based so don't get too excited). 

Rebasing is important because it allows us to move from an "active commit" state to a "code complete" state. We are officially declaring that we are done with this bit of work and we don't intend to do anything more with it as it relates to the task that we're working on. When we rebase we get a chance to edit your final commit message, which should ideally follow the rules above.

### Pull Requests
Pull requests is where I have most of my problems. PRs are a way for devs to share the changes they've made with other devs, and gather/address feedback. Things you may have missed in your changes, other repos to look at for similar things. In large orgs it's not unlikely that someone might point out to you a repo you've never heard of that does something similar that you can take inspiration from. These are valuable interactions to have - but they happen at the wrong time.

Pull Requests are always at the end of development process on a task. Once you've finished your changes, you submit them for review. I think this is just too late, and I'll explain why with some... history!

As I said before, git was designed to be distributed because the developers were distributed geographically. This was in "ye olde times", where slack didn't exist and IRC was king. In order to communicate effectively, and keep the conversations public for the commnity, these developers utilized the lost art of.. mailing lists! These lists were available for anyone with an email to join and follow along in the conversation. One of the things that this really fostered was bringing up conversations around code first.

Before anyone actually DID the work there was plenty of back and forth in the mailing list about the change that was going to happen. Not just theoritcal "we could do this", but code samples would be sent around, links to relevant code bits would be included so everyone had the same context. The evolution of the change was publicly documented and the subject matter experts were able to weigh in on the how they'd approach the change. This would go back and forth until there was a VERY clear understanding of what the change would look like. Then someone would take that and get it over the line. They'd then send the patches they made back to the mailing list for people to look at. This almost ALWAYS involved taking the patches, applying them locally and doing doing some testing to validate that it was working. At this point, the goal is that changes at this point are not major architectural ones, but smaller ones to tackle edge cases that people might have uncovered during testing.

This is the process that PRs are attempting to replicate -> except because of how most companies operate the details of the change only happen when you start working on it, and the architectural decisions are often only reviewed once they've been made. 

I think "Pull Requests" should really be put into multiple categories. There's an initial invesitgation/proposal process where people communicate and collaborate over how to approach the solution to a problem. This should definitely be time-boxed as it's too easy for this to stretch into infinity. The goal is to do those investigations and allow SMEs to contribute to the conversation early. The goal for this document is to have a very clear understanding of the change needed to be made. Schema changes, repos that might need to be adjusted AND WHERE. If there are no links to code within this then you're probably not done. Someone should be able to grab it and move ahead without necessarily being part of the conversation to craft the solution.

Then there's the Review process. After the code is complete sharing it with others and having them RETRIEVE YOUR CHANGES AND TEST THEM LOCALLY. Testing locally is important for many reasons - often the main one is that your test suite isn't robust enough, or it isn't trustworthy (then delete them, but that's another story). But also it highlights pain points in your development process that you may not deal with always. Missing documentation for how to run something, or how to set up some data for a test. Not being able to run your tests locally because they take too long. Having people really test your code is a great final step to getting your code reviewed.

## Conclusion
This was a lot of text - but thinking about development workflows/optimizations and really understanding where the problems/bottle-necks are is something I'm really passionate about. This was also a very high-level introduction to these ideas. There will be a follup post on commits and rebasing itself that will hopefully make things a bit easier for people to understand. If you have any questions, don't hesitate to reach out to me.
