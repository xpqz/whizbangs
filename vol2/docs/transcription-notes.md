# Transcription notes: Volume 2

Recorded while transcribing each page from the scan: readings that were uncertain (with the
crop command that shows them), places where the printed code looks wrong, and layout
decisions. Later findings (execution, blind re-reading, proofreading) are in
`aplplus-verification.md`; where they settle a question raised here, that file is the record.

## Notes: front matter and printed pages 1–8 (PDF 3–5, 7, 9–16)

Crop commands run from the repo root with `WB_VOL=vol2`.

### Front matter

- **00-1-title (PDF 3)**: no doubts. Phone number printed `301-984-5000`
  (the scan shows the hyphens faintly).
- **00-2-copyright (PDF 4)**: only the printer's key `10 9 8 7 6 5 4 3 2`
  and "Printed in the United States of America." are printed; the rest of
  the page is scan specks.
- **00-3-note-to-readers (PDF 5)**: the cartoon (robot-like computer) is
  given as a figure comment. The dagger footnote marker after *APL\*PLUS*
  is rendered as a Markdown footnote, as in volume 1. The Editor's Note is
  set entirely in italics and is transcribed as one italic paragraph.
- **00-4-contents (PDF 7)**: rendered as a table (title, page). "Rotation
  Problem—Results" uses an em dash, written `--`. In `)ORIGIN 0` the `0` is
  upright, the rest APL italic (`tools/crop.sh 7 80 470 200 20 500 OUT.png`).

### p001 (PDF 9)

- "43-character": the hyphen is crushed against the 3 in print ("43character"
  in the OCR); it is there in the scan (`tools/crop.sh 9 110 385 350 50 450 OUT.png`).
- Footnote marker `*` after "functions" rendered as a Markdown footnote.

### p002 (PDF 10)

- Input lines `1403= 1374 …` have one space after `=` (measured against the
  5.7 pt pitch of the APL font).
- Ends with a colon before code on p003: `<!-- continue -->`.

### p003 (PDF 11)

- First line `∨/A∘.=,B` is set in the regular (not bold) APL font, i.e. a
  statement shown, not entered. Kept as an indented code line.
- `⎕←L←¯1↑⍴NAMES`: arrow is `↑` (head at top)
  (`tools/crop.sh 11 125 395 80 12 700 OUT.png`).
- LENGTH ERROR caret sits at column 6, under the N of NAMES.

### p004 (PDF 12)

- `CC←(¯1↑⍴1/A),1↑⍴1/B` (up arrows) vs. prose `(¯1↓⍴A),1↓⍴B` and `¯1↓⍴A`
  (down arrows) — checked at 900 dpi (`tools/crop.sh 12 180 150 60 14 900 OUT.png`).
- Transpose glyph is `⍉` (circle with stroke from upper left to lower right)
  (`tools/crop.sh 12 175 202 50 14 900 OUT.png`).
- `∨⌿NAMES∧.=⍉SEV`: the slash carries a bar (`⌿`) (`tools/crop.sh 12 140 330 200 70 500 OUT.png`).
- The Boolean matrices (`NAMES∧.=⍉SEV`, `SEV∧.=⍉NAMES`) are printed one
  column to the right of the vectors (`9 3`, `1 0 1`); transcribed with a
  leading space as printed. Same on p007 for `BM`.
- The display line `∨/A∘.=VEC` carries a marginal note "Equivalent to
  A∊VEC" set in the text font at column 25. Kept inside the code block at
  its column (there is no other place for it).

### p005 (PDF 13)

- `VEC← 1374 143 …`: one space after `←`, as printed.
- Prose "14 0 3" (odd letter spacing) is 1403.

### p006 (PDF 14)

- The `↔` glyph is set two cells wide in the identity lines (`~A=B ↔ A≠B`,
  `VEC⍳A ↔ SA⍴…`, `↔ 1++/∧\A∘.≠VEC`): the text after it starts one column
  later than single-space would give. Transcribed with single spaces around
  `↔`; the two `↔` stay aligned
  (`tools/crop.sh 14 170 600 330 45 600 OUT.png`).
- "Value if not found; shape of A." is a text-font marginal note at column
  33 of the `NF←1+⍴VEC ⋄ SA←⍴A` line; kept in the code block.
- Last sentence runs to p007: `<!-- continue -->`.

### p007 (PDF 15)

- `NF←1+1↑⍴MAT ⋄ SA←¯1↓⍴A`: first arrow up, second down
  (`tools/crop.sh 15 125 652 140 16 900 OUT.png`).
- RANK ERROR carets at column 6.

### p008 (PDF 16)

- `C←'  SO BE IT IF   WE DO  AS IN TV   '`: spaces counted against the pitch
  (2 leading, 3 after IF, 2 after DO, 3 trailing)
  (`tools/crop.sh 16 145 330 300 60 500 OUT.png`). Uncertain by ±1 for the
  trailing run only (the closing quote is faint).
- **Suspected print discrepancy**: removing the first blank of each double
  blank should leave one leading (and one trailing) blank, i.e.
  ` SO BE IT …`, but the result is printed starting in column 0. Transcribed
  as printed.
- p009 starts a new article ("The 'All But' Case"), so no `<!-- continue -->`.

### Lint

`WB_VOL=vol2 python3 tools/lint_apl.py` reports no objections for these files.

## Notes: printed pages 9–17 (PDF 17–25)

Articles: "The "All But" Case" (pp. 9–12, dated November/December 1978),
"Numeric Sorts" (pp. 13–15, January/February 1979), "Other Sorts" (starts
p. 16, continues past p. 17).

All crop commands are run from the repository root with `WB_VOL=vol2`.

### General decisions (all pages)

- Single statements that the book sets on their own indented line in the
  regular (not bold) APL italic, inside the prose (e.g. p9
  `NEWREGCODES←3↑(~⎕AV∊REGCODES)/⎕AV`, p10, p11 `+/CODES`, p14, p15, p17),
  are given as ```` ```apl ```` blocks with the six-space input indent, though
  they are not printed as bold session input.
- Function listings: the book sets comment lines (`⍝`) and labelled lines
  one column to the left of ordinary statements. Both are transcribed
  outdented one column (`[1]  ⍝ ...`, `[3]  a:...`), as printed.
- Matrix displays (DATES on pp. 13–15) have one leading blank column in the
  print; kept (` 1978   10   31`). The *cs* display on p17 also has a leading
  blank, which is the space that begins the collating sequence.
- No lint objections for these pages; nothing overridden.

### p009 (PDF 17)

- `5 ¯2↓MATRIX`: the arrowhead is at the bottom (drop), matching the prose
  "drop (↓)". `tools/crop.sh 17 85 396 180 14 600 out.png`
- `(5↓⍳⌊/⍳0)`: `⌊` is clear at 300 dpi. `tools/crop.sh 17 85 400 370 85 300 out.png`
- Ends mid-sentence; `<!-- continue -->`.

### p010 (PDF 18)

- The two-column list of `B/VEC`, `(~B)/VEC`, `N↑VEC`, `N↓VEC` with
  explanations is transcribed as a Markdown table with an empty header.
- `VEC[(~(⍳⍴VEC)∊INDS)/⍳⍴VEC]       Select all but INDS.` -- the right-hand
  text is a marginal annotation printed in the text font on the same line as
  the input; kept in the code block on that line (it is not an APL comment).
  `tools/crop.sh 18 145 470 370 155 400 out.png`
- "dash" before "that is" written as `--`.

### p011 (PDF 19)

- `+/ 1 2  8 16  64 128 256 512 1024 2048 4096 8192`: the gaps where 4 and 32
  are omitted are two blanks wide (measured against the fixed pitch).
  `tools/crop.sh 19 90 495 370 110 400 out.png`
- "(3 2)" and "16 3 4 7" in prose are the APL-font numbers 32 and 16347 with
  typesetter letterspacing; written as 32 and 16347.
- Ends mid-sentence ("give myself ¯5 access (all"); `<!-- continue -->`.

### p012 (PDF 20)

- *ALLFNSBUTGRP* [4] `COLS←(1↓⍴ALLFNS)⌈1↓⍴TOKEEP`: both arrows have the head at
  the bottom (drop); [5] and [6] use take (`↑`). [7] ends `)⌿ALLFNS` (slash
  with bar) and uses `⍉TOKEEP`. `tools/crop.sh 20 175 272 200 40 900 out.png`
- *AFBG* [5] `⍎⎕FX TOKEEP,[0.5](⍴TOKEEP)↑'TOGO←⎕NL 3'`: the arrow after
  `(⍴TOKEEP)` is blurred; head looks to be at the top, read as `↑` (take).
  Uncertain. `tools/crop.sh 20 175 436 220 14 900 out.png`
- Header shows a visual gap before `;COLS`; read as no blank (the narrow `;`
  is centred in its cell).

### p013 (PDF 21)

- `DATES` and `DATES[⍋DATES[;1];]` are printed side by side; transcribed as two
  consecutive code blocks with an HTML comment saying so.
- Right display, row 3: the second digit of `30` is an ink blot; read as `0`
  (the row is 1978 11 30 from DATES). `tools/crop.sh 21 80 625 330 90 400 out.png`

### p014 (PDF 22)

- *DATASORT*/*INDSORT* [3] `a:→COL↓b`: arrow head at the bottom (drop).
  Labels A and B are underscored, written `a`, `b`.
  `tools/crop.sh 22 140 205 250 60 700 out.png`,
  `tools/crop.sh 22 140 343 250 60 700 out.png`
- **Suspected error in the original**: `MAT[⍋(⌈⌿MAT)⊥⍉MAT;]`. With the column
  maxima as radix, a value equal to its column maximum overflows into the next
  position, so this does not uniquely represent rows; `1+⌈⌿MAT` would. The next
  page's text ("computes the minimum values that ... will uniquely represent
  rows") describes the intended expression. Transcribed as printed; there is no
  `1+` in the print. `tools/crop.sh 22 175 702 110 16 900 out.png`

### p015 (PDF 23)

- `0 12 31 ⊥⍉DATES` and `S←DATES[⍋ 0 ¯12 31⊥⍉DATES;]`: the first number in
  both is a solid oval blot the size of a digit, read as a filled-in `0` (the
  shown results 736157 … agree with a radix whose first element is irrelevant).
  `tools/crop.sh 23 120 175 120 20 900 out.png`, `tools/crop.sh 23 120 365 220 50 800 out.png`
- In the *S* line, a short low bar between `31` and `⊥` and a bar under the
  `A` of `DATES` in the line above are stray marks (the latter is probably the
  high minus of `¯12`); ignored. Blank before `⊥` uncertain: none in the *S*
  line, one in the earlier `0 12 31 ⊥⍉DATES` line (by measured position).
- `R←|INDSORT DATES×(⍴DATES)⍴¯1 1 1` and `T←DATES[⍋DATES+.× ¯10000 100 1;]`:
  blank after `+.×` is visible; none after `⍴`.
- Identity line `⍒A ↔ ⍋-A ↔ ⍋A×¯1`: the double-headed arrows are written `↔`.
- `R←M,0 ⋄ R←M[⍋+⌿R<.-⍉R;]`: slash with bar (`⌿`).
  `tools/crop.sh 23 120 545 160 16 900 out.png`

### p016 (PDF 24)

- *CS* is underscored in all three statements, written `cs`.
  `tools/crop.sh 24 140 425 240 140 500 out.png`
- The last letter of `'ABC…XYZ'` looks like a `2` but is the italic `Z` of
  this font.
- Error caret written `∧` (as on vol2 p003).
- The sentence "We can sort the hand by suit alone, … by denomination alone,
  … or by denomination within suit," runs across onto p17;
  `<!-- continue -->`.

### p017 (PDF 25)

- *CS* underscored in the display, the *CINDSORT* header and line [3], the
  example call, the prose `⍴cs` and the encoding expression; written `cs`.
- Prose "base value (⊥.)": a dot follows the glyph; taken as a print artifact
  and written `` (`⊥`) ``. `tools/crop.sh 25 90 530 370 140 400 out.png`
- `CHRMAT[⍋(⍴cs)⊥cs⍳⍉CHRMAT;]`.
- Page 18 begins with the *MNOC* derivation display after "is as follows:", so
  no `<!-- continue -->`.

## Notes: printed pages 18–26 (PDF 26–34)

Crop commands run from the repo root as `WB_VOL=vol2 tools/crop.sh ...`.

### General conventions applied

- The global collating sequence is printed with an underscored *C̲S̲* and is
  written `cs`; the local *CS* in the header of *CSORTRX* (p21) is not
  underscored and stays `CS`. Underscored labels (A̲, B̲, L̲, S̲ …) are lowercase.
- Function listings: comment lines (`⍝`) are printed one column left of the
  statements, like labels, so they are written at column 5
  (`[1]  ⍝ …`). The listings themselves are slightly indented in print; the
  header `∇` is written at column 0 per the house rule.
- Numeric matrix output on these pages is printed with one leading blank
  (vectors and scalars are not); kept as printed.
- Marginal annotations printed beside code ("Data.", "Row number.",
  "11 characters, 3 functions, ⎕IO referenced", "Branch to either of two
  lines.", "A histogram.", the "or:" alternatives, "ROWS ,[¯0.5] COLUMNS")
  are kept on the same line inside the code block.
- Indented code that the book sets in the regular (non-bold) APL font
  (UTILHOW 'CSORTR', BR←…, the p23 primitive table, etc.) is written as
  6-space input lines.

### p018 (PDF 26)
- The six-line derivation above `⍴cs ⋄ ⎕←MNOC…` is printed in a box;
  transcribed as a code block with the left sides right-aligned, preceded by an
  HTML comment saying it is boxed. `tools/crop.sh 26 140 95 220 120 500 out.png`
- CMSORT [4] `→COL↓b`: the arrow glyph is blobby; arrowhead judged low (↓),
  compared with the clear ↑ in [2]. Semantics agree (branch out when COL=0).
  `tools/crop.sh 26 185 318 50 14 1200 out.png`
- CMSORT [5] `⍉MAT[…]` (circle with backslash), confirmed at
  `tools/crop.sh 26 215 324 45 14 1500 out.png`.
- ROWSORT [2] `''⍴⍴R←MAT`: the two quotes are adjacent (no blank inside).
  `tools/crop.sh 26 150 585 330 32 900 out.png`
- `⎕←M←? 3 6 ⍴9` spacing kept as printed (bold input font).

### p019 (PDF 27)
- `⍉(⌽A)⍴⍳1↑A` confirmed: `tools/crop.sh 27 205 117 130 14 1200 out.png`
- `ROW←⌈GRM÷1↓A` and NSORTROW/CSORTROW `⌈GRM÷1↓R`: arrowheads low (↓).
  `tools/crop.sh 27 210 345 60 14 1200 out.png`,
  `tools/crop.sh 27 250 682 100 12 1200 out.png`

### p020 (PDF 28)
- The display of `cs` starts in column 1: the collating sequence begins with
  a blank, which also explains the right-justified CSORTROW output.

### p021 (PDF 29)
- Article title printed as "*CSORTR* Algorithm" (CSORTR in bold italic APL
  font); written `## *CSORTR* Algorithm`.
- CSORTRX [2] `(1↑cs[])`: a short underline mark sits under the `1`, at the
  same height as the underscore of `cs`. Taken as a stray mark (it is directly
  above the high minus of `¯1` on line [3]); the 1 is not an underscored name.
  `tools/crop.sh 29 115 382 120 28 1200 out.png`
- CSORTRX [3] `L←⍴CS←⊖[,A] cs`: the mark under the C of the local `CS` is the
  high minus of `¯1↑S` on line [4]; local CS is not underscored. The glyph is
  clearly ⊖ (circle with horizontal bar). Spacing `K←K[1∊ ¯1 1 ∊A]` kept as
  printed. Possible print oddity: `⊖[,A]` with A = ¯1 or 1 as an axis looks
  doubtful (axis ¯1 would be an error), but it is what is printed.
  `tools/crop.sh 29 200 382 110 28 1200 out.png`
- CSORTRX [5] `K⍴1`: the bar above the 1 is the underscore of `b` on line [4]
  directly above, not a high minus. `tools/crop.sh 29 110 400 200 40 900 out.png`
- Prose: "membership (∊) search" has an underline under "(∊) search" in the
  scan; treated as a stray mark.

### p022 (PDF 30)
- No doubts.

### p023 (PDF 31)
- Primitive table, `R←○/[OSA]A` and `R←○\[OSA]A`: the operand is a heavy
  ring of x-height sitting on the baseline, larger and bolder than the jot of
  `∘.>` on p24; written `○` as a placeholder for "any function". Could be
  meant as `∘`. `tools/crop.sh 31 115 428 60 22 1500 out.png`
- Right column `ODR←⍒A` (grade down) vs left `ODR←⍋A`.
- The box glyph left of `⎕IO` in prose is ⎕ throughout.

### p024 (PDF 32)
- `10 ¯10[1]`: the first glyph is a damaged `1`, not `⍳`.
  `tools/crop.sh 32 170 80 70 14 1800 out.png`
- "For example, →l×⍳M≥C←C+1": the L is underscored (label).
- `VEC,[¯0.5]⌽VEC` output column widths counted as 3.
- Histogram output: 6, 2, 9, 6, 10 quads; the sixth (empty) row for the 0
  element is invisible in print and not written.

### p025 (PDF 33)
- `INP←'PRINT/34'`: the underline under the 3 is the high minus of `(¯1+` on
  the next line. `tools/crop.sh 33 90 85 280 50 700 out.png`
- `VEC←⎕IO↓0,VEC` read as ↓ (semantics agree).
- The three counter/limit snippets are statement fragments, not listings;
  written with statements at column 6 and the label line outdented one column.
- Code blocks that belong to bullet items are placed at column 0 after the
  item (the lint only checks fences at column 0).

### p026 (PDF 34)
- `→(s,v,m,a)[3⌊⍴⍴ARRAY]` and `→(a,l,v,f,x)[⎕NC 'NAME']`: all labels
  underscored. `tools/crop.sh 34 195 305 150 24 1000 out.png`
- Article ends with "May/June 1979"; no `<!-- continue -->`.

### Lint
- `WB_VOL=vol2 python3 tools/lint_apl.py`: no objections in p018–p026.

## Notes: printed pages 27–35 (PDF 35–43)

Crop commands run from the repository root with `WB_VOL=vol2`.

### p027 (PDF 35) -- Error Checking

- The character-data input under `⎕:` reads `'!'`: the middle glyph is a
  quote with a small dot below it. The dot is only 2×2 px at 144 dpi and
  fainter than the quotes, so it could be a speck, which would make the input
  `'''`. Uncertain. `tools/crop.sh 35 70 550 250 50 700 out.png`
- In the DOMAIN ERROR display the caret is under `=` (column 28, counted
  against the fixed pitch).
- Second fragment line `[3]`: `b:→(I<.<(⌈I), 500 1000)⍴c`. The ceiling (`⌈`,
  bar at the top) is clear, and there is one blank after the comma.
  `tools/crop.sh 35 80 660 300 35 700 out.png`
- The code fragments have no header. They follow the listing convention:
  label lines are outdented to column 5 and other statements start at column 6.

### p028 (PDF 36)

- The `⎕ERROR` test statements are printed indented with no line numbers.
  They are transcribed as input lines (6 spaces).
- `⎕ERROR(E≤.≥(⌈E), ¯2 2 *31)/'DOMAIN ERROR'`: the spacing was measured on
  the fixed pitch. The `¯` takes its own cell in this font, so this is one
  blank after the comma and one blank before `*`. The tests
  `B≤.≥(⌈B),2* 0 31` and `E≤.≥(⌈E), ¯2 2 *31` are inconsistent in form, but
  they are printed that way. `tools/crop.sh 36 160 416 260 54 650 out.png`
- `B← 0 1 0 0 0 0 0 0 0 1 0 /F[], 4 0` has 11 digits, with one blank before
  the first digit, before `/` and after the comma.
- The bullet list continues on p029 (`<!-- continue -->`).

### p029 (PDF 37)

- `⎕ELX←'⎕ERROR(∧\⎕DM≠⎕TCNL)/⎕DM'`: read clearly.

### p030 (PDF 38) -- A Clever Sort

- In *NMGU* line `[1]`, the initials N, M, G and U of the comment are
  underscored. They are written in lowercase as `⍝ nUMERIC mATRIX gRADE uP.`,
  following the volume 1 practice (docs/aplplus-verification.md). The `⍝` is
  outdented to column 5, as printed (line `[2]` starts at column 6).
- Line `[2]` shows overbars above `I`, `←` and `T`. They look like
  underscores from line `[1]` that bled into line `[2]`, so they are ignored.
- Line `[3]`: `a:→CI↓0` (down arrow). `tools/crop.sh 38 130 503 230 30 800 out.png`
- *MAT* display: on p031 the output rows are indented 3 columns relative to
  the left margin, with a common column width of 6, so the same 3-space indent
  is used on p030. In print, the input `MAT` stands at output column 3 on
  p030. It is written at column 6, the house input indent.

### p031 (PDF 39)

- *NMGRUP* line `[6]`: `PV⍲1⌽PV` (nand, `∧` with tilde). There is no blank
  between `≠` and `¯1`, measured by cell positions: the `¯` is drawn in its own
  cell, left of the `1`. `tools/crop.sh 39 95 447 270 45 800 out.png`
- Line `[7]`: `→a××⍴PV←UR/PV`, with no blank between the two `×`.
- The two-column "Line [n] / ⋄" explanation is transcribed as a Markdown
  table. It continues on p032 (`<!-- continue -->`, with the table rows
  carried on).

### p032 (PDF 40)

- In the *NMGRADEUP* comment only N and M are underscored (GRADE and UP are
  not), so it reads `⍝ nUMERIC mATRIX GRADE UP (WITH SPECIAL CASE HANDLING).`
  This may be a print inconsistency compared with *NMGRUP*.
  `tools/crop.sh 40 150 324 250 14 800 out.png`
- Line `[5]`: `→(⍴PV←U/PV)↓0` (down arrow).
- Inline `5 100⍴⍳100`: one blank after the 5.

### p033 (PDF 41) -- Arrays of Arrays

- The prose `1920 ↔ 24×80` has the non-APL `↔`. It is written as `1920` ↔
  `24×80`.
- Code spacing was measured: `24 80 ⍴(×/ 24 80)↑VEC` and
  `⍉ 80 24 ⍴(×/ 24 80)↑VEC`, with single blanks.

### p034 (PDF 42)

- "The underlined portions may be elided": Markdown code cannot show an
  underline, so the underlined part of each expression is recorded in an HTML
  comment after its block. In SCALARS, ACROSS the underline covers
  `24 80 ⍴ 1 2 ⍉`. In SCALARS, DOWN it covers `24 80 ⍴ 2 1`.
- `⍴MAT` gives `117 16`, while the text says "nominally ... 120". Figure 1 holds
  117 names (23 full rows plus ZAMBIA and ZANZIBAR), which agrees with the
  printed `⍴MAT`.
- Figures 1 and 2 are transcribed as `text` blocks with 16-character fields.
  The frame is only described.

### p035 (PDF 43)

- The underline in VECTORS, ACROSS runs from before `1 2 3` to under `×/`,
  that is `1 2 3 ⍉ 24 5 16 ⍴((×/`. That seems longer than the elidable part
  (compare SCALARS, ACROSS on p034). This may be a typesetting slip; it is
  recorded as printed. `tools/crop.sh 43 125 432 270 50 800 out.png`
- `⍴TEN` gives `18 6 16`, while the text says a 20-element vector (nominal).
- `24 80 ⍴ 1 3 2 4 ⍉ 4 5 6 16 ⍴((×/ 4 5), 6 16)↑TEN`: there is a blank after
  the comma, unlike the other expressions (`,16)`).
- Printed page 36 starts with Figure 3, so p035 has no `<!-- continue -->`.

### Lint

No objections in these files.

## Notes: printed pages 36–44 (PDF 44–52)

Crop commands are run from the repository root with `WB_VOL=vol2`.

### Conventions used on these pages

- Figures 3 and 4 (p036) are boxed terminal output. They are transcribed as
  `apl` code blocks (5 columns of 16 characters, trailing blanks dropped),
  preceded by an HTML comment and followed by the caption in bold.
- Prose annotations printed to the right of an input line ("Row totals.",
  "Count the number of leading blanks.", "or: 3 3 3⌽MAT") are placed as a
  separate paragraph after the code block.
- Non-bold expressions set on their own indented line (identities, "general
  form" lines, MATRICES ACROSS/DOWN summaries) are in `apl` blocks, indented
  six columns like input.
- Underscored letters are lower-cased (rule 3), also inside comments and
  string constants (p044).

### p036 (PDF 44)

- Figure 3, Templeton zip: an ink blot covers the first digit of `94105`;
  read as 9 (Figure 4 prints `94105` cleanly).
  `tools/crop.sh 44 290 210 200 60 600 out.png`
- Figure 3, Wilson street: the 5 of `35 WISCONSIN CT` is broken (looks like
  S); read as 5, as in Figure 4.
- Figure 3, `CHAPEL HILL` state looks like `HC`; it is the italic N of this
  font (same shape as in `SAN`). Read `NC`.
- Figure 4, Taylor street: first digit of `4701` is smudged; read 4 as in
  Figure 3.

### p037 (PDF 45)

- **Suspected print error**: MATRICES, ACROSS line prints `(×/ 4 5). 6 16`
  with a period where p035 and the DOWN line have a comma. Transcribed as
  printed (period). `tools/crop.sh 45 120 115 300 55 500 out.png`
- "Workspace 444 LABELS ... 444 ADDRFP": workspace numbers left as plain
  text, names in italics.

### p038 (PDF 46)

- LENGTH ERROR caret: measured position is under the blank between `0` and
  `\` (column 15), not under `\` (column 16). Transcribed at column 15 as
  printed; it may be a typesetting slip.
  `tools/crop.sh 46 165 630 100 30 800 out.png`
- "it meant APL ex-panded": both words italic; written `*APL* *expanded*`.
- The three forms of expansion with their descriptions are a two-column
  table, transcribed as a Markdown table.

### p039 (PDF 47)

- `APL\360` result `0 0 360 360 0`: last digit of the first 360 is an ink
  blot; read 0. `tools/crop.sh 47 95 80 200 60 500 out.png`
- JOHNS social security number `122567290`: the 7 has a stray pen stroke
  through it; read 7.
- `COND⍀COND⌿MAT`: first-axis expand and first-axis compress (both barred).
- `MAT×⍉(⌽⍴MAT)⍴COND`: transpose then rotate (reverse) glyphs read from shape.

### p040 (PDF 48)

- `'⍞ NOT FOUND: ⍞,LI6' ⎕FMT EN[N]`: the ⎕FMT text delimiters are a box
  with a mark hanging from its top edge; read as quote-quad `⍞`.
  Uncertain. `tools/crop.sh 48 170 352 280 14 900 out.png`
- INDEX ERROR caret is under the S of `SSEC` (column 45), as printed.
- `VRSELECT` listing: line [1] (a comment) is exdented one column (⍝ at
  column 5), measured from the scan; the book's ⎕VR style exdents comments
  and labels (p044 says so explicitly). Statements at column 6.
- `0 4 5 VRSELECT ⎕VR 'VRSELECT'` output: ∇ printed at column 4 with the
  header at column 6, as ⎕VR output; kept as printed (not reformatted to the
  house listing style, since it is output).
- `LN≠¯1↓0,LN` on line [5] (both copies): drop arrow, head at the bottom.

### p041 (PDF 49)

- `VTOM` line [2] `1↑V` (take) and line [3] `1↓(INDS-1)` (drop) read from
  arrowhead position. `tools/crop.sh 49 120 272 200 14 900 out.png`
- Line [4] `HIST←LEN∘.≥⍳0⌈⌈/LEN` — two ceiling glyphs.

### p042 (PDF 50)

- Identity lines `N⌽V ↔ ((⍴V)|N)⌽V` are in code blocks with `↔`.

### p043 (PDF 51)

- `2⍕CUM,[0.5] TRANS` output: column positions measured; all five columns
  are 8 wide, with a leading blank (` 400.00`).
  `tools/crop.sh 51 120 280 260 55 600 out.png`
- `CLEAN←1↓(B⍲1⌽B)/CV`: the glyph is ∧ overstruck with ~ (nand), which fits
  "not both blank and followed by a blank".
- The `'|',CV,'|'` display: spaces counted from the scan:
  `|  DELETE   ALL  EXTRA BLANKS   |` (CV after the `' ',CV` prefix).
- `TRANS←CUM-¯1↓0,CUM`: arrow is poorly printed; read as drop.
  `tools/crop.sh 51 150 330 150 16 700 out.png`
- Bulleted list items contain their code blocks (indented two spaces).

### p044 (PDF 52)

- `MAT0`: the final character is the upright digit 0, not the italic
  letter O.
- `CRTOVR` header: the letters T and O of the function name are underscored
  in print, so it is transcribed `CRtoVR`. This may be emphasis or a stray
  underline; check against the next article (p045), where the answer is
  given.
- Line [5]: `'ABC…ZΔ` followed by the underscored alphabet and underscored
  delta (`⍙`), then the digits. Label `A̲` → `a`; line [3] branches to `a`.
- Line [6]: the L of LABELS, O of OR, C of COMMENTS are underscored
  (mnemonic for LOC) → `lABELS oR cOMMENTS`.
- Line [7]: `YOUR CODE GOES HERE` is fully underscored → `your code goes
  here!`.
- Comment lines [1], [2], [6], [8] and label line [5] are exdented one column
  (column 5), as printed.
- The listing continues on p045 (lines [9]–), so the page ends with
  `<!-- continue -->` and no closing ∇.

### Lint

No lint objections in p036–p044.

## Notes: printed pages 45–51 (PDF 53–59)

Crop commands are run from the repository root with `WB_VOL=vol2`.
Column positions were measured from 600-dpi crops (fixed pitch 5.73 pt).

### Conventions used on these pages

- Function listings: in this book comment lines and label lines are printed
  exdented one column (statements at column 6, `⍝` or label at column 5;
  the text on p044 says so explicitly). Kept as printed. The header `∇` is
  printed at column 4 and the closing `∇` at column 3–4; written at column 0
  per house style.
- Underscored letters are lower-cased (rule 3), also inside comments, to
  match p044 (same function, same printed underscores).
- Non-bold expressions set on their own indented line are in `apl` blocks,
  indented six columns like input. The rule display on p051 starts at the
  text margin and is written from column 0.
- Delta is written `Δ` (U+0394), as in volume 1 and p044; the lint does not
  accept `∆` (U+2206).

### p045 (PDF 53)

- Continuation of `CRTOVR` from p044 (lines [9]–[16]). Line [9]
  `CR← ⍝  your code goes here!`: "YOUR CODE GOES HERE" is underscored,
  lower-cased as on p044 line [7]; two blanks after `⍝` (measured).
  `tools/crop.sh 53 90 82 310 42 500 out.png`
- Line [13]: four blanks before each `∇` inside the quotes (measured:
  quote at column 10 and 32, `∇` at 15 and 37).
  `tools/crop.sh 53 90 122 310 12 700 out.png`

### p046 (PDF 54)

- Header: a thin underline is printed under `TO` of `CRTOVR` (also on p044);
  lower-cased to `CRtoVR` per rule 3, matching p044. Probably a typesetting
  defect, not part of the name.
  `tools/crop.sh 54 35 343 150 22 600 out.png`
- Line [6]: underlines under the L of LABELS, O of OR and C of COMMENTS
  (also on p044) → `lABELS oR cOMMENTS`, matching p044. Probably defects.
- Line [7]: short bars above the P of `ALP`, the `;` of `[;1]` and the `=`
  (directly under the [6] underlines). Overbars are not underscores; ignored.
  `tools/crop.sh 54 35 392 240 30 600 out.png`
- Line [3] `→(0∊⍴CR)↓a`: arrowhead is at the bottom (↓), compared side by
  side with the `↑` in line [11].
  `tools/crop.sh 54 225 368 30 13 1000 out.png`
- Line [5]: second alphabet and the delta after it are underscored →
  `abc…z⍙`; the first `Δ` is not underscored.
- Line [4]: comma of `LOCKED,` measured at column 16, single blanks.

### p047 (PDF 55)

- `HIST` line [8] `R←r,' *○⍟'[…]`: the second R carries a thin underline,
  so it is written `r` per rule 3. Suspected print defect: the bar sits
  directly above the high minus of line [9] (`M←¯4`), same column; the same
  ghost bar appears above the `¯` on p048 line [5]. The function as written
  would use an undefined `r`; intended is surely `R←R,…`.
  `tools/crop.sh 55 85 627 120 34 800 out.png`
- Line [8] third character in the string read `⍟` (circle with star; also
  the bar glyph in the p048 histogram), consistent with overlap of `*` and
  `○`.
- Line [9] `M←¯4+⍳M+5`: the `¯` looks detached from the 4 but measures at
  column 8, 4 at column 9: no blank.
- Line [10] `⍉` (circle with backslash).
- Heading "Origin 0 (See also the article ")ORIGIN 0".)": the system
  command is in bold APL font; written in backticks.

### p048 (PDF 56)

- Histogram rows: symbol counts and ⍟/○/* classes measured by ink density;
  they agree with the REV/EXP data on p047. Axis labels at columns 9/14/19/24.
  `tools/crop.sh 56 135 82 175 92 500 out.png`
- `ROMAN` line [5] `(0 4 2 2 ⊤R)`: a thin underline under the 0, directly
  above the `¯` of line [6] (same ghost-bar defect as p047). A digit cannot
  be lower-cased; written `0`.
  `tools/crop.sh 56 175 349 185 30 900 out.png`
- Line [4] `R← 0 16 …` and line [7] `R←, 1 0 0 ⍉R`: the blanks after `←`
  and `,` are measured, as are the blanks before both `⊤` in line [5] and
  around `↑` in line [6].
- Line [6] string read `'MCXI DLV '` (blank between I and D, trailing blank);
  the D measures a bit left of its column, so this is the least certain
  spacing on the page.
- Line [7]: the second `←` (in `R←(R≠' ')/R`) is broken in print (looks like
  `·-`); read `←`.
- `ROMAN 2507` output `MMDVII`: looks like `MMD VII` at a glance, but it
  measures as six contiguous columns.
- Prose: "order-of-magnitude" is garbled in print ("order-of-rnagnitude").
- Last display `PRECOMPUTEDΔOUTPUTS [POSSIBLEΔINPUTS ⍳ INPUT]`: blanks
  before `[`, around `⍳` measured.

### p049 (PDF 57)

- "BIT▮ATES" (ink blot on the D) in the DETAIL paragraph; read BITDATES.
- `UNIQ←(¯1↓1,SORTED≠1⌽SORTED)/SORTED`: ↓ (head down); the `¯` again looks
  detached but no blank measured.
- Range "1001-9999" set in the APL font; written as plain text.

### p050 (PDF 58)

- `DENSERANK` line [2] has an opening parenthesis that is closed on line [3]
  (a parenthetical comment spanning two comment lines); two blanks after
  `(LIKE:`.
- Output rows: numbers in 3-column fields (leading blank), measured.
- The second row's ranks agree with the scores.

### p051 (PDF 59)

- Rule display: IS, IF, OR, AND, ELSE are underscored → `is if or and else`.
  Two blanks between the parts (measured).
  `tools/crop.sh 59 80 410 280 66 700 out.png`
- In `(⍴⍴B)>⍴⍴A` (rule) and `(1∊⍴,A)` (Gardner/Penfield line) the A is
  printed bold; font slip, not transcribed.
- Inline `2 3 4 + 1 1 ⍴7`: justified prose spacing makes blanks uncertain;
  the gaps around `+` and before `⍴` equal the gaps between the numbers, the
  gap after `⍴` is smaller.
  `tools/crop.sh 59 80 395 200 10 900 out.png`
- Footnote table: Markdown needs a header row; "Group | Functions" is added
  (not printed). Logicals third/fourth glyphs are `⍲` `⍱`; "Tall" ones are
  `| ⌊ ⌈ !`.

### Lint objections overridden

- p050:39/40 "unbalanced brackets" / "closing bracket without opening":
  the parenthesis in the comment of [2] closes in [3], as printed.
- p051:32 "`~` before a digit": the glyph is a tilde (wave at mid height,
  logical not), `~1∊⍴,B`, not a high minus.

