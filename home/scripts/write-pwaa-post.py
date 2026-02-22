#!/usr/bin/env python3
"""
PWAA Weekly Post Writer
=======================
Uses the Claude API to draft the next chapter in the "Python Warts and All"
series. Reads chapter notes from pwaa-notes.json, determines which post comes
next, generates a full blog post, and writes it to the correct path.

Run manually:
    python write-pwaa-post.py

Requires:
    pip install anthropic
    ANTHROPIC_API_KEY env var set
"""

import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import anthropic

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
POSTS_DIR = REPO_ROOT / "home" / "src" / "posts"
NOTES_FILE = SCRIPT_DIR / "pwaa-notes.json"

SYSTEM_PROMPT = """\
You are a technical blogger writing a chapter in the "Python Warts and All" series
for tankthinks.net, the personal blog of a founding engineer.

Tone:
- Opinionated but fair. Direct and honest.
- First person ("I've found...", "In my experience...")
- Concrete code examples where helpful (keep them short)
- Conversational but technically precise
- Aim for 600-900 words
- Not inflammatory, but willing to criticize Python where warranted

Structure (must follow this format exactly):

---
templateEngineOverride: njk,md
metaTitle: PWAA - {title}
metaDescription: {one sentence description}
title: PWAA - {title}
description: {one sentence description}
featuredImg:
subHeading: Python Warts and All
tags: ['python-warts-and-all', '{topic_tag}']
date: {date}
updated:
published: true
---

<div class="col-start-3 col-end-9">

# PWAA - {title}

[intro paragraph — hook the reader, 2-3 sentences]

*This is chapter {num} of [Python Warts and All]({works_url}).*

## The Good

[2-4 paragraphs covering what's genuinely great about this feature]

## The Warts

[2-4 paragraphs covering the genuine pain points, with examples where useful]

## The Verdict

[1-2 paragraph summary — what's your net take?]

---
*[Previous: {prev_title}]({prev_url}) | [Next: {next_title}]({next_url})*

</div>

Important rules:
- The front matter block must be the very first thing in the file (starting with ---)
- Do NOT add ```yaml or ``` fences around the front matter
- Do NOT add ```markdown or ``` fences around the body
- topic_tag should be a short kebab-case tag for the topic (e.g., 'comprehensions', 'typing')
- Include only the {next} or {prev} links that exist — omit the separator if only one applies
- Do not include Cloudinary image URLs — leave featuredImg blank
"""


def load_notes() -> dict:
    with open(NOTES_FILE) as f:
        return json.load(f)


def find_next_chapter(notes: dict) -> dict | None:
    """Find the first chapter that has status 'not_started'."""
    for chapter in notes["chapters"]:
        if chapter["status"] == "not_started":
            return chapter
    return None


def get_adjacent_chapters(notes: dict, current_num: int) -> tuple[dict | None, dict | None]:
    """Return (prev, next) chapters for navigation links."""
    chapters = notes["chapters"]
    prev_ch = next((c for c in chapters if c["num"] == current_num - 1), None)
    next_ch = next((c for c in chapters if c["num"] == current_num + 1), None)
    return prev_ch, next_ch


def post_url(chapter: dict) -> str:
    return f"../../posts/2026/02/{chapter['slug']}/"


def works_url(notes: dict) -> str:
    return notes["series"]["works_url"]


def build_user_prompt(notes: dict, chapter: dict) -> str:
    series = notes["series"]
    prev_ch, next_ch = get_adjacent_chapters(notes, chapter["num"])

    prev_info = ""
    if prev_ch:
        prev_info = f"Previous chapter: '{prev_ch['title']}' at URL: ../../posts/2023/07/{prev_ch['slug']}/"

    next_info = ""
    if next_ch:
        next_info = f"Next chapter: '{next_ch['title']}' at URL: (will be determined when written, use placeholder like ../../posts/2026/PENDING/{next_ch['slug']}/)"

    return f"""Write chapter {chapter['num']} of the "{series['title']}" series.

Chapter title: {chapter['title']}
Today's date: {date.today().isoformat()}
Works page URL: {series['works_url']}

Series description: {series['description']}

{prev_info}
{next_info}

Raw notes for this chapter:

GOOD things about this topic:
{json.dumps(chapter['notes']['good'], indent=2)}

WARTS (problems/annoyances):
{json.dumps(chapter['notes']['warts'], indent=2)}

Relevant links to consider including:
{json.dumps(chapter['notes'].get('links', []), indent=2)}

Write the full blog post now. Output ONLY the post content — no commentary, no explanation.
Start with the front matter block (---).
"""


def determine_post_path(chapter: dict) -> Path:
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    directory = POSTS_DIR / year / month
    directory.mkdir(parents=True, exist_ok=True)
    return directory / f"{chapter['slug']}.md"


def write_post(content: str, path: Path) -> None:
    path.write_text(content)
    print(f"Wrote post to: {path}")


def create_pr(chapter: dict, post_path: Path) -> None:
    """Create a git branch, commit the new post, push, and open a PR."""
    branch = f"claude/pwaa-chapter-{chapter['num']}-{chapter['slug']}"
    rel_path = post_path.relative_to(REPO_ROOT)

    cmds = [
        ["git", "-C", str(REPO_ROOT), "checkout", "-b", branch],
        ["git", "-C", str(REPO_ROOT), "add", str(rel_path)],
        [
            "git",
            "-C",
            str(REPO_ROOT),
            "commit",
            "-m",
            f"feat(pwaa): draft chapter {chapter['num']} — {chapter['title']}",
        ],
        ["git", "-C", str(REPO_ROOT), "push", "-u", "origin", branch],
    ]

    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running {' '.join(cmd)}:\n{result.stderr}", file=sys.stderr)
            sys.exit(1)

    # Create PR via gh CLI
    pr_body = f"""## PWAA Chapter {chapter['num']}: {chapter['title']}

This is an AI-drafted blog post for the Python Warts and All series.

**Please review:**
- [ ] Technical accuracy
- [ ] Tone and voice match the series
- [ ] Links work
- [ ] Front matter is correct
- [ ] Update the works page (`home/src/works/20230718-python-warts-and-all.md`) to add this chapter link

> Generated by Claude ({date.today().isoformat()})
"""

    result = subprocess.run(
        [
            "gh",
            "pr",
            "create",
            "--title",
            f"[PWAA Draft] Chapter {chapter['num']}: {chapter['title']}",
            "--body",
            pr_body,
            "--head",
            branch,
        ],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )

    if result.returncode == 0:
        print(f"PR created: {result.stdout.strip()}")
    else:
        print(f"PR creation failed (you can create it manually):\n{result.stderr}", file=sys.stderr)


LINKEDIN_SYSTEM_PROMPT = """\
You write LinkedIn posts for a software engineer's personal blog.

Tone:
- Professional but conversational, not corporate-speak
- First person
- No cringe hashtag spam — at most 3 relevant hashtags at the end
- Hook in the first line (no "Excited to share..." opener)
- 150-250 words total

Structure:
1. Opening hook (1 sentence — something punchy or provocative about the topic)
2. What the post covers (2-3 sentences)
3. A teaser — one concrete insight or surprising take from the post
4. Call to action with the link
5. 2-3 relevant hashtags on their own line

Output ONLY the LinkedIn post text. No commentary, no labels.
"""


def blog_post_url(post_path: Path) -> str:
    """Derive the live blog URL from the post file path."""
    # Path is like .../home/src/posts/2026/02/pwaa-3-comprehensions.md
    # URL is https://tankthinks.net/posts/2026/02/pwaa-3-comprehensions/
    parts = post_path.parts
    posts_idx = next(i for i, p in enumerate(parts) if p == "posts")
    url_path = "/".join(parts[posts_idx:])
    slug = url_path.removesuffix(".md")
    return f"https://tankthinks.net/{slug}/"


def generate_linkedin_post(client: anthropic.Anthropic, chapter: dict, post_content: str, url: str) -> str:
    prompt = f"""Here is a blog post I just published. Write a LinkedIn post to promote it.

Blog post URL: {url}

Chapter: {chapter['num']} — {chapter['title']}
Series: Python Warts and All

--- BEGIN POST ---
{post_content[:3000]}
--- END POST ---
"""
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=512,
        system=LINKEDIN_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def write_job_summary(chapter: dict, url: str, linkedin_text: str) -> None:
    """Write a copy-pasteable LinkedIn block to the GitHub Actions job summary."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    separator = "─" * 60

    block = f"""## LinkedIn Post — Chapter {chapter['num']}: {chapter['title']}

**Blog post:** {url}

Copy and paste the text below into LinkedIn:

```
{linkedin_text}
```

{separator}
"""

    # Always print to stdout so it shows in raw logs too
    print("\n" + separator)
    print(f"LINKEDIN POST FOR CHAPTER {chapter['num']}: {chapter['title']}")
    print(separator)
    print(linkedin_text)
    print(separator + "\n")

    if summary_file:
        with open(summary_file, "a") as f:
            f.write(block)


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    notes = load_notes()
    chapter = find_next_chapter(notes)

    if chapter is None:
        print("All chapters are complete! No posts to write.")
        sys.exit(0)

    print(f"Writing chapter {chapter['num']}: {chapter['title']}")

    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(notes, chapter)}],
    )

    post_content = message.content[0].text
    post_path = determine_post_path(chapter)
    write_post(post_content, post_path)

    url = blog_post_url(post_path)
    print(f"Blog post URL: {url}")

    linkedin_text = generate_linkedin_post(client, chapter, post_content, url)
    write_job_summary(chapter, url, linkedin_text)

    create_pr(chapter, post_path)


if __name__ == "__main__":
    main()
