#!/usr/bin/env python3
"""Emit one line per OCR word with its page and bounding box, in PDF points.

Columns: page  yMin  yMax  xMin  xMax  text

Coordinates are what tools/crop.sh expects, so a suspicious word in the text
layer can be cropped and inspected directly from the scan.
"""
import html
import re
import subprocess
import sys

import glob, os
# Run from the volume directory (tools/extract.sh does); the one PDF there is the source.
PDF = glob.glob("*.pdf")[0]
WORD = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>'
)

xml = subprocess.run(
    ["pdftotext", "-bbox", PDF, "-"], capture_output=True, text=True, check=True
).stdout

page = 0
for line in xml.splitlines():
    if "<page " in line:
        page += 1
    m = WORD.search(line)
    if m:
        xmin, ymin, xmax, ymax, text = m.groups()
        print(f"{page}\t{ymin}\t{ymax}\t{xmin}\t{xmax}\t{html.unescape(text)}")
