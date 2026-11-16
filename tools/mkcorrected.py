#!/usr/bin/env python3
"""Build docs/collected-whizbangs-corrected.md from docs/collected-whizbangs.md.

Applies the corrections recorded in docs/aplplus-verification.md as exact string
replacements. Each replacement asserts how many times its target occurs, so the
script stops instead of mis-patching if the source transcription changes.

usage: tools/mkcorrected.py [docs-dir]     (default: ../docs next to this script)
"""
import os, sys
d=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docs')
src=open(d+'/collected-whizbangs.md',encoding='utf-8').read()
s=src
def rep(old,new,n=1):
    global s
    c=s.count(old)
    assert c==n, (c,n,old)
    s=s.replace(old,new)
rep('## Contents\n','''> **Corrected copy.** This is `collected-whizbangs.md` with the corrections from
> `aplplus-verification.md` applied: readings checked against the scan and by
> running the code in APL\\*PLUS/PC 4.1. Underscored letters in the print
> (statement labels and some names) are written in lowercase, as APL\\*PLUS/PC
> does.

## Contents
''')
rep("→(2=(<\\C≠¯1)/C)⍴A\n","→(2=(<\\C≠¯1)/C)⍴a\n")
rep("[3]   A:R←A/[COORD] B","[3]   a:R←A/[COORD] B")
rep("<!-- labels are underlined in the source (A̲, A̲:); transcribed bare.","<!-- labels are underlined in the source (A̲, A̲:); written in lowercase (a, a:).")
rep("3 3⍳19","3 3⍴⍳9",3)
rep("V←?10⍴99 ⋄ V2←V[GV←⍒V] ⋄ ∧/V2=⌊\\V2\n85 41","      V←?10⍴99 ⋄ V2←V[GV←⍒V] ⋄ ∧/V2=⌊\\V2\n1\n      V,[1] GV,[0.5] V2\n85 41")
rep("```apl\nV,[1] GV,[0.5] ⍋GV\n","```apl\n      V,[1] GV,[0.5] ⍋GV\n")
rep("RA⊥ALP⍳NAMES","RA⊥ALP⍳⍉NAMES",2)
rep("[5]   'CITY_NAME________   _POP  RANK'","[5]   'city_name________   _pop  rank'")
old_rep='''CITY_NAME________   _POP  RANK
BOSTON, MA           641     8
CHICAGO, IL         3367     2
DENVER, CO           515     9
HOUSTON, TX         1233     5
LOS ANGELES, CA     2816     3
NEW YORK, NY        7868     1
PHILADELPHIA, PA    1949     4
SAN FRANCISCO, CA    716     7
WASHINGTON, DC       757     6
'''
rep(old_rep,old_rep.replace('CITY_NAME________   _POP  RANK','city_name________   _pop  rank').replace('     ','    '))
rep("F←'G⎕  T[9;9;9] ⎕'","F←'G⍞ T[9;9;9] ⍞'")
rep("T[2;3;1]  T[2;3;2]  T[2;3;5]  T[2;3;2]\nT[1;3;1]"," T[2;3;1]  T[2;3;2]  T[2;3;5]  T[2;3;2]\n T[1;3;1]")
rep("For `A[V1;V2;V3;...;VN]` (where\n`N←⍴⍴A`)","For `A[V1;V2;V3;...;Vn]` (where\n`n←⍴⍴A`)")
rep("(N⍴1)⍉A[V1;V2;V2;...;VN]","(n⍴1)⍉A[V1;V2;V2;...;Vn]")
rep("(⍴V1)⌊(⍴V2)⌊(⍴V3)⌊...⌊⍴VN","(⍴V1)⌊(⍴V2)⌊(⍴V3)⌊...⌊⍴Vn")
rep("      1111111222222222333333444555555\n","      111111112222222233333344445555555\n")
rep("[1]   ⍝ SCATTERED-POINT SELECTION.","[1]   ⍝ sCATTERED-pOINT sELECTION.")
rep("[1]   ⍝ SCATTERED-POINT ASSIGNMENT.","[1]   ⍝ sCATTERED-pOINT aSSIGNMENT.")
rep("[10]  R←⍴A ⋄ C←1↑1⍳1\n[11]  R←(,A)[(R⊥(1⌽1⍴⍴⍴B)⌽B)+C-R⊥C]","[10]  R←⍴A ⋄ C←''⍳1\n[11]  R←(,A)[(R⊥(1⌽⍳⍴⍴B)⍉B)+C-R⊥C]")
rep("[5]   R←,A ⋄ C←1↑1⍳1 ⋄ A←⍴A\n[6]   R[(A⊥(1⌽1⍴⍴⍴B)⌽B)+C-A⊥C]←DATA ⋄ R←A⍴R\n∇\n```\n",
    "[5]   R←,A ⋄ C←''⍳1 ⋄ A←⍴A\n[6]   R[(A⊥(1⌽⍳⍴⍴B)⍉B)+C-A⊥C]←DATA ⋄ R←A⍴R\n∇\n```\n")
# The display of M and the first SPS example are at the foot of p10 in the print,
# and the sentence introducing them is printed once.
rep("""A few examples should show the power of *SPS*:

<!-- source: PDF page 8, right half — printed page 11 -->

```apl
      ⎕←M←5 7⍴⍳35
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35
```

A few examples should show the power of *SPS*:

```apl
      M SPS 2,[1.5]""","""A few examples should show the power of *SPS*:

```apl
      ⎕←M←5 7⍴⍳35
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35

      M SPS 5 2⍴1 1,1 4,2 2,3 2,4 4
1 4 9 16 25
```

<!-- source: PDF page 8, right half — printed page 11 -->

```apl
      M SPS 2,[1.5]""")
rep("1 1  1 6\n1 2  2 5\n1 3  3 4\n1 4  4 3\n1 5  5 2\n","    1 1    1 6\n    1 2    2 5\n    1 3    3 4\n    1 4    4 3\n    1 5    5 2\n")
rep("1  6\n2 12\n3 18\n4 24\n5 30\n","      1      6\n      2     12\n      3     18\n      4     24\n      5     30\n")
rep("760714  a BASTILLE DAY","760714 ⍝ BASTILLE DAY")
rep("'I2,⎕/⎕,ZI2,⎕/⎕,ZI2' ⎕FMT D","'I2,⍞/⍞,ZI2,⍞/⍞,ZI2' ⎕FMT D")
rep("'I2,2P⎕/⎕ZI3' ⎕FMT D","'I2,2P⍞/⍞ZI3' ⎕FMT D")
rep("'G⎕Z9/99/99⎕' ⎕FMT D","'G⍞Z9/99/99⍞' ⎕FMT D")
rep("R←(VEC≠0)/MAT[;2 3 4]","R←(VEC≠0)⌿MAT[;2 3 4]")
rep("R←TEMP1/TEMP2 ⋄","R←TEMP1⌿TEMP2 ⋄")
rep("COL←COL-¯IO\n[3]   A:R←R[⍋MAT[R;COL]] ⋄ →A×IO≤COL←COL-1","COL←COL-~IO\n[3]   a:R←R[⍋MAT[R;COL]] ⋄ →a×IO≤COL←COL-1")
rep("→(condition)⍴LABEL   or →(condition)→LABEL\n→(×⍴vector)⍴LABEL    or →(⍴vector)→LABEL","→(condition)⍴LABEL   or →(condition)↓LABEL\n→(×⍴vector)⍴LABEL    or →(⍴vector)↓LABEL")
rep("T: ... ⋄ →T⌈⍳M≥C←C+1","t: ... ⋄ →t⌈⍳M≥C←C+1")
rep("[1]   R←1↑1↑⎕LC","[1]   R←1↑1↓⎕LC")
rep("[2]   A:→(C>M)⍴0 ⋄ PROCESS ⋄ C←C+1 ⋄ →A","[2]   a:→(C>M)⍴0 ⋄ PROCESS ⋄ C←C+1 ⋄ →a")
rep("[2]   A:PROCESS ⋄ →(M≥C←C+1)⍴A","[2]   a:PROCESS ⋄ →(M≥C←C+1)⍴a")
rep("→L←(M⍴A),0\n[2]   A:PROCESS ⋄ →L[C←C+1]","→L←(M⍴a),0\n[2]   a:PROCESS ⋄ →L[C←C+1]")
rep("[2]   A:→(M<C←C+1)⍴0 ⋄ PROCESS ⋄ →A","[2]   a:→(M<C←C+1)⍴0 ⋄ PROCESS ⋄ →a")
rep("((⍳D)-1)⊖A∘.=B","((⍳D)-⍳1)⊖A∘.=B")
rep("((⍳D)-1)⌽B∘.=A","((⍳D)-⍳1)⌽B∘.=A")
rep("((⍳D)-1)⌽(D,C)⍴A","((⍳D)-⍳1)⌽(D,C)⍴A")
rep("⋄ →B⌊A+D","⋄ →b⌊a+D",4)
rep("[2]   A:R←⍳C ⋄ →0 ⍝      EMPTY STRING","[2]   a:R←⍳C ⋄ →0 ⍝      EMPTY STRING",4)
rep("[4]   B:E←0⌈C-D-1","[4]   b:E←0⌈C-D-1",2)
rep("[4]   B:F←' ETAISON","[4]   b:F←' ETAISON",2)
rep("R←(A[R∘.+(¯1↑⍳1)↓⍳D]∧.=1↓B)/R","R←(A[R∘.+(¯1*⍳1)↓⍳D]∧.=1↓B)/R")
rep("matches. The `(¯1↑⍳1)↓⍳D` construct cleverly accounts for the index origin while\nremoving the index of the character already examined.","matches. The `(¯1*⍳1)↓⍳D` construct cleverly accounts for the index origin while\nremoving the index of the character already examined.")
rep("[7]   G←(F≠⍳D)/⍳D\n∇","[7]   G←(F≠⍳D)/⍳D\n[8]   R←(A[R∘.+G-⍳1]∧.=B[G])/R\n∇")
rep("[6]   C:→(⍴R←(A[R+C]∊B[C])/R)↓0\n[7]   →C×D>C←C+1","[6]   c:→(⍴R←(A[R+C]∊B[C])/R)↓0\n[7]   →c×D>C←C+1")
rep("[9]   C:→(⍴R←(A[R+G[C]]∊B[C])/R)↓0\n[10]  →C×D>C←C+1","[9]   c:→(⍴R←(A[R+G[C]]∊B[C])/R)↓0\n[10]  →c×D>C←C+1")
rep("[2]  A:→(TIMES>N)⍴B\n[3]   R←V⌹M\n[4]   TIMES←TIMES+1 ⋄ →A\n[5]  B:CPU←","[2]  a:→(TIMES>N)⍴b\n[3]   R←V⌹M\n[4]   TIMES←TIMES+1 ⋄ →a\n[5]  b:CPU←")
rep("      ∇FOR[¯3]∇\n","      ∇FOR[~3]∇\n")
# The wavy mark in the last row of both string-search tables is the same x-height tilde.
rep("'⍺∈⍳○∪⍴¯⍵'","'⍺∈⍳○∪⍴~⍵'",2)
rep('''∇ R←A TIMES B;C;D;RUN
[1]   ⍝CPU FOR A ITERATIONS OF EXPRESSION B
[2]   C←'⋄',B ⋄ C←1↓(A×⍴C)⍴C
[3]   C←⎕DEF '∇RUN',⎕TCNL,'[1]',C,'∇'
[4]   R←⎕AI ⋄ RUN ⋄ R←⎕AI-R
[5]   C←⎕DEFL 'RUN[1]',1↓A⍴'⋄'
[6]   D←⎕AI ⋄ RUN ⋄ D←⎕AI-D
[7]   R←(R-D)[2],A
∇''','''∇ r←a TIMES b;c;d;RUN
[1]   ⍝CPU FOR a ITERATIONS OF EXPRESSION b
[2]   c←'⋄',b ⋄ c←1↓(a×⍴c)⍴c
[3]   c←⎕DEF '∇RUN',⎕TCNL,'[1]',c,'∇'
[4]   r←⎕AI ⋄ RUN ⋄ r←⎕AI-r
[5]   c←⎕DEFL 'RUN[1]',1↓a⍴'⋄'
[6]   d←⎕AI ⋄ RUN ⋄ d←⎕AI-d
[7]   r←(r-d)[2],a
∇''')
rep("Line [2] replicates the expression *A* times","Line [2] replicates the expression *a* times")
rep("'P⎕ (⎕Q⎕)⎕BLI6' ⎕FMT NA","'P⍞ (⍞Q⍞)⍞BLI6' ⎕FMT NA")
rep("'I0,I2,A0,I4,3G⎕⎕,F8.3' ⎕FMT 4 8⍴⍳32","'I0,I2,A0,I4,3G⍞⍞,F8.3' ⎕FMT 4 8⍴⍳32")
rep("`'I0'` or `'A0'` or `'G⎕⎕'`","`'I0'` or `'A0'` or `'G⍞⍞'`")
rep("(e.g., `A÷B` or `A-B`)","(e.g., `A+B` or `A-B`)")
rep("(1,⍴A)⍴∘≠C⌽A,[0.5] B","(1,⍴A)⍴*⌿C⊖A,[0.5] B")
rep("`(N⍴0)↑SCALAR` has the same effect","`(N⍴0)↓SCALAR` has the same effect")
rep("      1 1 0 0 1 /A","      1 1 0 0 1 ⌿A")
rep("      0 1 1 0 0 /0 0 0 1 1 1 1 0 0 /A","      0 1 1 0 0 ⌿ 0 0 0 1 1 1 1 0 0 /A")
rep("      B/A[; 5 4 7 6]","      B⌿A[; 5 4 7 6]")
rep("CASHFLOW2","CASHFLO2",3)
rep("→N←((⍴R)⍴L),0\n[4]   L:T←CF","→N←((⍴R)⍴l),0\n[4]   l:T←CF")
rep("'RATRIX'","'RATMIX'")
rep("(C,R×R)⍴A","(C,R+×R)⍴A")
# ---- Proofreading of prose and tables against the scan ----
# Text
rep("substantial gains in CPU\n","substantial gains in CRU\n")   # CRU: STSC's billing unit (cf. MILLICRUS, p37)
rep("be restated as `(((⍴A),1)⍴A)∘.+(1,⍴B)⍴B` where `∘` can be any scalar dyadic","be restated as `(((⍴A),1)⍴A)o.+(1,⍴B)⍴B` where o can be any scalar dyadic")
rep("string-searching techniques is now moot","string-search techniques is now moot")
rep("*WS FULLS*","*WS FULL*s")
rep("*[L1;L2;L3;...]* and *[A;B;C;...]*","*{L1;L2;L3;...}* and *{a;b;c;...}*")
rep("∇ R←A IF B\n      R←B/A\n∇","∇ R←A IF B\n[1]   R←B/A\n∇")
# Layout
rep("can be calculated by\n\n```apl\n⌊TS÷5184000\n```\n\n(5184000 = the number","can be calculated by `⌊TS÷5184000`\n(5184000 = the number")
rep("      ROWS←1,[1.5]⍳5 ⋄ COLS←(⍳5),[1.5]7-⍳5\n      5 0 2 0","      ROWS←1,[1.5]⍳5 ⋄ COLS←(⍳5),[1.5]7-⍳5\n\n      5 0 2 0")
rep("no matches are possible.\n\nA somewhat better","no matches are possible.\nA somewhat better")
rep("of computer time to execute.\n\nSince computer time","of computer time to execute.\nSince computer time")
rep("(milliseconds).\n\nIf we wish to measure","(milliseconds).\nIf we wish to measure")
rep("```\n(Executed 2/25/77 at 9:19 P.M. EST\non APLPLUSC/470-10011 with 8 users)\n```","(Executed 2/25/77 at 9:19 P.M. EST\non APLPLUSC/470-10011 with 8 users)")
rep("```\n(Executed 24 Feb 78 at 6:46 PM EST\non APLPLUSC/470-10011 with 34 users)\n```","(Executed 24 Feb 78 at 6:46 PM EST\non APLPLUSC/470-10011 with 34 users)")
# Emphasis: the print underlines these words (written here as italics)
rep("we wish only to know what the current definition","we wish only to know what the *current* definition")
rep("(in *ORIGIN 1*)","(in *ORIGIN* 1)")
rep("`⍋⍒V` is the descending ranking vector","`⍋⍒V` is the *descending* ranking vector")
rep("is the ascending ranking vector on *V*, and","is the *ascending* ranking vector on *V*, and")
rep("represent all indices of a vector","represent all *indices* of a vector")
rep("*descending grade vector*","descending *grade vector*")
rep("*inverse permutation*","*inverse* permutation")
rep("sorted by both city name","sorted by *both* city name")
rep("can also be indicated by","can also be *indicated* by")
rep("so we decide to\narrange the report","so we decide to\n*arrange* the report")
rep("to express the ordering of","to *express* the ordering of")
rep("we will be using the ordering","we will be *using* the ordering")
rep("identifying elements of an array. Once *identified*, those","*identifying* elements of an array. Once identified, those")
rep("An *individual element* is","An individual element is")
rep("for each coordinate of the left","for each *coordinate* of the left")
rep("coordinate coupled to all","coordinate *coupled* to all")
rep("but *only if* they","but *only* if they")
rep("unless all the selected subarrays are *identified* by","*unless* all the selected subarrays are identified by")
rep("the other temporary value `MAT[;2 3 4]`, and the result","the other temporary value `MAT[;2 3 4]`, *and* the result")
rep("The most fundamental APL solution","The most fundamental *APL* solution")
rep("it both builds and shifts","it both builds *and* shifts")
rep("*least number of\nexpected* occurrences","*least* number of\n*expected* occurrences")
rep("performs `A*B` if C=0 and `B*A` if C=1:","performs `A*B` if *C*=0 and `B*A` if *C*=1:")
rep("The function ΔSS takes","The function *ΔSS* takes")
rep("function in APL called base value.","function in APL called *base value*.")
rep("also called decode,","also called *decode*,")
rep("base value evaluates polynomials.","base value *evaluates polynomials*.")
rep("evaluating a mixed radix polynomial","evaluating a *mixed radix* polynomial")
# Labels are outdented one column in the print: two spaces after the line number, not three.
import re
s,_n=re.subn(r'(?m)^(\[\d\])   ([a-z]+:)',r'\1  \2',s)
assert _n==17,_n
open(d+'/collected-whizbangs-corrected.md','w',encoding='utf-8').write(s)
assert '⚠' not in s
print('ok')
