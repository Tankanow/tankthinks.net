---
templateEngineOverride: njk,md
metaTitle: Property Based Testing
metaDescription: Property Based Testing
title: Property Based Testing
description: Property Based Testing
featuredImg: 
subHeading: 
tags: ['clojure','java','testing']
date: 2014-03-08
updated: 2014-03-08
published: true
---

<div class="col-start-3 col-end-9">




>
> Found, but not proven.
>
> -- Democritus

Part of my learning Clojure journey is to question my beliefs regarding testing. For the past few years I've lived the [Clean Code](http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1/181-8179541-6211637?ie=UTF8&qid=1394325126&sr=8-1&keywords=clean+code) [TDD](http://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1394325145&sr=8-1&keywords=test+driven+development) style of development: let the rails of unit tests guide you. However, the Clojure brain trust - Rich, Stu and the rest of the brilliant minds at [Cognitect](http://cognitect.com/) have made a compelling argument that unit tests, or at least expectation-based tests are old hat.

### Expectation-Based Testing
What is _Expectation-Based Testing_? This is, simply, what most of us have been doing ad nauseum. If you're like me, the following `given`-`when`-`then` structure will look familiar:


```java
@Test
public void testMethodExpectationStyle(){
	// given
	// here is where you would set up some mocks, or if you're working with bad/legacy
	// code, curse loudly as you foolishly try to mock static methods in between reading
	// the Mockito/Powermock docs

	// when
	Object actual = objectUnderTest.methodUnderTest(someKnownInput);

	// then
	assertThat(actual, equalTo(expected));
}
```

So what are the pros and cons of this approach?
### Pros
- simple set up the state, run the method, check the output
- readability well, sometimes, when the mocking doesn't get out of hand
- intention you know up front what the method should do


### On Intention

Allow me a brief diversion on _Intention_. It turns out _Intention_ is a blessing and a curse. The developer writing expection-based intends to test the functionality of a method by _knowing_ what it is supposed to do given a _known_ input. This is good, for example we know that the reverse of "ball" is "llab", as such we can test our reverse method is way. However, what if our understanding of the method is wrong? What if it functions differently under different conditions?


### Cons
- scale since we explicitly define the inputs and outputs, we are limited by the number of tests we are willing to write; we mitigate this by testing known boundary conditions, however, it is impractical to try to test > a handful of inputs for each method


### Property-Based Testing

Property-Based testing on the other hand is testing such that the developer defines properties of the method under test and uses a generator function to create large input sets. For example, in Clojure this might look like:


```clojure
;; my naive reverse a list implementation
(defn myreverse
  [xs]
  (loop [n 0
         ys []]
    (if (< n (count xs))
      (recur (inc n) (cons (nth xs n) ys))
      ys)))

;; define a property about that
;; in this case, simply that for all inputs, myreverse does the same thing as Clojure's reverse
(def prop-myreverse-equalto-cljreverse
  (prop/for-all [v (gen/vector gen/int)]
    (= (reverse v) (myreverse v))))
;; this is definitely cheating, because for any useful function, you won't have an existing one in the Clojure toolkit, so let's try again - how about that if a reverse twice I should get back the original list:
(def prop-reverse-reverse
  (prop/for-all [v (gen/vector gen/int)]
    (= v (myreverse (myreverse v)))))

;; then i can check these properties, N number of times (in this case N is 1000)
(c/quick-check 1000 prop-myreverse-equalto-cljreverse)
(c/quick-check 1000 prop-reverse-reverse)
```


So the `test.check` library I'm using in this case will generate 1000 lists of different sizes of random integers and then check each list again the properties i defined.

The power of this is huge. Instead of explicitly enumerating all of the inputs for a given function under test, I can simply define some properties that should be true for all inputs and then let someone else schlep up and down a mountain generating lots of input for me!

The difficult part here is that you will never have the contrived first property example I gvae above: where you will have another function to test against. Instead, almost certainly, one property won't do it for any of your functions ... instead you will have to tease out all of the salient properties to ensure the functionality of your method.

We have swapped "generate all of the import inputs and know what the outputs are supposed to be" for "generate all of the important properties".

Which do you prefer?
