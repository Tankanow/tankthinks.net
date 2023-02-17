{:title "Dynamic vs Static Languages" :layout :post :tags ["languages" "dynamic" "static" "clojure-conj-2015"] :toc true}

Elben Shira's thoughtprovoking [The End of Dynamic Languages](http://elbenshira.com/blog/the-end-of-dynamic-languages/) inspired many wonderful responses, for example [Have Static Languages Won?](http://pointersgonewild.com/2015/11/25/have-static-languages-won/), [What Consitutes Winning](http://exupero.org/hazard/post/what-constitutes-winning/), and [The Sky Is Not Falling](http://yogthos.net/posts/2015-11-28-TheSkyIsNotFalling.html).

If Elben is offering odds then I will absolutely put money a new successful dynamic programming language for 3 reasons:

1.  Most programmers don't start in a language with a powerful static type system. Organically these programmers seek the expression and creativity dynamic languages provide. Only after experiencing some malevolent runtime bugs will they seek out the safety of powerful type systems.

2.  Not all problems require static typing. To [@Yoghos's](https://twitter.com/yogthos) point, we correctly seek out languages that concisely express the solution. We need static typing in shell scripting languages and I'm sure a new one will come along at some point to replace Bash.

3.  Even if statically typed languages *are* the messiah, the discerning bettor must take the side of a single successful dynamic language appearing between now and the end of time.

A more serious question:

**Can we prove program correctness without static typing?**

Yes: we can use a [Formal Specification Language](https://en.wikipedia.org/wiki/Specification_language). Oh boy, but that looks much *more* complicated than using a powerful static type system ... and there are few tools to help us translate formal specifications to a programming language we can use. Ah. We have a short cut! [Property Testing](https://en.wikipedia.org/wiki/Property_testing)! Property Testing allows us to build a formal functional specification of our programs, proving them correct without the need of a Formal Specification Language. Benjamin Pierce's keynote [A Deep specification for Dropbox](https://www.youtube.com/watch?v=Y2jQe8DFzUM) from Clojure/Conj 2105 delves deeper into Formal Specification and Property Testing for correctness.
