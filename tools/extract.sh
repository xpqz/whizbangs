#!/usr/bin/env bash
# Deterministic extraction of everything the transcription needs from the PDF.
#
# Produces:
#   build/pages/NN.png           300dpi page images (the authority for all text)
#   build/text/acrobat/NN.txt    pdftotext text layer (OCR pass A)
#   build/text/tesseract/NN.txt  tesseract OCR (OCR pass B, independent)
#   build/text/bbox.tsv          word boxes from the Acrobat layer, 1 word per line
#   build/text/diff/NN.txt       line-level disagreements between the two passes
#
# Never trust either OCR pass for APL code: they both mangle the APL glyphs.
# Use them to seed prose and to build a review queue; the images decide.
set -euo pipefail

cd "$(dirname "$0")/.."
PDF="197808_APL Plus Collected WhizBangs_P036-0878.pdf"
PAGES=$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')

mkdir -p build/pages build/text/acrobat build/text/tesseract build/text/diff

echo "==> page images (300dpi)"
pdftoppm -r 300 -gray -png "$PDF" build/pages/page
for f in build/pages/page-*.png; do
  n=${f#build/pages/page-}; n=${n%.png}
  mv "$f" "build/pages/$(printf '%03d' "$((10#$n))").png"
done

echo "==> OCR pass A: embedded Acrobat text layer"
for p in $(seq 1 "$PAGES"); do
  pdftotext -f "$p" -l "$p" "$PDF" - > "build/text/acrobat/$(printf '%03d' "$p").txt"
done

echo "==> word boxes (Acrobat layer)"
python3 tools/bbox.py > build/text/bbox.tsv

echo "==> OCR pass B: tesseract"
for p in $(seq 1 "$PAGES"); do
  n=$(printf '%03d' "$p")
  tesseract "build/pages/$n.png" "build/text/tesseract/$n" --psm 3 -l eng 2>/dev/null
done

echo "==> review queue: pass A vs pass B line diff"
mkdir -p build/text/diff
for p in $(seq 1 "$PAGES"); do
  n=$(printf '%03d' "$p")
  # normalise whitespace, uppercase-insensitive compare of the word streams
  # (grep exits 1 when a page is blank, e.g. the back cover — tolerate that)
  tr -s ' \t' ' ' < "build/text/acrobat/$n.txt" | grep -v '^ *$' \
    > build/text/diff/$n.acrobat || true
  tr -s ' \t' ' ' < "build/text/tesseract/$n.txt" | grep -v '^ *$' \
    > build/text/diff/$n.tesseract || true
  diff -u "build/text/diff/$n.acrobat" "build/text/diff/$n.tesseract" \
    > "build/text/diff/$n.txt" || true
done

echo "done: $PAGES pages"
