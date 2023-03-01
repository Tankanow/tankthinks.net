---
templateEngineOverride: njk,md
metaTitle: Python Bytes 325
metaDescription: Python Bytes 325
title: Python Bytes 325
description: Python Bytes 325
featuredImg:
subHeading: Python Bytes 325
tags: ['know-notes', 'python-bytes']
date: 2023-03-01
updated:
published: true
---

<div class="col-start-3 col-end-9">


# [Python Bytes 325](home/src/posts/2023/02/changelog-news-monday-27-feb-2023.md)

## Parquet and PyArrow

We use a lot of Parquet at [CloudZero](https://cloudzero.com). I never thought of PyArrow as a replacement for pandas _DataFrames_, just as a replacement for CSV.
However, there are some places we may be able to benefit from Polars.

## FastAPI-Filter

We don't use FastAPI, but I did spearhead the design and implementation of [CloudZero's Resource-Oriented Programmatic APIs](https://docs.cloudzero.com/reference/introduction). We do think a lot about how to filter the GET <collection> endpoints.

I do like the declarative style of this library and will try to steal something from it. I do NOT like ORMs or tying external data models to internal ones. So I think the option to apply a FastAPI-Filter to a SQLAlchemy model, while convenient, is a mistake in the long term for most applications.

> Avoid Leaking Implementation Details at All Costs

## 12 Python Decorators to Take Your Code to the Next Level

Decorators are the best part of Python. I love decorators. There are some useful [Retry](https://github.com/rholder/retrying) and [Rate Limiting](https://github.com/tomasbasham/ratelimit) PyPI Packages that provide nice decorators.

## PyHamcrest

Ooooh. Reminding me of my Java days. For those who don't know, this was born out a Java Library and is now available in [many languages](https://hamcrest.org/) I do like improving readability.

## Extras

- Python 3.11.2 ... arrgghhh ... AWS Lambda is still on 3.9!
- I wonder how much imageoptim.com would help with this website
- pytest tips and tricks
    - OOOOh ... I did not know about `pytestmark = pytest.mark.foo`
