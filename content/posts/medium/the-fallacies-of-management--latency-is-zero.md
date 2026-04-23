---
date: Thu, 23 Apr 2026 12:21:01 GMT
draft: false
medium_link: https://xangelo.medium.com/the-fallacies-of-management-latency-is-zero-7f57eb414816?source=rss-d5a790d38792------2
slug: the-fallacies-of-management--latency-is-zero
summary: In the first post in this series around “The Fallacies of Management” (read
  on site), the fallacy was assuming the network was reliable.
title: The Fallacies of Management — Latency is Zero
---

You say the thing in a meeting. You send the Slack. You write the email. You explain the priority. And you assume the message has been delivered, interpreted correctly, and acted on in the way you intended.

But even when the words arrive, the meaning is still reconstructed locally.

That was the point of the first post.

This one is about the next mistake.

Let’s say the message \*does\* arrive.   
Let’s say it \*is\* understood.   
Let’s say the person \*would\* have acted on it correctly.

There is still another problem.

It might arrive too late.

That’s the next fallacy:

**Latency is zero.**

In distributed systems, latency is the delay between when a message is sent and when it becomes useful to the recipient. And if you’ve spent enough time building systems, you know that a delayed message can be almost as bad as a dropped one. Sometimes worse. The system doesn’t pause politely while the packet catches up. It keeps moving. Timeouts fire. Retries happen. State changes. By the time the message lands, the conditions that made it useful may already be gone.

Management works the same way.

A manager will often think:

* I’ll get to it.
* I’ll give the feedback next week.
* I’ll clarify priorities after this meeting.
* I’ll talk to them once things calm down.
* I’ll recognize that good work in the next 1:1.
* I’ll deal with that tension if it comes up again.

But organizations do not freeze while you catch up.

People continue executing against whatever local state they currently have. And if your message is delayed, they won’t wait for it. They’ll infer. They’ll compensate. They’ll route around the silence. They’ll make the best decision they can with stale data.

And once they do, you’re no longer communicating into a neutral system. You’re communicating into a system that has already adapted without you.

That’s what managers miss when they assume latency is zero.

#### The difference between “eventually” and “in time”

One of the reasons strong engineers often make strong managers is that they already understand something the industry tends to obscure: correctness isn’t just about content. It’s also about timing.

A perfectly correct answer that arrives too late is not a good answer. A fresh-but-imperfect signal is often more useful than a perfect but stale one. A delayed response is still part of the system’s behaviour.

That instinct transfers cleanly into management.

A lot of management advice gets framed as though the hard part is simply saying the right thing:

* give the right feedback
* make the right decision
* set the right expectation
* send the right message

But management isn’t only about being right.

It’s about being right while the system can still use the information.

That means timing is part of correctness.

A message that arrives two months after the behaviour it was meant to shape is not the same message. A decision made after the team has already improvised around your indecision is not the same decision. Praise delivered long after the moment has passed does not reinforce in the same way. Conflict addressed after resentment has hardened is no longer the same conflict.

With people, latency doesn’t just reduce usefulness.

It changes meaning.

#### A small example

I’ve seen this happen in a way that’s almost boring in its consistency.

Someone on a team does something slightly off. Maybe they handled a disagreement poorly in a meeting. Maybe they were too sharp in how they pushed back. Maybe they made a decision that was technically defensible but socially expensive. The kind of thing that usually does not require a dramatic intervention. Just a quick correction. A short conversation. A little bit of calibration.

But nobody says anything.

Not that day.   
Not that week.   
Not in the next 1:1.

So the person keeps going.

And because they keep going, one of two things usually happens. Either they assume the behaviour was acceptable, or they vaguely sense something is off without knowing what. Both are bad. One creates reinforcement. The other creates anxiety.

Then, weeks later, the feedback finally comes.

And now it lands differently.

What could have been: “hey, small note, watch that edge”   
lands as: “I’ve apparently been under silent review for a while.”

The content may not have changed much. But the latency changed the meaning.

That’s the management version of stale state. The correction arrived, but it arrived after the system had already evolved around its absence.

#### Feedback latency

This is probably the clearest example of the fallacy.

When feedback is timely, it still feels attached to the thing itself.

The person remembers the meeting. They remember the decision. They remember the tone they used, the sentence they said, the place where things started to wobble. The correction still feels local. Small. Useful.

There’s a direct line between action and response.

But when feedback sits in the queue, something else happens.

The original event starts to decay. Memory blurs. Other events pile on top. Patterns emerge, or at least seem to. And by the time the feedback is finally delivered, it doesn’t land as “here’s a small adjustment.”

It lands as judgment.

Not:

> that choice could have been better

But:

> I’ve been silently collecting evidence

That is a completely different emotional experience.

The content may be the same. The managerial intent may even be good. But the latency changed the meaning.

This is why so many managers accidentally turn coachable moments into performance narratives.

They wait because they want more certainty.   
They wait because they want to avoid awkwardness.   
They wait because they want to phrase it perfectly.   
They wait because one data point doesn’t feel sufficient.

And in doing so, they allow what could have been a quick correction to solidify into something heavier.

Feedback has a half-life.

Given quickly, it feels like guidance.   
Given late, it starts to feel like a case being built.

That’s not because people are irrational. It’s because the delay itself becomes part of the signal.

> Decision latency

If feedback latency is about delayed correction, decision latency is about delayed coordination.

A team asks for direction.

Which option are we choosing?   
Who owns this?   
Is this a one-off or a pattern?   
How much time should we invest here?   
Are we optimizing for speed or polish?   
Is this thing actually a priority?

Leadership does what leadership often does. It thinks. It gathers context. It waits for one more meeting. One more dependency. One more opinion. One more round of alignment.

Meanwhile, the team keeps moving.

Because it has to.

No one says, “let’s suspend execution until management reaches consistency.” That’s not how organizations work. Just like distributed systems, they continue under partial information.

So local heuristics take over.

Someone makes a call.   
Someone assumes the old rule still applies.   
Someone interprets silence as approval.   
Someone treats “not yet decided” as “probably yes.”   
A temporary workaround becomes the default path.   
An unofficial answer appears and starts behaving like an official one.

And when leadership finally does make the decision, it discovers the cost has changed.

Now the decision is not just “what should we do?”

Now it’s:

- what do we undo?  
- who needs to be realigned?  
- what work must be thrown away?  
- what assumptions have now spread?  
- which relationships have already adjusted to the absence of clarity?

Every delayed decision gets replaced by an unofficial one.

That’s one of the most important management truths nobody tells you.

Teams are not empty containers waiting for decisions. They are active systems under load. If you do not provide a timely coordination signal, the system will generate one internally.

It may be reasonable. It may even be clever. But it may not be globally optimal.

And at that point your job is no longer to decide in a vacuum. It is to reconcile the organization back from the local optimizations your latency created.

#### Recognition latency

Managers often treat praise as optional decoration.

It isn’t.

Recognition is reinforcement. It tells people what matters. It tells them what leadership notices. It tells them which behaviours are seen, valued, and worth repeating.

And like every other signal, it decays.

Praise that arrives close to the behaviour strengthens the connection. The person can still feel the effort. They know what they did. They know what tradeoff they made. They know what they prioritized. They know what almost fell apart and didn’t.

Late praise is not useless. But it is weaker.

The link between action and acknowledgment gets fuzzy. The energy of the moment has passed. The behaviour no longer feels actively reinforced; it feels historically recognized.

And if you do this consistently, people learn something you probably didn’t intend.

They learn that important work can be invisible for long stretches. They learn that cleanup work, glue work, mentoring work, and context-carrying work are only sometimes legible. They learn that leadership notices outcomes, but not always contribution.

Praise is also a signal.

Signals decay.

If you care about shaping a team, you cannot treat recognition as something that can always be deferred without consequence.

#### Intervention latency

This is where management gets expensive.

A small misalignment between two people.   
A little friction around ownership.   
A recurring pattern in meetings.   
A person who keeps shutting others down.   
A high performer quietly accumulating resentment.   
A team that is beginning to operate with two incompatible versions of reality.

These things are often cheap early.

Early, they are mostly about interpretation. A little awkwardness. A little clarification. A small conversation. A modest reset.

Left alone, they change category.

The technical issue becomes a relationship issue.   
The relationship issue becomes a trust issue.   
The trust issue becomes part of the team’s narrative.   
Now everyone has a story.   
Now there are sides.   
Now your intervention is not entering a fresh situation; it is entering a settled mythology.

This is why delayed management is so costly.

The work is no longer just fixing the original problem. The work is now unwinding all the meaning people built in the silence.

Most management problems are cheaper when they are still mostly technical.

By the time they become symbolic, they are much harder.

#### The people factor

In the first post, the hard part was that people do not receive messages like machines do. They bring their own context, insecurity, memory, and interpretation to what they hear. The words arrive, and then meaning is constructed locally.

Latency makes that even more complicated.

Because with people, delay is not merely transport time.

Delay changes interpretation.

Delayed praise can feel perfunctory.   
Delayed criticism can feel political.   
Delayed support can feel insincere.   
Delayed clarity can feel like cleanup rather than leadership.   
Delayed intervention can feel like abandonment.

This is one of the places where management becomes more complicated than distributed systems.

In software, a delayed packet does not develop self-esteem issues.   
A stale cache does not wonder why nobody told it sooner.   
A replica does not build a private theory of your motives.

People do.

Which means latency in management is not just about throughput or freshness. It is also about trust.

Silence is not neutral.

People interpret that too.

If you don’t say anything, the system does not remain in a waiting state. It begins constructing meaning around your absence.

And just as in the first post, the meaning people construct is often not the meaning you intended.

#### Why this is another reason strong engineers can grow into strong managers

This is the broader point behind the series.

There is a persistent idea in tech that engineering and management are almost opposite disciplines. That once humans become the medium, the system-thinking instincts developed through engineering stop being useful.

I think that’s only half true.

A good engineer doesn’t just think in code. They think in coordination, tradeoffs, failure modes, timing, state, and recovery. That is exactly why the distributed systems analogy works so well as a management frame in the first place.

The challenge is not that engineering instincts stop mattering.

The challenge is that they have to be adapted to a noisier runtime.

Humans are not deterministic components. They are meaning-making nodes with memory, emotion, pride, fear, and different local context. But that doesn’t make management alien to engineering. It makes it engineering under uncertainty, with softer interfaces and higher interpretive cost.

A strong engineer already knows stale state is dangerous.   
Management is full of stale state.

A strong engineer already knows that coordination delays create strange local behaviour.   
Management does too.

A strong engineer already knows systems do not pause for missing information.   
Neither do teams.

That doesn’t mean every great engineer will become a great manager. It does mean the distance between the two is smaller than people pretend.

#### What to do about it

If latency matters in management, then the managerial job is not just to be thoughtful.

It is to reduce the round-trip time on the signals whose value decays quickly.

That means:

* Give feedback while the moment is still alive
* Clarify priorities before the team is forced to invent its own answer.
* Recognize good work close to when it happens.
* Address tension before it becomes identity-shaped.
* Don’t wait for perfect certainty when a timely imperfect signal would keep the system healthy.

Not everything requires urgency. Some decisions should be slow. Some feedback should be considered carefully. Some situations do benefit from waiting a beat.

But part of becoming a good manager is learning which signals have short half-lives.

And then treating those signals with the same respect a good engineer gives to freshness, queue depth, and propagation delay.

#### TL;DR

In distributed systems, a delayed message can be almost as damaging as a dropped one.

In management, the same is true.

Feedback, decisions, recognition, and intervention all lose value as they sit in the queue. Worse, with people, delay doesn’t just reduce usefulness. It changes how the message is interpreted.

If it matters, don’t just say it clearly.

Say it while it can still change the system.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=7f57eb414816)

---

This was originally published on Medium - https://xangelo.medium.com/the-fallacies-of-management-latency-is-zero-7f57eb414816?source=rss-d5a790d38792------2