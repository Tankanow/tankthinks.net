---
templateEngineOverride: njk,md
metaTitle: First Principle - Understand the Domain
metaDescription: First Principle - Understand the Domain
title: First Principle - Understand the Domain
description: First Principle - Understand the Domain
featuredImg:
subHeading: First Principle - Understand the Domain
tags: ['first-principles', 'founding-engineer']
date: 2023-08-02
updated:
published: true
---

<div class="col-start-3 col-end-9">


# Understand the Domain

*Naming* and *Grouping* things is essential to any discipline. It's also, paradoxically, one of the hardest things to do. Have you ever designed and implemented a feature only to realize that one or more of the crucial names does not match user expectations?

*Alignment* is an organizational **super-lever**; well-aligned organizations will outperform their competition 99 times out of 100, especially if those organizations maintain strong alignment as they scale.

What is alignment? It's when your functional areas, Marketing, Sales, Product, Engineering, etc. are (1) speaking the same language and (2) have supporting goals.

How do you speak the same language?

> Be consistent with your *Naming* and *Grouping* across organization functions.

## The only way ...

... your team can Name and Group concepts consistently well is to *Understand your Domain*. There is no shortcut here. You must _do the work_: you must *read* foundational material, *interview* Subject Matter Experts, and *experience* the domain for yourself.

Menlo Innovations has a unique take on this process called [High-Tech Anthropology](https://menloinnovations.com/our-way/our-process). I recommend reading about their process and maybe even attending one of their free online seminars. You won't be able to (and should not) *replicate* their process in your organization; however, you _should_ apply a lot of the same principles.

<img src="/img/20230818_menlo.hta.notes_2.jpg" alt="High-Tech Anthropology" style="width:400px;margin-left:auto;margin-right:auto;"/>


## Background
There are a lot of resources for "Domain Driven" processes. An O'Reilly search for "domain driven" returns 896 items!

<img src="/img/20230818_oreilly_domain_search.png" alt="Domain Driven Stuff" style="width:400px;margin-left:auto;margin-right:auto;"/>

<br/>

I have read and re-read many of the canonical "domain driven" books. I have applied their advice to projects. I will dive-deep on these books in a future post. For now, I will say that all of these books contain wisdom; however, they can be frustrating when you try to follow the prescribed steps. The real world is never as neat as the examples. Few books do a good job describing abstract domains.

## Abstract Domains

Sometimes your team is building technology that mirrors something in the real-world. For example, many "domain driven" books use the examples "coffee shop ordering" or "airline booking". These example are great for these books because most readers have experience in those domains. Here the *Names* and *Groups* are obvious because they already exist in the real world. If you're implementing a Point-of-Sale system for a coffee shop, you can use the names *Order*, *Total*, and *Payment* without much ambiguity.

However, I have found that most of my work comes in "abstract domains", that is ones with no *direct* analog in the real word. Here you will often find yourself making up names like *Dimension*, *Analytics*, or *Explorer*.

So how do you know if your made up names are *good* names?
## Advice

### Write Stuff Down
If you've been following this book, you won't find this advice surprising. The first step on your domain journey is [write stuff down](../../07/first-principles-1-write-stuff-down/). The simple act of writing down your thoughts about your domain congeals the ideas behind the domain. Moreover, putting the domain to paper (or to Wiki) helps share the domain with your editors (teammates and stakeholders).

Two specific templates for writing stuff down are the *Domain Glossary* and the *Domain Story*.
#### Glossary
This simple, powerful template is the foundation of domain documentation. Define the *Names* and *Groups* in your domain. For example, in the identity domain, here is a possible Domain Glossary:

**User**
> A human who can access the system

**Permissions**
> What a **User** can do in the system.

**Administrator**
> A **User** with all **Permissions**.

**Group**
> A set of **User**s that allows an **Administrator** to apply **Permission**s to many **User**s at once.

Note how the definitions are self-referential within the glossary. This helps define the relationships between terms.

#### Story
The second template is the Domain Story. Write out in prose a scene using the terms defined in the glossary.

> The first *User* who logs into the system is an *Administrator*. She can view all existing **Permissions** and **Users**. The system guides her to create a **Group**, adding **User**s and **Permissions** to it.

### Find Physical Metaphors
I often think about this "[Building Composable Abstractions](https://twitter.com/atankanow/status/804743817014419456)" conference talk I saw in person, specifically "Find a Physical Metaphor". Our domain might be abstract to a point, but there is likely _something_ in the physical world that resembles what we're trying to represent. [Wundt](https://en.wikipedia.org/wiki/Wilhelm_Wundt) hypothesized that humans like novelty up to a point. I think it's the same when building digital experiences: we crave new, but not *too* new.

Good Physical Metaphors (1) answer questions and (2) give everyone (internal and external) a shared common ground. For example:

> In our system, a **User Identity** is like a Driver's License. It represents the important information we need to identify them uniquely, including name, address, and age.

### Focus on Actions/Events
See what I did above? I used a known domain, identity and access management, as an example. I cheated. What happens if you have no idea which terms to put into your *Glossary* and *Story* and can't find a good *Physical Metaphor*?

If you're stuck, focus on *actions* and *events*. This might seem weird because my examples above are mostly nouns. I did that on purpose to create common examples; however, the most important terms to define are *verbs*. Verbs are what your user _does_ with your systems, *Actions* are the present tense verbs in your domain that change the state of your system. *Events* are the past tense verbs that represent changes in your system. For example:

**Add Permission** (action)
An **Administrator** gives a more access to a **Group** of **User**s.

**Permission Added** (event)
More access was given to a **Group** of **Users**.

Actions define _what_ your users can _do_; events define _who cares_. One useful technique for this is [Event Storming](https://en.wikipedia.org/wiki/Event_storming).
## tl;dr

No matter what people sell you, there is no magic "Domain-Driven" process to ensure your team gets this right. The techniques I listed above have helped me defined and share domains. The most important takeaway from this chapter is

> Make the Important Parts Important

After you define your domain, take the important terms and *focus on them everywhere*. That is, make them a focus of your marketing materials, your sales pitches, and - for we engineers - make them names of features, components, micro-services, modules, classes, files, or however you chunk up your system.