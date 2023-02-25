---
templateEngineOverride: njk,md
metaTitle: I wonder
metaDescription: I wonder
title: I wonder
description: I wonder
featuredImg:
subHeading:
tags: ['clojure','interviewing']
date: 2014-03-01
updated: 2014-03-01
published: true
---

<div class="col-start-3 col-end-9">




I think my brother is coming into an opportunity. He is working at a new company that has lots of room for improvement. I asked him to bring a notebook to work and note any inefficiencies he comes across.

It got me thinking that I could free-lance for this company. However, I wonder if I have the skills to architect large solutions. I think I'm a strong software developer. I must not be an idiot because Yaning thinks I'm pretty smart. I think Peter thouht I was smart too. However, I did not do well in the HubSpot interview. Though that is really confusing to me.

What did I not do well on.

1.  Memoize

2.  Circular Buffer

3.  Write SQL to return Twitter feed

I don't think I nailed any of these. I think I did the best on the Circular Buffer - I did OK there. I shot myself in the foot with Memoize because I tried and failed at Clojure before moving on to a bad Java solution. The SQL I did OK, but again, failed to understand B-Trees and some basic SQL stuff.

Memoize in clojure:

```clojure
(defn memoize [f]
  (let [cache (atom {})]
    (fn [x]
      (if-let [ret (get @cache x)]
        (val ret)
        (let [fx (f x)]
          (do (swap! cache assoc x fx) fx))))))
```
