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

# THE INSTRUCTION WALL (added 2026-08-07, founder-named defect)
# "A wall of directions that were irrelevant and unreadable for my phone."
# Two thresholds, both about travel-before-action rather than words-on-screen:
INSTRUCTION_WORDS  = 60     # prose sitting ABOVE the first thing you can do
SCREENS_TO_ACTION  = 1.0    # if the first control is more than one screen down, it is a wall

# VIEWPORTS. The phone is BINDING - it is the founder's primary surface and the one
# an RP reader uses. The laptop is measured too, because a defect that shows only on
# the wide screen is still a defect, but the phone is the one that decides.
# Until today this gate measured 1280x800 ONLY, so the studio's wall-detector was the
# single instrument that never saw a phone. comfort-gate, comfort-audit and the SVG
# floor all measure 390/330. This one did not.
VIEWPORTS = [(390, 844, 'phone'), (1280, 800, 'laptop')]

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

  // \p{Extended_Pictographic} also matches the copyright and registered-trademark signs --
  // real legal/citation glyphs used across the corpus for rubric attribution (AAC&U,
  // etc.), not decorative emoji. Excluded.
  const emoji=((document.body.innerText||'').match(/\p{Extended_Pictographic}/gu)||[]).filter(c=>c!=='©'&&c!=='®').length;

  // navigation floor: every game needs a Home control and a Back control (present in DOM, even if hidden on the home screen)
  const navName = el => ((el.textContent||'')+' '+(el.getAttribute('aria-label')||'')+' '+(el.getAttribute('title')||'')).toLowerCase();
  const allctrl=[...document.querySelectorAll('button,a[href],[role=button]')];
  const hasHome = allctrl.some(e=>/\bhome\b/.test(navName(e)));
  const hasBack = allctrl.some(e=>/\bback\b/.test(navName(e)));

  // THE WALL THE FOUNDER ACTUALLY HITS.
  // Everything above measures the entry VIEWPORT. That misses the defect he named:
  // "a wall of directions, irrelevant and unreadable on my phone." In-viewport prose
  // actually goes DOWN on a narrow screen (less fits), so the old measure scored a
  // phone wall as an improvement. The honest question is not how much text is on
  // screen - it is HOW FAR YOU MUST TRAVEL BEFORE YOU CAN ACT.
  // CHROME IS NOT THE ACTION. The comfort control, the nav rail, the skip link and the
  // back/home buttons are furniture - they sit at y=0 on every studio page, so counting
  // them as "the first thing you can do" reports 0 words before action for a page that
  // is nothing but directions. The same pollution the 2026-08-03 ledger flagged for the
  // invitation count, hitting a different measure. Furniture is excluded by container
  // and by accessible name, never by tag.
  const CHROME_NAME=/\b(comfort|settings|theme|dark|light|text size|bigger|softer|skip|back|home|menu)\b/i;
  const chromeBox=e=>!!e.closest('nav,header,[class*="se-"],[id*="se-"],[class*="comfort"],[class*="skip"]');
  const docCtrls=[...document.querySelectorAll('button,a[href],[role=button],[onclick],input,select,summary')]
                   .filter(e=>vis(e))
                   .filter(e=>{ const n=((e.textContent||'')+' '+(e.getAttribute('aria-label')||'')).trim();
                                return !chromeBox(e) && !CHROME_NAME.test(n); });
  let firstTop=null;
  for (const e of docCtrls){ const t=e.getBoundingClientRect().top+window.scrollY;
    if(firstTop===null||t<firstTop) firstTop=t; }
  const screensToAction = firstTop===null ? null : +(firstTop/vh).toFixed(2);
  let pre='';
  if(firstTop!==null){
    const w2=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    while(w2.nextNode()){ const t=w2.currentNode, el=t.parentElement;
      if(!el||!vis(el)||inCtrl(el)) continue;
      if(el.getBoundingClientRect().top+window.scrollY < firstTop) pre+=' '+t.nodeValue; }
  }
  const proseBeforeAction=(pre.trim().match(/\S+/g)||[]).length;
  // horizontal scroll is a phone-only failure and always a defect
  const hOverflow = document.documentElement.scrollWidth > vw + 2;

  return { vw,vh, visualRatio:+visualRatio.toFixed(3), visualTag:vtag, hasHome, hasBack,
           screensToAction, proseBeforeAction, hOverflow,
           ctrlCount:ctrls.length, primaryCount:primary.length, proseWords, emoji,
           primaryLabels:primary.map(e=>(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,32)),
           ctrlLabels:ctrls.map(e=>(e.textContent||e.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ').slice(0,22)).filter(Boolean).slice(0,24) };
}
"""

def grade(m, vp='laptop'):
    """Return (severity, CODE, message). The CODE is the ratchet's unit — it must
    stay stable while the message carries the counts that move build to build."""
    findings=[]
    # --- the instruction wall. Phone-binding: a wall you must scroll past to act. ---
    if m.get("proseBeforeAction", 0) > INSTRUCTION_WORDS:
        findings.append(("CRITICAL" if vp == 'phone' else "HIGH", "INSTRUCTION-WALL",
                         f"{m['proseBeforeAction']} words of directions sit above the first "
                         f"control on {vp} - the player must read before they may act"))
    if m.get("screensToAction") is not None and m["screensToAction"] > SCREENS_TO_ACTION:
        findings.append(("CRITICAL" if vp == 'phone' else "HIGH", "ACTION-BELOW-FOLD",
                         f"first control is {m['screensToAction']} screens down on {vp} - "
                         f"nothing actionable is reachable without scrolling"))
    if m.get("hOverflow"):
        findings.append(("HIGH", "H-OVERFLOW",
                         f"the page scrolls sideways at {m['vw']}px - content runs off {vp}"))
    if m["emoji"]>0:
        findings.append(("CRITICAL", "EMOJI", f"{m['emoji']} emoji on entry (studio floor: none, ever)"))
    if m["visualRatio"] < WALL_VISUAL_RATIO and m["proseWords"] > WALL_PROSE_WORDS:
        findings.append(("CRITICAL", "WALL", f"WALL: {m['proseWords']} words of prose, no real scene "
                                     f"(largest visual only {m['visualRatio']*100:.0f}% of entry)"))
    if m["primaryCount"] == 0:
        findings.append(("HIGH", "NO-INVITE", "NO clear invitation on entry - nothing says what to do"))
    elif m["primaryCount"] > 1:
        findings.append(("HIGH", "MULTI-INVITE", f"{m['primaryCount']} co-equal invitations on entry "
                                 f"({', '.join(m['primaryLabels'])}) - want exactly ONE"))
    if m["visualRatio"] < TABLEAU_FLOOR:
        findings.append(("WARN", "SUB-50-TABLEAU", f"entry tableau {m['visualRatio']*100:.0f}% image "
                                 f"(<50%; studio-eyes owns the hard gate)"))
    if m["ctrlCount"] > LOAD_CTRL_WARN:
        findings.append(("WARN", "CTRL-CLUTTER", f"{m['ctrlCount']} controls compete on entry before the player acts"))
    return findings

# ---- the ratchet -------------------------------------------------------------
# Same shape as floor-baseline.json / gate-baseline.json, and the same one-way law:
# today's debt is CARRIED, never forgiven; anything new BLOCKS; the list may only
# shrink. Without this the gate is unmountable — Tableau Sweep #2 (2026-08-03) put
# 31 of 38 builds at SHIP-BLOCK, and a belt that is red on every push is a belt
# everyone learns to ignore. That is exactly how floor.yml got disarmed in July.
BASELINE = pathlib.Path(__file__).resolve().parent / "one-thing-baseline.json"
BLOCKING = ("CRITICAL", "HIGH")

def load_baseline():
    if BASELINE.exists():
        return json.loads(BASELINE.read_text())
    return None

def key_for(p, repo):
    """Baseline key = <repo>/<path relative to the repo root>.

    NOT the bare basename. Three of the five repos ship an index.html; keyed by
    basename they collide into one entry and the last one written silently grants
    or denies the other two. The belt runs one gate against many repos, so the key
    has to name the repo."""
    try:
        rel = pathlib.Path(p).resolve().relative_to(pathlib.Path.cwd())
    except ValueError:
        rel = pathlib.Path(pathlib.Path(p).name)
    return f"{repo}/{rel.as_posix()}"

def main(argv):
    ratchet = "--ratchet" in argv
    init    = "--init" in argv
    repo    = next((a.split("=",1)[1] for a in argv if a.startswith("--repo=")),
                   pathlib.Path.cwd().name)
    argv    = [a for a in argv if not a.startswith("--")]
    paths=[]
    for a in argv: paths += sorted(glob.glob(a)) or [a]
    paths=[p for p in paths if pathlib.Path(p).is_file()]
    if not paths:
        print("one-thing-gate: no files matched", file=sys.stderr); return 2

    base = (load_baseline() or {}).get("debt", {}) if (ratchet and not init) else {}
    if ratchet and not init and not BASELINE.exists():
        print("HALT - --ratchet asked for but one-thing-baseline.json is missing.\n"
              "       A gate that cannot find its baseline does not pass; it stops.",
              file=sys.stderr)
        return 2

    from playwright.sync_api import sync_playwright
    worst=0; frozen={}
    with sync_playwright() as pw:
        try: browser=pw.chromium.launch()
        except Exception:
            browser=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pages={vp:(browser.new_page(viewport={"width":w,"height":h}), w, h)
               for w,h,vp in VIEWPORTS}
        print("="*72)
        print("ONE-THING GATE  ·  entry-paint teeth  ·  "
              + " + ".join(f"{w}x{h} {vp}" for w,h,vp in VIEWPORTS)
              + ("  ·  RATCHET" if ratchet and not init else ""))
        print("="*72)
        for p in paths:
            url=pathlib.Path(p).resolve().as_uri()
            f=[]; seen=set(); shots={}
            for w,h,vp in VIEWPORTS:
                page=pages[vp][0]
                try:
                    page.goto(url, wait_until="networkidle", timeout=15000)
                except Exception:
                    page.goto(url, wait_until="load", timeout=15000)
                page.wait_for_timeout(400)
                mv=page.evaluate(MEASURE_JS)
                shots[vp]=mv
                # dedupe by CODE across viewports, keeping the worst severity. The phone
                # runs first, so a phone CRITICAL is what survives for a shared code.
                for s,c,msg in grade(mv, vp):
                    if c in seen: continue
                    seen.add(c); f.append((s,c,msg))
            m=shots[VIEWPORTS[0][2]]          # the phone is the binding surface
            name=key_for(p, repo)
            if init:
                frozen[name]=sorted({c for s,c,_ in f if s in BLOCKING})
            rank={"CRITICAL":3,"HIGH":2,"WARN":1}
            known=set(base.get(name, []))
            carried=[(s,c,msg) for s,c,msg in f if s in BLOCKING and c in known]
            live   =[(s,c,msg) for s,c,msg in f if not (s in BLOCKING and c in known)]
            sev=max([rank[s] for s,_,_ in live], default=0)
            worst=max(worst,sev)
            verdict = "SHIP-BLOCK" if sev>=2 else ("WARN" if sev==1 else "PASS")
            if ratchet and not init and carried and sev<2:
                verdict = "PASS (debt carried)"
            print(f"\n{name}   ->  {verdict}")
            for w,h,vp in VIEWPORTS:
                s=shots[vp]
                sta = '-' if s.get('screensToAction') is None else f"{s['screensToAction']}"
                print(f"   {vp:6s} {w:>4}px: {s['visualRatio']*100:3.0f}% image · "
                      f"{s['primaryCount']} invite · {s['ctrlCount']} ctrl · "
                      f"{s.get('proseBeforeAction',0):>4} words before first action · "
                      f"{sta} screens to act")
            for s,c,msg in carried:
                print(f"     [.] DEBT {c}: {msg}")
            for s,c,msg in live:
                mark = "X" if rank[s]>=2 else "!"
                print(f"     [{mark}] {s} {c}: {msg}")
            if not f: print("     clean entry: one scene, one invitation")
        browser.close()

    if init:
        # --merge keeps entries already frozen for OTHER repos; the belt seeds one
        # repo at a time and a plain rewrite would drop the others' debt.
        merged = dict((load_baseline() or {}).get("debt", {})) if "--merge" in sys.argv else {}
        merged.update({k:v for k,v in frozen.items() if v})
        BASELINE.write_text(json.dumps({
            "created": "2026-08-07",
            "why": ("Entry-paint debt frozen the day the one-thing-gate was mounted on the "
                    "studio belt. These findings are CARRIED - counted, not forgiven. Anything "
                    "NOT in this list blocks. The list may only shrink."),
            "rule": "Fix an entry, it leaves the baseline forever. It can never quietly regress again.",
            "debt": dict(sorted(merged.items())),
        }, indent=1) + "\n")
        carried_n=len(merged)
        print(f"\nBASELINE WRITTEN - {carried_n} file(s) carry known entry debt.")
        print("These do not block. Everything else does. The ratchet is armed.")
        return 0

    print("\n"+"-"*72)
    print("RESULT:", "SHIP-BLOCK - a build did not clear the entry gate" if worst>=2
          else ("WARN - entries readable but not yet ideal" if worst==1 else "PASS - all entries clean"))
    return 1 if worst>=2 else 0

if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))
