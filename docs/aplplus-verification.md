# Verification against APL\*PLUS/PC 4.1

The APL in `collected-whizbangs.md` was run in STSC APL\*PLUS/PC release 4.1
(1984) under DOSBox-X, and every disagreement was then checked against the
scan (`build/pages/NNN.png`). Nothing in the Markdown or in `src/pages` has
been changed; this file only records findings.

Page numbers are the booklet's printed pages. "Scan" means I looked at the
page image; "Run" means the result of executing in APL\*PLUS/PC.

## Summary

- 25 places where the Markdown differs from the print, most of them changing
  what the code does. Sections 1 and 2.
- One systematic problem: underscored names are transcribed as plain letters,
  which makes five functions wrong as written. Section 3.
- 12 statements in `transcription-notes.md` that execution shows to be wrong
  (code flagged as a probable typesetting slip that is in fact correct, or
  the reverse). Section 4.
- Differences that come from the interpreter being a 1984 PC version rather
  than the 1975–78 mainframe system. Section 5.
- With the corrections in section 1 applied, every printed result that can be
  recomputed is reproduced exactly, apart from the one print omission noted
  in section 5.

## 1. Transcription errors that change the code

Each row was confirmed in the scan unless the last column says otherwise.

The p18 branch arrows were first "confirmed" here as take (`↑`) and turned out
to be drop (`↓`) in the print: the reading had been steered by what runs. So
every correction in sections 1–3 was re-read in the scan by readers who were
given only the original transcription and its location, not the correction or
the reasoning behind it, and who zoomed to 1200–2400 dpi on easily confused
glyphs. All other corrections agree with what the print shows. That
re-reading also found that labels are outdented one column (two spaces after
the line number) and that p35 prints a space after the first `⌿`; both are
now in the corrected copy.

| Page | Markdown | Print | Run |
|---|---|---|---|
| 2 | `3 3⍳19` (three times) | `3 3⍴⍳9` | As transcribed: AXIS ERROR. Corrected: the three printed results. |
| 4 | REPORT [4] `⍋RA⊥ALP⍳NAMES` | `⍋RA⊥ALP⍳⍉NAMES` | Without `⍉`: INDEX ERROR in REPORT. With it: the printed report. |
| 5 | `⎕←CODED←RA⊥ALP⍳NAMES` | `⎕←CODED←RA⊥ALP⍳⍉NAMES` | Without `⍉`: 17 numbers near 1E12. With it and `⎕PP←3`: exactly `2.09E24 3.02E24 8.95E23 3.59E24 7.67E23 6.62E23 2.32E24 2.62E24 1.52E24`. |
| 6 | `F←'G⎕  T[9;9;9] ⎕'` | `F←'G⍞ T[9;9;9] ⍞'` (one space) | Two spaces give 11-wide fields. One space gives the printed 10-wide `T[2;3;1]  T[2;3;2] …`. |
| 10 | SPS [10] `C←1↑1⍳1` | `C←''⍳1` | As transcribed: RANK ERROR (dyadic `⍳` with a scalar left argument). |
| 10 | SPS [11] `(1⌽1⍴⍴⍴B)⌽B` | `(1⌽⍳⍴⍴B)⍉B` | With the print's line, all p11 SPS results are reproduced. |
| 10 | SPA [5], [6]: same two readings | `C←''⍳1` and `(1⌽⍳⍴⍴B)⍉B`, as in SPS | With `''⍳1` and `(1⌽⍳⍴⍴B)⍉B`, all three printed SPA matrices are reproduced. |
| 16 | GRADE [2] `COL←COL-¯IO` | `COL←COL-~IO` | `¯IO`: SYNTAX ERROR. `~IO`: grades a 30×3 matrix correctly, and returns `⍳5` for a 5×0 matrix. |
| 18 | `→(condition)→LABEL`, `→(⍴vector)→LABEL` | `→(condition)↓LABEL`, `→(⍴vector)↓LABEL` (arrowhead at the bottom, checked at 2400 dpi) | `→(1)→5` is a SYNTAX ERROR. An earlier pass read these as take (`↑`), assuming they repeat the left column; the print has drop, which branches when the condition is 0 or the vector is empty, the counterpart of `→LABEL×~condition` in the same column. |
| 19 | THISL `R←1↑1↑⎕LC` | `R←1↑1↓⎕LC` | Two takes: `→THISL IF …` loops forever. Take of drop: correct. |
| 21 | SS1 [2] `((⍳D)-1)⊖` | `((⍳D)-⍳1)⊖` | Same result in origin 1. In origin 0 the `-1` form is off by one (`1 20 40 52` for `0 19 39 51`). |
| 21 | SS1 [4] `((⍳D)-1)⌽` | `((⍳D)-⍳1)⌽` | As above. |
| 21 | SS2 [4] `((⍳D)-1)⌽` | `((⍳D)-⍳1)⌽` | As above. |
| 22 | SS3 [5] `(¯1↑⍳1)↓⍳D` | `(¯1*⍳1)↓⍳D` | Take: SS3 returns an empty result for `'THE'` and `'MATRIX'`. Power: correct in both origins. |
| 22 | SS4 ends at line [7] | Line [8] exists: `R←(A[R∘.+G-⍳1]∧.=B[G])/R` | Without it SS4 returns unfiltered candidates. With it SS4 agrees with the others. |
| 30 | `(1,⍴A)⍴∘≠C⌽A,[0.5] B` | `(1,⍴A)⍴*⌿C⊖A,[0.5] B` | As transcribed: LENGTH ERROR. Print: `5 6 7 8 9 16 25 27 32 36 49 64 81`. |
| 32 | `(N⍴0)↑SCALAR` | `(N⍴0)↓SCALAR` | `⍴(3⍴0)↑7` is `0 0 0` (empty). `⍴(3⍴0)↓7` is `1 1 1`, the rank-N singleton the text describes. |
| 34 | `1 1 0 0 1 /A` | `1 1 0 0 1 ⌿A` | `/`: LENGTH ERROR (A is 5×9). `⌿`: the printed three rows. |
| 35 | `0 1 1 0 0 /0 0 0 1 1 1 1 0 0 /A` | First slash is `⌿` | `/`: LENGTH ERROR. `⌿`: `24 25 26 27` / `34 35 36 37`. |
| 35 | `B/A[; 5 4 7 6]` | `B⌿A[; 5 4 7 6]` | `/`: LENGTH ERROR for a 5-element `B`. `⌿`: same result as the subscription form above it. |
| 40 | ΔSS [2] `(C,R×R)⍴A` | `(C,R+×R)⍴A` | `R×R`: all zeros. `R+×R`: identical to `⎕SS`, and safe for an empty target. |

The prose on p22 repeats the SS3 construct ("The `(¯1↑⍳1)↓⍳D` construct
cleverly accounts for the index origin"). The scan reads `(¯1*⍳1)↓⍳D`, as in
line [5].

## 2. Other differences from the print

| Page | Markdown | Print |
|---|---|---|
| 3 | After `V←?10⍴99 ⋄ V2←V[GV←⍒V] ⋄ ∧/V2=⌊\V2` the three rows follow directly | The result line `1` and a second input line `V,[1] GV,[0.5] V2` come first. Two lines are missing. |
| 5 | Report rows have five spaces before the rank (`641     8`) | Run gives four (`641    8`) for `X2,I3`; the digit sits under the `N` of `RANK`. |
| 10 | Tens row `      1111111222222222333333444555555` (37 characters) | Run gives `      111111112222222233333344445555555` (39): 6 blanks, 8 ones, 8 twos, 6 threes, 4 fours, 7 fives. The scan agrees. |
| 11 | `1 1  1 6` … under `5 0 2 0 ⍕ROWS,COLS`; `1  6` … under `7 0 ⍕…` | Column widths are as the format says: `    1 1    1 6` and `      1      6`. Whitespace was collapsed. |
| 12 | `760714  a BASTILLE DAY` | `760714 ⍝ BASTILLE DAY`: the same lamp as elsewhere. |
| 6, 12, 13, 29, 33 | `⎕` as the text delimiter inside `⎕FMT` strings | `⍞` (quote-quad), a different glyph from the `⎕` of `⎕FMT`. Both delimiters work in APL\*PLUS/PC and give identical output. |
| 15 | `R←(VEC≠0)/MAT[;2 3 4]` and `R←TEMP1/TEMP2` | Both are `⌿`. Scan only; my test data for this line was faulty, so it was not run meaningfully. |
| 30 | "(e.g., `A÷B` or `A-B`)" | "(e.g., `A+B` or `A-B`)" |
| 38 | `CASHFLOW2` (header, prose and call) | `CASHFLO2` throughout |
| 39 | `'RATRIX'` | `'RATMIX'`, as on p24 |
| 10–11 | "A few examples should show the power of *SPS*:" twice, the display of `M` at the top of p11, and no example after it | The sentence once, at the foot of p10, followed by `⎕←M←5 7⍴⍳35` and `M SPS 5 2⍴1 1,1 4,2 2,3 2,4 4` → `1 4 9 16 25` (reproduced). p11 begins with `M SPS 2,[1.5]⍳5`. |
| 10 | SPA [1] `SCATTERED-POINT ASSIGNMENT` | Underscored initials, as in SPS: `sCATTERED-pOINT aSSIGNMENT` |
| 26 | `∇FOR[¯3]∇` | `∇FOR[~3]∇`: a tilde at x-height, like p18's `~`, not a high minus. Not run. |
| 24, 39 | Last table row `'⍺∈⍳○∪⍴¯⍵'` | `'⍺∈⍳○∪⍴~⍵'`: the same tilde. The timing digits on both tables, and on p20, match the scan. |

## 2a. Proofreading of prose and tables

The prose was compared word by word with two independent OCR passes (the
Acrobat layer and Tesseract run on each half page); every disagreement was OCR
noise. Every page was then read against the scan for inline code, punctuation,
paragraphing and emphasis, and the tables on pp 1, 8, 20, 24, 28–30 and 39 were
checked cell by cell. Corrections, all in `tools/mkcorrected.py`:

| Page | Markdown | Print |
|---|---|---|
| 11 | No blank line between `ROWS←…` and `5 0 2 0 ⍕ROWS,COLS` | A blank line |
| 12 | `⌊TS÷5184000` as a separate block | Inline in the sentence |
| 18 | `[L1;L2;L3;...]`, `[A;B;C;...]` | `{L1;L2;L3;...}`, `{a;b;c;...}` (braces; *A*, *B*, *C* underscored) |
| 19 | *IF* body without a line number | `[1]   R←B/A` |
| 22, 25 | Three extra paragraph breaks | Continuations of the preceding paragraph |
| 24 | "gains in CPU efficiency" | "CRU" (STSC's billing unit; cf. MILLICRUS, p37) |
| 24, 39 | "(Executed …)" notes in code blocks | Prose |
| 32 | `(((⍴A),1)⍴A)∘.+(1,⍴B)⍴B` where `∘` can be … | `o.+`, "where o can be any scalar dyadic function": a letter o as a placeholder, making it an inner product |
| 39 | "string-searching techniques" | "string-search techniques" |
| 39 | *WS FULLS* | *WS FULL*s |

Underlined words for emphasis (written in italics) were added, removed or moved
on pp 1, 3, 4, 5, 6, 8, 15, 21, 22, 30, 40, 41 and 42 to match the print.
Not changed: the letterhead at the top of the Note to Readers (the same
address appears on the cover), the session-style layout of the Boolean examples
on p28 (rendered as a table), the label *(0,MILLICRUS,MILLISECONDS,0)* that sits
beside its result on p37, and the underlined "or"s on p18.

## 3. Underscored names

The booklet uses underscored letters as separate identifiers. The Markdown
drops the underscore, so the names collide with plain ones:

- **Labels that become argument names.** COMPRESS (label `A̲`, argument `A`),
  SS3–SS6 (labels `A̲`, `B̲`, `C̲`; arguments `A`, `B` and local `C`), GRADE,
  FOR, ITERATE2–4, CASHFLO2. In COMPRESS and SS3–SS6 the bare form is
  ambiguous or wrong: `→B⌊A+D` reads as arithmetic on the strings.
- **TIMES (p27).** Every name except `RUN` is underscored in print:
  `R̲←A̲ TIMES B̲;C̲;D̲;RUN`. That is what keeps them clear of the timed
  expression. Run with bare names: `5 TIMES 'R←V⌹M'` fails with LENGTH ERROR
  on line [4] because the expression overwrites the local `R`, and
  `5 TIMES ALG1` fails because `A` is the iteration count. With distinct
  names it works.
- **Smaller cases.** `N̲` on p7 (`N̲←⍴⍴A`, `(N̲⍴1)⍉A[…;VN̲]`); the REPORT
  heading on p4 line [5], which is underscored letters and not letters
  followed by underscores; `S̲CATTERED-P̲OINT S̲ELECTION` in the SPS comment.

APL\*PLUS/PC represents the underscored alphabet as lowercase, and that is
what I used to run these functions (`a:`, `→b⌊a+D`, `r←a TIMES b;c;d;RUN`).
Lowercase or a combining underline would both keep the code correct.

## 4. Claims in `transcription-notes.md` that execution contradicts

| Note | Claim | Result |
|---|---|---|
| p1 | `R←((¯1+(¯1=⌽A)⊥1)⌽A)[;1]` "does not evaluate to anything sensible" | It is correct. On a sample `⎕IDLOC`-style matrix all three p1 algorithms return the same `2 1 8`. |
| p10 | `(1⌽1⍴⍴⍴B)` is "semantically opaque" | Misreading; see section 1. |
| p12 | `1⊖` rotates the rows to (MM,YY,DD) | It gives (MM,DD,YY): `7 14 76` for 760714. All four p12–13 format lines print `7/14/76`. |
| p13 | `100⊥1⊖ 100 100 100 ⊤DATES` is a LENGTH ERROR | It works: `71476 90245 53169 70476`. |
| p16 | `COL←COL-¯IO` leaves COL out of range | The print has `~IO`; see section 1. |
| p22 | SS3 [5] uses take, `(¯1↑⍳1)` | It is power; see section 1. |
| p23 | SS6 [6] `G←G-F←⍳C←1` is "almost certainly a typesetting slip" | It is correct as printed. `F` is deliberately reused, and SS6 agrees with all the other searches in both origins. |
| p27 | The timed expression's `R` "lands in the global" | Only with the underscored names; see section 3. |
| p30 | The line has a jot and no outer product, "odd" | It is `*⌿C⊖`; see section 1. |
| p32 | `L[]←,R`: an index "was apparently left blank or lost" | The empty index is the point of the paragraph. It runs and preserves the shape. |
| p32 | `>\ 0.5 0.5 0.5` should be `0.5 0 0` | The printed `0.5 0 1` is right, and is what APL\*PLUS/PC returns. |
| p33 | `0×.+(⍋⍋K≠⍳⍴⍴A)⍉A` "does not appear to reproduce `×/[K]A`" | It does, for K = 1, 2 and 3 on a 2×3×4 array. |
| p36 | `1 1⍉A` on the 5×9 `A` is a LENGTH ERROR | It returns the five-element diagonal. All four printed diagonals are reproduced. |

Two fidelity rules caused several of the errors above. The lint rule that
treats `~` as an OCR slip for `¯` produced `COL-¯IO`, and the take, drop and
star glyphs were confused in at least four places (pp 18, 19, 22, 32).

## 5. Interpreter differences

These are not transcription problems.

- `ΔFMT` does not exist; `⎕FMT` was substituted. `ΔFMT(…;…;…)` is a SYNTAX
  ERROR, since the semicolon list is only valid with the system function.
- `⎕IDLOC`, `⎕ERASE`, `⎕SIZE`, `⎕SS`, `⎕DEF`, `⎕DEFL`, `⎕VR`, `⎕SI` and `⎕AI`
  all exist. COMPRESS was run with `⎕NC` and `⎕EX` before I found that
  `⎕IDLOC` and `⎕ERASE` work, so it was not run exactly as printed.
- p32: reversal or rotation along a nonexistent axis is an AXIS ERROR, so
  `V[⌽[K]⍒V]` works for K = 1 and fails for K = 2.
- p32: `''⍴A` for an empty `A` is a LENGTH ERROR. `⌊/ 2 3 0 ⍴6` is a 2×3
  matrix of `1.797693135E308`.
- p29: `0÷0` is 1, as printed.
- p30: the plot `' ⎕'[1+FREQ∘.≥⍳⌈/FREQ]` gives eight rows. The print shows
  seven (the 31-box row is missing in the original), so the Markdown is
  faithful here.
- p40: `⎕VR` output has a different layout from the mainframe's, so the
  constant in `VR[⎕IO-6-⍴VR]←'['` is version-specific. The OLD and NEW
  expressions still agree with each other.
- `⎕AI` has four elements and its second is fractional. Timings are not
  comparable with the printed ones; only the shape of each result was
  checked.
- `⍕` of a numeric matrix has a leading blank column in this version. The
  harness formats results with `⍕`, so matrix transcripts show it.
- Factorial and `⎕AI` arithmetic fail with LIMIT ERROR when DOSBox-X emulates
  an 8087. All results here were obtained with `fpu=false`, except the first
  runs of pp 1–24, which contain no factorial or timing arithmetic that
  passed.

## 6. Verified as transcribed

Every expression listed here reproduces its printed result.

- **p1:** the three `⎕IDLOC` idioms; `<\` and `∨\`.
- **pp 3–5:** permutation tests, `V`/`GV`/`V2`, `⍋GV`, `EW ⋄ ⍋EW ⋄ ⍋⍋EW`,
  `POP`, `GRADE`, `(⍒POP),[0.5] RANK`, and the report body (with `⍉`).
- **pp 6–9:** `T`, `T[L;R;C]` (both), `ET TU`, the `SPADE` matrix and its
  indexings, `SUITS` (both), `THEATER` (both), `JG`, `1 1 2⍉JG[…]`,
  `(8 7⍴JG)[1 4 3 8 5;]`, `IND` as `1 4 3 8 5`.
- **p10:** `JELL INTO A GEL`, the fifteen computed indices.
- **p11:** all SPS and SPA examples (with the print's SPS and SPA).
- **pp 12–14:** every date expression, including the whole algebraic chain;
  all give 71476 for 760714.
- **pp 15–17:** `A←+\⍳100`, `R←A[⌽⍳50]`, `R←101⍴2+⍳100`, `60÷⍳6`, `¯2*⍳31`,
  `!⍳12`, `A[]←2○0`, `CV←(⍴CV)⍴⍕1/,⍎'CV[]'` (with 800 for 80000),
  `BV/⍳⍴BV`.
- **pp 18–20:** IF, THISL (print form), `→(M≥C←C+1)↑⎕LC`, `→T⌈⍳M≥C←C+1`,
  `→(L4,L5) IF ¯1 1=×A`, ITERATE to ITERATE4 and the shortened ITERATE2 (0
  and 5 iterations each), and the recursive `⍎L←…` line.
- **pp 21–23:** SS1 (both lines), SS2 (both lines), SS3, SS4, SS5, SS6 and
  `⎕SS` agree on thirteen substrings in origin 1 and five in origin 0,
  including empty, single-character, overlapping, absent and overlong ones.
- **pp 25–27:** FOR, TIMES, ALG1 and ALG2 run; ALG1 and ALG2 return the same
  unique values.
- **pp 28–31:** everything, including the region report, both division rows,
  both tables (spot-checked with sample values), `7 11[B+1]` and its two
  alternatives, and `FACETIOUSLY`.
- **pp 32–33:** every "Did you know" item except the two noted in section 5;
  the `⎕FMT` suppression example matches character for character.
- **pp 34–36:** the matrix `A`, the subscription example, all eight take and
  drop headers, all sixteen two-step expressions, `''⍴A`, `9⍴A`, the four
  diagonals.
- **pp 37–38:** CASHFLOW, CASHFLO2 and FASTFLOW agree on random data (to
  2E¯12 for FASTFLOW) and handle zero rates.
- **pp 39–40:** the two table-lookup forms, ΔSS (print form), the four
  `DSPELL` state-indicator tests (all 1 inside a running `DSPELL`), ROWSS
  with both printed selections.
- **pp 41–43:** every result, the LENGTH ERROR, right-justification of a
  vector and a matrix, FASTFLOW, the ending-balance decode, and all three
  MONTHADD lines.

## 7. Not checked

- The function-editor lines on p26 (`∇FOR[3] R←99+⍳1300∇`, `∇FOR[~3]∇`)
  could not be run.
- The storage figures on pp 15–17 and `'I80' ⎕FMT 10000⍴1` at full size.

## 8. Method

The harness is in `~/work/aplplus/harness`. `tools/wbrun.py SPEC` writes the
statements to a file, starts APL\*PLUS/PC in a background DOSBox-X, and prints
what APL wrote back; a run takes about 15 seconds. The specs used are in
`harness/wb/spec`:

| Spec | Pages |
|---|---|
| `a1.txt` | 1–5 |
| `a3.txt`, `a4.txt` | 6–17 |
| `a6.txt` | 18–23 |
| `a8.txt` | 21–31 (origin-0 searches, timing, Booleans) |
| `a10.txt` | 25–27 rerun, 32–43 |
| `fp.txt` | factorial and `⎕AI` check |

Where the Markdown and the print differ, the specs contain both forms, so the
failures quoted in section 1 can be reproduced. Each function was run with
underscored labels written in lowercase. Output that a function prints itself
does not reach the transcript, so REPORT was run with its two display lines
assigned to variables.
