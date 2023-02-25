---
templateEngineOverride: njk,md
metaTitle: Run Length Decoding
metaDescription: Run Length Decoding
title: Run Length Decoding
description: Run Length Decoding
featuredImg:
subHeading:
tags: ['complexity','clojure','information theory']
date: 2014-03-17
updated: 2014-03-17
published: true
---

<div class="col-start-3 col-end-9">




> ...an idea is no more an even relatively constant thing than is a feeling or emotion or volitional process. There exist only changing and transient ideational processes; there are no permanent ideas that return again and disappear again.
>
> --  Wilhelm Wundt An Introduction to Psychology

**Complexity and Likeablity**

Wilhelm Wundt is famous for his many contributions to psychology. I have been interested in one particular contribution of his for many years now: the Wundt Curve. The Wundt Curve is a Bell-like curve laying on the x and y axes of Complexity and Likeability. The Wundt Curve shows how we like things to be more complex to a point (the apex of the curve) at which point any more complexity results in a decrease in likeability. The Wundt Curve plays nicely both into Clojure and the Run-Length encoding problem - [\# 12 in 99 Lisp Problems](http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html).

**Clojure**

First, since I would prefer not to incure the wrath of Rich Hickey, I must clearly state that the complexity I spoke of in the previous paragraph is not the complexity Rich spoke of in his seminal presentation [Simple Made Easy](http://www.infoq.com/presentations/Simple-Made-Easy). In fact, just to make things clear I won't use the word complexity anymore - suffice to say that we are talking about novelty here and not something consisting of interwoven parts.

I love Clojure. It is simply beautiful. For the other Comp Sci students like me that learned assembly and C rather than Lisp, it certainly has novelty in syntax, but over time, the Clojure student realizes that this novelty sits nicely in a spot that is very likeable. Beyond the syntax, the budding Clojurist realizes that the language is filled with beautiful data structures, ubiquitous interfaces (protocols) and a simple power that is *both* novel and very likeable indeed.

**Information Theory**

The Wundt curve always makes me think of Information Theory, of entropy and bits and data compression. Run length encoding is a simple form of lossless compression where the encoder reduces the size of an input sequence by representing repeating input elements as a tuple of the element and the count of the "run", for example we can encode the following input sequence `[:a :a :a :a :b :b :b :c :c]` as `[(4 :a) (3 :b) (2 :c)]` reducing our input by 33%.

Problem 12 in the 99 Lisp Problems concerns writing a run-length *decoder*. A very simple way to write this in Clojure is:

```clojure
(defn rl-decode [xs]
  (->> xs
       (map #(if (coll? %) (let [n (first %) x (second %)] (repeat n x)) %))
       flatten
       ))
```

First we thread our input collection `xs` into `map` with an anonymous function that either (a) returns the element unchanged or if the element is itself a collection (b) takes the first element as the count and the second element as the item to be repeated and does just that. Finally, thread that output to `flatten`, which could probably be replaced with better use of `mapcat`.

In any case, this is an elegent simple concise solution to an elegant simple concise problem. Huzzah.
