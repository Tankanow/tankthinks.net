---
templateEngineOverride: njk,md
metaTitle: Just Enough Design
metaDescription: Just Enough Design
title: Just Enough Design
description: Just Enough Design
featuredImg: 
subHeading: 
tags: ['design','complexity']
date: 2014-03-12
updated: 2014-03-12
published: true
---

<div class="col-start-3 col-end-9">




> Ticking away the moments that make up a dull day ...
>
> --  Pink Floyd Time

**Tick tick tick ...**

You were recently going through a codebase that was written no more than two years ago because a colleague asked you a domain question that was not answered in any spec. Despite a rigorous design and review process, the code is nigh unmaintainable. So you tick away a few hours trying to answer a simple question.

**Over or Under**

Sometimes we find that we **over**-design software. In these cases we are most often left with `Strategy`s and `Abstract*Factory`s littered throughout the code without mention of a core domain Entity in site. This kind of software is difficult to maintain because it is difficult to understand.

Sometimes we find that we **under**-design software. In these cases we are most often left with tightly coupled Class Hierarchies and broken dependencies in our wake. This kind of software is difficult to maintain because it is difficult to understand ... why we didn't think a little harder about what we were doing in the first place.

**Just in Time! Design!**

The truth is that it is quite difficult to design complex components. One nice guideline comes from Neal Ford

> Simplify Essential Complexity; Diminish Accidental Complexity
>
> --  Neal Ford 97 Things Every Software Architect Should Know

What does this mean? Distill, as much as possible, your core domain problem - the essential complexity - into its simplest form; remove the trappings you think you need to build - the accidental complexity - that don't solve the core domain problem.

So what kind of process might help us do this? One possible solution is `Just in Time Design`. In JIT Design we put off rigorous design until just before we are about to implement a smallish component. We can and should still have well though out High-Level <span class="line-though">Architecture</span> Shared Understanding that guides our smaller designs in the big picture, but put off the arguments about Class and Sequence diagrams until you are about to implement the goo.
