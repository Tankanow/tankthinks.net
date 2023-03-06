---
templateEngineOverride: njk,md
metaTitle: Changelog Ship It 90
metaDescription: Changelog Ship It 90
title: Changelog Ship It 90
description: Changelog Ship It 90
featuredImg:
subHeading: Changelog Ship It 90
tags: ['know-notes', 'the-changelog']
date: 2023-03-04
updated:
published: true
---

<div class="col-start-3 col-end-9">


# [Changelog Ship It 90](https://changelog.com/shipit/90)

This is my first (and last?) episode of Ship It! I love Gerhard's enthusiasm for the subject and the Kaizen! format of airing The Changelog's dirty laundry. Thanks to Adam, Jerod, and Gerhard. I plan on listening to the back catalog of Kaizen episodes.

## Dagger

### Data > Code

My spidey sense goes off whenever I here someone say:

> code is better than data

A more accurate statement is

> code is better than data ... at making developers feel useful

I find that the opposite is true, that is [data is almost always better than code](https://twitter.com/fogus/status/454582953067438080).

- Code is liability. Data is value.
- Data is declarative, portable, and transformable. Most code is not.

I'll stop here. I'll write a new post on all the reasons why I prefer Data to Code.

### Portability Fallacy

I prefer using the provider's IaaC directly. [Terraform](https://developer.hashicorp.com/terraform) is a successful project, and I bet few Enterprise Architects have been fired for choosing it over [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [ARM](https://learn.microsoft.com/en-us/azure/templates/), or [CDM](https://cloud.google.com/deployment-manager/docs).

The **Portability Fallacy**:

> Switching out your provider is never as easy as switching out your provider.

Most of these tools proffer portability as the main feature. It's kind of like using an ORM because "you can always swap out the database". Only, you can't _really_ ... because when is your problem solved by switching from mySQL to Postgres (actually, that's a bad example, that may actually solve your problem 🤣). My point here is that switching between _alike_ providers is not usually the solution to _real_ problems. And switching between disparate providers is harder than these intermediaries make it out to be.

We are in the process of switching to GitHub Actions from our current CICD tool. Would Dagger move all my secrets, change my authentication methods, upgrade pipelines to use new differentiated features that don't exist in our current tool?

2 other costs of intermediaries tools are:

1. **Debugging**: There is one fewer tool to debug. I find most debugging needs to be done in the provider anyway.
2. **Lagging**: There is one more tool to update when things change. Provider adds a new feature, when will the intermediary get it?

### Consistency may still be worth it

The real benefit of intermediaries like Terraform or Serverless Framework is _constistency_. If you are a large enterprise using many providers and programming languages, you can have consistent IaC across all teams. **Consistency** may be the most important value a product organization practices.

### The Benefits

That being said, the Dagger project has many laudable goals:
1. write once
2. local testing
3. speed

I am going to play around with the tool to see if there are ideas and ergonomics here we can steal for our own tools and processes.

