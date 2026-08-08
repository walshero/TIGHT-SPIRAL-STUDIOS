#!/usr/bin/env python3
"""
COMFORT-GATE — enforces the TSP Comfort Kernel by MEASUREMENT, not by guessing.

Why this exists
---------------
studio-eyes grounds contrast to `body` when it can't resolve a background, so it
HALTs light-on-dark text that is actually fine (the .cab-glyph/.lum-* false HALTs)
and it counts every `<a href>` and the SVG xmlns as an "offline break". An auditor
that cries wolf trains the founder to ignore it. This gate refuses to guess:

  1. CONTRAST  — renders the file in headless Chromium, walks each text node to its
                 REAL painted background, computes the ratio. Fails <4.5:1.
  2. LADDER    — requires the kernel's three light modes (day/dusk/night) and that
                 NIGHT actually goes dark (body bg luminance < 0.2). No dark => fail.
                 Every mode must pass contrast, not just the default.
  3. OFFLINE   — intercepts the network. A <a href> fires no request; a loaded CDN
                 font/script/img does. Fails only on a REAL external request.
  4. EMOJI     — pictographic emoji in visible text. Fails.

Every rule is a measurement. TICK-4: ships with canaries (comfort-gate-canary-*.html)
that PROVE it still catches a real white-on-white, a real missing-dark-mode, and a
real loaded CDN. A gate that stops false-positiving by going blind is broken the
other way.

Usage:  python3 comfort-gate.py <file.html> [<file.html> ...]
Exit 0 = all passed · 1 = a file failed · 2 = harness error
"""
import sys, re, os, json
try:
    from playwright.sync_api import sync_playwright
except Exception as e:
    print("comfort-gate: playwright unavailable:", e); sys.exit(2)

MODES = ["day", "dusk", "night"]

MEASURE = r"""
(mode) => {
  function lum(c){const[r,g,b]=c.map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b}
  function ratio(a,b){const L1=lum(a),L2=lum(b);return (Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05)}
  function parse(s){const m=s.match(/rgba?\(([^)]+)\)/);if(!m)return null;const p=m[1].split(',').map(parseFloat);return{rgb:[p[0],p[1],p[2]],a:p.length>3?p[3]:1}}
  function ebg(el){let e=el;while(e){const b=parse(getComputedStyle(e).backgroundColor);if(b&&b.a>0)return b.rgb;e=e.parentElement}return[255,255,255]}
  const bg=ebg(document.body);
  let min=99, worst=null, n=0;
  const els=document.querySelectorAll('p,li,span,a,h1,h2,h3,h4,h5,h6,td,th,button,summary,strong,em,label,dt,dd,figcaption,blockquote');
  for(const el of els){
    if(!el.getClientRects().length) continue;
    if(el.childElementCount) continue;
    const t=el.textContent.trim(); if(t.length<2) continue;
    const cs=getComputedStyle(el);
    if(cs.visibility==='hidden'||cs.display==='none'||parseFloat(cs.opacity)<0.3) continue;
    const fg=parse(cs.color); if(!fg||fg.a<0.5) continue;
    const r=ratio(fg.rgb, ebg(el)); n++;
    if(r<min){min=+r.toFixed(2); worst={sel:(el.className||el.tagName)+'', text:t.slice(0,32), ratio:+r.toFixed(2)}}
  }
  return {mode, bodyLum:+lum(bg).toFixed(3), min:+min.toFixed(2), n, worst};
}
"""

EMOJI = re.compile(r'[\U0001F000-\U0001FAFF☀-⛿✀-➿]')

def set_mode(pg, mode):
    # Kernel uses html[data-light]; also set body class fallbacks for pre-kernel files.
    pg.evaluate("""(m)=>{
      document.documentElement.setAttribute('data-light', m);
      document.body.classList.remove('day','dusk','night','softer','warm','daylight');
      if(m!=='day') document.body.classList.add(m);
    }""", mode)
    pg.wait_for_timeout(360)  # past the kernel's 180ms bg transition

def gate_file(pg_factory, path):
    fails = []
    external = []
    pg = pg_factory(external)
    try:
        pg.goto("file://" + os.path.abspath(path))
        pg.wait_for_timeout(300)
    except Exception as e:
        return ["LOAD ERROR: " + str(e)]
    # emoji (visible text)
    txt = pg.evaluate("()=>document.body.innerText")
    if EMOJI.search(txt or ""):
        fails.append("EMOJI in visible text (studio floor: none, ever)")
    # ladder + contrast per mode
    lums = {}
    for m in MODES:
        set_mode(pg, m)
        r = pg.evaluate(MEASURE, m)
        lums[m] = r["bodyLum"]
        if r["n"] == 0:
            fails.append(f"[{m}] no measurable text (render/selection failed)")
            continue
        if r["min"] < 4.5:
            w = r["worst"]
            fails.append(f"[{m}] CONTRAST {r['min']}:1 on '{w['text']}' ({w['sel']}) — needs 4.5")
    # night must actually be dark
    if lums.get("night", 1) >= 0.2:
        fails.append(f"NO DARK MODE — night body luminance {lums.get('night')} (kernel not mounted; must be < 0.2)")
    # offline: any external request that fired during load/mode cycling
    ext = sorted(set(u for u in external if not (u.startswith('file:') or u.startswith('data:') or u.startswith('blob:'))))
    for u in ext[:6]:
        host = re.sub(r'^https?://([^/]+).*', r'\1', u)
        fails.append(f"OFFLINE FLOOR BROKEN — loaded external {host}")
    pg.close()
    return fails

# ---- the ratchet -------------------------------------------------------------
# Added 2026-08-07 so this tick is MOUNTABLE ON THE HUB. Flat, it HALTs 23 of the
# hub's 131 surfaces — which is why the hub had never run the belt at all, and why
# every tick on it reached only the three files the spokes hold between them.
#
# The unit is a FILE, not a code: comfort-gate returns free-form failure strings,
# and inventing a code scheme for them is a change to a founder-facing gate, not a
# mounting chore. File-level is the same shape ratchet.py/floor-baseline.json
# already use and the studio already armed. It is WEAKER than the code-level
# ratchets on ticks 3-5: a new failure inside an already-red file is carried, not
# caught. Burn the list down and that weakness goes with it.
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'comfort-baseline.json')

def load_baseline():
    if os.path.exists(BASELINE):
        with open(BASELINE) as f:
            return set(json.load(f).get('debt', []))
    return None

def key_for(path, repo):
    ap  = os.path.abspath(path)
    rel = os.path.relpath(ap, os.getcwd())
    if rel.startswith(os.pardir):
        rel = os.path.basename(ap)
    return repo + '/' + rel.replace(os.sep, '/')

def main(argv):
    ratchet = '--ratchet' in argv
    do_init = '--init' in argv
    merge   = '--merge' in argv
    repo    = next((a.split('=', 1)[1] for a in argv if a.startswith('--repo=')),
                   os.path.basename(os.getcwd()))
    argv    = [a for a in argv if not a.startswith('--')]
    if not argv:
        print("usage: comfort-gate.py [--ratchet|--init] [--repo=NAME] <file.html> [...]"); return 2
    base = load_baseline() if (ratchet and not do_init) else set()
    if ratchet and not do_init and base is None:
        print("HALT - --ratchet asked for but comfort-baseline.json is missing.\n"
              "       A gate that cannot find its baseline does not pass; it stops.")
        return 2
    frozen = set(load_baseline() or set()) if (do_init and merge) else set()
    with sync_playwright() as pw:
        try: browser = pw.chromium.launch()
        except Exception: browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        def factory(sink):
            ctx = browser.new_context(viewport={"width": 390, "height": 844})
            def route(r):
                u = r.request.url
                if u.startswith('file:') or u.startswith('data:') or u.startswith('blob:'):
                    r.continue_()
                else:
                    sink.append(u); r.abort()
            ctx.route("**/*", route)
            return ctx.new_page()
        halted = 0; carried = 0
        for path in argv:
            fails = gate_file(factory, path)
            name = path.split('/')[-1]
            k = key_for(path, repo)
            if fails and do_init:
                frozen.add(k)
            if fails:
                if ratchet and not do_init and k in base:
                    carried += 1
                    print(f"\nDEBT  {name}  — carried by the ratchet, counted not forgiven")
                    for f in fails[:3]:
                        print("   " + f)
                    continue
                halted += 1
                print(f"\nHALT  {name}")
                for f in fails[:10]:
                    print("   " + f)
            else:
                print(f"\npass  {name}  — day/dusk/night all >=4.5, dark confirmed, offline, no emoji")
        browser.close()
        if do_init:
            with open(BASELINE, 'w') as f:
                json.dump({
                    'created': '2026-08-07',
                    'why': ('Accessibility-floor debt frozen the day the belt was mounted on '
                            'the hub. Carried, not forgiven. Any NEW red file blocks. '
                            'The list may only shrink.'),
                    'rule': 'Fix a file, it leaves the baseline forever.',
                    'debt': sorted(frozen),
                }, f, indent=1)
                f.write('\n')
            print(f"\nBASELINE WRITTEN - {len(frozen)} file(s) carry known comfort debt.")
            print("These do not block. Everything else does. The ratchet is armed.")
            return 0
        print(f"\n=== {halted} HALT of {len(argv)} ==="
              + (f"  ({carried} carried as debt)" if carried else ""))
        return 1 if halted else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
