{:title "Where is the OOP in my Layers?" :layout :post :tags ["oop" "java" "spring"] :toc true}

Help! I think I've lost the OOP in my Layers.

**Do I Smell Something?**

Is it just me or did my OOP disappear somewhere between my DAL and my service layer? I bet you've worked on a project with a tiered architecture that boiled down to something like `Controller Layer \-> Service Layer \-> Data Layer` with a nice `Model` holding the layers together tighter than a wrestlers unitard.

Our `Model` is just a set of `Value Object` classes because it's too difficult to use the data directly, and that is fine [sigh] but sends us down the slippery slope to follow. If we're using `Spring`, you might as well push us off a cliff.

We end up with a bunch of Classes that encapsulate *only* their injected dependencies but that are in all other ways groups of somewhat related (if we're lucky) functions. So at best we're doing poor man's functional programming in the context of a Class Diagram, or at worst we're in a procedural gobbledee-gook of spaghetti code.

**All in the name of Cap'n Crunch?**

Usually this is all in the name of some Cerealization (or Serialization ... fine) library that turns our `Model` objects into XML/JSON ... **for free**! Or so the architects keep telling me as I wonder why my `getStatus` method takes a `Job` object and a bunch of other beans as parameters instead of living with its data *in* the `Job` class.
