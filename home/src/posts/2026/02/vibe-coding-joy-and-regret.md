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

This is not a "first time I tried AI coding" story. I've been vibe coding real features for months — full implementations shipped from my phone in Claude Code while waiting for my kids at practice. Literally. On a metal bench outside a winter baseball session, no laptop, just the Claude and GitHub iOS Apps. It works. I've [advocated for extending DevOps principles to AI](/2025/07/ai-devops-post-1/) because I believe in the tooling enough to want governance around it.

So when I say today felt different, I mean something that had been consistently delightful backslid a bit. That's a more interesting question than "is vibe coding good?" The question is: what changed?

## The Task

The work was real platform engineering: enabling authentication in custom developer namespaces across multiple repositories. Developers running personal environments were blocked by auth failures because the setup workflow couldn't provision the required identity resources. The fix touched an authorizer library, an infrastructure orchestrator, and a downstream service for end-to-end validation. Three repos, sequenced deploys, live AWS smoke tests.

Not trivial. Not glamorous. Exactly the kind of work where vibe coding should shine — lots of mechanical coordination, clear success criteria, well-understood patterns.

## The Joy

**The first 40 minutes were magic.** The AI agent explored the codebase, implemented the core fix, wrote six tests, caught two integration bugs through those tests, hit 94% coverage, bumped the version, committed, triggered a CI deploy, cloned a second repo, deployed to AWS, and verified end-to-end. When CloudFormation blew up on pre-existing resources, the agent diagnosed the orphaned stacks, cleaned them up, and redeployed. I didn't touch the keyboard.

That's not an exaggeration. Forty minutes. For work that would have been a solid half-day of my time.

**Multi-repo orchestration was the killer feature.** The workflow required sequencing release candidate deploys across three repos (the authorizer must publish before the orchestrator can reference it), cross-referencing semantic versions in nested infrastructure templates, and running smoke tests against a live API Gateway. The agent managed this like a seasoned release engineer — triggering CI, monitoring progress, bumping version references in the right order, verifying each step before moving to the next.

**The mechanical work was free.** Lint fixes, conform code to existing style, git operations, AWS CLI calls, CloudWatch log tailing — these are the taxes of software development. Having them automated wasn't just faster; it was _cognitively_ freeing. I could think about architecture while the agent handled plumbing. This is exactly the Flow State advantage I wrote about [last week](/2026/02/first-principles-7-flow-state/). The agent absorbed the interrupts so I didn't have to context-switch.

## The Regret

**Scope creep nearly sank the day — and it was both of us.**

Around midday, I had a reasonable idea: make the authorizer more friendly for dev namespaces. It was essentially the same pattern we had just implemented, just in a slightly new context. It was a well-scoped enhancement. But during planning, the AI proposed an additional "save custom config" feature that let developers push arbitrary endpoint configurations. I didn't really notice when I reviewed the plan. I said yes without thinking hard about it.

This is the same dynamic that plays out in every standup and sprint planning meeting. A manager asks "can you just add one more thing?" and a week of team toil follows. The difference here is that the AI plays both roles — it proposes the scope _and_ builds it before you've finished your coffee. The feedback loop between "that sounds reasonable" and "it's already implemented" is dangerously short.

The custom config was architecturally broken in practice. It generated auth tokens scoped to the wrong namespace, which caused every single smoke test to fail with 401 Unauthorized. About **1.5 hours of a 6-hour day was spent implementing, debugging, and reverting a feature I thought was easy, AI misunderstood, added to, and poorly implemented.**

In fact, the agent had already implemented the feature I asked for (though with bad patterns) — but continued on to the feature it thought was a good idea that I had rubber stamped. I had to stop the agent and ask "What is this feature? Why do we need it?" — a question I should have asked at planning time. But I'd been riding the high of the first 40 minutes, and saying yes was easy when I wasn't the one typing.

I've written about [offloading critical thinking to AI](/2025/07/ai-devops-post-4/) before. Today I lived it.

**Convention drift was real and insidious.** The agent's initial implementation of feature 1 was pristine: clean code following surrounding conventions. But its implementation of feature 2 looked like it had farmed it out to its own junior intern agent. It broke all code conventions, introduced new mutations and side-effects, and did not check for conformance with existing patterns. Luckily, I caught them during review and forced a rewrite.

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

Vibe coding is phenomenal for _execution_. The mechanical throughput across repos, CI/CD pipelines, and AWS environments was easily 5x what I'd do manually. But it's dangerous when it lulls you to sleep and you are overwhelmed with planning fatigue. The AI optimizes for forward progress. It will happily build the wrong thing fast, and its confidence makes you less likely to question it.

The most valuable moment of my day was the 30 seconds I spent asking "wait, why do we need this?" That question saved an hour of further debugging. Thirty seconds of critical thinking vs. sixty minutes of rework. That's leverage.

## The Rule Going Forward

Be very careful expanding scope.

This isn't an AI lesson. It's a project management lesson that predates AI by decades. Teams of humans have always burned exponential time on "just one more thing." Fred Brooks wrote about it in 1975.[^1] The debugging, integration, and rework costs compound the same way regardless of who proposed the extra work.

AI just makes it faster to get into trouble, because saying yes to one more feature costs nothing when you're not the one typing.

The pattern is the same one I keep writing about in this series: **powerful tools require disciplined operators**. A Formula 1 car doesn't win races by default. Neither does an AI agent writing infrastructure code. The human in the loop — the one asking "wait, why?" — is still the most important part of the system.

I'll keep vibe coding. The 40-minute magic at the start of my day was real. But I'll review AI-proposed scope changes the way I'd review a junior engineer's PR: with curiosity, respect, and a healthy dose of skepticism.

# tl;dr

AI-assisted coding delivered at least a 5x mechanical throughput across three repos, CI/CD, and AWS. But together we talked ourselves into a feature that wasn't needed, and it cost 25% of my day. The most productive thing I did was spend 30 seconds asking "why do we need this?" Scope creep effects AI systems just like human systems.

# Notes

#### 1
Frederick P. Brooks Jr., _The Mythical Man-Month_ (1975). Still the best book on software project management. Lindy says it'll outlast us all.

</div>
