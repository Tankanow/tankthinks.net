---
templateEngineOverride: njk,md
metaTitle: First Principle - Choose Boring Technology
metaDescription: Startups reward novelty. Founding engineers who survive long enough learn the opposite lesson. Here's why boring technology is a competitive advantage.
title: First Principle - Choose Boring Technology
description: Startups reward novelty. Founding engineers who survive long enough learn the opposite lesson. Here's why boring technology is a competitive advantage.
featuredImg:
subHeading: First Principle - Choose Boring Technology
tags: ['first-principles', 'founding-engineer']
date: 2026-02-23
updated:
published: true
---

<div class="col-start-3 col-end-9">

# First Principle - Choose Boring Technology

There is a version of a startup pitch that goes like this: "We're building on [latest framework], [newest database], and [thing that just left beta]." The room nods. The stack sounds impressive. The technical co-founder looks competent.

Six months later, the framework's breaking changes wipe out a sprint. The database has one known expert, and it isn't you. The thing that just left beta has a production bug with seventeen GitHub thumbs-up and no resolution date. The team is now debugging three unfamiliar failure modes simultaneously, at midnight, while a customer waits.

I've seen this movie. I've been in this movie. The sequel is always the same.

## What "Boring" Actually Means

"Boring" is a technical term of art, not an aesthetic judgment. It was articulated well by Dan McKinley in 2015,[¹](#1) but the underlying principle is Lindy:[²](#2) the longer a technology has been in production, the more likely it continues to work in production.

Boring means:

- **You know how it fails.** Not theoretically — someone has blogged about it, opened an issue, posted a Stack Overflow answer, and written a postmortem. The failure modes are documented and understood.
- **The community has production experience.** Not just benchmarks and toy apps. Boring tech has been run at scale, in anger, by companies with real stakes.
- **The hiring pool knows it.** When you need to bring on an engineer who can be productive in week two, boring technology makes that possible.
- **You've seen it before.** This is the one that actually matters. Your own familiarity with a tool's quirks, limits, and sharp edges is an asset you can't download.

Boring is not outdated. PostgreSQL is boring. Linux is boring. HTTP is boring. None of these are going anywhere. Lindy says they'll outlast whatever's exciting at the conference next month.

## Innovation Tokens

McKinley's most useful contribution is the concept of *innovation tokens*. The idea: you have a small, finite budget for choosing non-default, non-boring technology. Every time you adopt something unusual, you spend a token. Tokens don't replenish quickly. You have maybe three.

Spend them on the things that actually differentiate your product.

If you're building a payments company, your database is not a competitive advantage. PostgreSQL is fine. Spend your innovation tokens on the fraud model, the settlement logic, the thing that is genuinely your product. If you're building a real-time multiplayer game, your message queue might actually matter — spend a token there. Everything else: boring.

The trap is that everything feels important when you're building it. The authentication layer feels important. The search implementation feels important. The API framework feels important. None of these are important in the sense that matters: none of them are why customers pay you. Boring tools for undifferentiated problems. Innovation tokens for the actual product.

## The Hidden Cost of Novelty

[Code is Liability.](/2024/09/first-principles-5-code-is-liability/) Every line must be maintained. Unfamiliar technology multiplies that liability by a factor you cannot price in advance.

When you choose a novel tool, you inherit its entire unsolved problem space. The documentation gaps. The missing StackOverflow answers — because nobody's hit that edge case yet. The API that changed between the version in the tutorial and the version in production. The upgrade path that doesn't exist.

Every one of these is a context switch. Every context switch is [an attack on Flow State.](/2026/02/first-principles-7-flow-state/) When you're navigating unfamiliar failure modes, you're not doing your real work. You're doing primary research that someone else already did for the boring alternative.

There's a subtler cost too: knowledge concentration. Novel technology creates experts. The engineer who spent three weeks getting the new distributed database to behave becomes the only person who can reason about it. That's not a hiring advantage — that's a [hero culture](/2026/02/first-principles-7-flow-state/) with a technological cause.

## The Compounding Effect

Technology choices outlast their context. The database you choose in year one will still be running in year three, after two re-orgs and one complete rewrite of the service that talks to it. The message queue you configure at the beginning will become infrastructure — meaning the thing you've stopped thinking about and started depending on absolutely.

This is why the decision matters disproportionately to how it feels in the moment. Choosing a boring, proven technology is an investment in future maintainability. Choosing something novel is a bet on the tool itself: that it will mature, that the community will grow, that the breaking changes will slow down. Sometimes that bet pays off. Usually it pays off on someone else's timeline, not yours.

The founding engineer's job is to build systems with compounding value.[³](#3) Boring technology compounds. It improves incrementally, with backward compatibility. It accumulates community knowledge. It gets more boring — which is to say, more reliable — over time.

## When to Break the Rule

The rule exists to be broken deliberately, not accidentally.

Break it when boring genuinely cannot solve the problem. Not "boring doesn't solve the problem as elegantly as I'd like" — when it actually cannot solve the problem. When you need a capability that simply doesn't exist in the mature ecosystem.

Break it when novelty *is* the product. If you're building the next generation of some infrastructure category, you might need to be at the frontier. That's a legitimate choice. But it's a whole-company bet, not a tooling preference.

Do not break it because:

- The new thing is exciting
- You want to learn it
- It scored better on a synthetic benchmark
- The conference talk will be more interesting
- The job postings are higher

These are all real motivations. They are all the wrong basis for a founding architecture decision.

## tl;dr

Boring technology is Lindy. Its failure modes are documented, its talent pool is deep, and its problems are already solved by someone else's Stack Overflow answer.

You have a small budget of innovation tokens. Spend them on the actual product — the thing that differentiates you. Spend boring everywhere else.

The founding engineer who ships reliable systems on dull technology is more valuable than the one who ships interesting systems on interesting technology. Customers don't see the stack. They see whether it works.

# Notes

#### 1
Dan McKinley, ["Choose Boring Technology"](https://mcfunley.com/choose-boring-technology) (2015). The original blog post and associated slides remain among the most useful artifacts in the engineering canon. Lindy confirms: it was true in 2015 and it's true now.

#### 2
[Respect Lindy — First Principle 3](/2023/08/first-principles-3-lindy/)

#### 3
[Code is Liability — First Principle 5](/2024/09/first-principles-5-code-is-liability/). The inverse of code-as-liability is system-as-asset: infrastructure that accrues value over time because it's stable enough to be trusted and boring enough to be maintained.

</div>
