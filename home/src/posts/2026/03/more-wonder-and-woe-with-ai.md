---
templateEngineOverride: njk,md
metaTitle: More Wonder and Woe with AI
metaDescription: An AI-assisted API build took 5 phases instead of 3 because domain knowledge stayed in one person's head. Eric Evans told us why in 2003.
title: More Wonder and Woe with AI
description: An AI-assisted API build took 5 phases instead of 3 because domain knowledge stayed in one person's head. Eric Evans told us why in 2003.
featuredImg:
subHeading: What Happens When You Skip the Map
tags: ['ai', 'founding-engineer', 'devaiops', 'first-principles']
date: 2026-03-02
updated:
published: true
---

<div class="col-start-3 col-end-9">

# More Wonder and Woe with AI

Last week I wrote about [joy and regret in a day of vibe coding](/2026/02/vibe-coding-joy-and-regret/). That was a scope creep story — fast execution, rubber-stamped expansion, 25% of a day lost. This week's failure mode is different and, I think, more important: building confidently in the wrong direction because the plan never captured what mattered most.

## The Task

Build a V2 public API exposing an existing capability. The V1 had been serving customers for years through a web app; now external consumers needed direct programmatic access. Five CRUD endpoints, pagination, an OpenAPI spec, infrastructure routing. Textbook AI-assisted work — clear patterns, a reference implementation to follow.

## The Wonder

I started with a solid PRD: the domain mapping, the endpoints, the conventions, the service dependencies. Then I did what felt responsible — I broke it into phases. Phase A: dependency upgrades. Phase B: initial API. Each phase got its own detailed plan. The AI executed each one beautifully: clean code, logical commits, passing tests. Fifteen sessions, a hundred human messages, five phase plans totaling about 2,500 lines. It _felt_ like going very fast.

That feeling is the wonder — and the trap. Each phase plan was a translation of the original PRD into implementation steps, and each translation got more specific about _how_ while getting quieter about _why_. The PRD said "a role is a group — use the groups service." Phase B's plan said "implement CRUD endpoints for roles" and listed eighteen steps for doing it. The domain mapping didn't survive the decomposition. Not because anyone deleted it — because phasing _selects for_ implementation detail and _selects against_ the kind of foundational context that doesn't look like a task.

## The Woe

Then I started UAT and sent a few curl requests. Every metadata field came back null. Names, descriptions, audit timestamps — all empty. Data access filters? Missing entirely. Structurally correct responses, full of nothing. The response shapes didn't follow our documented API conventions either — no wrapping object, no pagination, no filtering. These are standard requirements for any API we ship, but they weren't in the plan, so they weren't built.

That kicked off Phase D: eighteen steps fixing five issues that should have been specified from the start. But Phase D only treated symptoms.

Phase E revealed the disease. The V2 API had been built on the wrong service entirely.

In our system, what the public API calls a "role" is what the internal system calls a "group." Same entity, different names, different services. The V1 app had been using the groups service for years — it knew where the metadata lived, how to resolve access filters, how to traverse entity relationships. Two-plus years of battle-tested business logic.

Phase B built the V2 API by going directly to the roles data layer — a lower-level abstraction that touches one database table. It was the obvious choice _if you looked at the name_ ("roles API → roles service"). But the metadata lived on group entities. The access logic lived in the groups service. We'd bypassed all of it and gone straight to raw data, then wondered why the responses were empty.

<figure class="mb-10">
  <img loading="lazy" src="https://frinkiac.com/img/S05E15/1052951.jpg" alt="Homer Simpson in the space shuttle, realizing he's made a grave mistake" width="720" height="540">
  <figcaption class="text-center text-sm mt-3 text-gray-600 dark:text-gray-200">Me, realizing the API was built on the wrong abstraction while preparing to welcome our AI overlords.</figcaption>
</figure>

Phase E was a rewrite — not a bug fix. Five phases when there should have been three.

## Write Things Down

Here's the thing: I _knew_ that a role was a group. It wasn't trapped in my head, either — the AI actually asked me about it during planning. We discussed it in chat. The right knowledge was surfaced at the right time.

Then it disappeared. Not because nobody said it — because we buried it under five increasingly detailed phase plans totaling 2,500 lines of implementation steps. The insight was _in_ the conversation. It just didn't survive the iterative process of writing more detailed plans. Each new phase document was thorough about _how_ to build things and silent about _which things to build on_. As Dr. John put it: "I'd have said the right thing, but I must have used the wrong line."[^2]

That's the failure mode. Not a lack of knowledge — a lack of the _right_ detail in the _right_ place. More detail is not better than the right detail. 2,500 lines of plans, and not one of them contained the sentence: "A V2 role IS a V1 group — use the groups service." Ten seconds to write. Sixty percent of the project saved.

This is [Principle #1](/2023/07/first-principles-1-write-things-down/) on this blog for a reason. The goal isn't to tell the AI how to write every line. It's to make sure the important stuff — the domain mappings, the architectural decisions, the one sentence that changes which service you build on — makes it from conversation into the plan and _stays_ there through every revision.

Eric Evans formalized this in _Domain-Driven Design_ twenty-three years ago.[^1] His central insight isn't just "understand the domain" — it's that teams need a deliberate _process_ to surface and _record_ knowledge that feels obvious to whoever holds it. He called it _Ubiquitous Language_: a shared vocabulary, written down and enforced, that aligns code with reality. Evans' whole methodology exists because the instinct — _surely everyone knows this_ — is reliably wrong. We proved it. The AI asked. I answered. And then we wrote five plans that forgot to mention it.

The AI makes this failure mode sharper. It optimizes for the plan you give it. A clear, concise, _complete_ plan produces excellent work. A plan missing one key insight produces confident, clean, well-tested code built on the wrong foundation. Don't micromanage the implementation. But make damn sure the plan captures what matters.

## The Right Detail, Not More Detail

Five phases. Five plans. Five deploy-test-discover cycles. Each phase existed because the previous one was incomplete — not because it lacked detail, but because it lacked the _right_ detail. If I had written one comprehensive plan with the domain mapping front and center — dependencies, "role = group," API contract, implementation on the correct service, infrastructure, docs — the project compresses to three phases at most. One upfront plan with the right ten words beats five detailed plans that each discover what the last one missed.

The pattern is the same one I keep writing about: **powerful tools require disciplined operators**. The AI's execution was never the problem. My preparation was.

# tl;dr

Built a V2 API with AI over two days. Took five phases instead of three because a critical domain insight — "a role IS a group" — was discussed in chat but got lost across 2,500 lines of increasingly detailed phase plans. The AI asked the right question. I gave the right answer. Then we wrote five plans that forgot to mention it. More detail is not better than the right detail. Eric Evans described this in _Domain-Driven Design_ (2003): teams need a deliberate process to surface _and record_ knowledge that feels obvious to whoever holds it. Make sure the plan captures what matters.

# Notes

#### 1

Eric Evans, _Domain-Driven Design: Tackling Complexity in the Heart of Software_ (2003). The book that coined "Ubiquitous Language" and "Bounded Context." His core methodology is a _process_ for extracting domain knowledge from the people who have it and encoding it where the whole team — or your AI agent — can use it. Twenty-three years old and more relevant than ever. Lindy approves.

#### 2

Dr. John, "Right Place Wrong Time" (1973). A song about timing, miscommunication, and having all the right ingredients in all the wrong arrangements. Also a perfect description of a five-phase project plan.

</div>
