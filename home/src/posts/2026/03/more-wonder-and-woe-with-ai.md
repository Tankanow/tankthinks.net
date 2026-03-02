---
templateEngineOverride: njk,md
metaTitle: More Wonder and Woe with AI
metaDescription: An AI-assisted API build took 5 phases instead of 3. The root cause wasn't the AI — it was skipping the domain model mapping that Eric Evans told us about in 2003.
title: More Wonder and Woe with AI
description: An AI-assisted API build took 5 phases instead of 3. The root cause wasn't the AI — it was skipping the domain model mapping that Eric Evans told us about in 2003.
featuredImg:
subHeading: What Happens When You Skip the Map
tags: ['ai', 'founding-engineer', 'devaiops', 'first-principles']
date: 2026-03-02
updated:
published: true
---

<div class="col-start-3 col-end-9">

# More Wonder and Woe with AI

Last week I wrote about [joy and regret in a day of vibe coding](/2026/02/vibe-coding-joy-and-regret/). That was a single-day story: fast execution, scope creep, a 30-second question that saved an hour. Lesson learned, move on.

This week I have a different story. Same tool, same operator, but a different failure mode. This time the problem wasn't scope creep — it was building on the wrong abstraction from the start. And this time, it took two days and five phases of work before I figured out what had gone wrong.

## The Task

The work was building a new public API — a V2 version of an existing capability. The V1 API had been serving customers for years through a web application, but now external consumers needed direct programmatic access. Five CRUD endpoints, proper pagination, an OpenAPI spec, infrastructure routing, the works.

This is textbook AI-assisted work. Clear patterns, well-understood conventions, an existing reference implementation to follow. Exactly the kind of project where the AI execution loop shines.

## The Wonder

And it did shine — for the parts that were well-specified.

The first phase was a set of dependency upgrades: bumping the language runtime, upgrading internal libraries to versions that supported the new API framework. The AI executed this cleanly. I wrote a plan, handed it over, and it worked through the steps — updating configs, fixing breaking changes, running tests, committing. Mechanical work, done mechanically. Beautiful.

The second phase was the initial API implementation: five endpoints, unit tests, smoke tests against a staging environment. The AI produced clean code following existing conventions, wired up the test infrastructure, and committed in logical chunks. Twelve commits across the project, each with proper conventional commit messages. The commit discipline was better than most human engineers I've worked with.

Here's the interaction profile across the whole project:

| | |
|---|---|
| **AI sessions** | ~15-18 |
| **Human messages** | ~80-120 across all sessions |
| **Human time** | ~6-10 hours of active work over 2 days |
| **Commits** | 12 |
| **Phase plans written** | 5 detailed plans (~2,500 lines total) |

The execution loop — write a detailed plan, hand it to the AI, let it execute step by step — is genuinely efficient for well-specified work. The plans for the dependency upgrade and the initial implementation executed cleanly. The AI absorbed the mechanical toil so I could think about architecture, just like in the [vibe coding session](/2026/02/vibe-coding-joy-and-regret/).

## The Woe

Then I started UAT.

I deployed the API, sent a few curl requests, and immediately saw the problem: every metadata field was null. Names, descriptions, audit timestamps — all empty. The data access filters that should have controlled what each API key could see? Missing entirely. The API returned structurally correct responses full of nothing.

Worse, the response shapes didn't follow our documented conventions. No wrapping object. No pagination. No sorting or filtering. These aren't exotic requirements — they're standard for any API we ship. But they hadn't been specified in the plan, so they hadn't been built.

That kicked off Phase D: eighteen steps fixing five distinct issues. Response wrapping. Pagination. Metadata fields. A permissions endpoint. Standard stuff that should have been in the original implementation.

But Phase D only treated the symptoms. Phase E revealed the disease.

## The Root Cause

The V2 API had been built on top of the wrong data layer.

In our system, what the public API calls a "role" is actually what the internal system calls a "group." Same entity, different names, different services managing them. The V1 web application had been using the groups service for years — it knew where the metadata lived, how to resolve data access filters, how to traverse the entity relationships. Two-plus years of business logic, battle-tested.

Phase B built the V2 API by going directly to the roles data layer — a lower-level abstraction that only touches one database table. It was the obvious choice if you looked at the name ("roles API → roles service"), but it was wrong. All the metadata lived on the group entity. All the data access logic lived in the groups service. We had bypassed the business logic and gone straight to the raw data, then wondered why the responses were empty.

Phase E was a rewrite. Not a bug fix — a fundamental change in which service the API called. If I had spent thirty minutes before Phase B answering one question — "what is a V2 role, and what existing entity does it map to?" — Phases D and E would not have existed.

<figure class="mb-10">
  <img loading="lazy" src="https://frinkiac.com/img/S05E15/1052951.jpg" alt="Homer Simpson in the space shuttle, having caused a crisis by not understanding how things work" width="720" height="540">
  <figcaption class="text-center text-sm mt-3 text-gray-600 dark:text-gray-200">Me, realizing the API was built on the wrong abstraction for two days</figcaption>
</figure>

## What Eric Evans Told Us in 2003

This isn't a new failure mode. Eric Evans described it precisely in _Domain-Driven Design_ twenty-three years ago.[^1]

Evans' central argument is that software projects fail not because of technical complexity, but because of **domain complexity** — the gap between what the code models and what the business actually does. His prescription is the _Ubiquitous Language_: a shared vocabulary between developers and domain experts that keeps the code aligned with reality.

Our project violated this in the most basic way possible. The public API used the word "role." The internal system used the word "group." They meant the same thing, but nobody stopped to say that out loud. So the AI built a "roles" service, and I reviewed and approved a "roles" service, and we were both wrong.

Evans would have caught it. His first move on any project is to map the domain — draw the entities, name the relationships, align the vocabulary. Not write code. Not design APIs. _Understand the domain._ It's the same instinct behind my own [first principle about domain understanding](/2023/08/first-principles-3-domain/): the best code clearly represents domain rules, and you can't represent rules you haven't articulated.

The AI can't do this step for you. It will happily build a beautifully clean implementation on top of the wrong abstraction. It doesn't know that "role" and "group" are the same thing unless you tell it. The AI optimizes for the plan you give it. If the plan is wrong, it builds the wrong thing faster than any human could.

This is the same lesson from last week's post, but at a different altitude. Last week, scope creep cost 25% of a single day. This week, a missing domain mapping cost 60% of a two-day project. Same root cause: the human didn't do the thinking that only the human can do.

## What I'll Do Differently

**Before writing code, write the domain model.** Thirty minutes with a whiteboard (or a markdown file) answering: What entities exist? What are they called in each system? What maps to what? This isn't optional preparation — it's the prerequisite that determines whether everything downstream is building on rock or sand.

**Write the API contract first, not the implementation.** If I had drafted an OpenAPI spec with response shapes, pagination structure, and field lists before handing the AI a plan, every issue from Phase D would have been caught at design time. Design-first, not code-first.

**Stop building new APIs by going directly to the data layer.** A V2 API should be a thin conformance layer over existing service functions, not a parallel implementation. Two years of business logic already existed. Bypassing it to "keep things simple" created the most complex outcome possible.

**Treat infrastructure and documentation as part of "done."** Routing, OpenAPI specs, and docs aren't Phase C afterthoughts — they're part of the feature. If it's not routable and not documented, it's not shipped.

**Keep the AI execution loop — but feed it better plans.** The write-a-plan-then-execute pattern is genuinely efficient. The problem wasn't the loop. It was plan _quality_. The dependency upgrade plan was excellent and executed flawlessly. The API implementation plan was missing the most important line: "a role IS a group."

## The Theoretical Minimum

The project could have been three phases instead of five:

1. **Dependencies** — unavoidable prerequisite
2. **API implementation** — built on the groups service from day one, with proper response shapes, pagination, and docs included
3. **Final polish** — whatever genuinely novel issues emerge from UAT

Instead, I got five phases because I skipped the thirty-minute domain mapping that would have told me which service to build on. The AI didn't skip it — I did. The AI doesn't know what it doesn't know. That's my job.

# tl;dr

Built a V2 public API with AI over two days. It took five phases when it should have taken three, because I didn't map the domain model before writing code. The API used the word "role" — but in our system, a role is a "group," managed by a completely different service. We built on the wrong abstraction, got empty responses, and had to rewrite. Eric Evans described this exact failure mode in _Domain-Driven Design_ in 2003: if the code's vocabulary doesn't match the domain's vocabulary, the code is wrong. AI makes this worse, not better — it builds the wrong thing faster and with more confidence. The fix is the oldest trick in software: understand the domain before you write a line of code.

# Notes

#### 1

Eric Evans, _Domain-Driven Design: Tackling Complexity in the Heart of Software_ (2003). The book that coined "Ubiquitous Language" and "Bounded Context." If your team has ever argued about what a word means in your system, you need this book. It's twenty-three years old and more relevant than ever. Lindy approves.

---

## LinkedIn

Built a V2 API with AI assistance over two days. Should have been a three-phase project — dependency upgrade, implementation, polish. Instead it was five phases, because I skipped the most important step: mapping the domain model before writing code.

The API called the entity a "role." Our internal system called it a "group." Same thing, different name, different service. The AI built a clean implementation on the wrong abstraction. Every metadata field came back null.

Eric Evans described this failure mode in Domain-Driven Design in 2003. AI makes it worse — it builds the wrong thing faster than any human could. The fix is still the oldest trick in software: understand the domain first.

Full write-up: https://tankthinks.net/2026/03/more-wonder-and-woe-with-ai/

</div>
