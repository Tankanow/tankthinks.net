---
layout: single.njk
metaTitle: Experience — Adam Tankanow
metaDescription: Founding engineer. Nine years. Zero to 270k lines of code. Strong beliefs, loosely held.
title: Experience
description: I'm not looking for a job. I just believe in writing things down.
featuredImg:
templateEngineOverride: njk,md
---

<div class="col-start-3 col-end-9">

# Experience

I'm not looking for a job. But one of my [first principles](/about/) is _Write Things Down_ — you won't remember tomorrow. My last resume was from October 2015. That's a decade of unwritten things. Time to fix that.

## The Short Version

I'm the founding engineer at [CloudZero](https://www.cloudzero.com). I joined pre-funding in July 2017 and helped build a multi-tenant SaaS FinOps platform from 0 lines of code and 1 engineer to ~270,000 lines of code, 40+ engineers, and 300+ customers. Along the way I made every category of mistake available — architectural, organizational, interpersonal, sartorial — and learned from most of them. I can now direct a swarm of AI agents through a codebase I've been building for nine years, which turns out to be a surprisingly useful skill when you've made all the mistakes the agents are about to make.

Once called obstreperous. I took it as a compliment.

---

## Before CloudZero

The path here was not linear. That's the point.

**Tulane University** — B.S. Computer Science, 2004. Started programming with [HyperCard](https://en.wikipedia.org/wiki/HyperCard) in elementary school and made a Calvin and Hobbes trivia game. Spent college discovering that the interesting problems live at the intersection of disciplines.

**Bose Corporation** — Software Engineer, 2004–2005. First real job. First taste of the intersection of audio and software. Enough to know I wanted more.

**University of Miami** — M.S. Music Engineering Technology, 2007. Thesis: _Automatic Extraction of a Measure of Complexity from an Audio Sound File_. Taught machines to quantify what makes audio complex — spectral analysis, psychoacoustic modeling, signal decomposition. Published at [AES](https://www.aes.org/).

**Dolby Laboratories** — Implementation Engineer, 2007–2008. Helped Samsung, NEC, and STMicroelectronics implement Dolby technologies on embedded platforms. Learned that reading someone else's datasheet at 2am is a special kind of intimacy.

**Nuance Communications** — Sr. Software Engineer → Development Manager, 2008–2015. The seven-year tour. Operated speech recognition infrastructure serving 3 billion transaction lines per year. Led a monolith-to-microservices migration using DDD, Clean Architecture, and Spring Boot — before it was fashionable and after it was obviously necessary. Won an internal innovation challenge with a patent-pending prototype. Led cross-functional critical incident response. Increased engineering conference attendance 100% two years running because I kept asking people to go.

**MassMutual** — Application Engineer, 2015–2017. The "startup inside a Fortune 100" pitch. I learned a lot. It was not the dream.

---

## CloudZero: Founding Engineer (2017–Present)

This is the part that matters. Not a job description — an honest accounting.

### The Numbers

| | |
|---|---|
| **Lines of code** | 0 → ~270,000 |
| **Engineers** | 1 → 40+ |
| **Customers** | 0 → 300+ |
| **Monorepo packages** | 158 |
| **Deployable Lambda services** | 100+ |
| **Cloud providers** | 3 (AWS, Azure, GCP) |
| **Years** | ~9 and counting |

### What I Actually Built

**The Platform.** Serverless-first on AWS Lambda, API Gateway, EventBridge, SQS, SNS, DynamoDB, S3. Python and TypeScript. CloudFormation and Pulumi for infrastructure-as-code. GitHub Actions for CI/CD. Designed for a team of one, scaled to a team of forty.

**Multi-Tenant Authentication & Authorization.** Auth0 integration, SAML, SSO, OIDC, API keys, RBAC, data access controls. Tenant isolation across every layer — compute, storage, API, event bus. The kind of work where a bug isn't a bug, it's a breach.

**Data Pipelines.** Billing data ingestion from AWS, Azure, and GCP — each with their own special flavor of chaos — normalized into Snowflake. Custom dimension allocation via a DSL we call CostFormation. Anomaly detection. Forecasting. The plumbing that makes FinOps possible.

**The Frontend.** React and TypeScript. Evolved through Redux, an Nx monorepo, TanStack Router and Query, Chakra UI. Multiple generations, each one a reaction to what we learned from the last. The frontend is never done. Accept this and find peace.

**Multi-Cloud.** Adapter pattern for AWS, Azure, and GCP cost and resource data. A connector framework supporting 17+ providers. Multi-cloud is easy to say and hard to build because every provider thinks they invented billing.

**AI Integration.** Claude-powered cloud cost advisor built with LangChain and LangGraph. An MCP server. AI-driven ops tooling. The part where the platform I built starts building itself.

**Everything Else.** Internal CLIs, ops tooling, observability (SumoLogic, X-Ray), customer onboarding flows, a billing data generator for testing, Slack bots, ticket integrations (Jira, ServiceNow). The long tail of things that don't fit in a slide deck but keep the lights on.

**The Non-Code Parts.** Sales engineering. Customer support. Product strategy. Hiring. Culture-building. Incident response. Documentation. The work that doesn't show up in `git log` but determines whether the company survives.

### Certifications

- AWS Certified Solutions Architect — Professional (2019)

### Publications

- _Effects of Oversampling on SNR Using Swept-Sine Analysis_ — Audio Engineering Society, 2010
- _Automatic Extraction of a Measure of Complexity from an Audio Sound File_ — M.S. Thesis, University of Miami, 2007

---

## What I Learned

These aren't bullet points for a recruiter. These are first principles earned over nine years, not inherited. I got most of them wrong at least once before I got them right.

- **Code is liability.** Write less of it whenever possible.
- **Understand the domain.** The best code is the code that most clearly represents domain rules. If you don't understand the business, your abstractions are fiction.
- **Don't break your consumers.** 99% of the time, it is uncalled for.
- **Focus on flow.** Not just _your_ flow — your teammates' flow. Move value to the right.
- **Respect the Lindy Effect.** Research ideas that have been useful for a long time. Fred Brooks is still right. Eric Evans is still right. They'll be right after we're gone.
- **Write things down.** You won't remember tomorrow.
- **Strong beliefs, loosely held.** Have opinions. Back them with evidence. Change them when the evidence changes. This is not weakness.
- **Take long walks.** Don't listen to podcasts or music. Find trees.

---

## The Punchline

After building a platform from zero, watching it scale, making every category of mistake, leading teams, losing arguments, winning some back, and now directing AI agents to work in the codebase I've been building for nearly a decade — you develop opinions. Strong ones. Loosely held.

The strongest one: the hard part was never the code. It was understanding what to build, convincing people it mattered, and then writing it down so the next person didn't have to learn it the hard way.

I'm a natural Learner, Cultivator, Connector, and Arranger. My superpower is connecting people — to ideas, to each other, to the thing they didn't know they needed to read. If you've gotten this far, we should probably talk.

---

## If You're Hiring

I'm not actively looking — I'm still building at CloudZero and I'm not done yet. But I've advised startups in the Boston VC community on architecture, hiring, and engineering culture, and I'm always open to interesting conversations. If you're solving a hard problem and want a second opinion, I like those calls.

If you _are_ recruiting and think there's a fit worth exploring, I'm flattered. Just know: if your interview process includes me live-coding a leetcode problem on a whiteboard (virtual or physical), come prepared to explain why that matters — especially to your business value. I've spent nine years solving real problems in production systems with real customers and real consequences. I'm happy to show you that work. I'm less interested in proving I can reverse a linked list under fluorescent lighting. Unless it's Clojure — I'm almost always happy to write Clojure — even in service of an increasingly Byzantine hiring practice.

Strong belief, loosely held.

If your applicant tracking system requires a PDF instead of a URL, [here you go](/static/adam-tankanow-experience.pdf).

---

## Say Hello

- **Email:** adam.tankanow@gmail.com
- **GitHub:** [tankanow](https://github.com/tankanow)
- **LinkedIn:** [adamtankanow](https://www.linkedin.com/in/adamtankanow/)
- **Blog:** [tankthinks.net](https://tankthinks.net)

</div>
