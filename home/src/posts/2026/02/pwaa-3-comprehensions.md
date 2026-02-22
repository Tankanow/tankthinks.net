---
templateEngineOverride: njk,md
metaTitle: PWAA - Comprehensions
metaDescription: Python comprehensions are one of the language's best features, but nested comprehensions, single-use generators, and missing conveniences reveal real rough edges.
title: PWAA - Comprehensions
description: Python comprehensions are one of the language's best features, but nested comprehensions, single-use generators, and missing conveniences reveal real rough edges.
featuredImg:
subHeading: Python Warts and All
tags: ['python-warts-and-all', 'comprehensions']
date: 2026-02-22
updated:
published: true
---

<div class="col-start-3 col-end-9">

# PWAA - Comprehensions

If someone asked me to show a non-Pythonista one feature that captures why people love Python, I'd probably reach for a list comprehension. It's one of those rare language features that feels like it was designed by someone who actually writes code for a living. But like most things in Python, the elegance has a ceiling — and the ceiling is lower than you'd hope.

*This is chapter 3 of [Python Warts and All](../../works/20230718-python-warts-and-all/).*

## The Good

List comprehensions are, in my experience, the single most effective way to make Python code feel clean. The pattern is simple and reads almost like English:

```python
doubled = [x * 2 for x in items if x > 0]
```

Filter and transform in one expression. No `append` calls, no temporary variables, no ceremony. Once you internalize the pattern, you can read it at a glance. It's one of the few places where Python genuinely delivers on its "executable pseudocode" reputation.

And it's not just lists. Dict comprehensions and set comprehensions follow the same shape and feel equally natural:

```python
lookup = {k: v for k, v in pairs}
unique_lower = {word.lower() for word in words}
```

Then there are generator expressions — same syntax, but with parentheses instead of brackets, and they're lazy. They don't materialize a whole list in memory. If you're processing a million rows, `sum(x * 2 for x in items)` is doing the right thing without you having to think about it. That's good design.

There's also a practical performance benefit in CPython. List comprehensions compile to tighter bytecode than the equivalent `for` loop with `append` calls. The difference isn't enormous, but it's real and measurable — typically 10-30% faster. It's one of those nice cases where the more readable option is also the faster one.

## The Warts

The moment you nest comprehensions, the readability advantage evaporates. Consider transposing a matrix:

```python
transposed = [[row[i] for row in matrix] for i in range(4)]
```

Which `for` runs first? Which is the outer loop? I've been writing Python for over a decade and I still pause on these. The reading order is inside-out relative to how you'd write the equivalent nested `for` loops, and that's genuinely confusing. My rule of thumb: if a comprehension needs more than one `for` clause, it probably shouldn't be a comprehension.

The walrus operator (`:=`, introduced in 3.8) made things worse. It enables patterns like avoiding redundant function calls:

```python
results = [y for x in items if (y := expensive(x)) > threshold]
```

Clever? Yes. Easy to read six months later? Not in my experience. The assignment happens as a side effect inside a filter expression. It works, but it pushes comprehensions into territory where a plain `for` loop would be kinder to your future self.

There's a common task that has no clean comprehension solution: getting the first item that matches a predicate. The idiom is:

```python
first = next(x for x in items if x > 10)
```

This works, but if nothing matches, it raises `StopIteration` — not `ValueError`, not `None`, not some sensible default. You can pass a default to `next()` as a second argument, but the syntax gets awkward and most people forget it exists. Python could really use a built-in `first()` function.

Similarly, there's no comprehension syntax for flattening. If you want to flatten a list of lists, you either write a confusing nested comprehension or reach for `itertools.chain.from_iterable`. Neither is obvious to newcomers.

The subtlest wart is that generator expressions are stateful and single-use. Once you iterate through one, it's exhausted. Pass one to two different functions and the second gets nothing. This is a bug factory, especially for developers coming from languages where lazy sequences are replayable. Python gives you no warning — the generator just silently yields zero items.

One final historical note: in Python 2, list comprehensions leaked their loop variable into the enclosing scope. `[x for x in range(10)]` would leave `x = 9` hanging around after the comprehension. Python 3 fixed this by giving comprehensions their own scope, but if you learned Python before 3.0, the muscle memory of that gotcha lingers longer than you'd think.

## The Verdict

Comprehensions are one of Python's genuinely great ideas. For simple filter-and-transform operations on sequences, nothing in the language is more expressive or more readable. They deserve their reputation.

But Python leans on them too hard. The language lacks built-in conveniences for common patterns like "find the first match" or "flatten nested iterables," so people end up contorting comprehensions to fill those gaps. And once you add nesting or walrus operators, you've traded the original clarity for cleverness — which is almost always the wrong trade. Keep your comprehensions simple and they'll serve you well. The moment they stop being obvious at a glance, reach for a `for` loop without guilt.

---
*[Previous: The Python Data Model](../../posts/2023/07/pwaa-2-data-model/) | [Next: Generators](../../posts/2026/PENDING/pwaa-4-generators/)*

</div>