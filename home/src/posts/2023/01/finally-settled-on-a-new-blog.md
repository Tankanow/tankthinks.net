---
templateEngineOverride: njk,md
metaTitle: Finally Settled On a New Blog
metaDescription: Move to 11ty, Tailwind, etc.
title: Finally Settled on a New Blog
description: Move to 11ty, Tailwind, etc.
featuredImg: finally-settled-on-a-new-blog
subHeading: I have been failind to blog since 2014. I have some archives in an old static site generator. This year I want to get to know CSS, specifically TailwindCSS, and some other Web Stack Tools.
tags: ['Web Development']
date: 2023-02-25
updated:
published: true
---

<div class="col-start-3 col-end-9">

# Background

I have been failing to blog since 2014. I have had 28 posts, written between 2014 and 2016, stored in a public S3 bucket and hosted on http://tankthinks.net (no cert) for too long. I have a few ideas inspiring me. I want to publish them _this year_ on a **secure**, **mobile friendly**, **accessible** site. In the process, I wouldn't mind learning a few new technologies.

# The previous stack

I love [Clojure](https://clojure.org). In 2014, I was not programming professionally in Clojure and was looking for excuses to create Clojure projects. The old site was built on [Cryogen](http://cryogenweb.org/), a Clojure-built static site generator. This has served me well in the past 9 years. For the new site, I wanted to use a few technologies closer to current web standards.

# The new Stack

## Hosting

First, and perhaps easiest _for me_, was moving the site to a new private S3 bucket frontend by CloudFront. I used AWS ACM to create and manage a certificate that I could associate with the CloudFront distribution fronting the static site.

## 11ty

[11ty](https://www.11ty.dev/) is a flexible, simple, and fast static site generator. It supports several templating engines, including Markdown and Nunjucks, which are useful for authoring content and page templates respectively. It also gives you access to JavaScrit and all its useful packages while not requiring client-side JavaScript code. Also, it's very popular and actively maintained.

## Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework. It's actually not great for a CSS n00b like me, but it does have some benefits. Tailwind is NOT a great place for a CSS beginner because it has its own Domain-Spefic-Language (DSL) that translates to CSS. In other words, you have to learn the DSL _and_ CSS at the same time. In return for this cost, you get to use the composible utility classes directly in HTML. This means I don't have to worry about CSS selectors, organization and re-use, or even color/size details.

<div class="col-start-3 col-end-9">

This site is based on [this template](https://github.com/kailoon/kailoon.com). It scores the magic 400 on Google Lighthouse.

</div>
