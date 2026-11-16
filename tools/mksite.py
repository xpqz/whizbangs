#!/usr/bin/env python3
"""Generate the Zensical site sources in web/docs from docs/collected-whizbangs-corrected.md.

One page per article, plus the cover (index), the note to readers, a page about this
edition and the verification notes. Everything under web/docs except stylesheets/ and
fonts/ is derived and overwritten on each run.

usage: tools/mksite.py        then: zensical build   (or: make site)
"""
import os, re, shutil
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
SRC=os.path.join(ROOT,'docs','collected-whizbangs-corrected.md')
OUT=os.path.join(ROOT,'web','docs')
TITLES={ # printed heading -> (slug, display title)
"NOTE TO READERS":("note-to-readers","Note to Readers"),
"WHAT'S IN A NAME?":("whats-in-a-name","What's in a Name?"),
"PERMUTATION VECTORS IN APL - A RANK ANSWER":("permutation-vectors","Permutation Vectors in APL – A Rank Answer"),
"SUBSCRIPTION":("subscription","Subscription"),
"SOME NOTES ON DATE STORAGE":("date-storage","Some Notes on Date Storage"),
"STRETCHING THE WORKSPACE":("stretching-the-workspace","Stretching the Workspace"),
"BRANCHING AND ITERATION":("branching-and-iteration","Branching and Iteration"),
"STRING SEARCHING":("string-searching","String Searching"),
"TIMING ALGORITHMS":("timing-algorithms","Timing Algorithms"),
"USING BOOLEANS TO CONTROL COMPUTATION":("booleans","Using Booleans to Control Computation"),
"APL POTPOURRI":("apl-potpourri","APL Potpourri"),
"DATA SELECTION":("data-selection","Data Selection"),
"WHY NOT TO LOOP":("why-not-to-loop","Why Not to Loop"),
"CHARACTER SEARCHES":("character-searches","Character Searches"),
"BACK TO BASICS":("back-to-basics","Back to Basics"),
}
MONTHS="January February March April May June July August September October November December".split()
DATE=re.compile(r'^(%s) (19\d\d)$'%'|'.join(MONTHS))
SRCCOM=re.compile(r'\n\n<!-- source:(.*?)-->\n\n',re.S)

def pagemarks(t):
    """Turn the per-page source comments into visible page markers; rejoin sentences split by a page break."""
    def sub(m):
        pm=re.search(r'printed page (\d+)',m.group(1))
        before=t[:m.start()]; after=t[m.end():]
        if not pm: return '\n\n'
        n=pm.group(1)
        mark='<a class="pg" id="p%s" href="#p%s" title="printed page %s">%s</a>'%(n,n,n,n)
        if before and (before[-1].isalnum() or before[-1] in ',;-') and after[:1] and (after[0].islower() or after[0]=='('):
            return ' '+mark+' '
        return '\n\n<p class="pgline">'+mark+'</p>\n\n'
    return SRCCOM.sub(sub,t)

def admonitions(t):
    def sub(m):
        body=re.sub(r'^> ?','',m.group(0).strip(),flags=re.M).replace('⚠ **Proofread:** ','',1)
        return '\n!!! warning "Proofread"\n\n'+'\n'.join('    '+l for l in body.split('\n'))+'\n'
    return re.sub(r'\n> ⚠ \*\*Proofread:\*\*.*?(?=\n\n|\n```|\Z)',sub,t,flags=re.S)

def body(t):
    t=pagemarks('\n\n'+t.strip()+'\n\n').strip()
    t=admonitions('\n'+t+'\n').strip()
    t=re.sub(r'^### ','## ',t,flags=re.M)
    t=t.replace('```apl\n','```text\n')          # transcripts mix input and output: no syntax colouring
    t=re.sub(r'<!--.*?-->\n?','',t,flags=re.S)    # remaining editorial comments
    return t

def main():
    s=open(SRC,encoding='utf-8').read()
    s=s[s.index('<!-- source: PDF page 1'):]
    parts=re.split(r'^## (.+)$',s,flags=re.M)
    cover=parts[0]; arts=[]
    # a "<!-- source -->" comment at the end of a chunk belongs to the next article
    carry=''
    m=re.search(r'<!-- source:[^>]*-->\s*\Z',cover)
    if m: carry=cover[m.start():]; cover=cover[:m.start()]
    for i in range(1,len(parts),2):
        head=parts[i].strip(); text=carry+'\n\n'+parts[i+1]; carry=''
        m=re.search(r'<!-- source:[^>]*-->\s*\Z',text)
        if m: carry=text[m.start():]; text=text[:m.start()]
        arts.append((head,text))
    for d in os.listdir(OUT) if os.path.isdir(OUT) else []:
        if d.endswith('.md'): os.remove(os.path.join(OUT,d))
    os.makedirs(OUT,exist_ok=True)
    nav=[]; rows=[]
    for head,text in arts:
        slug,title=TITLES[head]
        lines=text.strip().split('\n'); date=''
        if DATE.match(lines[-1].strip()): date=lines[-1].strip(); text='\n'.join(lines[:-1])
        first=re.search(r'printed page (\d+)',text)
        b=body(text)
        sub=('<p class="dateline">%s</p>\n\n'%('APL*PLUS Service <em>News</em>, '+date) if date else '')
        if slug=='note-to-readers': sub=''
        open(os.path.join(OUT,slug+'.md'),'w',encoding='utf-8').write('# %s\n\n%s%s\n'%(title,sub,b))
        nav.append((title,slug+'.md'))
        if slug!='note-to-readers': rows.append((title,slug,date,first.group(1) if first else ''))
    # index
    idx=['---','title: Collected Whizbangs','hide:','  - toc','---','',
'<div class="cover" markdown>','','# Collected Whizbangs','',
'**An Anthology of Tutorials on APL Programming Techniques**','',
'by Roy A. Sykes, Jr.','','Volume 1 · Scientific Time Sharing Corporation · August 1978','',
'</div>','',
'Fourteen columns from *News*, the newsletter of the APL\\*PLUS time-sharing service, written between',
'December 1975 and May 1978 and collected by STSC as booklet P036-0878. Begin with the',
'[Note to Readers](note-to-readers.md), or pick an article:','',
'| | Article | First published | Page |','|--:|---|---|--:|']
    for n,(title,slug,date,pg) in enumerate(rows,1): idx.append('| %d | [%s](%s.md) | %s | %s |'%(n,title,slug,date,pg))
    idx+=['','!!! note "About this edition"','',
'    The text was transcribed from a scan of the booklet, and the APL was then checked by running it',
'    in a period interpreter, APL\\*PLUS/PC 4.1. See [About this edition](about.md) for what was',
'    changed and what is still uncertain.','',
'<p class="imprint">Scientific Time Sharing Corporation · 7316 Wisconsin Avenue, Bethesda, Maryland 20014 · P036-0878</p>','']
    open(os.path.join(OUT,'index.md'),'w',encoding='utf-8').write('\n'.join(idx))
    about='''# About this edition

This site presents *Collected Whizbangs, Volume 1* (STSC, August 1978) by Roy A. Sykes, Jr.,
transcribed from a 25-page scan of the booklet.

## How the text was made

The scan's OCR layer is usable for prose and useless for APL, so the code was transcribed
from the page images by eye. It was then **run**: every example that can be executed was fed to
STSC APL\\*PLUS/PC release 4.1 (1984) under DOSBox-X, and each disagreement between the
transcription and the interpreter was checked against the scan.

That pass found about 25 places where the first transcription differed from the print, 21 of
them changing what the code does. With those corrected, every printed result that can be
recomputed is reproduced by the interpreter. The full record is in the
[verification notes](verification.md).

## Conventions

- **Page numbers.** The small numbers in the margin, such as <a class="pg">12</a>, mark where
  each printed page begins.
- **Underscored names.** The booklet uses underscored letters for statement labels and for some
  names (all the locals of `TIMES`, for example). They are distinct identifiers. Here they are
  written in lowercase, which is how APL\\*PLUS/PC represents them: a label printed as
  underscored `A` appears as `a:`.
- **Emphasis.** Words the booklet underlines for emphasis are set in italics.
- **`ΔFMT`.** The early articles call the formatter `ΔFMT`; later ones use the system function
  `⎕FMT`. Both are as printed.

## What the interpreter cannot confirm

APL\\*PLUS/PC 4.1 is six years newer than the booklet and is the PC product, not the mainframe
service the articles describe. Timings and workspace-storage figures are specific to the 1970s
system and were not checked. The prose and tables were proofread against the scan.
'''
    open(os.path.join(OUT,'about.md'),'w',encoding='utf-8').write(about)
    v=open(os.path.join(ROOT,'docs','aplplus-verification.md'),encoding='utf-8').read()
    v=v.replace('# Verification against APL\\*PLUS/PC 4.1','# Verification notes',1)
    open(os.path.join(OUT,'verification.md'),'w',encoding='utf-8').write(v)
    print('wrote %d pages to web/docs'%(len(nav)+3))
    return nav
if __name__=='__main__': main()
