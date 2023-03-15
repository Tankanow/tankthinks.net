---
templateEngineOverride: njk,md
metaTitle: Talk Python to Me 406
metaDescription: Talk Python to Me 406
title: Talk Python to Me 406
description: Talk Python to Me 406
featuredImg:
subHeading: Talk Python to Me 406
tags: ['know-notes', 'talk-python-to-me']
date: 2023-03-01
updated:
published: true
---

<div class="col-start-3 col-end-9">


# [Talk Python to Me 406](https://talkpython.fm/episodes/show/406/reimagining-pythons-packaging-workflows)

## Guests
- Steve Dower
- [Pradyun Gedam](https://pradyunsg.me/blog/2023/01/21/thoughts-on-python-packaging/)
- [Ofek Lev](https://github.com/ofek) (Creator of Hatch)
- Paul Moore


## Overview

The guests agree that there is a problem but not how to solve it. The community has the appetite to solve this problem now, but does it have the momentum to follow through.

## Some Takeaways

- Python packaging is a bit interesting/different from other languagus in that Python does not itself provide many of the distributions, leaving that up to the individual platform communities, e.g. Ubuntu.
- `pip` occupies a special seat at the table because it ships with Python, but is it the right tool.


## My Thoughts

**pyenv**
No mention of `pyenv` as a possible tool.

**pipenv**
No mention of how the community (and python.org) backed `pipenv`.

**conda**
`conda` has been around for 10 years. Why hasn't it won the war?

**dependency hell**
No discussion of the specifics of dependency hell that the current resolvers in all major tools have, i.e. lacking the ability to override "incompatible" transitive dependencies, though Ofek hinted at something ...

**differences between libraries and applications**
Ofek mentioned that Python has a woeful application development experience. Coincidentally, I discussed this with Erik, CTO of CloudZero, this week. Libraries and Applications have different tooling requirements. For example:

- Applications should pin dependencies, Libraries should not
- Applications target 1 Python version, Libraries target many

**lockfiles**
Ofek rightly brings up that the lack of a lockfile standard hampers solving dependency problems.

## tl;dr;
I'm concerned that Python's community is overly democratic w.r.t to tooling. Perhaps a BDFL would be able to rally the troops around a common solution faster than discord discussions.