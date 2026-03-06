---
templateEngineOverride: njk,md
metaTitle: The Right Detail, Not More Detail
metaDescription: AI artifacts generated from AI artifacts lose signal fast. One clear document and lots of validation beats five detailed plans that each discover what the last one missed.
title: The Right Detail, Not More Detail
description: AI artifacts generated from AI artifacts lose signal fast. One clear document and lots of validation beats five detailed plans that each discover what the last one missed.
featuredImg:
subHeading: What AI-Assisted Development Taught Me About Signal and Noise
tags: ['ai', 'founding-engineer', 'devaiops', 'first-principles']
date: 2026-03-02
updated:
published: true
---

<div class="col-start-3 col-end-9">

# The Right Detail, Not More Detail

Last week I wrote about [joy and regret in a day of vibe coding](/2026/02/vibe-coding-joy-and-regret/). That was a scope creep story. This one is about something quieter and more dangerous: signal decay.

## The Task

Build a V2 public API exposing an existing capability. The V1 had been serving customers for years through a web app; now external consumers needed direct programmatic access. Five CRUD endpoints, pagination, an OpenAPI spec, infrastructure routing. Textbook AI-assisted work.

## What Happened

I wrote a PRD. It was solid — domain mapping, endpoints, conventions, service dependencies. Then I handed it to an AI agent and asked it to generate a detailed implementation plan. That plan was good, so I asked for a more detailed plan for the first phase. That plan was good, so I asked for a more detailed plan for the next phase. Five phases, five plans, 2,500 lines of implementation steps.

Each plan was generated from the one before it. Each was more detailed than the last. And each was a little further from the original document that actually mattered.

Here's the sentence that was in my PRD: **"A V2 role IS a V1 group — use the groups service."**

Here's what Phase B's plan said: "Implement CRUD endpoints for roles." Eighteen steps. Not one mentioned the groups service.

The AI built the V2 API by going directly to the roles data layer — a lower-level abstraction that touches one database table. It was the obvious choice _if you looked at the name_ ("roles API -> roles service"). But in our system, what the public API calls a "role" is what the internal system calls a "group." Same entity, different names, different services. The metadata lived on group entities. The access logic lived in the groups service. Two-plus years of battle-tested business logic, all bypassed.

I ran a few curl requests. Every metadata field came back null. Data access filters? Missing entirely. Structurally correct responses, full of nothing.

<figure class="mb-10">
  <img loading="lazy" src="https://frinkiac.com/img/S05E15/1052951.jpg" alt="Homer Simpson in the space shuttle, realizing he's made a grave mistake" width="720" height="540">
  <figcaption class="text-center text-sm mt-3 text-gray-600 dark:text-gray-200">Me, realizing the API was built on the wrong abstraction.</figcaption>
</figure>

Five phases when there should have been three. Not because the AI was bad — the code was clean, the tests passed, the commits were logical. Because the one sentence that mattered didn't survive the game of telephone I'd set up between my documents.

## Signal Decay

Here's the pattern: you write a document. You ask the AI to generate a more detailed document from it. You ask the AI to generate a more detailed document from _that_. Each generation is a lossy compression. Implementation detail goes up. Domain context goes down. By the third derivative, the AI is optimizing for the shape of the plan, not the shape of the problem.

This is the same thing that happens when you photocopy a photocopy. Or when a meeting summary gets summarized into a status report that gets summarized into an executive briefing. Each step selects for what _looks_ like the right kind of detail and drops what doesn't fit the format. The critical insight — "a role is a group" — doesn't look like an implementation step, so it doesn't survive.

As Dr. John put it: "I been in the right place, but it must have been the wrong time."[^2] The knowledge was surfaced at the right moment. The AI actually _asked me_ about the domain mapping during planning. I answered correctly. Then we generated five plans that forgot to mention it.

Eric Evans described this problem twenty-three years ago in _Domain-Driven Design_.[^1] His central insight isn't "understand your domain" — any competent engineer does that. It's that teams need a deliberate process to surface and _record_ knowledge that feels obvious to whoever holds it. He called it _Ubiquitous Language_: a shared vocabulary, written down and enforced, that keeps code aligned with reality. Evans' whole methodology exists because the instinct — _surely everyone knows this_ — is reliably wrong. AI makes it worse, because the AI _did_ know it, briefly, in one conversation, before burying it under 2,500 lines of generated plans.

I've [written about this before](/2023/08/first-principles-4-domain/). _Make the important parts important._ The failure here wasn't that I didn't understand my domain. It was that I let the important parts get diluted across a stack of derivative documents until they weren't important anymore.

## One Document, Many Validators

The fix isn't "write better plans." It's: **write one clear document and then spend the rest of your time validating it.**

That one document is your domain map. Not a phase plan. Not a task list. A short, authoritative source of truth that says _what things are_, _what they're called_, and _which services own them_. The kind of document Evans would call a Ubiquitous Language spec. In my case, the ten words that would have saved 40% of the project: "A V2 role IS a V1 group — use the groups service."

Then, instead of generating more plans from that document, point agents _at_ it as validators:

- A **unit test agent** that writes tests against the domain map, not the implementation. "Does the roles endpoint call the groups service?"
- A **conformance agent** that checks the implementation against your API conventions. "Does every response include the wrapping object, pagination, and filtering?"
- A **UAT agent** that runs curl requests and verifies real responses against expected shapes. "Does the metadata come back populated?"

Each of these agents is cheap. Each one catches a different class of drift. And critically, each one points _back_ at the source document rather than generating a new derivative of it. The document stays still. The validators orbit around it.

This is the inversion that matters: don't use AI to generate more artifacts from your plan. Use AI to _validate_ the artifact you already have. More detail is not better than the right detail. One document and five validators beats five documents and zero validators every time.

## The Pattern

It's the same one I keep writing about: **powerful tools require disciplined operators**. The AI's execution was never the problem. The game of telephone I set up between my documents was.

Write the domain map. Keep it short. Keep it authoritative. Then stop generating plans and start generating tests.

# tl;dr

Built a V2 API with AI assistance. A critical domain insight — "a role IS a group" — was in my original PRD but got lost across five AI-generated plans, each more detailed and further from the source. The code was clean; it was just built on the wrong service. AI artifacts generated from AI artifacts lose signal fast. Eric Evans told us why in 2003: teams need a deliberate process to record knowledge that feels obvious. The fix: write one clear domain document and spend the rest of your time on validation agents — unit tests, conformance checks, UAT — that point back at the source instead of generating more derivatives from it.

# Notes

#### 1

Eric Evans, _Domain-Driven Design: Tackling Complexity in the Heart of Software_ (2003). The book that coined "Ubiquitous Language" and "Bounded Context." His core methodology is a process for extracting domain knowledge from the people who have it and encoding it where the whole team — or your AI agent — can use it. Twenty-three years old and more relevant than ever. Lindy approves.

#### 2

Dr. John, "Right Place Wrong Time" (1973). A song about timing, miscommunication, and having all the right ingredients in all the wrong arrangements. Also a perfect description of domain knowledge that gets surfaced in chat and buried in plans.

</div>
