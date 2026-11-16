#!/usr/bin/env python3
"""Assemble docs/collected-whizbangs.md from src/pages/*.md.

Page sources are ordered by filename. Each starts with an HTML comment naming
the PDF page and printed page it came from; those comments are preserved (they
are invisible in rendered Markdown) so the output stays traceable.

A page source whose last line is `<!-- continue -->` is joined to the next page
with no paragraph break, for sentences and code that run across a page boundary.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# WB_VOL selects a volume directory (e.g. vol2); unset means volume 1 at the repo root.
ROOT = REPO / os.environ["WB_VOL"] if os.environ.get("WB_VOL") else REPO
SRC = ROOT / "src" / "pages"
OUT = ROOT / "docs" / "collected-whizbangs.md"

PAGE_FILES = sorted(p for p in SRC.glob("*.md"))
CONTINUE = "<!-- continue -->"


def main() -> int:
    if not PAGE_FILES:
        print("no page sources in src/pages", file=sys.stderr)
        return 1

    parts: list[str] = []
    for path in PAGE_FILES:
        body = path.read_text().rstrip("\n")
        parts.append(body)

    text = ""
    for i, body in enumerate(parts):
        if text:
            joiner = "\n" if text.rstrip().endswith(CONTINUE) else "\n\n"
            text = text.rstrip("\n") + joiner
        text += body

    text = text.replace(f"\n\n{CONTINUE}\n", "\n").replace(CONTINUE, "")

    # Table of contents from the level-2 headings.
    toc = []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            title = m.group(1)
            anchor = re.sub(r"[^a-z0-9 -]", "", title.lower())
            anchor = re.sub(r"\s+", "-", anchor.strip())
            toc.append(f"- [{title}](#{anchor})")
    contents = "## Contents\n\n" + "\n".join(toc) + "\n\n"

    meta = ROOT / "src" / "frontmatter.yaml"   # per-volume metadata; volume 1's is the default
    front = ("---\n" + meta.read_text() + "---\n\n") if meta.exists() else (
        "---\n"
        'title: "Collected Whizbangs"\n'
        'subtitle: "An Anthology Of Tutorials on APL Programming Techniques, Volume 1"\n'
        'author: "Roy A. Sykes, Jr."\n'
        'publisher: "Scientific Time Sharing Corporation"\n'
        "date: 1978-08\n"
        'source: "197808_APL Plus Collected WhizBangs (P036-0878)"\n'
        "---\n\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(front + contents + text.strip() + "\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(PAGE_FILES)} page sources)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
