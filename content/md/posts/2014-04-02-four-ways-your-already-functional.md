{:title "4 Ways Your Enterprise is Already Doing Functional Programming" :layout :post :tags ["architecture" "clojure"] :toc true}

> Can't see the forest for the trees.
>
> --  idiom humans

Most enterprise architectures are *scared* of functional programming. The funny thing is that they're probably already doing "functional" programming in Java, just poorly.

1.  The standard tiered architecture is more functional than OOP. Tiered architectures pushes everything into services. Services are just groups of functions, not unlike Clojure namespaces, with no data. This is mostly procedural code, but it is definitely closer to Functional than OOP.

2.  Lots of Value Objects with no behavior. This goes hand in hand with the tiered architecture. The truth here is that we just have lots of data separate from the methods that operate on that data. The fact that we create so many different containers for the data rather than just using maps is a non-functional thing we do, but the basic idea of "data" and separate "functions" is the same.

3.  Immutable Classes. If you follow Joshua Bloch, as most enterprise java developers do, then they are almost certainly trying for immutability. We know it's a good idea. We just impose it ourselves with boilerplate code rather than allowing the language, e.g. Clojure, to ensure we are doing the right thing.

4.  Lots of anonymous classes. We create these all the time when we want to create executables or reify interfaces with one method. Often times we create anonymous classes solely for the purpose of passing them to as a parameter to a method. Where else have I seen that. Oh yeah. First class functions - the foundation of "functional" languages.

If your architect pushes back on you using a functional programming language because it is new, trendy and unproven - just point her to your enterprise standard tiered architecture and say we're doing this in the wrong tool.
