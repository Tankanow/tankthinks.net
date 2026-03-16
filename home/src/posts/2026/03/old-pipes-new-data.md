---
templateEngineOverride: njk,md
metaTitle: "Old Pipes, New Data"
metaDescription: "Ten people, three days, one system. What an AI-assisted hackathon taught me about velocity, signal decay, and the ideas that actually held up."
title: "Old Pipes, New Data"
description: "Ten people, three days, one system. What an AI-assisted hackathon taught me about velocity, signal decay, and the ideas that actually held up."
subHeading: "What an AI Hackathon Taught Me About First Principles"
tags: ['ai', 'architecture', 'founding-engineer', 'devaiops', 'first-principles']
date: 2026-03-12
published: true
---

<div class="col-start-3 col-end-9">

# Old Pipes, New Data

Ten engineers. Three days. One goal: build a system that captures costs across the entire organization, in real time. Every person on the team ran with an AI coding assistant running multiple agents.

I've written about [what happens when AI-assisted development goes well and when it doesn't](/posts/2026/02/vibe-coding-joy-and-regret/), and about [what happens when AI artifacts compound into signal loss](/posts/2026/03/more-wonder-and-woe-with-ai/). Those were solo field reports — one person, one day, one lesson. This is the version at scale: ten people, three days, a system spanning multiple repos and services, and a hard demo deadline. What holds up? What breaks? And which ideas — some of them decades old — predicted the answers?

## The Numbers

Before the narrative, the data. These are from git history and Claude session logs across five repositories:

- **147 commits**, roughly **95,000 lines of code** across four active repos in 72 hours
- **117 Claude sessions** across my two repos alone
- **Peak day** (March 11): 96 commits
- A **greenfield repo** went from a cookiecutter template to a working MQTT-based session system

The numbers tell the joy story on their own: AI scaffolded entire subsystems, ran framework migrations with full test coverage, wrote a 908-line Flink app in one prompt, and handled the [mechanical taxes](/posts/2026/02/vibe-coding-joy-and-regret/) of development so humans could stay in [flow](/posts/2026/02/first-principles-7-flow-state/). The interesting question isn't whether it was fast — it's what went wrong.

## What AI Hindered

Eleven bug fix commits tell the real story — AI-generated code that compiled, passed lint, and looked structurally correct, but broke at runtime or under real data. That 908-line Flink app — it satisfied the Java compiler but failed on missing JARs and undefined methods; an IoT credential policy was syntactically valid but missing a business-rule prefix, silently killing every MQTT connection; two rewrites totaling 3,400+ lines were admissions that AI had optimized for the shape of the plan, not the shape of the problem — [signal decay](/posts/2026/03/more-wonder-and-woe-with-ai/) at hackathon speed. The pattern underneath all of it: when you're moving fast, you review less, and AI's confident mistakes compound.

## Three Old Ideas

Here's where it gets interesting. The hackathon surfaced three ideas, each older than most of the tools we used, that predicted almost everything that went right and wrong.

### Conway's Law (1967)

"Organizations which design systems are constrained to produce designs which are copies of the communication structures of those organizations."[<sup>1</sup>](#1)

This is the biggie.

The system architecture mirrored the team structure exactly. 5 2-person teams with one or two subsystems per team. Guess where the interfaces in the architecture were. The interfaces between systems — stream contracts, API specifications, event schemas — were the coordination points. And those coordination points still need design — and teamwork. Whether or not you think AI can do this coordination in the future, the point is that communication and coordination is *important*. Even a 1M Token Context Window cannot hold your entire system design. Humans and AI need to coordinate. Those coordination points become important interfaces.

AI — like a human — excelled _within_ a bounded context. Give it one repo, one service, one well-defined problem, and it produced. But everyone needs a bridge when crossing a chasm.

Conway told us this fifty-nine years ago: the hard part is the seams, not the components.

### Build-Measure-Learn (2011)

Eric Ries formalized the Build-Measure-Learn loop in _The Lean Startup_, but the idea descends from Toyota's lean manufacturing principles in the 1950s.[<sup>2</sup>](#2) The insight is directional: you build in order to measure, and you measure in order to learn. Build is not the goal. Learning is.

AI compressed "Build" so dramatically that the bottleneck shifted to "Measure" and "Learn." The eleven bug fix commits, the 1,800-line rewrites — those are evidence of the team building faster than it could validate. Ninety-five thousand lines of code is a vanity metric. The question is how many survived first contact with production. The bug fixes _are_ the validated learning.

When Build is nearly free, the discipline shifts: did you measure before you built more? The loop became Build-Build-Build, and the Measure phase got batched into painful debugging sessions.

I can't stress this enough. When build is nearly free, measurement is *even more* important!

### The Lindy Effect

The patterns that held up under hackathon pressure — streaming pipelines, pub/sub messaging, fail-open contracts, event envelopes — are all forty to fifty years old. The hackathon didn't invent architecture. It stress-tested which old ideas still work when you're moving at AI speed. Every one of them was [Lindy](/posts/2023/08/first-principles-3-lindy/).[<sup>3</sup>](#3)

No one proposed a novel data structure. No one invented a new messaging paradigm. Under time pressure, we reached for the patterns that have survived decades of production use. AI accelerated the implementation of those patterns, but it didn't replace the judgment that selected them.

### The Synthesis

Conway tells you _where_ the hard parts are: the seams between components, the interfaces between teams. Lean tells you _how_ to approach them: build-measure-learn, not build-build-build. Lindy tells you _what to build with_: the patterns that have already survived.

## The Closing

Same refrain: **powerful tools require disciplined operators.**

AI made 95,000 lines across five repos in three days possible. But there were still inefficiency loops, mostly due to building faster than we measured. The hackathon's real lesson isn't about AI at all. It's about the gap between velocity and validation.

AI is a force multiplier on whatever you already are. If you have clear domain knowledge and good architectural instincts, AI accelerates you into remarkably productive territory. If you're winging it, AI accelerates that too — right into a wall of confident, structurally correct, semantically wrong code that you'll spend your evening debugging.

Ten people proved this in seventy-two hours.

# tl;dr

Ten engineers used AI to write 95,000 lines of code across five repos in three days — but the story is nuanced. Three ideas older than the tools predicted it all: Conway's Law (the hard part is the seams), Build-Measure-Learn (when Build is free, the discipline is Measure), and the Lindy Effect (under pressure, reach for proven patterns). AI is a force multiplier on whatever you already are.

# Notes

#### 1

Melvin E. Conway, "How Do Committees Invent?" _Datamation_ (1967). The original paper argues that system structure mirrors organizational structure — not as a suggestion, but as a constraint. Fifty-nine years later, our hackathon proved it again: AI was powerful within bounded contexts but blind at the seams between them.

#### 2

Eric Ries, _The Lean Startup_ (2011). The Build-Measure-Learn loop descends from Toyota's lean manufacturing principles (1950s). Ries' contribution was framing it for product development: build the minimum thing, measure whether it works, learn from what you find. When AI makes Build nearly free, the discipline — and the bottleneck — shifts entirely to Measure and Learn.

#### 3

See [First Principles 3: Lindy](/posts/2023/08/first-principles-3-lindy/) for a longer treatment of why old ideas that have survived tend to keep surviving.

#### 4

See also: [Joy and Regret in 6 Hours of Vibe Coding](/posts/2026/02/vibe-coding-joy-and-regret/) and [The Right Detail, Not More Detail](/posts/2026/03/more-wonder-and-woe-with-ai/) — the solo field reports that preceded this one.

</div>
