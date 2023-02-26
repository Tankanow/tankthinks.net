---
templateEngineOverride: njk,md
metaTitle: 10 Observations From Scrumbut
metaDescription: 10 Observations From Scrumbut
title: 10 Observations From Scrumbut
description: 10 Observations From Scrumbut
featuredImg: 
subHeading: 
tags: ['scrum','hickey']
date: 2014-03-01
updated: 2014-03-01
published: true
---

<div class="col-start-3 col-end-9">




**Scrumbut**

What is scrumbut?

1.  Scrum has a lot of overhead Between the planning, scrums, review and retrospectives this is a heavy weight process.

2.  Scrumbut has *MORE* overhead Does it? Or is this a nice headline

3.  We do the easy but least-effective parts of scrum I think Venkat said this in a presentation: we choose the easy but useless parts of scrum. We choose to do the daily standups but what benefit are they? We kind of do user stories

4.  Grooming the backlog is hard Speaking to you as an engineer turned manager: grooming the backlog is not easy. When you are scrumming in a fixed-length project, managing the backlog is essential *and* difficult.

5.  Functionality is everything You must build incremental functionality. Every sprint show something. Demo. Demo. Demo. Prototype if you have to. Just don't disappear down the rabbit hole for 3 weeks with nothing to show for it.

6.  Simplicity over All Else Rich Hickey joked about this in the seminal presentation Simple Made Easy; How can you sprint forever? Just fire the starting gun every 40 yards. Teams can't sprint forever. However, teams can build simple software that is easier to maintain and extend.

7.  Binary Rules When in doubt, distill a problem to two alternatives ... then choose the one that is more flexible.

8.  Baby Steps Take small steps. It doesn't make any sense to refactor your bad design into a perfect SOA in one sprint. As Bob said, "baby steps".

9.  Executable Acceptance Tests over Unit Tests Don't get me wrong, I love unit tests. Unit tests are essential if you want to refactor later. However, unit tests don't guarantee functionality. Functional tests gaurantee funcitonality, but we don't know if it is the *right* functionality. Only acceptance tests, executable use case acceptance tests, are valuable as repeatable tests to see if your module/deliverable/artifact does what the stakeholders want it to do.

10. Never forget deployment Have you written beatiful code only to realize that deploying it is a tangled hairball. Start with the end. Think about the machines on which your code will run first. Then work your way back to the design. Too often teams focus on class diagrams 90% and spend only 10% on component/deployment design.