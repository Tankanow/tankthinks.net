---
templateEngineOverride: njk,md
metaTitle: 3tilt Kickoff
metaDescription: 3tilt Kickoff
title: 3tilt Kickoff
description: 3tilt Kickoff
featuredImg:
subHeading:
tags: ['3tilt','docker','aws','learning','brain']
date: 2015-11-30
updated: 2015-11-30
published: true
---

<div class="col-start-3 col-end-9">




> The learning principle is to plunge into the detailed mystery of the micro in order to understand what makes the macro tick.
>
> I've been recording "3 Things I Learned Today" off and on for the past year. I was inspired by Raju Gandhi's ([@looselytyped](https://twitter.com/looselytyped)) NFJS talk "Learning to Learn" a few years ago. In May I gave a career day presentation to 7th graders at my wife's school and told them to start a "3tilt" (3 things I learned today) journal. The things you learn don't have to be traditionally academic: you could learn how to beat a difficult mission in Starcraft II or even the train schedule. The point of the exercise is reflection, gratitude, and continuous learning.
>
> ---
>
> `docker-compose` is a good tool for dev testing
> ... especially if you're travelling down the microservices route where your app has several external resources. A few recommendations when using `docker-compose`:
>
> 1.  `image` > `build` in the `docker-compose` configuration file: i.e. build the images for the app and its resources outside `docker-compose` and reference those prebuilt images from its configuration. Play around a bit, you'll see I'm right.
>
> 2.  upgrade to `docker-compose` v 1.5.0 or greater so you can use variable substitution in your `image` references
>
> 3.  remember that your links and environment are injected at `docker` "run" time, you can use the same images for testing and production with different environments
>
> create links between Elastic Beanstalk environments
> ... much like `docker-compose` allows you to create links between containers, Elastic Beanstalk let's you [create links between environments](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html): simply create an `env.yaml` file in the root directory of your application (more precisely the root dir where you will call the `eb` cli) and follow AWS's always sensible randomized configuration file format.
>
> stories are powerful
> ... I grabbed [Remapping Your Mind](http://www.amazon.com/gp/product/159143209X?keywords=remapping%20your%20mind&qid=1448935799&ref_=sr_1_1&sr=8-1) off the "New Non-Fiction" shelf of my local library when I returned Felicia Day's excellent memoir [You're Never Weird on the Internet (almost)](http://www.amazon.com/gp/product/1476785651?keywords=felicia%20day&qid=1448935874&ref_=sr_1_1&sr=8-1). I love the brain and usually read any book with the words "synapse", "mind", "neuroscience", etc. on the cover. This book makes a compelling case for the position stories in medicine. The authors use a plethora of techniques ranging from NLP to Native American spirit quests to help patients recover from acute medical conditions. A real testament to the power of the mind and the true physiology of the brain.
>
> --  Josh Waitzkin The Art of Learning
