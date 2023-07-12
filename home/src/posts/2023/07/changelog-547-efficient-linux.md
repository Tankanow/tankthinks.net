---
templateEngineOverride: njk,md
metaTitle: Changelog 547 - Efficient Linux at the CLI
metaDescription: Changelog 547 - Efficient Linux at the CLI
title: Changelog 547 - Efficient Linux at the CLI
description: Changelog 547 - Efficient Linux at the CLI
featuredImg:
subHeading: Changelog 547 - Efficient Linux at the CLI
tags: ['know-notes', 'the-changelog']
date: 2023-07-10
updated:
published: true
---

<div class="col-start-3 col-end-9">


# [Changelog 547 - Efficient Linux at the CLI](https://changelog.com/podcast/547)

I was first schooled at the bash terminal in 2001. I was home from college and I had a summer gig at NMS Communications in Framingham, MA. Back in those days we barely had datacenters, I think we still called them computer labs: a room in the office with 10-50 racked computers, about 5-10 monitors that could be switched between the different servers, and you needed a parka because the max temperature seemed around 45℉.

We were using a few different flavors of Linux there. I remember RHEL and something like CentOS (though CentOS didn't exist yet). I foundered around at the terminal, barely finding my way from point A to B. But I had a wonderful manager, whose name I can't remember unfortunately, who was a wizard at the terminal. It was mindblowing to watch him work. He taught me many tricks I still use today, for example these aliases:

```bash
alias u='cd ..'
alias uu='cd ../..'
alias uuu='cd ../../..'
alias dv='dirs -v | column -t'
```


Then in 2008, my first gig back in Boston after 8 years away, I worked at Nuance Communications (no relation to NMS Communications) on a backend Speech Recognition system written entirely in [gasp] perl, bash, and Makefiles. This is where I really honed my bash skills.

## The Episode

I loved this episode. The only topic that I didn't recognize was `CDPATH`. That is pretty useful!

## On Process Substition

Another common use of process substition is `while` loop input. For example, a `while` can take a file as input this way:

```bash
while read dir ; do
  echo ${dir}
done < /tmp/some-text-file.txt
```

You can use process substition to chain more complicated commands together, e.g. loop through all child directories of the current directory, sorted, and exclude the `'.'` directory reference:

```bash
while read dir ; do
  echo ${dir}
done < <(find . -maxdepth 1 -type d | sort | grep -v -e '^\.$')
```

> NOTA BENE: Some may be wondering why not just pipe the output of the command directly into the `while`. You can do that in many cases, though I try to limit pipes interacting with loops because you can run into some pretty nefarious and hard to track down bugs, e.g. when _one_ iteration of a loop fails in its [piped subshell](https://www.gnu.org/software/bash/manual/bash.html#Pipelines).