---
templateEngineOverride: njk,md
metaTitle: Joy and Regret in 6 Hours of Vibe Coding
metaDescription: What happens when AI-assisted coding delivers 3-5x mechanical throughput but also invents features you never asked for. A field report.
title: Joy and Regret in 6 Hours of Vibe Coding
description: What happens when AI-assisted coding delivers 3-5x mechanical throughput but also invents features you never asked for. A field report.
featuredImg:
subHeading: A Field Report from the Frontier
tags: ['ai', 'devops', 'founding-engineer', 'devaiops']
date: 2026-02-26
updated:
published: true
---

<div class="col-start-3 col-end-9">

# Joy and Regret in 6 Hours of Vibe Coding

Today was the first day in a while where I'm not sure if I was more productive vibe coding. That's worth unpacking.

This is not a "first time I tried AI coding" story. I've been vibe coding real features for months — full implementations shipped from my phone in Claude Code while waiting for my kids at practice, multi-repo changes landed from the couch on a Saturday morning. It works. I've [advocated for extending DevOps principles to AI](/2025/07/ai-devops-post-1/) because I believe in the tooling enough to want governance around it.

So when I say today felt different, I mean something that had been consistently delightful backslid a bit. That's a more interesting question than "is vibe coding good?" The question is: what changed?

## The Task

The work was real platform engineering: enabling authentication in custom developer namespaces across multiple repositories. Developers running personal environments were blocked by auth failures because the setup workflow couldn't provision the required identity resources. The fix touched an authorizer library, an infrastructure orchestrator, and a downstream service for end-to-end validation. Three repos, sequenced deploys, live AWS smoke tests.

Not trivial. Not glamorous. Exactly the kind of work where vibe coding should shine — lots of mechanical coordination, clear success criteria, well-understood patterns.

## The Joy

**The first 40 minutes were magic.** The AI agent explored the codebase, implemented the core fix, wrote six tests, caught two integration bugs through those tests, hit 94% coverage, bumped the version, committed, triggered a CI deploy, cloned a second repo, deployed to AWS, and verified end-to-end. When CloudFormation blew up on pre-existing resources, the agent diagnosed the orphaned stacks, cleaned them up, and redeployed. I didn't touch the keyboard.

That's not an exaggeration. Forty minutes. For work that would have been a solid half-day of my time.

**Multi-repo orchestration was the killer feature.** The workflow required sequencing release candidate deploys across three repos (the authorizer must publish before the orchestrator can reference it), cross-referencing semantic versions in nested infrastructure templates, and running smoke tests against a live API Gateway. The agent managed this like a seasoned release engineer — triggering CI, monitoring progress, bumping version references in the right order, verifying each step before moving to the next.

**The mechanical work was free.** Lint fixes, style conformer alignment, git operations, AWS CLI calls, CloudWatch log tailing — these are the taxes of software development. Having them automated wasn't just faster; it was _cognitively_ freeing. I could think about architecture while the agent handled plumbing. This is exactly the Flow State advantage I wrote about [last week](/2026/02/first-principles-7-flow-state/). The agent absorbed the interrupts so I didn't have to context-switch.

## The Regret

**Scope creep nearly sank the day — and it came from the AI, not me.**

Around midday, I had a reasonable idea: make the authorizer more friendly for dev namespaces by adding a permissive mode for unmapped endpoints. That was a well-scoped enhancement. But during planning, the AI independently decided to also add a "save custom config" feature that let developers push arbitrary endpoint configurations. I approved the plan without scrutinizing that addition closely enough.

It was architecturally broken in practice. The custom config generated auth tokens scoped to the wrong namespace, which caused every single smoke test to fail with 401 Unauthorized. About **1.5 hours of a 6-hour day was spent implementing, debugging, and reverting a feature the AI invented and I rubber-stamped.**

The permissive authorizer already solved the problem. I had to stop the agent and ask "What is this feature? Why do we need it?" — a question I should have asked at planning time.

The AI's instinct to add "helpful" features is a trap. It generates plausible-sounding scope that a tired human will approve on autopilot. I've written about [offloading critical thinking to AI](/2025/07/ai-devops-post-4/) before. Today I lived it.

**Convention drift was real and insidious.** The agent's initial implementation used `monkeypatch` for environment variables (the codebase uses a custom fixture) and introduced infrastructure parameters where the codebase favors in-code detection. Both violations made it past the agent's own conformer check. I caught them during review and forced a rewrite. The lesson: AI can check _syntax_ patterns reliably, but _architectural_ conventions require human eyes.

**Small bugs compound.** A dictionary key in the wrong case. Test assertions against raw dicts when the handler JSON-serializes the body. A `git add -A` that staged two entire cloned repos into a commit. Each was a two-minute fix, but they erode trust incrementally — you start second-guessing every line and the speed advantage evaporates.

**The same bug bit us twice.** The authorizer caches configuration in memory for about a minute. Both times we ran smoke tests immediately after setup, all 21 tests failed. Both times the fix was "wait and retry." The agent diagnosed it correctly the first time but didn't internalize the lesson for the second. It has no persistent memory across that kind of boundary. Today's AI doesn't learn from its own mistakes within a session the way a human would.

## The Scorecard

| | |
|---|---|
| **Wall-clock time** | ~6 hours |
| **Sessions** | 10 (3 failed launches, 7 productive) |
| **Repos touched** | 3 |
| **RC versions burned** | 5 |
| **CI deploys** | ~6 |
| **Time on reverted work** | ~1.5 hours (25%) |
| **Final result** | 21/21 smoke tests, 70 unit tests, 3 repos at release versions |

## The Verdict

Vibe coding is phenomenal for _execution_. The mechanical throughput across repos, CI/CD pipelines, and AWS environments was easily 3-5x what I'd do manually. But it's dangerous for _design_. The AI optimizes for forward progress. It will happily build the wrong thing fast, and its confidence makes you less likely to question it.

The most valuable moment of my day was the 30 seconds I spent asking "wait, why do we need this?" That question saved an hour of further debugging. Thirty seconds of critical thinking vs. sixty minutes of rework. That's leverage.

## The Rule Going Forward

Be very careful expanding scope.

This isn't an AI lesson. It's a project management lesson that predates AI by decades. Teams of humans have always burned exponential time on "just one more thing." Fred Brooks wrote about it in 1975.[^1] The debugging, integration, and rework costs compound the same way regardless of who proposed the extra work.

AI just makes it faster to get into trouble, because saying yes to one more feature costs nothing when you're not the one typing.

The pattern is the same one I keep writing about in this series: **powerful tools require disciplined operators**. A Formula 1 car doesn't win races by default. Neither does an AI agent writing infrastructure code. The human in the loop — the one asking "wait, why?" — is still the most important part of the system.

I'll keep vibe coding. The 40-minute magic at the start of my day was real. But I'll review AI-proposed scope changes the way I'd review a junior engineer's PR: with curiosity, respect, and a healthy dose of skepticism.

# tl;dr

AI-assisted coding delivered 3-5x mechanical throughput across three repos, CI/CD, and AWS. It also invented a feature I didn't ask for, which cost 25% of my day. The most productive thing I did was spend 30 seconds asking "why do we need this?" Vibe coding is a force multiplier for execution. For design decisions, the human is still the bottleneck — and that's a feature, not a bug.

# Notes

#### 1
Frederick P. Brooks Jr., _The Mythical Man-Month_ (1975). Still the best book on software project management. Lindy says it'll outlast us all.

</div>
