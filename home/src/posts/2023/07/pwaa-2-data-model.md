---
templateEngineOverride: njk,md
metaTitle: PWAA - The Python Data Model
metaDescription: Python's data model — the system of dunder methods that makes everything tick — is one of its most elegant ideas. It's also one of the most convention-heavy, and conventions have a way of biting back.
title: PWAA - The Python Data Model
description: Python's data model — the system of dunder methods that makes everything tick — is one of its most elegant ideas. It's also one of the most convention-heavy, and conventions have a way of biting back.
featuredImg:
subHeading: Python Warts and All
tags: ['python-warts-and-all', 'data-model']
date: 2023-07-15
updated:
published: true
---

<div class="col-start-3 col-end-9">

# PWAA - The Python Data Model

There's a chapter in the Python documentation called "The Python Data Model" that reads almost like philosophy. It explains the system of special methods — `__len__`, `__getitem__`, `__iter__`, `__enter__` — that determines how objects behave with Python's built-in operations. Once you understand it, you understand why Python feels so consistent. It's also where some of Python's most persistent frustrations live.

*This is chapter 2 of [Python Warts and All](../../works/20230718-python-warts-and-all/).*

## The Good

The core idea is elegant: Python's built-in functions and operators don't call methods on objects directly. Instead, they dispatch through a consistent set of special methods. When you call `len(x)`, Python calls `x.__len__()`. When you write `x[key]`, Python calls `x.__getitem__(key)`. When you use `with x:`, Python calls `x.__enter__()` and `x.__exit__()`.

This means any class can opt into any built-in behavior by implementing the right methods:

```python
class Deck:
    def __init__(self, cards):
        self._cards = cards

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

Now `len(deck)` works. `deck[0]` works. `random.choice(deck)` works. `for card in deck:` works. `deck[-1]` works. All of that falls out of just two methods. You didn't have to register the class anywhere, implement an interface, or inherit from a base class. You just implemented two well-named methods, and Python rewarded you with a full suite of behavior.

This creates a genuine level playing field. A list and a custom sequence class both respond to `len()` and indexing. A file and a custom context manager both work with `with`. The consistency means you can write generic code that works on anything that behaves right, regardless of type hierarchy.

This is Python's best version of duck typing, and it's a real competitive advantage over languages where you have to explicitly declare every interface you participate in.

## The Warts

### The Dunder Aesthetic

The double underscores — dunders — are unavoidable in the data model. `__repr__`, `__add__`, `__mul__`, `__contains__`, `__bool__`. The convention exists to avoid collisions with user-defined methods, which is reasonable, but the result is visually noisy in a way that never quite becomes invisible. Skimming a class definition and encountering `__getattribute__` feels like reading a sentence in ALL CAPS — technically correct, hard to tune out.

More practically, the naming implies these methods are private or internal, but many of them (especially `__init__`, `__repr__`, `__str__`) are things you're *expected* to implement and *expected* to see in everyday code. The dunder convention muddles the distinction between "internal implementation detail" and "standard protocol you should implement."

### No Formal Protocol Declaration

The data model is entirely convention-based. There's no way to declare that your class participates in the sequence protocol, the context manager protocol, or the iterator protocol. You just implement the right methods, and Python assumes you know what you're doing:

```python
class WeirdSequence:
    def __len__(self):
        return 5

    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return i * 10
```

Does this class correctly implement the sequence protocol? Partially. Python won't tell you. `len()` works, some indexing works, iteration works (Python will try `__getitem__` with increasing integers until it hits `IndexError`). But the behavior at indices 3 and 4 — which `__len__` says exist — is wrong. There's no static check, no runtime validation, no declaration to document intent.

Python 3.8 introduced `Protocol` in the `typing` module, which lets you express what a type must look like. But this is opt-in, and most code doesn't use it. The data model predates static typing in Python by two decades, and it shows.

### `__eq__` and the Hash Contract

If you define `__eq__`, Python automatically sets `__hash__` to `None`, making your objects unhashable:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p = Point(1, 2)
{p}  # TypeError: unhashable type: 'Point'
```

This is technically correct behavior — the Python docs explain that objects which compare equal must have the same hash, and if you've defined equality, Python can't know whether your hash function satisfies that contract. But the failure mode is silent until you try to put the object in a set or use it as a dict key, which may be far removed from where you defined `__eq__`. The fix is to also define `__hash__`, but nothing tells you that until the `TypeError`.

### `__repr__` vs `__str__`

Two methods for "turn this object into a string." `__repr__` should produce an unambiguous, ideally machine-readable representation. `__str__` should produce a human-friendly one. When you call `str(x)`, Python uses `__str__`. When you put an object in a collection and print the collection, Python uses `__repr__`. When you use f-strings, Python uses `__str__` by default, but `{x!r}` uses `__repr__`.

In theory this is fine. In practice, most classes only implement one, get confused about which one to implement, or implement `__repr__` to return the human-readable form (defeating its purpose). The Pythonic convention — "if in doubt, implement `__repr__` and have `__str__` fall back to it" — is not written anywhere obvious, and many developers invert it.

### `__new__` vs `__init__`

Python has two hooks for object construction. `__new__` is a static method that creates and returns the new object; `__init__` is an instance method that initializes the already-created object. For almost all code, you only ever need `__init__`. But `__new__` exists, it's documented, and it's occasionally necessary for metaclasses, singletons, and subclassing immutable types like `tuple`.

The existence of `__new__` creates a mental model split that doesn't need to exist for most developers. It also means that when someone asks "how do you implement a singleton in Python," the answer involves overriding `__new__` — which feels wildly disproportionate to the task.

### `__getattr__` vs `__getattribute__`

Two methods for attribute access. `__getattr__` is called only when normal attribute lookup fails; `__getattribute__` is called for every attribute access, every time. Implementing `__getattribute__` incorrectly is an infinite recursion waiting to happen, because accessing `self.anything` inside `__getattribute__` calls `__getattribute__` again:

```python
class Broken:
    def __getattribute__(self, name):
        return self.data[name]  # infinite recursion — self.data calls __getattribute__
```

The fix is `object.__getattribute__(self, 'data')`, which most developers don't know until they hit the recursion. It's a real footgun in a language that prides itself on being approachable.

## How Other Languages Handle This

Python's data model trades formal structure for flexibility. Other languages make different trade-offs:

**Clojure** uses explicit protocols. You declare a named interface with `defprotocol`, then implement it for specific types with `extend-type` or `defrecord`:

```clojure
(defprotocol Describable
  (describe [this]))

(defrecord Point [x y]
  Describable
  (describe [this]
    (str "Point at " x ", " y)))
```

Everything is explicit. The protocol name is visible in the code. If you implement a protocol partially, you get a clear error at definition time — not a `TypeError` at runtime. Code that depends on a protocol documents that dependency by name. This is expressive functional programming done right: you get the flexibility of duck typing, but you declare your protocols rather than relying on convention.

**Haskell** takes this to its logical conclusion with typeclasses. `Eq`, `Ord`, `Show`, `Num`, `Functor` — these are formally declared typeclasses, and if your type claims to implement one, the compiler verifies it:

```haskell
data Point = Point Int Int

instance Show Point where
  show (Point x y) = "Point at " ++ show x ++ ", " ++ show y

instance Eq Point where
  (Point x1 y1) == (Point x2 y2) = x1 == x2 && y1 == y2
```

The `Eq` typeclass automatically implies that `(/=)` works too, because it's defined in terms of `(==)`. The `Ord` typeclass requires `Eq` as a superclass — these constraints are checked at compile time. There are no silent `TypeError`s and no undiscoverable contracts. Haskell's typeclasses are the gold standard for what Python's data model is trying to do.

**C# (.NET)** uses interfaces with compiler enforcement:

```csharp
public class Point : IEquatable<Point>, IFormattable
{
    public int X { get; }
    public int Y { get; }

    public Point(int x, int y) => (X, Y) = (x, y);

    public bool Equals(Point? other) =>
        other is not null && X == other.X && Y == other.Y;

    public string ToString(string? format, IFormatProvider? provider) =>
        $"Point at {X}, {Y}";
}
```

More ceremony than Python, certainly. But the compiler will tell you if you declared `IEquatable<Point>` without implementing `Equals`. The BCL's standard interfaces — `IComparable`, `IEnumerable`, `IDisposable` — are documented, discoverable, and checked. When you implement `IDisposable`, you know exactly what contract you're signing up for, and the compiler holds you to it. This is the OOP answer to Python's convention-heavy model: explicit, type-checked, and self-documenting.

## The Verdict

Python's data model is one of the language's most thoughtful ideas. The insight that built-in operations should dispatch through a consistent set of special methods — giving user types and built-in types equal standing — is genuinely powerful, and it's baked into everything Python does well.

But the implementation is showing its age. Convention over declaration means tools can't check your work. The dunder naming makes protocols look more private than they are. The interaction between `__eq__` and `__hash__` is a bug factory for anyone who doesn't already know the rule.

Languages like Haskell and Clojure show that you can preserve all the flexibility of a protocol-based system while making the protocols explicit and checkable. C# shows that explicit interfaces don't have to be oppressively verbose. Python has moved in this direction with `Protocol` in `typing`, `abc.ABC`, and abstract base classes — but these are additions on top of the original system, not replacements for it. The seams show.

---
*[Previous: Literal Data Structures](../../posts/2023/07/pwaa-1-literal-data-structures/) | [Next: Comprehensions](../../posts/2026/02/pwaa-3-comprehensions/)*

</div>
