---
templateEngineOverride: njk,md
metaTitle: Why Clojure is Great Data
metaDescription: Why Clojure is Great Data
title: Why Clojure is Great Data
description: Why Clojure is Great Data
featuredImg:
subHeading:
tags: ['clojure','java']
date: 2014-05-05
updated: 2014-05-05
published: true
---

<div class="col-start-3 col-end-9">




> It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures.
>
> --  Alan Perlis

You've probably seen this quote before. I've seen in in countless blogs and books. It is referenced in the wonderful Clojure book [The Joy of Clojure](http://joyofclojure.com/). I recently experienced the joy of Clojure directly through Perlis' pearl of wisdom (all puns intended).

I recently read a nice blog post on avoiding [unexpected issues](http://www.javacodegeeks.com/2014/05/clojure-how-to-prevent-expected-map-got-vector-and-similar-errors.html) in Clojure functions. I like the advice: small fns, destructuring and pre/post conditions so thought I would integrate it into a few functions. The epiphany came with the pre/post conditions.

Let's start with a simple function that transforms a list to a vector.

```clojure
(defn list->vector [xs] (reduce conj [] xs))
```

I want to add pre/post conditions to this simple function, but I can't seem to remember the syntax. Let's see if I can figure it out using the Clojure composite data types: set, vector, list and map.

First: there are two named types of conditions, `:pre` and `:post`. Well the Clojure composite data type that supports named associations is a map, does this look right:

```clojure
{:pre nil :post nil}
```

Second, let's think of what the values for each of the `:pre` and `:post` keys should be. It seems reasonable that there could be more than one `:pre` function and more than one `:post` function, so each value should be a collection of some sort. We don't really need to name the elements of these collections, but some sort of sequential collection makes sense so that the Clojure internals can apply the functions in order. In fact, doesn't `seq` makes sense because I'm sure the Clojure internals would love to use first `first` and `rest` to apply a collection of somethings. It seems the choice is between `list` and `vector`, and when choosing between a list and vector, we usually use vectors unless we are generating code forms because of the nice visual offset of the `[]`, so a vector makes sense for each value:

```clojure
{:pre [] :post []}
```

Lastly, we know that we are creating pre and post conditions, which are functions, so there's only one Clojure data types for this job, `list`, I've filled in each of the :pre and :post vectors with two functions that just have a bunk name "fn" and some "args".

```clojure
{:pre [(fn args) (fn args))] :post [(fn args) (fn args))]}
```

Let's say that we want our functions to ensure that our input is a list and not empty and our output is a vector and not empty; putting it all together:

```clojure
(defn list->vector [xs]
  {:pre [(list? xs) (not (empty? xs))]
   :post [(vector? %) (not (empty? %))]}
  (reduce conj [] xs))

[1 2 3] AssertionError Assert failed: (list? xs) user/list->vector (form-init2119333260165711694.clj:1) AssertionError Assert failed: (not (empty? xs)) user/list->vector (form-init2119333260165711694.clj:1)
```

Imagine trying the same process of discovery in Java for example without the aid of an IDE to show you the available methods on each object. It would be nearly impossible to do this in Java because most bits of data are wrapped in Objects with named fields and methods. This is one of the reasons Clojure is so intuitively powerful. And one of the reasons Perlis was so right.
