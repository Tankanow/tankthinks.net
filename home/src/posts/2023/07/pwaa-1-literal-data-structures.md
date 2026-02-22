---
templateEngineOverride: njk,md
metaTitle: PWAA - Literal Data Structures
metaDescription: Python's literal data structures are one of its best features — until you hit tuples, sets, and mutability defaults that reveal a language that evolved rather than was designed.
title: PWAA - Literal Data Structures
description: Python's literal data structures are one of its best features — until you hit tuples, sets, and mutability defaults that reveal a language that evolved rather than was designed.
featuredImg:
subHeading: Python Warts and All
tags: ['python-warts-and-all', 'data-structures']
date: 2023-07-13
updated:
published: true
---

<div class="col-start-3 col-end-9">

# PWAA - Literal Data Structures

If you've spent time in Java or C# before coming to Python, there's a moment early on where you stop and think: *is it really this easy?* You write a dict or a list directly in code, no constructors, no generics, no ceremony — and it just works. That feeling is earned. Python's literal data structures are genuinely great. They're also where you first start collecting your list of complaints.

*This is chapter 1 of [Python Warts and All](../../works/20230718-python-warts-and-all/).*

## The Good

Python lets you write structured data directly in code, the same way you'd write it on a whiteboard:

```python
user = {"name": "Alice", "age": 30, "roles": ["admin", "editor"]}
primes = [2, 3, 5, 7, 11]
point = (4, 9)
unique_ids = {101, 102, 103}
```

This is worth appreciating before picking it apart. Compare it to the Java equivalent of the dict above:

```java
Map<String, Object> user = new HashMap<>();
user.put("name", "Alice");
user.put("age", 30);
user.put("roles", Arrays.asList("admin", "editor"));
```

Java's verbosity isn't just aesthetic noise — it's friction that makes you less likely to reach for a map when a map is the right tool. Python removes that friction entirely. You see data and you write data.

The dict literal syntax also mirrors JSON so closely that Python has become a natural choice for data work. Reading a JSON API response and immediately working with it as a Python dict, with no manual parsing or deserialization, feels like the language was built for this decade. In a sense, it was — the feature predates JSON as a standard, but the alignment turned out to be fortuitous.

Set literals earn their place too. Once you see `{1, 2, 3}` for "a collection with no duplicates," you can't unsee how clean it is relative to most languages' alternatives.

## The Warts

### Tuples and the Trailing Comma Trap

The tuple is probably the first literal data structure that surprises you. Parentheses don't make a tuple — the comma does:

```python
x = (1)    # int, not tuple
x = (1,)   # tuple with one element
x = 1,     # also a tuple — no parens needed
```

That trailing comma on the single-element tuple is mandatory, and it's a source of genuine bugs. The parens-as-grouping and parens-as-tuple-constructor collision is an accident of Python's history, and it never gets fully comfortable. If you're building a tuple programmatically, you'll second-guess yourself every time.

### The Empty Set Problem

This one trips up almost everyone:

```python
empty_dict = {}    # dict
empty_set = set()  # set — no literal syntax
```

There is no empty set literal. `{}` was already taken by dicts when sets got their literal syntax in Python 2.7. So non-empty sets get a clean literal (`{1, 2, 3}`), but you can't write an empty set the same way. `set()` looks like a function call, not a value — and in a language that otherwise has clean literal syntax for everything, the inconsistency sticks out.

### Mutability Is the Default

Python's built-in collection types are mutable by default. Lists, dicts, and sets are all mutable; only strings and tuples are immutable. This seems reasonable until you start passing data structures around and hitting aliasing bugs:

```python
def process(config):
    config["debug"] = True  # oops — mutated the caller's dict

settings = {"debug": False}
process(settings)
print(settings["debug"])  # True — surprise
```

Python offers `tuple` as an immutable alternative to `list`, but it's a second-class option: `tuple` can't be used where a sequence is expected in many APIs, it reads differently, and there's no immutable equivalent for dicts at all in the builtins. `frozenset` exists for sets, but with syntax so inelegant it barely counts:

```python
frozen = frozenset({1, 2, 3})
```

That's not a literal — it's a constructor call wrapping a set literal. You feel the seam.

### Dictionary? Really?

A minor complaint, but worth naming: Python calls its hash map a `dict` (short for "dictionary"). Most languages call it a map, hash, or hash map. The Python name is intuitive once you know it, but "dictionary" is the term for an alphabetically-ordered reference book — not for an arbitrary key-value store. The name reflects the language's age more than a principled choice.

## How Other Languages Handle This

Python's literals are good but not the state of the art. For comparison:

**Clojure** takes literal data structures further. It has vectors `[1 2 3]`, maps `{:name "Alice" :age 30}`, and sets `#{1 2 3}`. The key difference: all Clojure collections are **immutable by default**. Persistent data structures let you "modify" a collection and get back a new version efficiently, without mutating the original. The aliasing bugs that catch Python developers simply don't exist. Clojure's maps also use keywords (`:name`, `:age`) as keys, which are self-documenting, fast, and more expressive than plain strings. The entire data model is more principled.

```clojure
;; All of these are immutable
(def user {:name "Alice" :age 30 :roles ["admin" "editor"]})
(def primes [2 3 5 7 11])
(def unique-ids #{101 102 103})
```

**TypeScript** keeps JavaScript's object and array literals but adds a type layer that catches mistakes at compile time:

```typescript
const user: { name: string; age: number; roles: string[] } = {
  name: "Alice",
  age: 30,
  roles: ["admin", "editor"],
};
```

More ceremony, but the type annotation means a typo in a key name or the wrong value type is a compile error, not a runtime surprise. TypeScript also has `readonly` and `ReadonlyArray<T>` for expressing immutability at the type level — something Python's type system can gesture at with `Final` but can't enforce.

**C# (.NET)** has object initializers and collection initializers that close the verbosity gap significantly:

```csharp
var user = new Dictionary<string, object>
{
    { "name", "Alice" },
    { "age", 30 }
};
```

More syntax than Python, but the types are explicit. With C# 9 records, you get value-type semantics with clean initialization for structs:

```csharp
record Point(int X, int Y);
var p = new Point(4, 9);  // immutable by default
```

Records in .NET give you the OOP answer to Python's tuple: an immutable, structurally-typed value with named fields and proper equality semantics. Python's `dataclasses` module with `frozen=True` gets you partway there, but it's opt-in and less discoverable.

## The Verdict

Python's literal data structures are one of the language's genuine strengths, and they deserve their reputation. The friction-free syntax for dicts, lists, and sets makes data-heavy code readable and fast to write.

But the cracks show quickly. The tuple's trailing comma, the empty set oddity, and the mutable-by-default stance are small decisions that compound into a pattern: Python's data model was built up incrementally rather than designed holistically. Languages like Clojure show what it looks like to start from first principles — immutability as the default, data as a first-class concept — and the difference in day-to-day code quality is real.

Python's literals get you far. Just don't mistake "far" for "all the way."

---
*[Next: The Python Data Model](../../posts/2023/07/pwaa-2-data-model/)*

</div>
