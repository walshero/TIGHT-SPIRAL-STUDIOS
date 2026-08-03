#!/usr/bin/env python3
"""
reply-shape-gate.py  ·  Tight Spiral Studios  ·  the pre-send enforcer.
os-block-bodyguards.md named it MISSING: "a reply-shape check that runs before send.
It does not exist. Naming it here is not building it." This builds it.

Turns three behavioral guards into arithmetic, run on a DRAFT reply before it lands:
  DOORMAN  (Guard 1): line one answers; nothing throat-clears above it.
  MIRROR   (Guard 4): no perform-listening openers, no banned words.
  TLDR KID (Guard 3): verdict on line one; a buried lede is an RP accessibility defect.
Plus NO-FARMING (Guard 2, already arithmetic): <=2 questions to the founder, 1 is the target.

exit 0 = the reply may land.  exit 1 = HALT, reshape before send.
Usage:  reply-shape-gate.py <draft.md>   |   producing-cmd | reply-shape-gate.py -
"""
import sys, re

BANNED_OPENERS = [   # throat-clearing that must never precede the answer (Doorman)
  r"before i (answer|start|begin|dive|get)", r"let me\b", r"let'?s\b", r"i'?ll\b",
  r"i'?m going to", r"i'?m about to", r"to answer( your)?\b", r"first,? ",
  r"great question", r"good question", r"just to\b", r"as you (know|mentioned|said)",
  r"i understand\b", r"i want to\b", r"i'?d be happy", r"happy to\b", r"sure[,!]",
  r"certainly\b", r"of course\b", r"thanks? (for|you)", r"i can (help|do)\b",
  r"here'?s what i('?ll| will| can| am| plan| want)", r"in this (reply|response)",
]
BANNED_ANYWHERE = [  # Mirror + banned words, anywhere (founder-canon: cut on sight)
  r"i hear you", r"\bgenuinely\b", r"\bhonestly\b", r"\bstraightforward\b",
  r"as an ai\b", r"i appreciate", r"that'?s a (great|good|fair) (point|question)",
]
MAX_Q = 2; LONG_LINES = 48; LONG_CHARS = 3400

def first_content_line(text):
    for raw in text.splitlines():
        s = re.sub(r'^[#>\-\*\d\.\)\s`]+', '', raw.strip())
        if s: return s
    return ""

def grade(text):
    f=[]; low=text.lower(); l1=first_content_line(text); l1l=l1.lower()
    for pat in BANNED_OPENERS:
        if re.match(pat, l1l):
            f.append(("HALT","DOORMAN", f'line one throat-clears: "{l1[:52]}"')); break
    if l1.endswith("?"): f.append(("HALT","DOORMAN","line one is a question, not the answer"))
    if not l1: f.append(("HALT","DOORMAN","reply has no content line"))
    for pat in BANNED_ANYWHERE:
        m=re.search(pat, low)
        if m: f.append(("HALT","MIRROR", f'banned phrase: "{m.group(0)}"'))
    q=text.count("?")
    if q>MAX_Q: f.append(("HALT","NO-FARMING", f"{q} questions (cap {MAX_Q}, target 1) — cut the weakest"))
    elif q==MAX_Q: f.append(("WARN","NO-FARMING", f"{q} questions — target 1; decide any you're >=75% on"))
    nlines=len([x for x in text.splitlines() if x.strip()])
    if nlines>LONG_LINES or len(text)>LONG_CHARS:
        f.append(("WARN","TLDR-KID", f"{nlines} lines / {len(text)} chars over two screens — verdict on line one, offer the rest"))
    return f

def main(argv):
    src = sys.stdin.read() if (not argv or argv[0]=="-") else open(argv[0],encoding="utf-8").read()
    f=grade(src); halt=any(s=="HALT" for s,_,_ in f)
    print("="*60); print("REPLY-SHAPE GATE  ·  pre-send enforcer (bodyguards 1/2/3/4)"); print("="*60)
    for sev,g,msg in f: print(f"  [{'X' if sev=='HALT' else '!'}] {g}: {msg}")
    if not f: print("  clean: line one answers, no throat-clearing, <=1 question, tight.")
    print("-"*60); print("HALT — reshape before send." if halt else "PASS — the reply may land.")
    return 1 if halt else 0

if __name__=="__main__": sys.exit(main(sys.argv[1:]))
