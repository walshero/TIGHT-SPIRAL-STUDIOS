#!/usr/bin/env python3
"""
one-thing-gate.py  ·  Tight Spiral Studios  ·  the teeth on the scene-first floor
=================================================================================
Canon this enforces (already ruled, previously toothless):
  - SCENE-FIRST FLOOR (locked 2026-06-27): a game opens by landing the player
    in a scene, never a wall of text.
  - ONE THING AT A TIME (Matt, 2026-07-12): the entry offers exactly ONE
    invitation. Expansion is the player's to pull, not the screen's to shove.
  - TABLEAU COHERENCE + CLEAR INVITATION: the first paint reads as one picture
    that says what to do.

This gate measures the REAL first paint (headless Chromium, 1280x800 laptop),
not the source. It is arithmetic, not judgment.

Division of teeth (one canon writes, others read):
  - IMAGE-AREA and CONTRAST across the whole page  -> studio-eyes-sweep.py /
    preship-contrast-gate.py already own that. This gate does NOT re-litigate it.
  - THE ENTRY PAINT — wall, invitation-count, entry-tableau — is THIS gate's lane.

Exit 1 if any CRITICAL or HIGH finding. That is the ship block.

Usage:  python3 one-thing-gate.py <file-or-glob> [<file> ...]
"""
import sys, glob, json, pathlib

# ---- thresholds (the arithmetic; change here, nowhere else) -------------------
WALL_PROSE_WORDS   = 40     # prose words on entry that, with no real visual, = a wall
WALL_VISUAL_RATIO  = 0.20   # a visual smaller than this doesn't count as "a scene"
TABLEAU_FLOOR      = 0.50   # entry should be >=50% image (WARN here; studio-eyes = hard gate)
LOAD_CTRL_WARN     = 3      # more than this many controls competing on entry = clutter

MEASURE_JS = r"""
() => {
  const vw = window.innerWidth, vh = window.innerHeight, VA = vw*vh;
  const vis = el => { const s=getComputedStyle(el);
    if (s.display==='none'||s.visibility==='hidden'||parseFloat(s.opacity||'1')===0) return false;
    const r=el.getBoundingClientRect(); return r.width>0 && r.height>0; };
  const inVp = el => { const r=el.getBoundingClientRect();
    return r.top < vh && r.bottom > 0 && r.left < vw && r.right > 0; };

  // largest visual painted in the entry viewport
  const visuals=[...document.querySelectorAll('img,svg,canvas,video,picture')].filter(e=>vis(e)&&inVp(e));
  let maxA=0, vtag='';
  for (const e of visuals){ const r=e.getBoundingClientRect();
    const a=Math.max(0,Math.min(r.right,vw)-Math.max(r.left,0))*Math.max(0,Math.min(r.bottom,vh)-Math.max(r.top,0));
    if(a>maxA){maxA=a; vtag=e.tagName.toLowerCase();} }
  const visualRatio = maxA/VA;

  // interactive controls painted in the entry viewport (dedupe nested)
  let ctrls=[...document.querySelectorAll('button,a[href],[role=button],[onclick],input,select,summary,[tabindex]')]
              .filter(e=>vis(e)&&inVp(e));
  ctrls = ctrls.filter(e=>!ctrls.some(o=>o!==e && o.contains(e)));

  // PRIMARY invitation = a large, filled/weighted call to act
  const primary = ctrls.filter(e=>{ const r=e.getBoundingClientRect(); const s=getComputedStyle(e);
    const w=parseInt(s.fontWeight)||400; return r.width>=90 && r.height>=40 && w>=600; });

  // prose (visible viewport text NOT inside a control)
  const cset=new Set(ctrls);
  const inCtrl=n=>{let p=n;while(p){if(cset.has(p))return true;p=p.parentElement;}return false;};
  let prose='';
  const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
  while(w.nextNode()){ const t=w.currentNode, el=t.parentElement;
    if(!el||!vis(el)||!inVp(el)||inCtrl(el)) continue; prose+=' '+t.nodeValue; }
  const proseWords=(prose.trim().match(/\S+/g)||[]).length;

  const emoji=((document.body.innerText||'').match(/\p{Extended_Pictographic}/gu)||[]).length;

  // navigation floor: every game needs a Home control and a Back control (present in DOM, even if hidden on the home screen)
  const navName = el => ((el.textContent||'')+' '+(el.getAttribute('aria-label')||'')+' '+(el.getAttribute('title')||'')).toLowerCase();
  const allctrl=[...document.querySelectorAll('button,a[href],[role=button]')];
  const hasHome = allctrl.some(e=>/\bhome\b/.test(navName(e)));
  const hasBack = allctrl.some(e=>/\bback\b/.test(navName(e)));

  return { vw,vh, visualRatio:+visualRatio.toFixed(3), visualTag:vtag, hasHome, hasBack,
           ctrlCount:ctrls.length, primaryCount:primary.length, proseWords, emoji,
           primaryLabels:primary.map(e=>(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,32)),
           ctrlLabels:ctrls.map(e=>(e.textContent||e.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ').slice(0,22)).filter(Boolean).slice(0,24) };
}
"""

def grade(m):
    findings=[]
    if m["emoji"]>0:
        findings.append(("CRITICAL", f"{m['emoji']} emoji on entry (studio floor: none, ever)"))
    if m["visualRatio"] < WALL_VISUAL_RATIO and m["proseWords"] > WALL_PROSE_WORDS:
        findings.append(("CRITICAL", f"WALL: {m['proseWords']} words of prose, no real scene "
                                     f"(largest visual only {m['visualRatio']*100:.0f}% of entry)"))
    if m["primaryCount"] == 0:
        findings.append(("HIGH", "NO clear invitation on entry — nothing says what to do"))
    elif m["primaryCount"] > 1:
        findings.append(("HIGH", f"{m['primaryCount']} co-equal invitations on entry "
                                 f"({', '.join(m['primaryLabels'])}) — want exactly ONE"))
    if m["visualRatio"] < TABLEAU_FLOOR:
        findings.append(("WARN", f"entry tableau {m['visualRatio']*100:.0f}% image "
                                 f"(<50%; studio-eyes owns the hard gate)"))
    if m["ctrlCount"] > LOAD_CTRL_WARN:
        findings.append(("WARN", f"{m['ctrlCount']} controls compete on entry before the player acts"))
    return findings

def main(argv):
    paths=[]
    for a in argv: paths += sorted(glob.glob(a)) or [a]
    paths=[p for p in paths if pathlib.Path(p).is_file()]
    if not paths:
        print("one-thing-gate: no files matched", file=sys.stderr); return 2
    from playwright.sync_api import sync_playwright
    worst=0
    with sync_playwright() as pw:
        try: browser=pw.chromium.launch()
        except Exception:
            browser=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        page=browser.new_page(viewport={"width":1280,"height":800})
        print("="*72)
        print("ONE-THING GATE  ·  entry-paint teeth  ·  1280x800")
        print("="*72)
        for p in paths:
            url=pathlib.Path(p).resolve().as_uri()
            try:
                page.goto(url, wait_until="networkidle", timeout=15000)
            except Exception:
                page.goto(url, wait_until="load", timeout=15000)
            page.wait_for_timeout(400)
            m=page.evaluate(MEASURE_JS)
            f=grade(m)
            rank={"CRITICAL":3,"HIGH":2,"WARN":1}
            sev=max([rank[s] for s,_ in f], default=0)
            worst=max(worst,sev)
            verdict = "SHIP-BLOCK" if sev>=2 else ("WARN" if sev==1 else "PASS")
            print(f"\n{pathlib.Path(p).name}   ->  {verdict}")
            print(f"   entry: {m['visualRatio']*100:.0f}% image ({m['visualTag'] or 'none'}) · "
                  f"{m['primaryCount']} primary invite(s) · {m['ctrlCount']} controls · "
                  f"{m['proseWords']} prose words · {m['emoji']} emoji")
            for s,msg in f:
                mark = "X" if rank[s]>=2 else "!"
                print(f"     [{mark}] {s}: {msg}")
            if not f: print("     clean entry: one scene, one invitation")
        browser.close()
    print("\n"+"-"*72)
    print("RESULT:", "SHIP-BLOCK — a build did not clear the entry gate" if worst>=2
          else ("WARN — entries readable but not yet ideal" if worst==1 else "PASS — all entries clean"))
    return 1 if worst>=2 else 0

if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))
