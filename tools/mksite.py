#!/usr/bin/env python3
"""Generate the Zensical site sources in web/docs from the corrected copies of both volumes.

  web/docs/index.md            landing page for the collection
  web/docs/about.md            about this edition (both volumes)
  web/docs/vol1/, vol2/        per volume: cover (index.md), note to readers, one page per
                               article, verification notes

It also rewrites the `nav = [...]` block in zensical.toml. Everything under web/docs except
stylesheets/ and fonts/ is derived and overwritten on each run. A volume whose corrected copy
does not exist yet is skipped.

usage: tools/mksite.py        then: zensical build   (or: make site)
"""
import os, re, shutil
ROOT=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
WEB=os.path.join(ROOT,'web','docs')
MONTHS="January February March April May June July August September October November December".split()
MONTH=r'(?:%s)'%'|'.join(MONTHS)
SRCCOM=re.compile(r'\n\n<!-- source:(.*?)-->\n\n',re.S)

# ---------------------------------------------------------------- volume 1
V1_TITLES={ # printed heading -> (slug, display title)
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

def slugify(s):
    s=s.replace('⍴','rho ').replace('←',' gets ').replace('⎕','quad ')
    s=re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
    return s

def pagemarks(t):
    """Turn the per-page source comments into visible page markers; rejoin sentences split by a page break."""
    def sub(m):
        pm=re.search(r'printed page (\d+)',m.group(1))
        before=t[:m.start()]; after=t[m.end():]
        if not pm: return '\n\n'
        n=pm.group(1)
        mark='<a class="pg" id="p%s" href="#p%s" title="printed page %s">%s</a>'%(n,n,n,n)
        if before and (before[-1].isalnum() or before[-1] in ',;-') and after[:1] and (after[0].islower() or after[0]=='('):
            # mid-sentence: the marker goes in the margin (or as a raised number on narrow screens)
            return mark.replace('class="pg"','class="pg pgin"')+' '
        # before a code block, table or admonition the marker takes its own line, so as not to
        # squeeze the block; before prose it floats beside the text
        cls='pgline pgown' if re.match(r'\s*(```|\||!!!|<)',after) else 'pgline'
        return '\n\n<p class="%s">'%cls+mark+'</p>\n\n'
    return SRCCOM.sub(sub,t)

def admonitions(t):
    def sub(m):
        body=re.sub(r'^> ?','',m.group(0).strip(),flags=re.M).replace('⚠ **Proofread:** ','',1)
        return '\n!!! warning "Proofread"\n\n'+'\n'.join('    '+l for l in body.split('\n'))+'\n'
    t=re.sub(r'\n> ⚠ \*\*Proofread:\*\*.*?(?=\n\n|\n```|\Z)',sub,t,flags=re.S)
    def note(m):
        body=re.sub(r'^> ?','',m.group(0).strip(),flags=re.M).replace('**Note.** ','',1)
        return '\n!!! note "Print error"\n\n'+'\n'.join('    '+l for l in body.split('\n'))+'\n'
    return re.sub(r'\n> \*\*Note\.\*\*.*?(?=\n\n|\n```|\Z)',note,t,flags=re.S)

def body(t):
    t=pagemarks('\n\n'+t.strip()+'\n\n').strip()
    t=admonitions('\n'+t+'\n').strip()
    t=re.sub(r'^### ','## ',t,flags=re.M)
    t=t.replace('```apl\n','```text\n')          # transcripts mix input and output: no syntax colouring
    t=re.sub(r'<!--.*?-->\n?','',t,flags=re.S)    # remaining editorial comments
    return t

def split_articles(s):
    """Split a corrected copy at '## ' headings. Returns (front, [(heading, text)])."""
    parts=re.split(r'^## (.+)$',s,flags=re.M)
    front=parts[0]; arts=[]
    carry=''   # a "<!-- source -->" comment at the end of a chunk belongs to the next article
    m=re.search(r'<!-- source:[^>]*-->\s*\Z',front)
    if m: carry=front[m.start():]; front=front[:m.start()]
    for i in range(1,len(parts),2):
        head=parts[i].strip(); text=carry+'\n\n'+parts[i+1]; carry=''
        m=re.search(r'<!-- source:[^>]*-->\s*\Z',text)
        if m: carry=text[m.start():]; text=text[:m.start()]
        arts.append((head,text))
    return front,arts

def clean(d):
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(d)

def write(path,text):
    open(path,'w',encoding='utf-8').write(text)

def verification(src,dst,title):
    v=open(src,encoding='utf-8').read()
    v=re.sub(r'^# .*$','# '+title,v,count=1,flags=re.M)
    write(dst,v)

def volume1():
    src=os.path.join(ROOT,'docs','collected-whizbangs-corrected.md')
    out=os.path.join(WEB,'vol1'); clean(out)
    s=open(src,encoding='utf-8').read()
    s=s[s.index('<!-- source: PDF page 1'):]
    _,arts=split_articles(s)
    date_re=re.compile(r'^(%s) (19\d\d)$'%MONTH)
    nav=[]; rows=[]
    for head,text in arts:
        slug,title=V1_TITLES[head]
        lines=text.strip().split('\n'); date=''
        if date_re.match(lines[-1].strip()): date=lines[-1].strip(); text='\n'.join(lines[:-1])
        first=re.search(r'printed page (\d+)',text)
        sub=('<p class="dateline">%s</p>\n\n'%('APL*PLUS Service <em>News</em>, '+date) if date else '')
        if slug=='note-to-readers': sub=''
        write(os.path.join(out,slug+'.md'),'# %s\n\n%s%s\n'%(title,sub,body(text)))
        nav.append((title,'vol1/'+slug+'.md'))
        if slug!='note-to-readers': rows.append((title,'vol1/'+slug+'.md',date,first.group(1) if first else ''))
    idx=['---','title: Collected Whizbangs, Volume 1','hide:','  - toc','---','',
'<div class="cover" markdown>','','# Collected Whizbangs','',
'**An Anthology of Tutorials on APL Programming Techniques**','',
'by Roy A. Sykes, Jr.','','Volume 1 · Scientific Time Sharing Corporation · August 1978','',
'</div>','',
'Fourteen columns from *News*, the newsletter of the APL\\*PLUS time-sharing service, written between',
'December 1975 and May 1978 and collected by STSC as booklet P036-0878. Begin with the',
'[Note to Readers](note-to-readers.md), or pick an article:','',
'| | Article | First published | Page |','|--:|---|---|--:|']
    for n,(title,path,date,pg) in enumerate(rows,1): idx.append('| %d | [%s](%s) | %s | %s |'%(n,title,os.path.basename(path),date,pg))
    idx+=['','<p class="imprint">Scientific Time Sharing Corporation · 7316 Wisconsin Avenue, Bethesda, Maryland 20014 · P036-0878</p>','']
    write(os.path.join(out,'index.md'),'\n'.join(idx))
    verification(os.path.join(ROOT,'docs','aplplus-verification.md'),os.path.join(out,'verification.md'),'Volume 1: verification notes')
    return {'nav':[('Cover','vol1/index.md')]+nav+[('Verification notes','vol1/verification.md')],'rows':rows}

# ---------------------------------------------------------------- volume 2
def volume2():
    src=os.path.join(ROOT,'vol2','docs','collected-whizbangs-corrected.md')
    if not os.path.exists(src): return None
    out=os.path.join(WEB,'vol2'); clean(out)
    s=open(src,encoding='utf-8').read()
    # article dates from the printed contents: "Title (July/August 1978) 2"
    dates={}
    contents=os.path.join(ROOT,'vol2','src','pages','00-4-contents.md')
    for line in open(contents,encoding='utf-8'):
        m=re.search(r'(%s(?:/%s)? 19\d\d)'%(MONTH,MONTH),line)
        if m:
            t=re.sub(r'\s*\(.*$','',line).strip(' |*-').strip()
            dates[slugify(t)]=m.group(1)
    start=s.find('<!-- source: PDF page 5')
    _,arts=split_articles(s[start:] if start>=0 else s)
    nav=[]; rows=[]
    for head,text in arts:
        title=re.sub(r'\*','',head).replace('--','–'); slug=slugify(title)
        if slug=='contents': continue
        date=dates.get(slug,'')
        # the printed dateline at the end of an article becomes the dateline under its title
        m=re.search(r'\n\*?(%s(?:/%s)? 19\d\d)\*?\s*\Z'%(MONTH,MONTH),text)
        if m: date=date or m.group(1); text=text[:m.start()]
        first=re.search(r'printed page (\d+)',text)
        sub=('<p class="dateline">%s</p>\n\n'%('APL*PLUS Service <em>News</em>, '+date) if date else '')
        write(os.path.join(out,slug+'.md'),'# %s\n\n%s%s\n'%(title,sub,body(text)))
        nav.append((title,'vol2/'+slug+'.md'))
        if slug!='note-to-readers': rows.append((title,'vol2/'+slug+'.md',date,first.group(1) if first else ''))
    idx=['---','title: Collected Whizbangs, Volume 2','hide:','  - toc','---','',
'<div class="cover" markdown>','','# Collected Whizbangs','',
'by Roy A. Sykes, Jr.','','Volume 2 · STSC, Inc. · 1981','',
'</div>','',
'Columns from *APL\\*PLUS Service News*, STSC\'s corporate newsletter, written between July 1978',
'and October 1980. Begin with the [Note to Readers](note-to-readers.md), or pick an article:','',
'| | Article | First published | Page |','|--:|---|---|--:|']
    for n,(title,path,date,pg) in enumerate(rows,1): idx.append('| %d | [%s](%s) | %s | %s |'%(n,title,os.path.basename(path),date,pg))
    idx+=['','<p class="imprint">STSC, Inc. · 2115 E. Jefferson Street, Rockville, Maryland 20852</p>','']
    write(os.path.join(out,'index.md'),'\n'.join(idx))
    vsrc=os.path.join(ROOT,'vol2','docs','aplplus-verification.md')
    extra=[]
    if os.path.exists(vsrc):
        verification(vsrc,os.path.join(out,'verification.md'),'Volume 2: verification notes')
        extra=[('Verification notes','vol2/verification.md')]
    return {'nav':[('Cover','vol2/index.md')]+nav+extra,'rows':rows}

# ---------------------------------------------------------------- collection
ABOUT='''# About this edition

This site presents Roy A. Sykes, Jr.'s *Collected Whizbangs*, the APL tutorials he wrote for
STSC's newsletter between 1975 and 1980, as STSC collected them in two volumes:

- [Volume 1](vol1/index.md) (August 1978), transcribed from a 25-page scan of the booklet.
- [Volume 2](vol2/index.md) (1981), transcribed from the scan on the Internet Archive.

## How the text was made

The scans' OCR is usable for prose and useless for APL, so the code was transcribed from the
page images by eye. It was then **run**: every example that can be executed was fed to STSC
APL\\*PLUS/PC release 4.1 (1984) under DOSBox-X, and each disagreement between the transcription
and the interpreter was checked against the scan. A correction is made only where the scan shows
it; where the print itself is wrong, the text says so. With the corrections, every printed
result that can be recomputed is reproduced. The full record is in the verification notes for
[Volume 1](vol1/verification.md) and [Volume 2](vol2/verification.md).

The prose and tables were proofread against the scans.

## Conventions

- **Page numbers.** The small numbers in the margin, such as <a class="pg">12</a>, mark where
  each printed page begins.
- **Underscored names.** The books use underscored letters for statement labels and for some
  names. They are distinct identifiers. Here they are written in lowercase, which is how
  APL\\*PLUS/PC represents them: a label printed as underscored `A` appears as `a:`.
- **Emphasis.** Words Volume 1 underlines for emphasis are set in italics.
- **`ΔFMT`.** The early articles in Volume 1 call the formatter `ΔFMT`; later ones use the
  system function `⎕FMT`. Both are as printed.

## What the interpreter cannot confirm

APL\\*PLUS/PC 4.1 is the PC product, not the mainframe service the articles describe, and is
newer than both books. Timings and workspace-storage figures are specific to the mainframe
system and were not checked.
'''

def landing(v1,v2):
    t=['---','title: Collected Whizbangs','hide:','  - toc','---','',
'<div class="cover" markdown>','','# Collected Whizbangs','',
'**Tutorials on APL Programming Techniques**','','by Roy A. Sykes, Jr.','',
'</div>','',
'From December 1975 to October 1980, Roy Sykes wrote a column called the "Whizbang" for the',
'newsletter of STSC\'s APL\\*PLUS time-sharing service: short tutorials on APL techniques, from',
'idioms to timing and storage. STSC collected them in two volumes.','']
    for name,v,sub,link in (('Volume 1',v1,'Scientific Time Sharing Corporation, August 1978','vol1/index.md'),
                            ('Volume 2',v2,'STSC, Inc., 1981','vol2/index.md')):
        if not v: continue
        t+=['## [%s](%s)'%(name,link),'',sub,'','| Article | First published | Page |','|---|---|--:|']
        for title,path,date,pg in v['rows']: t.append('| [%s](%s) | %s | %s |'%(title,path,date,pg))
        t.append('')
    t+=['!!! note "About this edition"','',
'    The text was transcribed from scans of the books, and the APL was then checked by running it',
'    in a period interpreter, APL\\*PLUS/PC 4.1. See [About this edition](about.md) for what was',
'    changed and what is still uncertain.','']
    write(os.path.join(WEB,'index.md'),'\n'.join(t))

def tomlnav(v1,v2):
    def section(name,v):
        items=',\n'.join('    { %s = "%s" }'%(toml(t),p) for t,p in v['nav'])
        return '  { %s = [\n%s,\n  ] },'%(toml(name),items)
    lines=['nav = [','  { "Home" = "index.md" },',section('Volume 1',v1)]
    if v2: lines.append(section('Volume 2',v2))
    lines+=['  { "About this edition" = "about.md" },',']']
    path=os.path.join(ROOT,'zensical.toml')
    s=open(path,encoding='utf-8').read()
    s2=re.sub(r'(?ms)^nav = \[.*?^\]\n','\n'.join(lines)+'\n',s,count=1)
    assert s2!=s or '\n'.join(lines) in s
    write(path,s2)

def toml(s):
    return '"%s"'%s.replace('\\','\\\\').replace('"','\\"')

def main():
    for f in os.listdir(WEB):
        if f.endswith('.md'): os.remove(os.path.join(WEB,f))
    v1=volume1(); v2=volume2()
    landing(v1,v2)
    write(os.path.join(WEB,'about.md'),ABOUT)
    tomlnav(v1,v2)
    n=len(v1['nav'])+(len(v2['nav']) if v2 else 0)+2
    print('wrote %d pages to web/docs'%n)

if __name__=='__main__': main()
