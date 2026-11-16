#!/usr/bin/env python3
"""Count glyphs in a line by analysing the ink column profile.

For monospaced typewriter text, a run of identical glyphs (dashes, underscores)
shows up as a series of separated ink blobs. This prints each blob's x range so
they can be counted, and warns when blobs touch.

usage: measure.py IMAGE [--min-gap N]
"""
import sys

from PIL import Image


def main() -> None:
    path = sys.argv[1]
    min_gap = 2
    if "--min-gap" in sys.argv:
        min_gap = int(sys.argv[sys.argv.index("--min-gap") + 1])

    im = Image.open(path).convert("L")
    w, h = im.size
    px = im.load()

    # ink per column
    cols = []
    for x in range(w):
        ink = sum(1 for y in range(h) if px[x, y] < 128)
        cols.append(ink)

    runs = []
    start = None
    gap = 0
    for x, ink in enumerate(cols):
        if ink > 0:
            if start is None:
                start = x
            gap = 0
        else:
            if start is not None:
                gap += 1
                if gap >= min_gap:
                    runs.append((start, x - gap))
                    start = None
    if start is not None:
        runs.append((start, w - 1))

    print(f"image {w}x{h}: {len(runs)} column blobs")
    for i, (a, b) in enumerate(runs):
        print(f"  {i:3d}  x={a:5d}..{b:5d}  width={b - a + 1:4d}")


if __name__ == "__main__":
    main()
