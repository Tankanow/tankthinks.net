---
templateEngineOverride: njk,md
metaTitle: First Principle - Don't Break Consumers
metaDescription: First Principle - Don't Break Consumers
title: First Principle - Don't Break Consumers
description: First Principle - Don't Break Consumers
featuredImg:
subHeading: First Principle - Don't Break Consumers
tags: ['first-principles', 'founding-engineer']
date: 2023-08-02
updated:
published: true
---

<div class="col-start-3 col-end-9">

# Don't Break Consumers

[Hyrum's Law](https://www.hyrumslaw.com/):

> With a sufficient number of users of an API,
> it does not matter what you promise in the contract:
> all observable behaviors of your system
> will be depended on by somebody.

In other words, when you have enough external users; you should be thoughtful about changes.

## What _are_ breaking changes?

Before I rant, let's agree on the 3 types of changes: bug fixes, accretion, and breakage.


### Bug Fixes ...
... oft referred as patches, are just that: no _new_ functionality and no _changed_ functionality; only something that used to be broken is now fixed in some way.

For example, your "Hello World" API has an endpoint `/hello` used to erroneously return

```json
{
    "hello": "Dlrow"
}
```

and now you've fixed it to return

```json
{
    "hello": "world"
}
```

### Accretion ...
... sometimes called new features, is **additive** change. This is requiring _less from_ a user OR returning _more to_ a user OR adding a new interface.

For example, your "Hello World" API `/hello` endpoint used to _require_ a Query String Parameter of `?theWholeWorld=true` and now it does not require it; importantly, I can still send it if I want to, but I don't _have_ to send it anymore. This is requiring less.

OR maybe your "Hello World" API endpoint `/hello` now also returns the time:

```json
{
    "hello": "world",
    "as-of": "2024-10-10T01:22:32Z"
}
```

This is returning _more to_ a user. They didn't ask for it, but that's OK; they still get their "hello" field returning as it always did.

OR maybe it a new resource in your "Hello World" API, `/goodbye`:

```json
{
    "shutting": "down"
}
```

They may not use it, but that's OK; they still have `/hello` for all their current use cases.

### Breakage ...

... sometimes called major changes, is **regressive** change. This is requiring _more from_ a user OR returning _less to_ a user OR changing the semantics of an existing interface.

For example, your "Hello World" API `/hello` endpoint now _requires_ a Query String Parameter of `?noDryRun=true`; importantly, if I don't send it I get different results than I used to.

OR maybe your "Hello World" API endpoint `/hello` now _only_ returns the time when it used to return more:

```json
{
    "as-of": "2024-10-10T01:22:32Z"
}
```

This is returning _less to_ a user. They probably needed that data.

OR maybe it a changing the semantics of an existing resource in your "Hello World" API, `/hello`:

```json
{
    "hello": "world",
    "as-of": "1728537752"
}
```

The `as-of` changes from an ISO datetime with timezone to an epoch. Are these the same thing? Well ... they _convert_ to the same thing if you assume certain timezone restrictions and don't use a shitty date conversion library (which is pretty much all of them). But it's NOT the same thing, because, for example, they don't lexicographically sort together the same way.

## Lost Hours


## `<soapbox>`

Semantic Versioning.

## tl;dr

There are so many examples of disastrous breaking changes to consumers. In the tech world alone, I think of Python 2 -> Python 3, Angular 1 -> Angular 2, and every Google service that's disappeared over the years.

I've heard the argument so many times: it's onerous to maintain the existing "bad stuff", we _must_ remove it, and we can make a new major version.

Here's an idea: just deprecate and leave the old thing and _make a new thing_. When you deprecate and leave the old thing, guess what: the community will take over ownership if the service is still valuable. When you make a new thing, you never break existing users. This is why versioning APIs in the URL works: you are making _new resources_ and leaving the existing ones for existing consumers. If you are interested in companies who do this amazingly well, check out [stripe](https://stripe.com/blog/api-versioning?featured_on=talkpython) (and a good overview in [this podcast](https://talkpython.fm/episodes/show/450/versioning-web-apis-in-python)) and [Werner Vogel's rules of API design](https://thenewstack.io/werner-vogels-6-rules-for-good-api-design/).