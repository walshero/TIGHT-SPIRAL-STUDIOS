#!/usr/bin/env python3
"""
VERSION-STAMP — every page shows "Last updated <date> · v<N> <hash>" at the top,
so nobody plays a stale game.

COMPUTED > TYPED: the date is document.lastModified (live, per serve); the version is
derived from git — v<N> = number of commits that ever touched the file, <hash> = short
hash of the last one. This script stamps mechanically; a hand-typed version is the
hollow-claim bug and is exactly what this replaces. Idempotent: replace-don't-add.

Usage:
  python3 version-stamp.py <file.html> [...]   stamp (run BEFORE commit; stamps N+1
                                               since the commit about to happen bumps it)
  python3 version-stamp.py --check <files>     exit 1 if any page lacks stamp+version
"""
import sys, os, re, subprocess

MARK_OPEN  = '<span class="se-version" '
STYLE = 'style="font:inherit;opacity:.85"'

def git_version(path):
    n = subprocess.run(["git","rev-list","--count","HEAD","--",path],
                       capture_output=True,text=True).stdout.strip()
    h = subprocess.run(["git","log","-1","--format=%h","--",path],
                       capture_output=True,text=True).stdout.strip()
    n = int(n or 0) + 1          # the commit this stamp ships in
    return f"v{n}", h or "new"

STAMP_BLOCK = '''<p class="se-stamp" style="margin:.4rem 0 1rem;font-family:ui-monospace,'SF Mono',Menlo,monospace;font-size:.76rem;opacity:.92;display:flex;align-items:center;gap:.45rem"><span id="seUpdated">Last updated&hellip;</span>{VER}</p>
<script>(function(){var u=document.getElementById('seUpdated');if(!u)return;var d=new Date(document.lastModified);u.textContent=isNaN(d.getTime())?'Last updated recently':'Last updated '+d.toLocaleDateString(undefined,{year:'numeric',month:'long',day:'numeric'});})();</script>'''

def ver_span(path):
    v,h = git_version(path)
    return f'{MARK_OPEN}{STYLE}>&middot; {v} <span style="opacity:.75">{h}</span></span>'

def stamp(path):
    s = open(path,encoding='utf-8').read(); orig = s
    span = ver_span(path)
    # 1) strip any prior version span (idempotent)
    s = re.sub(r'<span class="se-version" [^>]*>.*?</span>', '', s, flags=re.S)
    # 2) existing stamp element? append version as its sibling
    m = re.search(r'(<[a-z]+[^>]*id="(?:seUpdated|faceUpdated|kUpdated)"[^>]*>.*?</[a-z]+>)', s, re.S)
    if m:
        s = s.replace(m.group(1), m.group(1)+' '+span, 1)
    else:
        # 3) no stamp at all: insert full stamp block after chrome header, else after <body>
        blk = STAMP_BLOCK.replace('{VER}', span)
        hm = re.search(r'(</header>)', s)
        if hm: s = s.replace(hm.group(1), hm.group(1)+'\n'+blk, 1)
        else:
            bm = re.search(r'(<body[^>]*>)', s)
            if not bm: return 'SKIP (no body)'
            s = s.replace(bm.group(1), bm.group(1)+'\n'+blk, 1)
    if s != orig:
        open(path,'w',encoding='utf-8').write(s)
        return 'stamped '+ver_span.__doc__ if False else 'stamped'
    return 'unchanged'

def check(paths):
    bad = []
    for p in paths:
        s = open(p,encoding='utf-8').read()
        if 'se-version' not in s or not re.search(r'id="(seUpdated|faceUpdated|kUpdated)"', s):
            bad.append(p)
    for p in bad: print("MISSING stamp/version:", p)
    return 1 if bad else 0

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == '--check':
        sys.exit(check(args[1:]))
    for p in args:
        print(f"{stamp(p):10} {p}  ({' '.join(git_version(p))})")
