#!/usr/bin/env python3
"""Build vol2/docs/collected-whizbangs-corrected.md from vol2/docs/collected-whizbangs.md.

Applies the corrections recorded in vol2/docs/aplplus-verification.md as exact string
replacements. Each replacement asserts how many times its target occurs, so the script
stops instead of mis-patching if the source transcription changes. A correction is made
only where the scan shows it; print errors are kept and noted.

usage: tools/mkcorrected_vol2.py
"""
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','vol2','docs')
s=open(D+'/collected-whizbangs.md',encoding='utf-8').read()
def rep(old,new,n=1):
    global s
    c=s.count(old)
    assert c==n,(c,n,old)
    s=s.replace(old,new)

# ---- corrections (filled in from the verification and proofreading passes)
# Misreadings of the scan are corrected in vol2/src/pages. What remains here are notes on
# places where the print itself is wrong (vol2/docs/aplplus-verification.md, section 3).
N='\n> **Note.** '
rep("      (~C ⎕SS '  ')/C\nSO BE IT IF WE DO AS IN TV\n```\n",
    "      (~C ⎕SS '  ')/C\nSO BE IT IF WE DO AS IN TV\n```\n"+N+"The result is printed without its leading blank. Run, it is\n> `' SO BE IT IF WE DO AS IN TV '`: removing the first blank of each pair leaves one\n> blank at each end.\n")
rep("      MAT[⍋(⌈⌿MAT)⊥⍉MAT;]\n```\n",
    "      MAT[⍋(⌈⌿MAT)⊥⍉MAT;]\n```\n"+N+"As printed, the radix is the column maxima, so a value equal to its column's\n> maximum overflows into the next column and rows are not encoded uniquely: for\n> `4 2⍴2 0 1 2 1 1 0 2` the rows come out in the wrong order. The radix should be\n> `1+⌈⌿MAT`, as the text on the next page describes. It happens to give the right\n> order for *DATES*.\n")
rep("      24 80 ⍴ 1 3 2 4 ⍉ 4 5 6 16 ⍴((×/ 4 5). 6 16)↑TEN\n```\n",
    "      24 80 ⍴ 1 3 2 4 ⍉ 4 5 6 16 ⍴((×/ 4 5). 6 16)↑TEN\n```\n"+N+"The period after `(×/ 4 5)` is printed as shown and is a *SYNTAX ERROR*; it\n> should be a comma, as in the line below and on page 35.\n")

open(D+'/collected-whizbangs-corrected.md','w',encoding='utf-8').write(s)
print('ok')
