# APL glyph key for this booklet

The booklet was typeset on a 1970s APL\360-style typewriter font, not a modern
Dyalog font. The same character looks different enough that OCR resolves it
into ordinary letters, so identification has to be done from the rendered page
at 600–2400 dpi. This file records every glyph decision and the evidence for
it. Crop commands reproduce the evidence exactly.

Coordinate convention: `tools/crop.sh PAGE X Y W H DPI OUT` with X/Y/W/H in PDF
points.

## The OCR failure mode

The Acrobat text layer and Tesseract both silently substitute a plausible
ASCII character for each APL glyph. Examples actually observed:

| printed glyph        | APL char | OCR "sees"      |
|----------------------|----------|-----------------|
| left arrow           | `←`      | `+`, `«`, `<`   |
| quad (tall box)      | `⎕`      | `D`, `U`, `O`, `{` |
| rho (p with tail)    | `⍴`      | `p`, `P`        |
| high minus           | `¯`      | `~`, `-`, `1`   |
| diamond              | `⋄`      | `◇`, `%`, `©`   |
| lamp (script a)      | `⍝`      | `A`, `a`        |
| del (inverted tri)   | `∇`      | `V`, `Y`, `W`   |
| circle-bar           | `⌽`      | `«`, `Φ`, `~`   |

Consequence: **never** derive code from either OCR pass. Both are used only to
seed prose and to build the review queue in `build/text/diff/`.

## Confirmed glyphs

| APL | printed appearance | evidence |
|-----|--------------------|----------|
| `←` | left arrow with filled head | p7 `⎕←JG←(4 7 ρJ),[0.5] 4 7 ρG`; p13 line 1 of SS1 |
| `→` | right arrow | p3 `→(2=(<\C≠¯1)/C)⍴A`; p13 `→L[C←C+1]` |
| `⎕` | tall empty rectangle, taller than caps | p3 `⎕SIZE`, `⎕IDLOC`, `⎕ERASE` |
| `⍴` | **lowercase rho**: round bowl with a descender, *not* a circle | p7 `4 7 ρG`; p13 `C←ρA←,A`; all of p36 |
| `⌽` | **circle with a vertical stroke** through it (circle-bar) | p36 line `1 1 ⍉⌽A`; p3 alg 1/2 `⌽A` (reverse) |
| `⍉` | **circle with a diagonal stroke** through it, extending past the circle | p36: printed alongside `⌽` and `⊖`, so all three are distinguishable at once; p6 `1 1 ⍉M[…]`; p7 `1⍉V[C]` |
| `⊖` | **circle with a horizontal stroke** (circle-minus) | p36 `1 1 ⍉⊖A` — reverse-first-axis, printed in the same block as `⌽` and `⍉` |
| `⍳` | small iota, a curl like `ι` | p13 SS1 line 4 `(⍳D)-1`, `⍳E` |
| `↑` | true up arrow with head | p13 SS1 line 2 `E↑B` — distinct from the up-tack `⊥` used on p3 |
| `∧` | capital lambda `Λ` | p13 `B∧.=(D,C+1)ρA` |
| `∨` | lowercase v, small x-height | p3 prose "`<\` is similar to `∨\`" |
| `⋄` | open diamond, larger than a period | p3 line [1]; p13 `SETUP ⋄ C←1` |
| `∇` | inverted open triangle | every function header, e.g. p3 `∇ R←A COMPRESS B;C` |
| `≠` | two horizontals joined by a steep diagonal | p3 `A≠¯1`; p3 line [1] `C≠¯1` |
| `¯` | high minus, a short bar at cap height | p3 `¯1` |
| `~` | tilde, a wave at x-height (never at cap height) | p18 `→LABEL×~condition`; p26 `∇FOR[~3]∇`; pp 24, 39 `'⍺∈⍳○∪⍴~⍵'` |
| `⍝` | a script/loop `a` shape sitting on the baseline | p3 line 2 `⍝ ⎕SIZE ↔ STORAGE REQUIRED`; p13 line [3] `⍝ OR ALTERNATIVELY,` |
| `∘` | small raised circle (jot) | p13 `A∘.=B` |
| `⊖` | circle with a **horizontal** stroke (circle-minus) | p36 `1 1 ⍉⊖A`, printed in the same block as `⌽` and `⍉` |
| `Δ` | bare triangle, no crossbar — used as a **name character** | p40 `ΔSS`, p5 `ΔFMT`; the roman prose on p5 prints the same triangle, and the italic `A` in `R←A` on the same line is clearly a different shape |
| `⊥` | **up-tack**: vertical stroke with the bar at the *bottom* | p3 alg 1 `(¯1=⌽A)⊥1` — see uncertain cases |

## Typesetting conventions (not glyphs)

* **Underlined name = label.** `A̲:` at the start of a line and `⍴A̲` / `→A̲` when
  branching to it. Confirmed on p3 (`A̲:R←A/[COORD] B`) and p13
  (`A̲:PROCESS ⋄ →L[C←C+1]`). Transcribed as a bare label, as in modern
  listings.
* **`→(cond)⍴label`** is the period conditional branch: the branch argument is
  a vector, and an empty vector falls through. p13 `→(M<C←C+1)ρ0` reads
  "if M<C then return".
* **Italics** (in the typewriter, a second strike) mark the subject of the
  sentence, e.g. *ORIGIN 1*, *SETUP*, _PROCESS_. Transcribed as `*emphasis*`.
* **`[axis]`** after a function is the axis operator, not indexing:
  `A/[COORD] B` is "compress along axis COORD" (p3).
* Prose underlining (e.g. the table header "object is currently") is emphasis,
  not a glyph.

## Uncertain cases

Recorded here and in `docs/transcription-notes.md`. Nothing in this table has
been silently guessed.

| page | printed | read as | note |
|------|---------|---------|------|
| 3 | `(¯1=⌽A)⊥1` | `⊥` up-tack | The glyph is unambiguously a tack, not an arrow (`↑` on p13 has a head) and not `↓`. Read as base-value `⊥`, which is in APL\*PLUS but makes the expression semantically odd; may be a typesetting slip for `↓` in the original. Transcribed as printed. |
