#!/usr/bin/env python3
"""Fidelity checks for the APL code blocks in src/pages/*.md.

The conversion is done by eye from page images; this linter is the safety net
that catches the two failure modes that matter:

  1. a glyph outside the APL character set (an OCR artifact that slipped in),
  2. a character that is *plausible* but is the OCR's ASCII stand-in for an APL
     glyph (e.g. `D` for `⎕`, `~` for `¯`, `Φ` for `⌽`).

Run with --list to print the glyph inventory used across the document.
"""
from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# WB_VOL selects a volume directory (e.g. vol2); unset means volume 1 at the repo root.
ROOT = REPO / os.environ["WB_VOL"] if os.environ.get("WB_VOL") else REPO
SRC = ROOT / "src" / "pages"

# Every character that may legitimately appear in an APL statement.
APL_GLYPHS = set(
    "←→⎕⍴⌽⍉⍳↑↓∘⍝⋄∇≠¯∊⍋⍒⊥⊤⌈⌊⌹⍟○⊂⊃∩∪⍷⍕⍎⍬⍺⍵≡≢¨⍨⍣⍤⌶⌷⊣⊢⍀⌿⍞⌸⍙⍚⍛⍜⍮⍭⍯⍰⍱⍲"
    # APL\360 / APL*PLUS also had these, and they appear in this booklet
    "∧∨↔≤≥⊖⍁"
    # Greek delta: p40 prints the function name ΔSS with a bare triangle,
    # distinct from the italic capital A beside it. Kept as printed.
    "Δ"
)
ASCII_OK = set(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " \t'\"_,.;:()[]+-*/\\|<>=?!×÷°^~"
)

# Things that look like APL but are OCR stand-ins.
SUSPECT = [
    (re.compile(r"\bD(?:SIZE|IDLOC|FMT|ERASE|CR|NL|IO|AV|TS|EX|WSID|LX|PW)\b"),
     "`D` looks like OCR for `⎕`"),
    # `~` is legitimate APL (logical not), but `~` before a digit is the usual
    # OCR of the high minus.
    (re.compile(r"~(?=\d)"), "`~` before a digit looks like OCR for `¯`"),
    (re.compile(r"[Φφ]"), "circle glyph written as a letter; use `⌽` or `⍉`"),
    (re.compile(r"◇"), "use `⋄` for the statement separator"),
    (re.compile(r"∇\s*$", re.M), None),  # legitimate: del at end of listing
    (re.compile(r"[%&#@$]"), "not an APL character"),
    (re.compile(r"^V\s+\S", re.M), "`V` at line start looks like OCR for `∇`"),
    (re.compile(r"\bp(?=[A-Z])"), "`p` before a name looks like OCR for `⍴`"),
]

FENCE = re.compile(r"^```(\w*)\s*$")


def balanced(line: str) -> str | None:
    """Report unbalanced brackets, ignoring quoted strings."""
    depth_p = depth_b = 0
    in_str = False
    for ch in line:
        if ch == "'":
            in_str = not in_str
        if in_str:
            continue
        if ch == "⍝":   # a comment may open a parenthesis that closes on the next line
            break
        if ch == "(":
            depth_p += 1
        elif ch == ")":
            depth_p -= 1
        elif ch == "[":
            depth_b += 1
        elif ch == "]":
            depth_b -= 1
        if depth_p < 0 or depth_b < 0:
            return "closing bracket without opening"
    if in_str:
        return "unterminated character literal"
    if depth_p or depth_b:
        return "unbalanced brackets"
    return None


# Lines checked by eye that a SUSPECT pattern flags anyway: one exact line (stripped)
# per line of src/lint-allow.txt, each with a reason in a comment above it.
ALLOW_FILE = ROOT / "src" / "lint-allow.txt"
ALLOW = {l.strip() for l in ALLOW_FILE.read_text().splitlines()
         if l.strip() and not l.startswith("#")} if ALLOW_FILE.exists() else set()


def main() -> int:
    errors = 0
    inventory: Counter[str] = Counter()
    files = sorted(SRC.glob("*.md"))

    for path in files:
        text = path.read_text()
        first = text.splitlines()[0] if text else ""
        if not first.startswith("<!-- source: PDF page"):
            print(f"{path.name}:1: page source must start with a "
                  f"'<!-- source: PDF page ... -->' comment")
            errors += 1
        m = re.match(r"p(\d{3})\.md$", path.name)
        if m and f"printed page {int(m.group(1))}" not in first:
            print(f"{path.name}:1: comment does not mention printed page "
                  f"{int(m.group(1))}")
            errors += 1
        lang = None
        fence_open_line = 0
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            m = FENCE.match(line)
            if m:
                if lang is None:
                    lang = m.group(1) or "text"
                    fence_open_line = lineno
                    if lang != "apl":
                        # non-APL fences are data displays; glyphs unchecked
                        lang = "_data"
                else:
                    lang = None
                continue
            if lang != "apl":
                continue

            where = f"{path.name}:{lineno}"
            for ch in line:
                if ch in APL_GLYPHS:
                    inventory[ch] += 1
                if ch not in APL_GLYPHS and ch not in ASCII_OK:
                    print(f"{where}: character {ch!r} (U+{ord(ch):04X}) "
                          f"is not in the APL character set")
                    errors += 1
                    break
            for pattern, msg in SUSPECT:
                if msg and line.strip() not in ALLOW and pattern.search(line):
                    print(f"{where}: {msg}: {line.strip()[:60]}")
                    errors += 1
            problem = balanced(line.lstrip("0123456789 "))
            if problem:
                print(f"{where}: {problem}: {line.strip()[:60]}")
                errors += 1
        if lang is not None:
            print(f"{path.name}: unclosed fence opened at line {fence_open_line}")
            errors += 1

    if "--list" in sys.argv:
        print("\nglyph inventory (count):")
        for ch, n in sorted(inventory.items(), key=lambda kv: -kv[1]):
            print(f"  {ch}  U+{ord(ch):04X}  {n}")

    if errors:
        print(f"\n{errors} problem(s)")
        return 1
    print(f"ok: {len(files)} page sources, {sum(inventory.values())} APL glyphs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
