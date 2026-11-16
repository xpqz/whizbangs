# Collected Whizbangs — PDF to Markdown

A repeatable conversion of both volumes of Roy A. Sykes, Jr.'s *Collected
Whizbangs* into Markdown and a web site:

> *Collected Whizbangs: An Anthology Of Tutorials on APL Programming Techniques,
> Volume 1*, Scientific Time Sharing Corporation, August 1978
> (`originals/197808_APL Plus Collected WhizBangs_P036-0878.pdf`, 25 scanned pages).
>
> *Collected Whizbangs, Volume 2*, STSC, Inc., 1981
> (`originals/Collected Whizbangs Volume 2.pdf`, 68 scanned pages, from the Internet
> Archive item `collected-whizbangs-volume-2`). See [Volume 2](#volume-2).

Most of this README describes Volume 1, which sits at the repository root.

Output: [`docs/collected-whizbangs.md`](docs/collected-whizbangs.md), the
transcription built from `src/pages`, and
[`docs/collected-whizbangs-corrected.md`](docs/collected-whizbangs-corrected.md),
the same text with the corrections found by running the code (see
[Verification by execution](#verification-by-execution)).

## Why this is not a one-liner

The PDF is a 300 dpi 1-bit scan with an Acrobat "Paper Capture" OCR layer. That
text layer is fine for prose (about 95%) and **useless for APL**: it drops some
code lines entirely and replaces every APL glyph with a plausible ASCII letter.
Both available OCR engines do this:

| printed | APL | Acrobat layer | Tesseract |
|---------|-----|---------------|-----------|
| ⎕       | quad | `D`, `U`, `O`, `{` | `USIZE`, `{]` |
| ←       | arrow | `+`, `«` | `<`, `«` |
| ⍝       | lamp | `A`, `a` | `%`, `A` |
| ⍴       | rho | `p`, `P` | `p`, `P` |
| ⍳       | iota | `1`, `l` | `1`, `l` |
| ⋄       | diamond | `◇` | `%`, `©` |
| ∇       | del | `V`, `Y` | `VY`, `W` |

So the code is transcribed from the page images by eye, and the OCR passes are
used only to seed prose and to build a review queue. `src/glyphs.md` records
every glyph decision with the evidence for it, and the "uncertain" list in
[`docs/transcription-notes.md`](docs/transcription-notes.md) records everything
that could not be resolved.

## Pipeline

```
make extract   # PDF -> build/pages/*.png, build/text/{acrobat,tesseract}, bbox.tsv, diffs
make build     # src/pages/*.md -> docs/collected-whizbangs.md
make lint      # APL fidelity checks on every code fence (fails the build)
python3 tools/mkcorrected.py   # docs/collected-whizbangs.md -> docs/collected-whizbangs-corrected.md
```

Everything under `build/` is derived and disposable. The transcription of
record is `src/pages/*.md`, one file per *printed* page:

| file | content |
|------|---------|
| `src/pages/00-cover.md` | front cover |
| `src/pages/00-note-to-readers.md` | unnumbered preface |
| `src/pages/pNNN.md` | printed page `NNN` |

Each page file starts with an HTML comment naming the PDF page and the half it
came from (from PDF page 4 on, each PDF page is a two-up spread of two printed
pages). A file ending in `<!-- continue -->` is joined to the next page with no
paragraph break, for sentences and listings that run across a page boundary.

## Reviewing a transcription

Re-render the exact region a block came from:

```sh
tools/crop.sh 3 350 270 130 16 1600 build/review/p3-alg1.png
```

`tools/crop.sh PAGE X Y W H [DPI] [OUT]` takes PDF points from the top-left
corner — the same coordinates `pdftotext -bbox` reports, so a suspicious word in
`build/text/bbox.tsv` can be cropped and inspected directly. `tools/measure.py`
counts glyph blobs in a crop, which is how runs of underscores and the width of
formatted numeric columns were pinned down.

## Fidelity rules used

1. **Transcribe what is printed, never what "should" be.** Where the printed
   code looks wrong (and there are such places in a 1970s newsletter), it is
   reproduced as printed and listed in `docs/transcription-notes.md`.
2. **No glyph is guessed.** Every glyph in `src/glyphs.md` is backed by a cited
   crop. Where two characters are near-identical in this typeface (`⌽` vs `⍉`,
   `⍋` vs `⍕`, `⍳` vs `1`), the reading is settled by a context where the
   meaning is unambiguous, and the reasoning is recorded.
3. **Typesetting conventions are decoded, not copied.** Underlined names in code
   are statement labels; `→(cond)⍴label` is a conditional branch.
4. **Numbers are checked.** Where printed output can be recomputed from the
   printed code (decode, grade, indexing, reshape), it was — that is how
   `RA⊥ALP⍳NAMES` was confirmed as base-value and how `ρJG` was confirmed to be
   `2 4 7` rather than `4 2 7`.
5. **`make lint` must pass.** It rejects any character outside the APL character
   set inside an `apl` fence, unbalanced brackets, and the known OCR
   substitutions (`D` for `⎕`, `~` for `¯`, `p` for `⍴`, `Φ` for `⌽`).

## Verification by execution

The code in the transcription was run in a period interpreter, STSC
APL\*PLUS/PC release 4.1 (1984), under DOSBox-X, and every disagreement was
then checked against the scan. The findings are in
[`docs/aplplus-verification.md`](docs/aplplus-verification.md).

How it was done:

- The interpreter comes from the Danish computer museum's disk images
  (<https://datamuseum.dk/wiki/Bits:30003640>). The DOSBox-X setup and the
  test harness live outside this repo, in `~/work/aplplus` (`README.md` and
  `harness/` there).
- `harness/tools/wbrun.py SPEC` writes APL statements to a file, starts
  APL\*PLUS/PC in a background DOSBox-X, and prints what the interpreter
  wrote back. The spec files used for this booklet are in
  `harness/wb/spec` (`a1.txt` to `a10.txt`), one group of pages each.
- Where the Markdown and the print differ, the specs run both forms, so each
  finding can be reproduced: the transcribed form fails (an error, a wrong
  result or, for `THISL`, an infinite loop) and the print's form gives the
  printed result.
- DOSBox-X must run with `fpu=false`; with its emulated 8087, factorial and
  `⎕AI` arithmetic fail in this interpreter.

What it found:

- About 25 places where the transcription differs from the print, 21 of them
  changing what the code does (for example `3 3⍳19` for `3 3⍴⍳9`, a missing
  `⍉` in *REPORT*, `¯` for `~` in *GRADE*, take for power in *SS3*, and a
  missing line [8] in *SS4*).
- Underscored names transcribed as plain letters collide with other names
  and break *COMPRESS*, *SS3*–*SS6* and *TIMES*. The corrected copy writes
  them in lowercase, as APL\*PLUS/PC does.
- 13 statements in `docs/transcription-notes.md` are contradicted by
  execution. That file has not been revised.
- With the corrections applied, every printed result that can be recomputed
  is reproduced.

Limits: the interpreter is six years newer than the booklet and is the PC
product, not the mainframe service, so a few things differ (`ΔFMT` is
`⎕FMT`; rotation along a nonexistent axis is an error). The function-editor
lines on p26 could not be run; they, the prose and the timing tables were
checked against the scan instead.

The corrections are **not** in `src/pages`. `tools/mkcorrected.py` applies
them to the built Markdown as exact string replacements and stops if the
source text has changed. Every reading that was marked uncertain has since been
settled against the scan. Two of the fidelity rules above
contributed to the errors: the lint check that treats `~` as an OCR slip for
`¯` produced `COL-¯IO`, and the take, drop and star glyphs were confused in
several places.

## Web site

`make site` builds a [Zensical](https://zensical.org/) site from the corrected
copy into `web/site`; open `web/site/index.html`, or run `make serve` for a
live preview.

- `tools/mksite.py` splits each volume's corrected copy into one page per
  article in `web/docs/vol1` and `web/docs/vol2`, adds a cover page and the
  verification notes for each, a landing page and an "About this edition"
  page for the collection, writes the `nav` in `zensical.toml`, turns the per-page source comments into
  printed-page markers, and rejoins sentences that a page break had split.
  The `.md` files in `web/docs` are generated; edit the corrected copy or the
  script instead.
- `zensical.toml` holds the navigation and theme. `web/docs/stylesheets` and
  `web/docs/fonts` are hand-written; the code font is APL386 Unicode (public
  domain), bundled so that the APL glyphs render without a network request.
- Zensical is installed in `.venv` (`python3 -m venv .venv &&
  .venv/bin/pip install zensical`); version 0.1.1 was used.

## Volume 2

Volume 2 lives in `vol2/` with the same layout (`src/pages`, `docs`, `build`),
and the same tools work on it with `WB_VOL=vol2` (`make vol2-extract`,
`make vol2-build`, `make vol2-lint`). It is typeset rather than typewritten,
scanned at 144 dpi, one page per PDF page: printed page *n* is PDF page *n*+8.
The conventions are in [`vol2/src/TRANSCRIBING.md`](vol2/src/TRANSCRIBING.md).

It went through the same stages as Volume 1, in this order: transcription by
eye from the page images; the fidelity lint; running every executable example
in APL\*PLUS/PC 4.1; a blind re-reading of every place where the run and the
transcription disagreed; and a proofread of every page against the scan. The
record is in [`vol2/docs/aplplus-verification.md`](vol2/docs/aplplus-verification.md),
the per-page notes in [`vol2/docs/transcription-notes.md`](vol2/docs/transcription-notes.md).

Unlike Volume 1, misreadings are corrected in `vol2/src/pages` itself, so
`vol2/docs/collected-whizbangs.md` is already the corrected text.
`tools/mkcorrected_vol2.py` only adds notes at the three places where the print
itself is wrong (pp 8, 14, 37), giving
`vol2/docs/collected-whizbangs-corrected.md`. The lint accepts lines checked by
eye that a pattern flags anyway when they are listed in `vol2/src/lint-allow.txt`.

## Requirements

`poppler` (`pdftotext`, `pdftoppm`, `pdfinfo`), `tesseract`, `python3` (Pillow for
`tools/measure.py`). macOS paths as used here are Homebrew's.

## Status

All 24 content pages are transcribed: 43 printed pages plus the cover and the
unnumbered preface, carrying 15 articles dated December 1975 to May 1978.
`make build && make lint` is clean (about 1400 APL glyphs across 168 code
fences). A clean lint does not mean the code is right: running it found the
errors listed under [Verification by execution](#verification-by-execution). The blank scan of the back cover (PDF page 25) is not transcribed.

Layout note: PDF pages 1–3 are single pages (cover, preface, printed page 1);
from PDF page 4 every PDF page is a two-up spread, so PDF page *N* carries
printed pages *2N−6* (left) and *2N−5* (right).

The APL code is the part that cannot be automated, so it is the part that was
checked hardest:

- every glyph in `src/glyphs.md` is backed by a crop of this scan;
- printed numeric results were recomputed from the printed code wherever the
  code allows it (grade/rank tables, decode/encode examples, the `SPA`/`SPS`
  index arithmetic, all sixteen take/drop expressions on p35, the `MONTHADD`
  results on p43);
- every case where the recomputation disagreed, or where the printed code is
  self-inconsistent, is listed in `docs/transcription-notes.md` and reproduced
  as printed rather than corrected.
