# CLAUDE.md

This file provides guidance for Claude Code when working in this repository.

## Project Overview

Personal blog for Adam Tankanow (tankthinks.net). Built with Eleventy (11ty) and
Tailwind CSS, deployed to AWS S3 + CloudFront via GitHub Actions.

The repository contains two site implementations:

- `home/` — **Active** Eleventy/Tailwind site (all new work goes here)
- `blog/` — **Archived** Clojure/Cryogen site (do not modify)

## Development

All commands run from the `home/` directory.

```bash
cd home
npm install          # install dependencies (first time only)
npm start            # dev server with hot reload at http://localhost:8080
npm run build        # dev build → home/_site/
npm run build:prod   # production build → home/_site/
```

There are no test or lint scripts. The CI check is a successful `build:prod`.

## Repository Structure

```
home/
├── src/
│   ├── posts/          # Blog posts (Markdown, dated filenames)
│   ├── _layouts/       # Nunjucks templates (base, single, posts, works, index)
│   ├── _components/    # Reusable Nunjucks partials
│   ├── _data/          # Site metadata, authors, services (JSON)
│   ├── css/            # Tailwind + custom styles
│   ├── img/            # Static images
│   └── admin/          # Netlify CMS config (config.yml)
├── .eleventy.js        # Eleventy config (plugins, Cloudinary, Markdown)
├── tailwind.config.js  # Tailwind JIT config
├── postcss.config.js   # PostCSS pipeline (Tailwind → Autoprefixer → cssnano)
└── package.json

.github/workflows/
├── build-eleventy.yml  # Build & artifact upload (all branches)
└── deploy.yaml         # S3 sync + CloudFront invalidation (main branch only)

template.yaml           # AWS SAM/CloudFormation infrastructure definition
samconfig.toml          # AWS SAM CLI deploy config
```

## Key Conventions

### Adding a Blog Post

Create a Markdown file in `home/src/posts/` using the front matter format:

```yaml
---
title: Post Title
description: Short description
date: 2024-01-01
tags:
  - tag-name
featuredimage: https://res.cloudinary.com/ddkpjnidm/...
publish: true
---
```

### Templating

Templates use **Nunjucks** (`.njk`). The layout chain is:
`base.njk` → `single.njk` / `posts.njk` / etc.

### Images

Images are hosted on **Cloudinary** (cloud name: `ddkpjnidm` / `tankthinks`).
The `.eleventy.js` config generates responsive `<picture>` elements at widths
400, 600, 768, 820, and 1240px in WebP format.

Do not commit large images directly to the repo — use Cloudinary URLs instead.

### CSS

Tailwind JIT purges unused classes from Nunjucks and Markdown files. Custom
styles live in `home/src/css/`. PostCSS runs the full pipeline on build.

## Deployment

Merging to `main` triggers the full deploy pipeline automatically:

1. GitHub Actions builds `home/` with `npm run build:prod`
2. Artifacts are synced to `s3://tankthinks.net/`
3. A CloudFront invalidation clears the CDN cache

Infrastructure (S3, CloudFront, WAF, Route53, ACM) is defined in
`template.yaml` and managed via AWS SAM.
