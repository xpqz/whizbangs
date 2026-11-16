# Transcription notes

Every point where the printed page is ambiguous, internally inconsistent, or
looks like a typesetting slip. Nothing here has been silently corrected in the
Markdown: the transcription reproduces what is printed, and this file records
what is doubtful and why.

Format: printed page → item.

---

## p1 — WHAT'S IN A NAME?

- `R←((¯1+(¯1=⌽A)⊥1)⌽A)[;1]` — the `⊥` is unambiguously an up-tack (bar at the
  bottom), not an arrow, and the same glyph is confirmed as base-value/decode on
  p4 (`RA⊥ALP⍳NAMES`) where the printed output forces that reading. In this
  one-line "cumbersome" solution, however, the expression as printed does not
  evaluate to anything sensible; it may be a typesetting slip in the original
  (possibly `↓` was intended). Transcribed as printed.
- `C←,⎕IDLOC 'COORD' ⋄ →(2=(<\C≠¯1)/C)⍴A` — the trailing `⍴A` branches to the
  underlined label `A` only when the condition is 2; the `⍴` is as printed and
  is the standard "branch to a vector, empty falls through" idiom.
- Statement labels are underlined in the source (`A̲:`, `⍴A̲`). Transcribed bare.
- The table header underlining ("object is currently") is emphasis, not a glyph.

## p2

Three `COMPRESS`/`SUB` session examples. `3 3⍳19` — the iota glyph is easily
mistaken for the digit 1 in this typeface; the displayed result confirms `⍳`.

## p5 — REPORT

- `'CITY_NAME________   _POP  RANK'` — the padding characters were counted from
  the scan with `tools/measure.py`: 17 characters in the name field (9 + 8
  underscores), then 3 spaces, then `_POP`, 2 spaces, `RANK`. They sit at
  baseline height, i.e. underscores, not hyphens.
- `FORMAT←'17A1,X3,I4,X2,I3'` — the leading `17` is printed as digits (not
  `I7`): the same shape as the `1` in `A1`, and it makes sense as "seventeen
  A1 fields", matching the 17-wide name column in the output.
- `FORMAT ΔFMT(NAMES[GRADE;];POP;RANK)` — the glyph before `FMT` is a bare
  triangle (`Δ`), not an italic capital A: the prose three lines above prints the
  same bare triangle in `ΔFMT`, where a roman `A` would show its crossbar. The
  author's function names `ΔFMT` and `ΔSS` (p40) therefore begin with a delta;
  this is preserved as printed. (An earlier draft read it as `AFMT`, following
  the OCR; the prose glyph disproves that.)

## p6 — SUBSCRIPTION

- `F←'G⎕  T[9;9;9] ⎕'` — the two quads are printed as boxes with a *filled top
  band*, unlike the plain `⎕` used elsewhere on the same page. They are
  transcribed as `⎕` because the surrounding code is a format template; the
  printed shape may be `⍞`.

## p7

- `(Nρ1)⍉A[V1;V2;V2;...;VN]` — printed with `V2` twice (the prose two lines
  above says `V1;V2;V3;...;VN`). Transcribed as printed.

## p9

- `IND←(⍳1)+(¯1↓ρJG)⊥IND-⍳1` — verified: it reproduces the printed `1 4 3 8 5`
  only if `ρJG` is `2 4 7` (so `¯1↓ρJG` is `2 4`), which is consistent with
  `⎕←JG←(4 7ρJ),[0.5] 4 7ρG` — `,[0.5]` inserts a new *first* axis.

## p10 — SPS / SPA

- `R←(,A)[(R⊥(1⌽1⍴⍴⍴B)⌽B)+C-R⊥C]` and the corresponding line in SPA: the two
  circle glyphs are printed as circle-bar (`⌽`), and are transcribed as printed.
  The sub-expression `(1⌽1⍴⍴⍴B)` is semantically opaque; it may be a typesetting
  slip for `(¯1↓1⍴⍴⍴B)` or similar. Flagged, not corrected.
- `'I2' ΔFMT B/⍳⍴B` — the index display that follows is a formatter-produced
  digit stream (tens row, units row, then `B/V`). Reproduced from the scan; the
  tens row is easy to mis-count.
- p11 examples mutate `M` in place across three `SPA` calls; each printed result
  was checked against the printed indices and `DATA`, and all three agree.

## p11

- `5 0 2 0 ⍕ROWS,COLS` and `7 0 ⍕M SPS ROWS,[2.5] COLS` — `⍕` is printed as a
  small filled down-triangle (distinct from `⍎`, a filled dot on a stem, on
  p20/21). The numeric left argument is a format specification.

## p32 — APL POTPOURRI

- `A←⍴R ⋄ L←(×/A)⍴0 ⋄ L[]←,R ⋄ R←A⍴L` — the subscript in the third statement is
  printed empty (`L[]←,R`). The statement occupies seven character cells
  (`L [ ] ← , R`), so a blank cell really is typeset between the brackets; the
  intended index (`L[I]←` would be the obvious one) was apparently left blank or
  lost in the original. Transcribed as printed.
- `⌊/ 2 3 0 ⍴6` — the glyph is an L-shaped floor (vertical stroke at the *left*
  end of the foot). On p33 the base-value `⊥` prints with the vertical *centred*
  on the foot, so the two are distinguishable; read as `⌊`, which also makes the
  "and why?" question turn on the identity element of min.
- `V[⌽[K]⍒V]` — the inner glyph is the solid inverted triangle with a stem
  (grade down, identical to p4) and the outer circle has a *vertical* stroke
  (`⌽`). That reading matches the text: on a vector, `⌽` along the only existing
  axis turns the descending grade into ascending order, and on a nonexistent axis
  it is a no-op.
- `>\ 0.5 0.5 0.5` prints `0.5 0 1`. Scanning `>` from 0.5 gives `0.5 0 0`; the
  third element is printed as `1`. Output transcribed as printed.
- `~K∈⍳⍴⍴A` — `~` is APL *without* here, not an OCR high minus. The iota is the
  small x-height mark (the same line's digits are cap height); this fragment is
  kept in inline code, where the linter's `~`→`¯` heuristic does not apply.
- `where ∘ can be any scalar dyadic function` — the placeholder is the same small
  baseline circle used for the jot in `A∘.+B` on the same line (4.5 pt tall
  against 4.8 pt for the jot), so it is transcribed `∘`.
- `''⍴A` — two apostrophes are printed, and the empty shape does make the first
  element a scalar, which is what the item asserts.

## p33

- `0×.+(⍋⍋K≠⍳⍴⍴A)⍉A` — the two glyphs after `(` are hollow apex-up triangles with
  stems (`⍋`, identical to p4's grade-up) and the circle before the final `A` has
  a diagonal stroke (`⍉`); both differ from the circle-bar `⌽` in the next item
  and in `V[⌽[K]⍒V]` on p32. As printed the identity is doubtful: the permutation
  puts axis *K* first rather than last, and a scalar left argument reduces
  nothing, so the expression does not appear to reproduce `×/[K]A`. Flagged, not
  corrected.
- `(⌽×\(⍴A)↑1,⌽A)+.×B` — both circle glyphs here are circle-bar (vertical
  stroke).
- `'I0,I2,A0,I4,3G⎕⎕,F8.3'` — the two glyphs after `3G` are the "box with a
  filled top band" variant also seen on p6; treated as `⎕` for consistency with
  that decision. The printed output matches field widths 0, 2, 0, 4, 0 and 8
  (14 columns in all), which also confirms that the characters after `I` and `A`
  are the digit `0`, not the letter `O`.

## p34 / p35

- Display lines such as `A[2 5 1 ; 9 1 5 7 5 5]` are letter-spaced to fill the
  measure; the wide gaps between characters are not significant and are
  normalised to single spaces. The space after `;` is kept because it is printed
  in all three subscription examples.
- `⎕IO←1 ⋄ ⎕←A←(10×⍳5)∘.+⍳9` — the iota in `(10×⍳5)` prints like the digit `1`;
  the printed 5×9 matrix (11..19 down to 51..59) confirms `⍳5`, not `15`.
- `B/⍳⍴B` — the glyph after `/` is x-height with a flag at the top left (the
  iota), not the cap-height digit `1`. `B/1⍴B` would not conform for a boolean
  *B*, and the printed subscription needs the row indices, so `⍳` is read.
- The four take/drop headers use the comment lamp: `3 5↑A ⍝ ¯2 ¯4↓A`, i.e. the
  equivalent drop expression is printed as a comment. Each pair was checked
  against its printed 3×5 result and all four agree.
- `(∧ ∨ ⍲ ⍱ ~)` — the third and fourth glyphs are the NAND/NOR forms (`∧` and
  `∨` with a stroke above), transcribed `⍲` and `⍱`.
- Each of the 16 take/drop expressions was evaluated against the printed matrix
  *A* and all 16 reproduce `A[2 3;4 5 6 7]` (`24 25 26 27` / `34 35 36 37`).

## p20

- `→L←(M⍴A),0` — the `A` is underlined in print (it is the label `A` on line
  [2]), so the branch table is "M copies of the label's line number, then 0".
  Transcribed bare, as elsewhere.
- `(Executed 11/29/76 at 7:27 P.M. EST on *APLPLUSC* with 20 users)` — the
  program name is printed with no asterisk: `APLPLUSC`, not `APL*PLUS`.
  Transcribed as printed (cf. the `APL\*PLUS` convention for the spelled-out
  product name).
- The timing table's column headings (`0 1 10 100 1000`) are underlined in the
  print in place of a rule; reproduced as a dashed rule line under the heading.
- Section heading `3. ⍎ Recursed!` uses the execute glyph as a pun on "execute";
  verified as a filled dot on a stem, not `⍕` or `&`.

## p21 — SS1 / SS2

- SS1 line [2] prints `⊖` (circle with a **horizontal** stroke) while its
  "alternatively" line [4] prints `⌽` (circle with a vertical stroke). The two
  are different characters in this typeface and both are transcribed as
  printed. `⊖` is confirmed as a genuine booklet glyph on p36 (`1 1⍉⌽⊖A`, where
  the printed outputs distinguish the two axes of reversal). Read as first-axis
  rotate in SS1 line [2], which is what that expression needs
  (`A∘.=B` is target-by-substring); line [4] uses `⌽` on the transposed product
  `B∘.=A`.
- `E←0⌈C-0⌈D-1` — **two** `⌈` (max) in both SS1 and SS2, not the more usual
  `0⌊`. The prose on the same page says "The two `0⌈`'s are to correctly handle
  empty or overlong substrings", so the double max is what was meant and
  printed. The `⌈` glyph is the Γ-shaped one; `⌊` is L-shaped (confirmed on
  p4, `∧/V2=⌊\V2`).
- SS1 line [2] `R←(E↑∧/((⍳D)-1)⊖A∘.=B)/⍳E` — the reduction glyph is a plain
  slash (`/`, last axis); in the alternative line [4] it is a slash with a
  horizontal bar (`⌿`, first axis): `⍝R←(E↑∧⌿((⍳D)-1)⌽B∘.=A)/⍳E`. The bar is
  faint at 1200 dpi but unmistakable at 2400 dpi, and the axis makes sense of
  the two variants (the products are transposes of one another).
- `(⎕WA)` — plain tall box, no filled top band; read as `⎕`.
- `BV/⍳ρBV` — italic in print; the iota is the small hooked glyph, the rho the
  p-with-tail. (Prose wording of the index vector.)
- SS2 line [2] `R←(E↑B∧.=(D,C+1)ρA)/⍳E` — `∧.=` and the reshape are as printed.

## p22 — SS3 / SS4

- SS3/SS4 line [1] `→B⌊A+D` — the glyph between `A` and `D` is a plain `+`
  (verified at 2400 dpi; it is *not* the starred `↑` take glyph that appears
  later in the same lines). With the label values (`A` on line 2, `B` on line
  4) `B⌊A+D` selects line 2 for an empty substring, line 3 for a one-element
  substring, and line 4 otherwise — the "unusual branch on line [1]" the prose
  describes. Transcribed as printed.
- SS3 line [4] `→(ρR←(E↑A∊1↑B)/⍳E)↓0` — dyadic `↓` (down arrow) with a scalar
  0: a count of 0 branches to line 0, a positive count drops to an empty vector
  and falls through. Not `⍴` and not `↑`.
- SS3 line [5] `R←(A[R∘.+(¯1↑⍳1)↓⍳D]∧.=1↓B)/R` — the glyph after the closing
  paren is `↓` (drop), and the argument is `⍳D`, i.e.
  `(¯1↑⍳1)↓⍳D`, matching the prose sentence "The `(¯1↑⍳1)↓⍳D` construct ...".
  At 1200 dpi this is easy to misread as `1↓D`; the iota's hooked foot was
  checked at 2400 dpi.
- SS4 line [4] `F←' ETAISONRLCFHUDMPBWYGKVJQXZ.,'` — there is a **leading
  space** inside the quotes (one character cell between `'` and `E`), and the
  string is 26 distinct letters plus `.,`. Same string, same leading space, in
  SS6 on p23.
- SS4 line [5] `F←G⍳⌈/G` — index of the largest frequency weight.
- Page ends mid-sentence ("... the letter with the fewest"), so p22 ends with
  `<!-- continue -->`.

## p23 — SS5 / SS6

- SS5 line [5] `B←(⍳C←1)↓B` — the glyph between `C` and `1` is a left arrow.
  In the italic face at low resolution it looks like `+`; at 2400 dpi the barb
  is clear, and the prose ("initializes the substring element counter, and
  modifies *B* so that the counter is appropriate in either origin.") confirms
  `C←1` plus a drop.
- SS5/SS6 last line `→C×D>C←C+1` — the label `C` (underlined in print) is
  multiplied by the loop condition; read as printed.
- SS6 line [5] `B←B[G←⍒F⍳B]` — `⍒` (inverted delta with stem) here, not `⍋`.
- SS6 line [6] prints `G←G-F←⍳C←1` — three left arrows, so as printed the line
  assigns `F←⍳C←1` and then subtracts. That overwrites `F`, which line [7] and
  line [8] still use as the distribution vector, so the line is almost
  certainly a typesetting slip (possibly `G←G-F⍳⍳C←1`); transcribed exactly as
  printed, not corrected.
- SS6 lines [7]–[10]: `↑` (take) appears in `E↑`, `↓` (drop) in `G[F]↓`,
  `F↓G`, `F↓B` and in the `↓0` branch idiom. The two arrow shapes are distinct
  at 2000 dpi (take: starred head above a crossbar; drop: filled head below
  the stem).
- p23 ends with a complete paragraph; the article itself continues on p24, so
  no `<!-- continue -->` marker is used.
- Tooling note: the printed `≥` (p20 `→(M≥C←C+1)/L`) is flagged by
  `tools/lint_apl.py` because `≥` is not in its `APL_GLYPHS`/`ASCII_OK` sets;
  the character is correct as printed (same glyph as p37's `→L20×N≥I←I+1`).

## p24

- The timing table's second header is `⍴R` (lowercase rho with descender, not a
  Latin `p`) printed above `HITS`; `B` sits above `SUBSTRING`. Read as "the shape
  of the result", i.e. the number of hits. The `SS1`..`SS6` headers are italic
  and underlined in print; transcribed plainly.
- The table's row labels are character literals built from the typewriter's
  Greek-form APL glyphs, and are transcribed as the APL characters they denote:
  `'⍵'`, `'⍺⍵'`, and the last row `'⍺∈⍳○∪⍴¯⍵'` (the printed run is alpha,
  epsilon, iota, omicron, upsilon, rho, the wavy mark, omega). They are APL
  symbols, not Greek letters standing as text.
- The 7th character of the last row is a wavy horizontal mark at cap height,
  pixel-identical to the certain high minus in p26's `∇FOR[¯3]∇`, so it is read
  as `¯`. In this typeface a tilde `~` would be indistinguishable; Acrobat's
  text layer returns three 1pt fragments for it and Tesseract returns `~`.
  Recorded, not resolved.
  **Superseded:** at 1200 dpi the mark is a wave at x-height, the same shape as
  the `~` on p18, and p26's mark is the same tilde (see p26). The row is
  `'⍺∈⍳○∪⍴~⍵'`; the corrected copy has it.
- The space-only rows were measured quote-to-quote (character pitch 5.72 pt,
  cells counted from the quote positions): `''` is empty, `' '` is one space
  (quotes 2 cells apart), `'  '` is two spaces (3 cells apart).
- The `(Executed 2/25/77 ...)` stamp prints as a two-line block, kept verbatim in
  a plain fence.
- The page is dated March 1977 although the article that starts overleaf is
  dated May 1977: p24 is the tail of the preceding article.

## p25 — TIMING ALGORITHMS

- `R←V⌹M` — the glyph is a small rectangle divided into quadrants with dots
  (quad-divide/domino), not a quad. It is the "solve 40 equations in 40
  unknowns" step the prose describes.
- `M←? 40 40 ⍴100` — the spacing is as printed: a space after `?` and before
  `⍴100`, unlike the `V←?40⍴1000` on the same line.
- `⎕AI[2]` is a plain tall box in both prose and code.
- The title is the running head at the top of the right half (the article's first
  page), transcribed as the section heading.

## p26

- `[1]   CPU←⎕AI ⋄ TIMES←1` — no `[2]` index on this line although the session
  lines above and below use `⎕AI[2]`; line [5] indexes the difference
  (`(⎕AI-CPU)[2]`), so the printed form is coherent.
- The labels `A:` and `B:` are outdented one character in the listing (and
  underlined in print); transcribed bare, as in the other listings.
- `∇FOR[3] R←99+⍳1300∇` and `∇FOR[¯3]∇` are function-editor lines delimited by
  `∇` at both ends, not expressions. `[¯3]` deletes line [3]; the mark is the
  high minus (wavy in this typeface), not a tilde.
  **Superseded:** at 1200 dpi the mark is a wave at x-height, like p18's `~`,
  not the straight cap-height high minus of p3 and p19. It is printed
  `∇FOR[~3]∇`; the corrected copy has it.
- The two `FOR 10` runs are consecutive lines in print (line spacing 9–10 pt, no
  blank line); the two `∇FOR[3]` runs are separated by a blank line.
- `131.4` / `131.2` (two runs of `FOR 10`) and `1.84` / `0.32` are transcribed
  from the print; only their order and repetition are meaningful.

## p27

- `C←1↓(A×⍴C)⍴C` — the glyph is a down arrow with its head at the bottom
  (checked at 2400 dpi), i.e. drop. `↑` would leave a one-character vector and
  break the example.
- `⎕DEF` and `⎕DEFL` are plain boxes; the second really ends in a capital `L`.
- `'⋄',B` and `A⍴'⋄'` hold the statement-separator diamond as literal data (the
  small open diamond of the print), which is what "inserting diamonds" means.
- `R←⎕AI ⋄ RUN ⋄ R←⎕AI-R` (line [4]) — Acrobat's text layer reads the final
  glyph as `B`; at 2400 dpi it is an italic `R`. `R` is localized by the result
  header, so the timed expression's own `R←V⌹M` lands in the global, not here.
- The printed outputs agree with the printed code arithmetically: 1306/10 =
  130.6; 147/100 = 1.47; 20/50 = 0.4; 38/50 = 0.76; 115/50 = 2.3; 810/5 = 162;
  115/5 = 23.
- `A←?7⍴20` — the first test vector is 7 elements (`?7⍴20`, not `?70⍴20`); the
  three tests use 7, 70 and 700 elements, matching the closing paragraph.

## p12 — SOME NOTES ON DATE STORAGE

- `760714  a BASTILLE DAY` — the character before the italic remark is printed
  as a lowercase roman `a`: it is *not* in the italic code face used for the rest
  of the line (the digits are italic), and its shape (rounded top, closed
  counter) is not the flat-topped script lamp `⍝` seen in p3's `⍝ ⎕SIZE`. Read as
  the article "A"; transcribed as printed.
- `D←⍉1⊖ 100 100 100 ⊤DATES` — this article's typewriter prints **three** different
  circle glyphs: `⍉` (circle with a steep diagonal, as in p9's `1 1 2 ⍉JG[...]`),
  `⊖` (circle with a horizontal bar, protruding on both sides) and `⌽` (circle
  with a vertical bar, as in p10's `1⌽1⍴⍴B`). The horizontal-bar glyph is read as
  `⊖` (APL*PLUS first-axis reverse/rotate); the same three shapes are
  distinguished on p36, where `1 1⍉⌽A` and `1 1⍉⊖A` print different diagonals.
  Note that `1⊖` here rotates the three encode rows to (MM,YY,DD), not the
  (MM,DD,YY) the prose aims at; printed as is, not corrected.
- `'I2,⎕/⎕,ZI2,⎕/⎕,ZI2'` and `'I2,2P⎕/⎕ZI3'` — in both format phrases the two
  delimiters are printed as boxes with a *filled top band*. They are identical to
  each other and different from the plain `⎕` of `⎕FMT` on the same line, so they
  are probably not `⎕`; see the p6 note (they may be `⍞`). Transcribed as `⎕` per
  the glyph key.
- `⌊TS÷5184000` — the floor glyph is an `L` whose stem descends below the
  baseline, distinct from the `⊥` (stem over a wide base bar) two lines below.
- Linter: `⊖` (U+2296) was missing from `APL_GLYPHS` in `tools/lint_apl.py` when
  these pages were first linted; the set now includes it, and p12-p15 are clean.

## p13

- `D←100⊥1⊖ 100 100 100 ⊤DATES` — as printed, `100⊥` takes the 3×N result of
  `100 100 100⊤DATES` as its right argument, which is a length error for a
  vector `DATES` (the scalar left argument is extended along the last axis).
  Transcribed as printed; it may be a typesetting slip for the intended
  "encode, reorder, decode".
- `'G⎕Z9/99/99⎕'` — filled-top-band boxes again; see the p12 note.
- The "symbolic illustration" is a box drawn round `YY` with an arrow to the end
  of the string, i.e. "move the year to the end". Reproduced as ASCII art in a
  plain fence; the arrow path is not drawn to scale.
- The step numbers 1-5 are printed as a numbered list whose displays are centred;
  each display is kept as its own `apl` fence with the result at the left margin.

## p14

- `100⊥⊖ 0 10000 ⊤DATES` — the spacing is as printed (a space after `⊖` and
  before `⊤DATES`), unlike the two-space-separated numbers in it. Same `⊖` glyph
  as p12/p13.
- Arithmetic check: with YYMMDD=760714 (MD=714), `(YYMMDD+999999×MD)÷10000` is
  exactly 71476 = 07/14/76, and p13's `⌊(YYMMDD+1000000×MD)÷10000` gives the same
  value; the algebra shown on this page is correct.

## p15 — STRETCHING THE WORKSPACE

- The article opens with a quotation set as `"... programs execute faster in
  less space".` — the ellipsis has a space after it and the closing quote follows
  the period; kept as printed.
- `A←+\⍳100` and the prose `⍳100` — the iota prints as a small `ι` (not a `1`);
  the prose in the following sentence repeats it the same way.
- Text runs off the foot of the page in the middle of a sentence ("...over that
  temporary"); continued on p16.

## p16 — storage/datatypes (article continued from p15)

- `R←A[⌽⍳50]` — the glyph after `[` is the circle-bar (`⌽`, vertical stroke,
  unlike the diagonal `⍉`) and the index is `⍳` (small `ι` shape, no base
  serif). The italic glyph in the printed comment ("BOTH FOR ⌽ AND []") is the
  same circle-bar.
- `A←100⍴0 ⋄ A[]←2○0` — two separate findings:
  - The index brackets are printed *empty* (`A[]`). Checked at 2400 dpi: there
    is no glyph between `[` and `]`. The same elided-index form is used on p17
    (`⍎'CV[]'`), so it looks deliberate rather than a lost character.
  - The right-hand value is `2○0`, not `200`: the middle glyph is the circle
    function `○` (cos, with a left argument of 2). The following sentence —
    "even though 2○0 is a floating-point 1" — confirms it, and the two circles
    are visually identical to the digits `0` in this typeface.
- `60÷⍳6 ⋄ ¯2*⍳31 ⋄ !⍳12` — checked arithmetically against "all return 4-byte
  integer results": `60÷⍳6` is `60 30 20 15 12 10`; `!⍳12` ends at 479001600;
  and `¯2*⍳31` stays inside 32-bit two's complement (the last element,
  `¯2147483648`, is exactly the minimum 32-bit integer — which is presumably
  why the base is `¯2` and not `2`). Transcribed as printed.
- GRADE line [2], `→(COL←(⍴MAT)[IO+1])↓0 ⋄ COL←COL-¯IO`:
  - The glyph after `)` is a down-arrow (`↓`, drop): a thin stem above a
    full-width bar that tapers to a point below. It is *not* the up-arrow seen
    on p17 (`500000↑1`, `↑⎕LC`), whose apex is at the top with a thick stem
    below, and not the up-tack `⊥` of p1 (bar at the very bottom, no tail).
  - Read as printed, `↓0` yields `,0` (i.e. a branch to line 0, exit) when the
    count is 0 and an empty vector (no branch) otherwise — the standard
    "return if there are no columns" idiom.
  - `COL←COL-¯IO` then leaves *COL* one greater than the last column index
    under either origin, so the first `MAT[R;COL]` of line [3] looks out of
    range. Transcribed as printed; not corrected.
- `IO←''⍳1` — two apostrophes (empty vector literal) followed by iota.
- `A:` and `→A` are underlined labels in the print; transcribed bare.

## p17 — name referencing / specialized mechanisms

- `CV←(⍴CV)⍴⍕1/,⍎'CV[]'` — glyph identification, both checked at 2400 dpi
  against known instances:
  - `⍕` = flat wide top bar + filled down-triangle + stem below, the same shape
    as `5 0 2 0 ⍕ROWS,COLS` on p11.
  - `⍎` = filled dot on a stem standing on a horizontal base (the shape
    glyphs.md records for ⍎), not the outlined inverted delta of `⍒` (p3).
  The expression is semantically odd (formatting a character result), but both
  shapes are unambiguous.
- `⍝    ^^  ^^^   ^   PASS POINTERS` — the carets are the printed annotation
  marking the pointer-passing sub-expressions; reproduced verbatim inside the
  listing (they are typewriter carets, not APL characters).
- `'I80' ⎕FMT 10000⍴1` — the character after the quote is a serif capital `I`
  (serifs top and bottom, no top-left flag), not the digit `1`.
- `BV← 500000↑1`, `→⎕LC`, `⎕LC` — take-arrow and plain quads; the space after
  `←` is as printed.

## p18 — BRANCHING AND ITERATION

- `→LABEL×⍳condition` — the glyph after `×` is iota (`ι`), i.e. the classic
  `→LABEL×⍳condition` conditional branch.
- `→(condition)⍴LABEL` — rho (branch to a vector; empty falls through).
- `→LABEL×~condition` — the glyph before `condition` is a *tilde at x-height*
  (wavy), clearly different from the straight high minus at cap height used on
  p19 (`¯1`); read as the APL "not" function `~`, verified at 2400 dpi.
- `[L1;L2;L3;...]` and `[A;B;C;...]` — the delimiters are square brackets
  (horizontal serifs at top and bottom, no curves), and the whole notation is
  italic in the print.
- The four-line "or" table keeps the printed two-column layout, including the
  repeated, underlined `or` between the columns, and uses `∧` (printed like
  `Λ`) in `→(∧/conditions)⍴LABEL`.
- The page ends mid-sentence; the continuation is the first line of p19.

## p19

- `→(M≥C←C+1)↑⎕LC` — this up-arrow is `↑` (apex at top, thick stem below),
  distinct from the `↓` of `→M↓0` two paragraphs later (thin stem above, head
  tapering to a point below). Both are printed as shown.
- `T: ... ⋄ →T⌈⍳M≥C←C+1` — the glyph after `T` is `⌈` (printed like `Γ`), then
  iota; `T` is an underlined label in the print (transcribed bare).
- `∇ R←A IF B` — the single body line carries no line number in the print,
  unlike the `[1]` on the neighbouring *THISL* definition.
- `R←1↑1↑⎕LC` — two take arrows, as printed.
- ITERATE line [2] starts `→0 IF C>M`: the character is the digit zero.
- `A:→(C>M)⍴0`, `A:PROCESS` — underlined labels, transcribed bare.

## p36

- The page opens with the tail of the session that starts at the foot of p35:
  the sentence "...selects the first element as a scalar:" ends p35, and its
  code line sits on p36's top edge, clipped by the scan. Read as `''⍴A`
  (two apostrophes in *adjacent* cells, i.e. the empty vector as left argument;
  quote-to-quote 5.6 pt) with `11` printed at the left margin, i.e. a rank-0
  result, which is what "as a scalar" requires. It is not `' '⍴A`: the printed
  space-only literals are two cells wide (cf. p39's measurements).
- `1 1⍉A`, `1 1⍉⌽A`, `1 1⍉⊖A`, `1 1⍉⌽⊖A` — the four outputs (the two diagonals
  and their reversals) need a *square* argument. `A` as defined on p34 is 5×9
  (`A←(10×⍳5)∘.+⍳9`), for which dyadic transpose with a duplicated axis is a
  LENGTH ERROR; the printed results are exactly the diagonals of the leading
  5×5 block. Transcribed as printed, not corrected.
- Three circle glyphs are used and are distinct at 2400 dpi: `⍉` (diagonal
  stroke, dyadic transpose), `⌽` (vertical stroke, reverse last axis) and `⊖`
  (horizontal bar, reverse first axis). The axis assignment is forced by the
  printed outputs: `⌽` gives 19 28 37 46 55, `⊖` gives 51 42 33 24 15.
- This article's code (like p1 and p21-p23) is set in the italic typewriter; no
  italic markup is applied inside fences.

## p37

- `[3] →N↓0 ⋄ I←1` — the mark between `N` and `0` is a **down arrow** (`↓`):
  full cap height, a serif bar across the top, and a filled triangular head at
  the bottom. It is not the booklet's `≠`, which is a small x-height "z with a
  bar" (p1 `C≠¯1`, p39 `∨.≠`). The reading is forced by the semantics: `N↓0` is
  the standard "branch out if N is zero" idiom (0 when N=0 → branch to line 0 →
  return; empty otherwise → fall through), whereas `→N≠0` would be a computed
  branch to line [1] and would restart the function forever. An earlier draft
  read `≠`, following Acrobat's `~` mapping; corrected here.
  `→L20×N≥I←I+1` on line [5] is the companion computed branch, using the label's
  line number as a value.
- `(0,MILLICRUS,MILLISECONDS,0)` — printed in italics and underlined, on the
  same line as the `⎕AI-T` output. It is the author's gloss on the units of the
  four `⎕AI` elements, not part of the result, so it is kept as an italic line
  after the fence rather than as data inside it.
- The FORTRAN listing is a plain fence (not APL); its three continuation dots
  are indented one character, as printed.
- `L20:` is a statement label but is *not* underlined in this listing (unlike
  p20/p38); transcribed bare either way.

## p38

- `→N←((⍴R)⍴L),0` and `L:` — `L` is underlined in both places, i.e. the label's
  line number is used as a value: N becomes ⍴R+1 targets, 4 for every rate plus
  a final 0, and `→N[I←J]` on line [4] loops or exits through it. Same device as
  p20's `→L←(M⍴A),0`.
- `D←1↓CF←D` — down arrow (drop). Checked against the printed output: after
  the drop `D` is DEP[2..N+1] while `CF` keeps all of DEP, so line [4]
  `T←CF[J←I+1]←D[I]+T×R[I]` reproduces the FORTRAN loop exactly.
- The three timings on p37-p38 agree with the prose: 2070 → 1301 ("reduced ...
  by one third") → 26 ("50 times faster").
- "We've" is printed with a typewriter apostrophe.

## p39

- The table is the same experiment as p24's, and the columns cross-check: `⍴R`
  is 3683/783/0/342/33/0/20/16/5/0/15/15/0/0 in both, and the "25 FEB 1977"
  SS2/SS3/SS4 columns reproduce p24's SS2/SS3/SS4 exactly (19/2/2, 60/8/8,
  56/2/2, 105/27/28, ...). All eight current columns were read digit by digit.
- Row labels containing Greek-looking glyphs: the run prints as italic alpha,
  epsilon, small iota, full-height circle, upsilon, rho, wavy mark, omega. They
  are transcribed as the APL symbols used for the identical table on p24 —
  `'⍵'`, `'⍺⍵'`, `'⍺∈⍳○∪⍴¯⍵'` — which the APL context also suggests (a test of
  symbols that do not occur in the target text). The seventh character is a
  small *wavy* mark at x-height, like the tilde p18 records, yet it is read as
  `¯` to match p24. Unresolved; recorded here.
  **Superseded:** it is a tilde, as on p24: `'⍺∈⍳○∪⍴~⍵'`.
- Space-only rows, measured quote-to-quote (cell pitch ≈5.1 pt): `''` 4.8 pt
  (adjacent cells), `' '` 9.6 pt, `'  '` 15.2 pt.
- `APLPLUSC/470-10011` is printed without the asterisk, as on p20.
- Tooling: `⊖` and `≥` were missing from `tools/lint_apl.py`'s glyph sets when
  these pages were first written; both have since been added by another editor,
  and the lint now passes. They are correct as printed.

## p40 — CHARACTER SEARCHES (continued)

- `∇ R←A ΔSS B;C` — the function name starts with a *bare triangle* (delta),
  not a letter. In the same header the italic capital `A` has a clear crossbar
  while the triangle is hollow with a flat base; both were compared at 2400 dpi.
  Transcribed as `Δ` (U+0394). The same glyph is used for `ΔFMT` on p10.
- `R←R↑(-C)↓B∧.=(C,R×R)ρA` — `↑` (take) and `↓` (drop) are both printed with
  distinct arrow heads and are transcribed as printed; the expression is
  cryptically terse but both arrows are unambiguous.
- OLD line 2 reads `∨/(((1↑⍴⎕SI),7)↑⎕SI)∧.='DSPELL['` — the constant is `7`
  (hard-coded length of `'DSPELL['`), as printed, not `1+⍴,FN` as on the line
  above.
- `VR[⎕IO-6-⍴VR]←'['` — printed as `⎕IO-6`, not `⎕IO+6`.
- `(STATES ROWSS 'NIA')⌿STATES` — the compress symbol is a slash crossed by a
  short bar (`⌿`), clearly different from the plain `/` of `∨/` earlier on the
  page; the row-mask semantics confirm `⌿`.

## p41 — BACK TO BASICS

- `⊥` in `10⊥ 8 2 9 5`, `100⊥ 6 5 77`, `60⊥ 2 10 38`, `3⊥ 4 2`, `4⊥ 3 2` and in
  the prose "represented by the ⊥ symbol (shift B)": up-tack with the bar at the
  bottom, stem ending at the bar (not `↓`, whose stem passes below the bar).
- `100⊥ 6 5 77 ⍝ (10000×6)+(100×5)+1×77` and the corresponding `60⊥` line end in
  a *lamp* comment: the glyph is a small filled script-`a` with a white counter,
  identical to the `⍝` on p3 (PDF p3) side by side at 2400 dpi. Both OCR passes
  read it as `A`/`a`; it is a comment giving the expanded polynomial.
- Underlined words in this article ("base value", "decode", "evaluates
  polynomials", "esoteric", "same as" twice, "mixed radix" on p42) are the
  booklet's emphasis mark, not italic. Transcribed plain, as on p1.
- `1⊥VEC`, `0⊥VEC`, `¯1↑VEC` in the question paragraph: the first two use
  up-tack, the third high-minus then take-arrow.
- The first body line of the column starts with a stray printed dot before
  "only" (`●nly`); a print defect, not transcribed.
- Arithmetic checked: `10⊥8 2 9 5 = 8295`, `(8×X*3)+(2×X*2)+(9×X)+5 = 8295`
  and `5+X×9+X×2+X×8 = 8295` for `X←10` (right-to-left evaluation), `100⊥6 5 77
  = 60577`, `60⊥2 10 38 = 7838`, `3⊥4 2 = 4⊥3 2 = 2+3×4 = 14`.

## p42

- `60* 3 -1 2 3` — the minus is printed at *mid height* (the same strike as the
  subtraction in `(⍴B)-⍳⍴B`), not the cap-height high minus that the same page
  uses in `¯743 60 60 ⊥ 10 0 120`. Transcribed as `-1`, i.e. as printed. Read as
  subtraction, `60*(3-1 2 3)` gives `2 1 0` and `60*2 1 0` gives the `3600 60 1`
  printed on the next line, so the line may be a compact two-step expansion; no
  change made.
- The `W←⌽1,×\⌽1↓A` block is printed flush to the left margin (no six-space
  session indent), unlike the `A←`/`B←`/`A⊥B` block above it; the left-column
  layout is reproduced, including the `week … ms` column labels that sit under
  the weights of `W←604800000 86400000 3600000 60000 1000 1`. Column positions
  were measured from the PDF text layer.
- `⌽` (circle-bar) is reverse and `↓` is drop in `⌽1,×\⌽1↓A`; the arithmetic of
  the whole display was checked step by step, ending at `604800000 … 1000 1`.
- The paragraph starting "base value is evaluating a mixed radix polynomial."
  begins with a lowercase `b` in the print; kept.
- `W← A*(⍴B)-⍳⍴B` — the exponent argument is `(⍴B)-⍳⍴B`, the iota printing as a
  small `ι` that resembles a `1`.
- All printed values verified: `A⊥B = 788645006` for the week/day/hour/… mixed
  radix, `+/W×B = 788645006`, and the two `314` and four `36120` results
  (including `¯743 60 60 ⊥ 10 0 120`, where the first element is only a
  placeholder).

## p43

- LENGTH ERROR display: `60 60⊥10 0 120` fails, and the re-display
  `60 60 ⊥ 10 0 120` carries the printed caret under the gap immediately before
  `⊥`; it is transcribed under the `⊥`. `LENGTH ERROR` is italic in the print.
- `(1-(V=' ')⊥1)⌽V` — the symbol before the `1` is the up-tack `⊥` (flat bar at
  the bottom, stem ending there), not `↓`; the prose ("as an and-scan (∧\)",
  "+/W×1", "1+ the number of contiguous ending spaces") confirms the decode
  reading: for two trailing blanks the expression is `(1-3)⌽V`, a two-position
  right rotation.
- `⊤` (down-tack, bar at the top) is encode in
  `R←1+100⊥10000 12⊤A+12⊥10000 100⊤YM-1`, distinct from `⊥` in the same line;
  the closing paragraph names the pair explicitly, decode (⊥) and encode (⊤).
- `(⍳6) MONTHADD 197806+⍳6` — both iotas print as small `ι` marks.
- All MONTHADD results verified by hand: `7 MONTHADD 197805 7806 197912` →
  `197812 7901 198007`, `¯5 ¯11 ¯16 MONTHADD 197804` → `197711 197705 197612`,
  `(⍳6) MONTHADD 197806+⍳6` → `197808 197810 197812 197902 197904 197906`.
  `FASTFLOW` and `(0,IR+1)⊥SB,DP` were also recomputed; the printed
  `100 120 200 316 100 105 234.56` and `234.56` are correct.

## p28 — USING BOOLEANS TO CONTROL COMPUTATION

- The article title is letter-spaced capital letters with no italics;
  transcribed as an `##` heading, as with the other article openings.
- The seven `+/`, `∧/`, `∨/`, `<\`, `⍳`, `/` and `/⍳⍴` examples are printed as
  two columns: the expression indented six spaces in the left part of the
  column, the explanation flush right, and each result alone at the left
  margin. They are transcribed as a three-column table (result, expression,
  explanation) so that each explanation stays with its expression. The page
  prints no column headings, so the header row is empty. (An `apl` fence
  cannot hold the marginal prose: "if it's more than 1." on p29 would open a
  character literal for the linter, and putting English inside code would
  read as code.)
- `V[⍒V>8]` — the glyph inside the brackets is an apex-**down** triangle with
  a stem, i.e. `⍒` grade down, not `⍋`; compare `⍋` on p4 (`RANK←⍋⍒POP`),
  where the triangle points up. The printed result
  `11 9 12 14 13 8 7 5 8 3 6 1 5 7` (the 1s first, each group in original
  order) is what grade down produces.
- `V←?14⍴14 ⋄ V,[0.5] V>8` — the separator is the diamond `⋄`. The display is
  a formatted two-row matrix; its numeric rows are reproduced on the print's
  three-character column grid (2-wide right-justified fields, one space
  apart), measured from the scan.
- Verified from the printed `V`: `+/V>8` = 5, `∧/V>8` = 0, `∨/V>8` = 1,
  `(V>8)⍳1` = 3, `(V>8)/V` = `11 9 12 14 13`, `(V>8)/⍳⍴V` = `3 5 6 11 14`,
  and `<\V>8` has its single 1 in position 3. `V>8` itself is
  `0 0 1 0 1 1 0 0 0 0 1 0 0 1`, as printed.

## p29

- `DISP⌿REGS` and `(~DISP)⌿REGS` — the symbol between `)`/`DISP` and `REGS`
  is a diagonal slash crossed by a short *horizontal* bar, not the plain `/`
  printed in `+/V>8` on p28. Read as `⌿` (compress along the first axis),
  which is what selecting rows of the region-name matrix requires, and which
  is the reading another page uses for the same glyph shape (p40). Recorded
  because the 1970s typeball draws `⌿` with a horizontal rather than vertical
  stroke.
- `DISP⌿REGS,'P⎕ (⎕Q⎕)⎕BLI6' ⎕FMT NA` — the four `⎕` *inside the quoted
  format string* are printed as boxes with a filled top band (the italic form
  of the quad; the same shape occurs on p6 in `'G⎕  T[9;9;9] ⎕'`), while the
  `⎕` of `⎕FMT` is a plain tall upright box. All are transcribed as `⎕`.
  The string is a `⎕FMT` picture (letters like `I`, `P`, `Z`, `G` are format
  codes in this booklet — see pp12, 13, 17, 33). Cell-by-cell measurement of
  the scan gives exactly one space after `P⎕`, i.e. `'P⎕ (⎕Q⎕)⎕BLI6'`; no
  interpretation of the picture is offered.
- The `DISP←NACC>0` / `NA←NACC×NACC>1` pair carries two-line marginal
  explanations and is printed in the same two-column style as p28;
  transcribed as a two-column table for the same reason.
- The region report is aligned on the print's character grid: the name is
  padded to column 19 (from the column margin) on every line and the
  parenthesised count starts there, left-justified (`(3)`, `(10)`), so the
  `(` is at the same x in all six lines.
- `A÷B ⋄ A÷B*B≠0` — the first row's `0÷0` prints as `1` (the APL\360 /
  APL\*PLUS convention), giving `2 1.75 1 2.5 1 1 1.25 0 0 3.5`; the second
  expression `A÷B*B≠0` substitutes 1 for the zero divisors and prints the
  `0`s. Both rows recomputed and they match. The prose's `0÷1` and
  `A÷B+B=0` are also as printed.
- Operation table: `BOOLEAN!A` is binomial (`0!A`=1, `1!A`=A) and
  `BOOLEAN|A` is residue (`0|A`=A, `1|A`=0), with the footnote marker printed
  after the `0` in the `BOOLEAN←1` column and "(#) Only for integer *A*."
  below. The table headers are underlined in the print (rendered as table
  headers), and the pipe in `BOOLEAN|A` is escaped as `\|` inside the table.

## p30

- `(1,⍴A)⍴∘≠C⌽A,[0.5] B` — between the second `⍴` and `≠` the print has a
  single small raised circle (`∘`). Character-cell measurement shows exactly
  one cell for each of the two glyphs, so there is **no** outer-product dot:
  the line is not `∘.≠`. As printed the phrase is odd (a jot applied to
  `≠`), yet the displayed result
  `5 6 7 8 9 16 25 27 32 36 49 64 81` is exactly what reducing the
  conditional rotation gives (`A*B` where C=0, `B*A` where C=1; verified
  column by column against the printed `A`, `B` and `C` rows). Transcribed
  glyph for glyph, nothing added or dropped.
- `A,[1] B,[0.5] C` — the second row prints `27` in a two-character field;
  the display is reproduced on that column grid. `C` alternates
  `0 1 0 1 0 1 0 1 0 1 0 1 0`, and with it every printed result value checks
  out (16, 25, 27, 32, 36, 49, 64, 81 included).
- Prose kept as printed even though it looks like a slip: "(e.g., `A÷B` or
  `A-B`)" (the inverse of `÷` is `×`) and "one of `×*|!`" (a plain vertical
  bar).
- The plotting display `' ⎕'[1+FREQ∘.≥⍳⌈/FREQ]` prints only **seven** bar
  rows: 10, 24, 15, 21, 35, 5 and 18 boxes. `FREQ` has eight elements
  (`10 24 15 21 35 31 5 18`), so the row for `31` is absent from the print;
  the line pitch between the 35-box row and the 5-box row is unchanged, so no
  line was simply dropped by the scanner. Transcribed exactly as printed
  (7 rows).
- The plotted character is a `⎕`: the string is `' ⎕'` (quote, one space,
  quad, quote — measured on the character grid) and the bars are drawn as
  quad outlines.

## p31

- `(VOWELS,CONS)[⍋⍋MERGE]` — both grade glyphs are apex-**up** triangles with
  stems (`⍋`), i.e. a double grade, not `⍒`. Verified: `MERGE` is
  `1 0 1 0 1 0 0 0 1 1 0`, `+/~MERGE` = 6 = `⍴VOWELS`, `+/MERGE` = 5 =
  `⍴CONS`, `⍋⍋MERGE` = `7 1 8 2 9 3 4 5 10 11 6` and
  `'AEIOUYFCTSL'[...]` = `FACETIOUSLY`.
- The transcript has no blank lines between statements in the print (uniform
  line pitch); the visual gaps are just the short single-value result lines.
- `July 1977` is the closing date line of the article.
