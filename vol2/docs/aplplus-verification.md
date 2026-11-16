# Verification against APL\*PLUS/PC 4.1 (Volume 2)

The APL in `vol2/docs/collected-whizbangs.md` was run in STSC APL\*PLUS/PC
release 4.1 (1984) under DOSBox-X. Each disagreement became a *candidate*; no
candidate was applied until a separate reader, given only the transcribed text
and asked what the scan prints, had re-read it blind. Every page was also
proofread against the scan (section 2a).

Page numbers are the book's printed pages (PDF page = printed page + 8).
"Run" means the result of executing in APL\*PLUS/PC. "Scan" means the page
image or the word boxes in `vol2/build/text/bbox.tsv`.

## Summary

- **2 corrections that change the code** (section 1): p51, the
  Gardner/Penfield solution, `(⍴⍴A)↑⍴B` → `(⍴⍴A)↓⍴B`; and p47, *HIST* [8],
  `R←r,` → `R←R,`. Both were misreadings: the blind re-reading found the print
  agrees with the run.
- **Spacing**: the p39 displays of *MAT* and `COND⍀COND⌿MAT` have the leading
  blank column that both the run and the scan show (section 2); the
  proofreading found eight more layout and spacing slips (section 2a).
- **3 print errors**, where the code or output is wrong as printed and the
  text follows the print, with a note beside it (section 3): p8, p14, p37.
- 31 uncertain readings and suspicions from the transcribers' notes were
  tested. Execution decides 24 of them, all in favour of the transcription
  (or confirming the notes' suspicion of a print error) except p47 `r`. The
  other 7 cannot be decided by running (section 5).
- Interpreter differences: no `⎕GRP` and no component files; reversal along a
  nonexistent axis is an AXIS ERROR; error carets sit elsewhere; matrix
  column widths differ in two displays (section 6).
- With the corrections, every printed result that can be recomputed is
  reproduced, apart from the p8 print error and the spacing in section 6.

## 1. Corrections that change the code

**Resolved.** Both candidates below were then re-read in the scan by a reader who was given
only the transcribed line and asked what is printed, with no hint of the run result. Both were
transcription errors, and the print agrees with the run: p51 prints `(⍴⍴A)↓⍴B`, with the
arrowhead at the bottom, the same shape as the known `↓` on p49 and unlike the `↑` earlier on
p51; and on p47 the bar under the second `R` of line [8] is the high minus of `¯4` on line [9].
It is 4.25 pt wide, like the high minuses on p45 and p48, against 5.5–6 pt for a real underscore.
The same ghost explains the "underscored" `0` in *ROMAN* [5]. Both are corrected in
`vol2/src/pages`; the table records the run evidence.

These are CANDIDATES. The run shows only that the transcribed code is
inconsistent with its own text or results. It does not show what the book
prints.

| Page | Transcribed | Proposed | Run evidence | Alternative |
|---|---|---|---|---|
| 51 | `((~1∊⍴,B)/⍴B),(1∊⍴,B)/(⍴A),(1∊⍴,A)/(⍴⍴A)↑⍴B` | `…/(⍴⍴A)↓⍴B` (drop) | Compared with the actual `⍴A+B` and with the printed rule on 15 argument pairs. With `↑` it is wrong whenever both arguments are singletons: `A←1 1⍴5`, `B←7` gives `1 1 0 0` (should be `1 1`); `A←7`, `B←1 1⍴5` gives an empty vector (should be `1 1`); `A←1 1 1⍴5`, `B←1 1⍴7` gives `1 1 1 1 1 0`; `A←1⍴5`, `B←7` gives `1 0`. With `↓` all 15 agree with `⍴A+B` and with the rule. Both forms are 43 characters, as the text says (`⍴` of the string is 43). | The print really has `↑` and the published "record" solution is wrong for the both-singleton case, which the article itself raises ("Did your solution work for …"). Scan (not blind): at 144 dpi the glyph is a bold arrow, flat at the top and widest in its lower half, unlike the `↑` in the conformability line above it, which comes to a point at the top. My reading leans to `↓`. Re-read at 1200–2400 dpi (`WB_VOL=vol2 tools/crop.sh 59 338 489 28 24 2400 out.png`) next to the `↑` at `tools/crop.sh 59 247 355 28 24 2400 out.png`. |
| 47 | *HIST* [8] `R←r,' *○⍟'[2⊥REVEXP∘.>⍳M←⌈/,REVEXP]` | `R←R,' *○⍟'[…]` | As transcribed: `VALUE ERROR` on line [8] (`r` is undefined). With `R`: `1974 HIST REV,[0.5]EXP` reproduces the printed histogram, all seven rows and both axis rows, character for character. | The underline is really printed (scan, not blind: a short bar under the second `R`, directly above the `¯` of `M←¯4` on line [9]; the transcribers' notes call it a ghost bar, and the same defect sits under the `0` of ROMAN [5]). If the print is read as underscored, the book has a print error, not a different meaning: an underscored `R̲` would be an undefined name in the book's own system too. |

## 2. Other differences from the run (spacing etc.)

| Page | Transcribed | Run | Scan / assessment |
|---|---|---|---|
| 39 | *MAT* display `1 1 2 1 1 1 2 3 4 3` … (column 0) | ` 1 1 2 1 1 1 2 3 4 3` (leading blank, as for every other numeric matrix in the book) | Corrected in the source: a blind re-reading measured one leading blank column in all 12 rows of both displays. Word boxes: the matrix digits start at x≈106.7, while the vectors `19 27 30 19 18 29` and `0 1 1 0 0 1` on the same page start at x≈101.0, one column (5.75 pt) to the left. So the print has the leading blank. |
| 39 | `COND⍀COND⌿MAT` display (column 0) | Leading blank column | Corrected, as above. |
| 24 | `VEC,[¯0.5]⌽VEC` → ` 6  2  9  6 10  0` | `  6  2  9  6 10  0` (uniform width 3, so two leading blanks) | Not a candidate. Word boxes put the first column at column 1 (x=148.5; column 0 is at 143.5), so the transcription matches the print. The print's first column is one narrower than the rest. Elsewhere the book uses the uniform width (p19 `GRM,[0.5] ROW` `  6 13 14 …`, p26 `   0  10 …`, p30 `   617 …`), so this is a print inconsistency or a display rule of the mainframe system. |
| 43 | `2⍕CUM,[0.5] TRANS` → ` 400.00  300.00 …` | `  400.00  300.00 …` (all columns 8 wide) | Not a candidate. Same pattern as p24: the input line starts at x=163.6 (column 6), so `400.00` begins in column 1, as transcribed. The other four columns are 8 wide in both. |
| 24 | Histogram `' ⎕'[VEC∘.>⍳⌈/VEC]`: five rows | Six rows; the sixth (for the element 0) is all blank | Consistent with the print (the notes say the empty row is invisible). |

## 2a. Proofreading against the scan

The prose was compared word by word with two OCR passes (the archive.org text
layer and Tesseract); every disagreement was OCR noise. Four readers then
checked every page against the scan: prose, inline code, code blocks glyph by
glyph, column positions measured against the fixed pitch, tables and figures.
Corrected in `vol2/src/pages`:

| Page | Was | Print |
|---|---|---|
| 4 | margin note "Equivalent to A∊VEC" | "Equivalent to A∊VEC." |
| 8 | `C←'  SO BE IT IF   WE DO  AS IN TV   '` | two trailing blanks, not three |
| 10 | margin note at column 39 | column 37 |
| 15 | `S←DATES[⍋ 0 ¯12 31⊥⍉DATES;]` | `31 ⊥⍉DATES`, as in the line above; the "mark" in the gap is the `¯` of the next line |
| 18 | boxed derivation with two blanks around `≤` and `=` | one blank on each side |
| 23 | right-hand column of the primitives table at column 34 | column 33 |
| 39 | matrix displays at column 0 | one leading blank column (section 2) |
| 40 | `INDEX ERROR` caret at column 45 | column 44, under the first S of `SSEC` |
| 47 | *HIST* [8] `R←r,` | `R←R,` (section 1) |
| 51 | `(⍴⍴A)↑⍴B` | `(⍴⍴A)↓⍴B` (section 1) |

Kept as a convention: the book sets `↔` two cells wide (pp 6, 15, 33, 42);
the transcription gives it one cell. Notes printed beside code in the text
font are placed approximately, since that font is proportional. The header row
of the p51 footnote table is not printed; Markdown needs one.

## 3. Print errors (the code or output is wrong as printed)

| Page | As printed (and transcribed) | Problem | Evidence |
|---|---|---|---|
| 8 | `(~C ⎕SS '  ')/C` → `SO BE IT IF WE DO AS IN TV` at column 0 | The result must begin with a blank. Removing the first blank of each overlapping pair leaves one leading blank (and one trailing blank). | Run: ` SO BE IT IF WE DO AS IN TV ` (28 characters). Its first character is a blank with 1, 2 or 3 leading blanks in `C`, so the uncertain blank count in `C` does not matter. Scan (not blind): `SO` at x=151.0, the same as column 0 of the `0 1 0 …` result above. The print dropped the blank. |
| 14 | `MAT[⍋(⌈⌿MAT)⊥⍉MAT;]` | With the column maxima as radix, a value equal to its column maximum overflows, so rows are not uniquely represented (as the notes suspect). The text describes `1+⌈⌿MAT`. | On *DATES* it happens to give the right order. On `4 2⍴2 0 1 2 1 1 0 2` the keys are `4 4 3 2` and the rows come out `0 2 / 1 1 / 2 0 / 1 2`; *INDSORT* and `(1+⌈⌿MAT)⊥` give `… 1 2 / 2 0`. |
| 37 | `24 80 ⍴ 1 3 2 4 ⍉ 4 5 6 16 ⍴((×/ 4 5). 6 16)↑TEN` (period) | SYNTAX ERROR. | The p35 form with a comma reproduces Figure 3 exactly. |

## 4. Underscored names

The volume 2 transcription already writes underscored letters in lowercase,
and they were run as transcribed: labels `a`, `b`, `c`, the global collating
sequence `cs` (also as the left argument of *CINDSORT* and *CMSORT*), the
p26 labels `s v m a` and `a l v f x`, *CRtoVR*, and the underscored alphabet
and `⍙` in *CRtoVR* [5]. In APL\*PLUS/PC, `⎕AV` code 241 is accepted as a
name character, so it was used for `⍙`. *CRtoVR* then handles a test
function named `ab⍙Q` with label `ab⍙:` correctly. No name collisions arise.
The only lowercase letter that breaks code is `r` in *HIST* [8] (section 1).

## 5. Uncertain readings in the transcribers' notes, tested

| Note | Reading | Result |
|---|---|---|
| p8 | Printed result lacks the leading blank | Confirmed as a print error (section 3). The ±1 uncertainty in `C`'s blanks is not visible in the result. |
| p12 | *AFBG* [5] `(⍴TOKEEP)↑'TOGO←⎕NL 3'`, arrow blurred, read `↑` | Supports `↑`. With `↑`, *AFBG* returns exactly what *ALLFNSBUTGRP* returns (three groups tried). With `↓`: LENGTH ERROR in the lamination. |
| p14 | `(⌈⌿MAT)⊥` suspected wrong | Confirmed (section 3). |
| p15 | Blotted first digit of `0 12 31` and `0 ¯12 31` read as 0 | Not decidable. The first element of the radix does not affect the result, so any digit reproduces `736157 …` and the sort. |
| p18 | *CMSORT* [4] `→COL↓b`, arrowhead judged low | Supports `↓`. With `↑` the function returns *WEST* unsorted. |
| p18 | *ROWSORT* `''⍴⍴R←MAT`, quotes adjacent | Works. |
| p21 | *CSORTRX* [3] `⊖[,A] cs`: "axis ¯1 would be an error" | In APL\*PLUS/PC, `1 CSORTRX WEST` reproduces the p20 result, but `¯1 CSORTRX` is an AXIS ERROR (`⊖[,¯1]` on a vector). If a nonexistent axis is taken as identity (as the volume 1 report found for the mainframe `⌽[K]`), `¯1` gives a correct *descending* row sort. So `A=¯1` plausibly selects descending order. Interpreter difference (section 6), not a reading problem. `⊖` and `⌽` cannot be told apart by execution here. |
| p21 | Stray mark under the `1` of `1↑cs[]` | Not decidable; `1` works (the line is the implicit type check; a numeric argument gives DOMAIN ERROR there, as the text says). |
| p24 | `10 ¯10[1]`, first glyph a damaged `1`, not `⍳` | Supports `1`. `10 ¯10[1]` gives 10 and ¯10 in origins 1 and 0; `10 ¯10[⍳1]` gives 10 in origin 0. It is also the stated 9 characters. |
| p25 | `VEC←⎕IO↓0,VEC` read as `↓` | Supports `↓`. `⎕IO↑0,VEC` has one element. |
| p27 | Input `'!'` or `'''` | Supports a valid character constant such as `'!'`. `'''` is not a well-formed constant (`⍎` of it is an error), so it would not reach line [3]. With `I←,'!'`, line [3] gives DOMAIN ERROR. |
| p27 | Caret under `=` (column 28) | Not decidable: APL\*PLUS/PC puts it under `⌊` (column 29), the primitive that fails. |
| p28 | `B≤.≥(⌈B),2* 0 31` and `E≤.≥(⌈E), ¯2 2 *31` "inconsistent in form" | Both are valid and do what the text says (integer in range: tie number 1 to `¯1+2*31`, index in signed 32-bit range); tested on 16 values. The spacing does not affect execution. |
| p30 | Overbars on *NMGU* [2] ignored | The function as transcribed reproduces both printed results. |
| p37 | Period instead of comma | SYNTAX ERROR (section 3). |
| p38 | LENGTH ERROR caret at column 15 | Not decidable: APL\*PLUS/PC puts it under `\` (column 16). |
| p39 | `0 0 360 360 0` blot | Supports 0. |
| p40 | `⎕FMT` delimiters read `⍞` | Not decidable: `⍞` and `⎕` give identical output. The blank before `NOT` is decided. `' NOT FOUND: '` plus `LI6` is 18 wide, the width of *RPT*; without the blank the assignment `RPT[N;]←` would fail. |
| p40 | `LN≠¯1↓0,LN` drop arrows | Supports `↓`. *VRSELECT* reproduces the printed output, and the [5] variant `PV←PV\LN≠¯1↓0,LN` gives identical results for three selections. |
| p41 | *VTOM* `1↑V`, `1↓(INDS-1)` | Supports both: `5 6` and the printed matrix. |
| p43 | `TRANS←CUM-¯1↓0,CUM`, arrow poorly printed | Supports `↓`: identical to the rotate form. |
| p43 | Spaces in the `'|',CV,'|'` display | Consistent: *CLEAN* comes out as printed with both methods. |
| p45 | *CRtoVR* [13] four blanks before each `∇` | Supports four. *CRtoVR* output is identical (`≡`) to `⎕VR` for *CRtoVR*, *VTOM*, *VRSELECT* and a test function with labels and comments. |
| p46 | *CRtoVR* [3] `→(0∊⍴CR)↓a` | Supports `↓`. With `↑` the logic is inverted: the error message is printed for an existing function. |
| p47 | *HIST* [8] `r` | See section 1. |
| p47 | Third string character `⍟` | Supports `⍟`: the histogram reproduces with `⍟`/`○`/`*`. |
| p47 | `M←¯4+⍳M+5`, no blank | Works. The axis labels fall at columns 9/14/19/24 as printed. |
| p48 | ROMAN [6] `'MCXI DLV '`, least certain spacing | The trailing blank is decided: without it (`'MCXI DLV'`) 3999, 1990 and 49 come out `MMMCCXXII MCCXX XLII` instead of `MMMCMXCIX MCMXC XLIX`. The blank between `I` and `D` is fixed by the printed `MCDXLIV`/`MDCLXVI` (it puts `D` in column 1 of the fives row). |
| p48 | `ROMAN 2507` = `MMDVII` (contiguous) | Run: `MMDVII` (six characters). |
| p49 | `¯1↓1,SORTED≠1⌽SORTED` | Supports `↓`. |
| p51 | `~1∊⍴,B` (tilde, not `¯`) | Supports `~`. |

## 6. Interpreter differences

These are not transcription problems.

- `⎕GRP` does not exist (SYNTAX ERROR). *ALLFNSBUTGRP* and *AFBG* were run
  with a function `GRP` that returns the named variable, a matrix of names.
- No component file system: `⎕FCREATE` is a VALUE ERROR and `⎕FAPPEND` hung
  the interpreter. `⎕FNUMS` returns an empty vector. The p10 tie-number
  expressions were run on stand-in vectors, the p25 loops with a stand-in
  for `⎕FREAD`, and of the p28 tests only those that do not touch files.
- Reversal or rotation along a nonexistent axis is an AXIS ERROR
  (`⊖[,¯1]`, `⊖[,2]` on a vector), so `¯1 CSORTRX` fails (section 5).
- Error classification: p7 `BM/⍳⍴BM` is printed as RANK ERROR. In
  APL\*PLUS/PC, `⍳⍴BM` (monadic iota of a 2-element vector) fails first with
  LENGTH ERROR; `BM/⍳7` alone is a RANK ERROR.
- Error carets: APL\*PLUS/PC puts the caret under the failing primitive. The
  book has it at column 6 (start of the statement) for `NAMES∧.=SEV` (p3),
  `NAMES⍳'GRAZULIS'` and `BM⍳1` (p7). It is one column left on p27 and p38,
  and under the `S` of `SSEC` (column 45) on p40, where the run puts it under
  the `I` of `SSEC[I]`. p16 `LET[⍋LET]` agrees (under `⍋`).
- `⎕VR` has the book's layout (labels and comments exdented) but ends with a
  newline after the closing `∇`. *VRSELECT*'s `¯6↓` then leaves a newline and
  a blank instead of a bare newline; the visible output is the same, and it
  was also run on `¯1↓⎕VR` with identical results.
- Numeric matrix display uses one uniform column width. Two printed displays
  (p24, p43) make the first column one narrower (section 2).
- `⍕` of a matrix includes the leading blank column. The harness displays
  results with `⍕`, so transcript matrices show it; it agrees with the book's
  numeric matrices except as noted in section 2.

## 7. Verified as transcribed

Every expression listed reproduces its printed result, including column
spacing unless noted.

- **p2:** all six `1403` examples.
- **p3:** *NAMES*, *SEV*, `'JAKOBY'∊NAMES` (`0 1 0 0 1 0`), `L`, both
  JAKOBY searches, GRAZULIS, SMITH; `NAMES∧.=SEV` is a LENGTH ERROR;
  `∨/A∘.=,B` equals `A∊B`.
- **p4:** the conformability rule `CC←(¯1↑⍴1/A),1↑⍴1/B ⋄ 1∊CC,=/CC`
  (6 cases) and the result shape `(¯1↓⍴A),1↓⍴B`; `⍴⍉SEV`;
  `NAMES∧.=⍉SEV` (leading blank as printed); `∨⌿`; `SEV∧.=⍉NAMES`; `∨/`;
  `∨/A∘.=VEC` equals `A∊VEC`; `∨/A∧.=⍉MAT`.
- **pp 5–7:** every *VEC*/*SCAL* result, including the not-found cases
  (`0`, empty, `7`); both dyadic-iota emulations for vectors and the
  vector-in-matrix emulations (`3 8 5`); `NAMES⍳…` and `BM⍳1` are RANK
  ERRORs; *BV*, *BM*.
- **p8:** the three `⎕SS` results; blank squeezing apart from the print
  error in section 3.
- **pp 9–11:** NEWREGCODES (both), TIENO (all three forms, on stand-in
  vectors), `VEC[INDS]` (TELL/BELT), both "all but" selections (US),
  BEETLE, *ALLBUT*, EE, BATTLE, 1033, 16347, ¯37, `(2*N)|¯37`.
- **p12:** *ALLFNSBUTGRP* and *AFBG* agree (with `GRP` for `⎕GRP`).
- **pp 13–15:** `⍋VEC`, `VEC[INDS]`, *DATES*, `DATES[⍋DATES[;1];]`,
  *DATASORT* = *INDSORT* and the sorted display, `100⊥⍉DATES`,
  `0 12 31 ⊥⍉DATES`, the three descending-year sorts (`1` and the display),
  and `R←M,0 ⋄ R←M[⍋+⌿R<.-⍉R;]` (on *DATES* and on a 6×4 matrix).
- **pp 16–17:** DOMAIN ERROR for `LET[⍋LET]`, `cs⍳LET`, ABCDEEFK, the
  three *HAND* sorts, the *cs* display, *CINDSORT* and the base-value sort
  on *WEST*.
- **pp 18–20:** `⍴cs` 39 and *MNOC* 10 (and the boxed inequality: `39⊥10⍴38`
  is below `2*56`, `39⊥11⍴38` is not), *CMSORT* (also with `2*31`, and on
  a 12-row matrix that includes INDIVIDUALIST/INDIVIDUALISM, agreeing with
  *CINDSORT*), *ROWSORT* (and on a 0×6 matrix), *L* and its three
  rearrangements, `A⍴L`, `GRM,[0.5] ROW` (widths as printed), `A⍴(,M)[…]`,
  *NSORTROW*, the p20 *cs* display and *CSORTROW WEST* (right-justified as
  printed).
- **pp 21–22:** `1 CSORTRX WEST` (identical to *CSORTROW*), *CSORTRX* on a
  vector and its DOMAIN ERROR for numeric data, `⌈2⍟⍴cs` (5), and the radix
  sort by `BR` and `CHR←CHR[T←⍋BR[N;]] ⋄ BR←BR[;T]` (sorts WASHINGTON).
- **pp 23–24:** `⍳10` in origin 0; all five 10/¯10 expressions in both
  origins, with their character counts; `→LABEL×⍳C` versus `⌈⍳`; `VEC⍳`
  (`5 1 6 0 2`); `⎕IO+⍴VEC` and `¯1↑⍳1+⍴VEC`; `+/⍳N` = `2!N` in origin 0;
  the lamination (values; spacing in section 2); `(L1,L2)[D>⍴VEC]`; the
  histogram.
- **p25:** both *INP* splits (`1`), `VEC[4 6 3]` with both prefixes in both
  origins (`2 21 12`), the three counter/limit loops (origin 1, origin 0,
  either origin), each filling every element.
- **p26:** *M* and *N* displays, `15 10 25 6`, `150 100 250 60`, the February
  expression and its alternative, the rank branch, `⎕ELX←'⎕ERROR(⎕DM⍳⎕TCNL)⍴⎕DM'`
  (first line only in origin 0; one extra character in origin 1), both
  inverse scattered-point expressions, `→⍳∨/V ⎕SS 'END'`.
- **pp 27–29:** line [3] gives DOMAIN ERROR for character input; both
  versions of line [1] and of line [3] agree on 6 and 9 test inputs; the
  non-file `⎕ERROR` tests; `B← 0 1 0 0 0 0 0 0 0 1 0 /F[], 4 0` gives
  `F[2],4` and RANK/DOMAIN/LENGTH ERROR for matrix or scalar, character and
  8-element *F*, as listed; `(FI)[F[9]]` gives DOMAIN/INDEX/RANK ERROR as
  listed; `⎕ELX←'⎕ERROR(∧\⎕DM≠⎕TCNL)/⎕DM'`.
- **pp 30–32:** the *MAT* display, `NMGU MAT` (`5 3 7 2 6 1 4`),
  `MAT[NMGU MAT;]`. *NMGRUP* and *NMGRADEUP* agree with *NMGU* on the printed
  *MAT*, on 40×4 and 30×3 matrices with many duplicates, on `5 100⍴⍳100`,
  and on 1×3, 3×1, 4×0, 0×3 and all-equal matrices.
- **pp 33–37:** both SCALARS forms; `⍴MAT` 117 16. Figure 2, computed by
  `24 80 ⍴ 2 1 3 ⍉ 5 24 16 ⍴((×/ 24 5),16)↑MAT` from the *MAT* that
  Figure 1 implies, is identical to the transcribed Figure 2 (24 rows). The
  VECTORS ACROSS form reproduces Figure 1. `⍴TEN` is 18 6 16. Figure 4,
  computed from the *TEN* implied by Figure 3, is identical to the
  transcribed Figure 4, and Figure 3 is reproduced by its own expression.
- **pp 38–39:** both expansion examples (`AN TE PEN  UL  TI MATE` with its
  blanks), the LENGTH ERROR, the axis-expansion rules, `APL\360`, `B/B\A`,
  `B\B/A` = `B×A`, `+/MAT`, *COND*, `COND⍀COND⌿MAT` (equal to the
  multiplication form), the `⎕FMT (ENOS;ENAS;SSEC)` table character for
  character.
- **p40:** the INDEX ERROR, the expanded *RPT* (with its blank rows), the
  NOT FOUND rows, *VRSELECT* `0 4 5` output, and the alternative line [5].
- **p41:** *VTOM* (`5 6` and the matrix; also `'/'` and `'//AB/'`).
- **pp 42–44:** RESPECT/SPECTRE/TRESPEC, HEIGHT, both canonical-form
  identities, `53 ¯7`, *TRANS* (both forms), the `2⍕` values (spacing in
  section 2), both *CLEAN* forms and the bar displays, both *B* marks,
  GERMAN/VESSEL/OUTPUT (also `3 3 3⌽`), ESPRIT/CENTRE/OUTLAY/LISTEN, *CM*,
  `7 3 9 0`, the left-justified display.
- **pp 44–46:** *CRtoVR* (see section 5).
- **pp 47–48:** *HIST* with `R` (section 1); *ROMAN* 1444, 1666, 2507, 3888
  (also 3999, 1990, 49, 0); `1 0 0⍉R` = `⍉0 1 1⍉R`; `(⍟⍳15)[V]` = `⍟V`.
- **pp 49–50:** the three UNIQ techniques agree; fast epsilon equals `A∊B`;
  `IP[PV]←IP` equals `⍋PV` and `PV⍳⍳⍴PV`; `R[⍋V]←R` equals `⍋⍋V` and
  `(⍋V)⍳⍳⍴V`; `RESULT[GV]←RESULT` equals `RESULT[⍋GV]`; *DENSERANK*
  *GOLFSCORES* (display as printed); `A[]` (RANK ERROR for a matrix and a
  scalar), `(1/A)[]`, `A['';'']`; the demotion statements preserve *A*.
- **p51:** the conformability expression agrees with whether `A+B` fails, on
  15 pairs; the printed `⍴A+B` rule agrees with the actual shape on all 15;
  `2 3 4 + 1 1 ⍴7` has shape 3; 21 scalar dyadic functions (4+3+4+6+4).

## 8. Not checked

- p9 `5↓⍳⌊/⍳0` and `API←⍳⌊/⍳0` (the point is that they are impractical).
- p11 `⎕FSTAC` codes beyond the arithmetic; p17 `UTILHOW 'CSORTR'`
  (workspace not available).
- p27 the input loop itself. `⎕` input cannot be fed through the harness, so
  the conditions were tested on assigned values instead.
- p28 the `⎕FAVAIL`, `⎕FNUMS`, `⎕FSIZE` and `⎕FREAD` tests and the `⎕FREAD`
  half of the implicit check (no component file system).
- p23 the table of origin-sensitive primitives (a schematic, not code), and
  `→(L1,L2)[…]`-style branches beyond computing their targets.
- Costs and timings (p15 percentages were checked as arithmetic only; p49
  dollar figures; p50 "almost twice as fast").
- Workspace 444 *LABELS*, 6 *SORT*, 6 *DATES* and *BITDATES*.

## 9. Method

The harness is in `~/work/aplplus/harness`. `tools/wbrun.py SPEC` writes the
statements to a file, starts APL\*PLUS/PC in a background DOSBox-X and prints
what APL wrote back, in about 15 seconds; specs were run one at a time. The
volume 2 specs are in `harness/wb/spec` and are run through the wrapper
`v2run.py`, which adds `⍙` (`⎕AV` code 241) to the encoder and otherwise
calls `wbrun.py` unchanged:
`python3 ~/work/aplplus/harness/wb/spec/v2run.py SPEC`.

| Spec | Pages |
|---|---|
| `v2-probe.txt` | Name characters (finding `⍙`), `⎕VR`/`⎕CR`/`⎕FMT` behaviour |
| `v2-probe2.txt` | `⎕GRP`, component files (times out at `⎕FAPPEND`) |
| `v2-probe3.txt` | *AFBG*/`⎕FX` with valid groups |
| `v2-a.txt` | 2–12 |
| `v2-b.txt` | 13–22 (sorts, *CSORTRX*, `⊖[,A]`) |
| `v2-c.txt` | 15 and 21–29 (origin 0, error checking) |
| `v2-d.txt` | 30–37 (grade functions, Figures 1–4, generated from the transcription) |
| `v2-e.txt` | 38–46 |
| `v2-f.txt` | 47–51, plus reruns of p15, p25 and p38 with corrected test data |
| `v2-g.txt` | Discriminating checks: ROMAN string, alternative arrows in *CMSORT*/*CRtoVR*, p7 error type, `10 ¯10[⍳1]`, p8 blank counts |

Origin-0 examples were run inside functions with `⎕IO` localised, because the
harness must stay in origin 1. Underscored names were used in lowercase as
transcribed. Where the transcription and an alternative reading differ, the
specs contain both forms. Scan positions come from `vol2/build/text/bbox.tsv`
(pitch 5.75 pt) and from crops made with `WB_VOL=vol2 tools/crop.sh`; none of
these readings were blind.
