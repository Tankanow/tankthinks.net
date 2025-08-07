---
templateEngineOverride: njk,md
metaTitle: Building Systems for AI - Lessons from DevOps History
metaDescription: Why the Three Ways of DevOps become even more critical when your newest team member is an LLM
title: Building Systems for AI - Lessons from DevOps History
description: Why the Three Ways of DevOps become even more critical when your newest team member is an LLM
featuredImg:
subHeading: From Release Engineer to AI Wrangler
tags: ['ai', 'devops', 'founding-engineer', 'systems-thinking']
date: 2025-01-17
updated:
published: true
---

<div class="col-start-3 col-end-9">

# Building Systems for AI: Lessons from DevOps History

In 2008, Nuance hired me as a "Release Engineer." DevOps wasn't a thing yet – DevOpsDays wouldn't happen until 2009. But I was doing DevOps all the same, writing Makefiles and bash scripts to deploy code to hundreds of Linux machines.

Every 2 AM deployment failure, every "works on my machine" mystery – they were lessons in why systems thinking matters more than tools. Now, watching teams adopt AI with the same chaotic enthusiasm we had for cloud computing, I see history preparing to teach the same lessons. Just with bigger bills.

## The Great Awakening Redux

Remember when DevOps was the radical idea that people who write code should talk to people who run it? Revolutionary stuff. But everyone forgets: DevOps wasn't about tools. It was about systems thinking, feedback loops, and creating a culture where failure was a teacher.

**We must deliberately extend these principles to govern AI usage, infrastructure, and costs.** This isn't optional. It's survival.

## The Three Ways (Now With More Dimensions)

### The First Way: Systems Thinking

When I joined CloudZero as a founding engineer in 2017, one of my first principles was "Understand the Domain." You can't optimize what you don't understand.

With AI, systems thinking becomes multidimensional:
- **Traditional DevOps**: Follow code from commit to production
- **AI-Augmented DevOps**: Follow code from prompt to production, through model selection, token consumption, and hallucination detection

AI agents struggle to determine when to use tools versus internal knowledge. This complexity is expensive – reasoning through problems requires multiple LLM calls. Without constraints, instead of a stack overflow, you get a credit card overflow.

### The Second Way: Amplifying Feedback Loops

AI is like a brilliant Golden Retriever. Super intelligent but... SQUIRREL! Without structured feedback loops, you're maximizing productivity while minimizing hallucinations with an assistant that has the attention span of a caffeinated kid playing Roblox.

At CloudZero, we've developed a structured workflow:

1. Human prompts with requirement
2. AI asks clarifying questions (feedback loop #1)
3. Human answers, creating shared context
4. AI generates PRD
5. Human reviews and approves (feedback loop #2)

Each stage has human checkpoints. Not because we don't trust AI, but because AI without feedback is like a Ferrari without brakes. Fast, exciting, and guaranteed to hit something expensive.

### The Third Way: Culture of Experimentation

"Move fast and break things" hits different when "things" includes your AWS budget. But we still need experimentation – just with guardrails.

Teams succeeding with AI created safe spaces for experimentation. Think of it as a sandbox filled with Monopoly money for API credits.

## The Patterns Are Already Here

During my time at Nuance/Microsoft, I lived through the microservices revolution. The patterns apply directly:

- **Service governance then**: Service discovery, API versioning
- **AI governance now**: Model versioning, prompt engineering standards
- **Cost management then**: Reserved instances, right-sizing
- **Cost management now**: Token optimization, model selection
- **Observability then**: Distributed tracing, metrics
- **Observability now**: Prompt tracking, hallucination rates

Same game, new players. Teams that win build the boring stuff – governance, observability, cost controls – before they need it.

## Code Is Still Liability

One of my core principles: "Code is Liability." Every line you write must be maintained, debugged, and eventually replaced. AI doesn't change this – it shifts liability like a shell game.

When AI generates code, you're trading direct liability (I wrote this) for indirect liability (AI wrote this, but I deployed it). It's like hiring a contractor who works at superhuman speed but occasionally builds doors that open into walls.

## What Good Looks Like

We're building the right systems when:
- Junior developers can use AI without burning the budget
- AI agents have circuit breakers preventing infinite loops
- We can trace generated code to its prompt and model
- "AI did something weird" triggers a runbook, not panic
- FinOps dashboards show AI costs per feature

This isn't utopia. Teams are building these systems today, quietly and methodically.

## The Road Ahead

Good systems take time. AI won't wait for us to figure it out. It's already generating code and running up bills. The question is whether we'll build systems to govern it or let it govern us.

Every few years, our industry rediscovers that technical problems were never the hard part. The hard part is the human systems around technology. AI is forcing us to evolve again. But evolution doesn't mean throwing away what we've learned.

*[Read the full post on CloudZero →](https://www.cloudzero.com/blog/building-systems-for-ai)*

</div>