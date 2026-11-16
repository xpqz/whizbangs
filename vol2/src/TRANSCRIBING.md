# Transcribing Volume 2

*Collected Whizbangs, Volume 2*, by Roy A. Sykes, Jr. (STSC, July 1981), from
`vol2/Collected Whizbangs Volume 2.pdf` (archive.org item
`collected-whizbangs-volume-2`). The book is typeset: proportional serif text
with a bold APL font for input and a regular APL font for output. It is
scanned at 144 dpi, one page per PDF page, 612 × 792 pt.

**Printed page *n* is PDF page *n* + 8.** Front matter: PDF 3 title, PDF 4
copyright, PDF 5 Note to Readers, PDF 7 Contents. PDF 9–59 are printed pages
1–51. The blank NOTES pages and the feedback form (PDF 60–68) are not
transcribed.

## Tools

All commands run from the repository root with `WB_VOL=vol2`.

- Page images: `vol2/build/pages/NNN.png` (144 dpi, whole page).
- Zoom: `WB_VOL=vol2 tools/crop.sh PAGE X Y W H DPI OUT.png`, with X, Y, W, H
  in PDF points from the top-left. 400–600 dpi is enough to read; the scan
  has no more detail than 144 dpi, so a doubtful glyph is settled by its shape
  and by comparison with the same glyph elsewhere, not by more zoom.
- OCR, for prose only (it mangles APL): `vol2/build/text/acrobat/NNN.txt`
  (the archive.org text layer), `vol2/build/text/tesseract/NNN.txt`, and word
  boxes in `vol2/build/text/bbox.tsv` (page, yMin, yMax, xMin, xMax, word),
  which give the coordinates for `crop.sh`.
- Lint: `WB_VOL=vol2 python3 tools/lint_apl.py`. Build:
  `WB_VOL=vol2 python3 tools/build.py`.

## Files

One file per printed page in `vol2/src/pages/`: `p001.md` … `p051.md`, and
`00-1-title.md`, `00-2-copyright.md`, `00-3-note-to-readers.md`,
`00-4-contents.md` for the front matter. Each file starts with

    <!-- source: PDF page 17 — printed page 9 -->

(front matter: `<!-- source: PDF page 5 (front matter) -->`). A file whose
last line is `<!-- continue -->` is joined to the next page without a
paragraph break; use it when a sentence or a code listing runs across the page
boundary.

## Rules

1. **Transcribe what is printed, never what "should" be.** If code looks
   wrong, reproduce it and record it in your notes. Do not run code to decide
   a reading. Do not change a reading to satisfy the lint; if the lint objects
   to a correct reading, record that in your notes.
2. **No glyph is guessed.** Decide every APL glyph from its shape. Easily
   confused in any APL font: `↑`/`↓` (where is the arrowhead?), `¯` (bar at
   cap height) / `~` (wave) / `-`, `/` / `⌿`, `\` / `⍀`, `⌽` / `⊖` / `⍉`,
   `⍴` / `⍳`, `⎕` / `⍞` / `⌹`, `×` / `÷` / `+`, `∘` / `○` / letter o, `⌈` / `⌊`,
   `⊂`/`⊃`/`∩`/`∪`, `⍋`/`⍒`, `∊` / `ε`, `⍝`, `⋄`, `∇`. Use the APL Unicode
   characters (`⍴ ⍳ ∊ ⍝ ⎕` …), never Greek or ASCII stand-ins.
3. **Underscored letters** in APL names are distinct identifiers. Write an
   underscored letter in lowercase (`A̲` → `a`), as APL\*PLUS/PC does.
4. **Code blocks** are fenced with ```` ```apl ````. Input lines are
   indented six spaces; output starts in column 0, with its spacing counted
   against the fixed pitch of the APL font. Function listings: `∇` header at
   column 0, line numbers `[n]` at column 0, statements starting at column 6
   (`[1]   R←…`, `[10]  R←…`); a line that starts with a label or a comment
   is outdented one column (`[2]  a:…`, `[1]  ⍝ …`), as the book prints it.
   Show the closing `∇` on its own line. A note the book prints beside a code
   line, in the text font, stays on that line after a few blanks, at about the
   printed column. Matrix displays keep the leading blank column the book
   prints; vectors and scalars start in column 0.
5. **Prose** is re-wrapped freely, with print hyphenation removed. Use `--`
   for a dash, straight quotes `"` and `'`. Inline APL expressions go in
   backticks (`` `∧/A∊B` ``); a bare APL name in prose is written in italics
   (*CSORTR*). Text the book sets in italics for emphasis is *italic*; bold is
   **bold**. Article titles are `## Title` exactly as printed; section
   headings inside an article are `###`. Keep the article date or other
   bylines where the book prints them.
6. **Tables and figures**: a table becomes a Markdown table; a figure that is
   a picture gets a one-line description in an HTML comment plus anything
   legible in it.
7. Running heads and the page-number footer are not transcribed.

## Notes

Write your notes to `vol2/docs/notes/<range>.md`: for every page, each
reading you were not sure of (with the crop command that shows it), each place
where the printed code looks wrong, and each lint objection you overrode.
These feed `vol2/docs/transcription-notes.md`.
