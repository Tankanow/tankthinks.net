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

The AI execution loop worked exactly as advertised. Phase A was dependency upgrades: bumping the runtime and internal libraries. I wrote a plan, handed it over, the AI executed — updating configs, fixing breaking changes, running tests, committing. Phase B was the initial API: five endpoints, unit tests, smoke tests against staging. Clean code, logical commits, good conventions. Across the whole project: roughly fifteen sessions, a hundred human messages, twelve commits, and five phase plans totaling about 2,500 lines. The mechanical throughput was exceptional.

When the plan was clear, the AI was phenomenal.

## The Woe

Then I started UAT and sent a few curl requests. Every metadata field came back null. Names, descriptions, audit timestamps — all empty. Data access filters? Missing entirely. Structurally correct responses, full of nothing. The response shapes didn't follow our documented API conventions either — no wrapping object, no pagination, no filtering. These are standard requirements for any API we ship, but they weren't in the plan, so they weren't built.

That kicked off Phase D: eighteen steps fixing five issues that should have been specified from the start. But Phase D only treated symptoms.

Phase E revealed the disease. The V2 API had been built on the wrong service entirely.

In our system, what the public API calls a "role" is what the internal system calls a "group." Same entity, different names, different services. The V1 app had been using the groups service for years — it knew where the metadata lived, how to resolve access filters, how to traverse entity relationships. Two-plus years of battle-tested business logic.

Phase B built the V2 API by going directly to the roles data layer — a lower-level abstraction that touches one database table. It was the obvious choice _if you looked at the name_ ("roles API → roles service"). But the metadata lived on group entities. The access logic lived in the groups service. We'd bypassed all of it and gone straight to raw data, then wondered why the responses were empty.

<figure class="mb-10">
  <img loading="lazy" src="https://frinkiac.com/img/S05E15/1052951.jpg" alt="Homer Simpson in the space shuttle, realizing he's made a grave mistake" width="720" height="540">
  <figcaption class="text-center text-sm mt-3 text-gray-600 dark:text-gray-200">Me, realizing the API was built on the wrong abstraction for two days</figcaption>
</figure>

Phase E was a rewrite — not a bug fix. Five phases when there should have been three.

## Write Things Down

Here's the thing: I _knew_ that a role was a group. It wasn't trapped in my head, either — the AI actually asked me about it during planning. We discussed it in chat. But somehow, that conversation never made it into the implementation plan. The insight survived the discussion and died in the document.

That's the lossy step. Not brain-to-conversation — conversation-to-plan. We talked about the right abstraction, and then the plan said "build a roles service" and neither of us caught the gap. What's not in the plan doesn't exist — not for the AI picking it up in a new session, and frankly, not for any collaborator picking it up on a Monday morning.

This is [Principle #1](/2023/07/first-principles-1-write-things-down/) on this blog for a reason. The goal isn't to tell the AI how to write every line. It's to make sure the _important_ stuff — the domain mappings, the architectural decisions, the one sentence that changes which service you build on — is written down where it can't be lost. "A V2 role IS a V1 group — use the groups service." Ten seconds to write. Sixty percent of the project saved.

Eric Evans formalized this in _Domain-Driven Design_ twenty-three years ago.[^1] His central insight isn't just "understand the domain" — it's that teams need a deliberate _process_ to surface and _record_ knowledge that feels obvious to whoever holds it. He called it _Ubiquitous Language_: a shared vocabulary, written down and enforced, that aligns code with reality. Evans' whole methodology exists because the instinct — _surely everyone knows this_ — is reliably wrong. We proved it. The AI asked. I answered. And we both moved on without writing it down.

The AI makes this failure mode sharper. It optimizes for the plan you give it. A clear, concise, _complete_ plan produces excellent work. A plan missing one key insight produces confident, clean, well-tested code built on the wrong foundation. Don't micromanage the implementation. But make damn sure the plan captures what matters.

## One Plan, Not Five

The other lesson is structural. Five phases, five plans, five deploy-test-discover cycles. Each phase existed because the previous one was incomplete. If I had written one comprehensive plan — dependencies, domain mapping, API contract, implementation on the correct service, infrastructure, docs — the project compresses to three phases at most. One upfront plan that captures the full picture beats five iterative plans that each discover what the last one missed. The iteration _felt_ productive. Each phase had clean execution. But the aggregate cost of building, deploying, discovering, replanning, and rebuilding dwarfed what a single morning of thorough planning would have cost.

The pattern is the same one I keep writing about: **powerful tools require disciplined operators**. The AI's execution was never the problem. My preparation was.

# tl;dr

Built a V2 API with AI over two days. Took five phases instead of three because a critical domain insight — "a role IS a group" — was discussed in chat but never written into the plan. The AI asked the right question. I gave the right answer. Neither of us wrote it down. Eric Evans described this in _Domain-Driven Design_ (2003): teams need a deliberate process to surface _and record_ knowledge that feels obvious to whoever holds it. Don't tell the AI how to write every line. Make sure the plan captures what matters.

# Notes

#### 1

Eric Evans, _Domain-Driven Design: Tackling Complexity in the Heart of Software_ (2003). The book that coined "Ubiquitous Language" and "Bounded Context." His core methodology is a _process_ for extracting domain knowledge from the people who have it and encoding it where the whole team — or your AI agent — can use it. Twenty-three years old and more relevant than ever. Lindy approves.

---

## LinkedIn

Built a V2 API with AI over two days. Should have been three phases — it was five. The AI asked the right domain question during planning. I gave the right answer. Neither of us wrote it down in the plan.

The API called the entity a "role." Internally it was a "group." We discussed this — then the plan said "build a roles service" and nobody caught the gap. Clean code, wrong abstraction, null responses.

Eric Evans described this in Domain-Driven Design (2003): teams need a process to surface AND record knowledge that feels obvious. Don't micromanage the AI. Make sure the plan captures what matters.

Full post: https://tankthinks.net/2026/03/more-wonder-and-woe-with-ai/

</div>
