---
templateEngineOverride: njk,md
metaTitle: AI Won't Be Productive by Default (And That's OK)
metaDescription: Why AI adoption follows the same patterns as every other transformative technology
title: AI Won't Be Productive by Default (And That's OK)
description: Why AI adoption follows the same patterns as every other transformative technology
featuredImg:
subHeading: Lessons from a Founding Engineer
tags: ['ai', 'devops', 'founding-engineer']
date: 2025-07-07
updated:
published: true
---

<div class="col-start-3 col-end-9">

# AI Won't Be Productive by Default (And That's OK)

I've been thinking about the early days of cloud adoption. Remember deploying from laptops? FTPing files to production at 2 AM? We thought we were being efficient. Spoiler: we weren't.

Now I'm watching teams adopt AI with that same wild-west enthusiasm, and I'm having déjà vu. The difference? This time the bills are much, much bigger.

## The Pattern Recognition Game

After years at MassMutual, Nuance/Microsoft, and now as a founding engineer at CloudZero, I've seen this movie before. New technology arrives with grand promises. We adopt it enthusiastically. Then we discover it creates entirely new constraints we never imagined.

Here's what I've been sharing in my talks: **AI will not be productive by default. We must deliberately extend DevOps principles to govern AI usage, infrastructure, and costs.**

This isn't pessimism – it's pattern recognition.

## The Velocity Problem

The speed of change with AI is staggering. We're not just dealing with code completion anymore. We're managing:

- Custom LLMs for every team
- Agent fleets that can spin up infrastructure autonomously
- AI-powered testing that generates more cases than humans can review
- Embedded agents making runtime decisions

Each represents a fundamental shift in how we build software. Each brings its own special flavor of chaos.

## Enter the Theory of Constraints (Again)

Remember "The Goal" by Eliyahu Goldratt? Every system has constraints. Remove one, another emerges. It's organizational whack-a-mole, except now the moles are GPU-powered and cost $1,000 per query.

Traditional constraints:
1. **The Code** - How fast can we write it?
2. **The Server** - How quickly can we deploy?
3. **The Wallet** - How much can we afford?

AI doesn't eliminate these. It transforms them into something more complex. The code constraint becomes about quality consistency and attribution. The server constraint morphs into managing agent fleets. The wallet constraint? Let's just say it explodes in ways that would make your CFO cry.

## The Three Ways Still Apply

Gene Kim's "The Phoenix Project" taught us the Three Ways of DevOps: systems thinking, feedback loops, and experimentation. These principles didn't disappear when containers arrived. They won't disappear because AI can write code.

What we're witnessing is the birth of "DevAIOps" – applying everything we've learned about managing complex systems to this new reality.

## What Good Looks Like

When AI adoption is working well:
- Your AI-augmented pipeline tests and deploys with predictable costs
- Observability tools alert you to unexpected AI behavior
- You can sleep without worrying about runaway AI expenses

In other words, it feels exactly like good DevOps. Because it is.

## The Path Forward

The patterns and practices from a decade of DevOps provide our foundation. We just need to adapt them thoughtfully. AI is transformative, but transformation without discipline is just expensive chaos.

We've solved harder problems than this. We turned early cloud chaos into refined practices. We can do the same with AI.

After all, we have about seven years until the singularity. Might as well build some good systems while we wait.

*[Read the full post on CloudZero →](https://www.cloudzero.com/blog/ai-wont-be-productive-by-default)*
