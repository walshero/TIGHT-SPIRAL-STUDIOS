#!/usr/bin/env python3
"""
STUDIO FINGERS · FEEL PROBE                               Tight Spiral Productions
-----------------------------------------------------------------------------
Added 2026-11-08 (founder: "improve playtesting and studio builds ergo art, physics,
screen cohesion, intuitive UI and gameplay"). Every other sense grades what the screen
LOOKS like at rest. Nothing measured what a tap FEELS like: whether the game answers,
how fast, and whether the motion holds together while it does.

It plays the build on a touch phone (390x844, hasTouch) and measures, in the browser:

THE FLOORS
  F1 DEAD TAP      a visible, enabled control that changes no pixel within 400 ms   HALT
                   of a tap. Doherty threshold (Doherty & Thadani 1982, IBM: under
                   400 ms keeps a user engaged). A sound-only answer still fails:
                   accessibility adds channels, so every tap answers on screen.
  F2 SLOW ANSWER   first visible change lands after 100 ms                          WARN
                   (Card, Moran & Newell's ~100 ms perceptual cycle; Swink, Game Feel,
                   2009: under ~100 ms a response reads as caused by the hand).
  F3 SCRIPT ERROR  any uncaught exception or console.error during play              HALT
  F4 FRAME PACING  p95 frame interval over 33 ms (below 30 fps) while animating     WARN
                   long tasks over 200 ms block input outright                      HALT
  F5 BROKEN MOTION a rendered element whose transform or box is NaN/Infinity, or a  HALT
                   moving element that leaves the page box for good (physics escape)

WHAT IT DOES NOT CLAIM
  It cannot tell you a game is fun. It tells you the floor under fun is there: every
  tap answers, fast, without errors, at a steady frame rate. The seats judge the rest.

USAGE
  feel-probe.py --self-test          grade the two canaries first
  feel-probe.py <build.html> [--taps 30] [--json out.json]
  exit 1 on any HALT.
"""
import sys, os, json, io, time

DEAD_MS, SLOW_MS = 400, 100
P95_WARN_MS, LONGTASK_HALT_MS = 33.4, 200

INIT = r"""
(() => {
  const F = window.__feel = {frames: [], errors: [], long: []};
  let last = 0;
  const tick = t => { if (last) F.frames.push(t - last); last = t; requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
  addEventListener('error', e => F.errors.push(String(e.message || e.error || e)));
  addEventListener('unhandledrejection', e => F.errors.push('unhandled rejection: ' + String(e.reason)));
  const ce = console.error.bind(console);
  console.error = (...a) => { F.errors.push(a.map(String).join(' ').slice(0, 200)); ce(...a); };
  try { new PerformanceObserver(l => l.getEntries().forEach(e => F.long.push(e.duration)))
          .observe({type: 'longtask', buffered: true}); } catch (e) {}
})();
"""

CONTROLS = r"""() => {
  const vis = el => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    return r.width >= 8 && r.height >= 8 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0.05; };
  const out = [];
  document.querySelectorAll('[data-feel]').forEach(e => e.removeAttribute('data-feel'));
  const els = document.querySelectorAll('button,[role=button],a[href^="#"],input[type=range],summary,[onclick],canvas');
  let n = 0;
  for (const el of els) {
    if (!vis(el) || el.disabled || el.getAttribute('aria-disabled') === 'true') continue;
    const r0 = el.getBoundingClientRect();
    if (r0.right <= 0 || r0.left >= innerWidth) continue;   // parked off-canvas (a skip link until focused)
    if (el.closest('.se-chrome,[data-studio-chrome],header.topbar')) continue;   // studio chrome is not the game
    el.setAttribute('data-feel', String(n));
    out.push({i: n++, sel: el.tagName.toLowerCase() + (el.id ? '#' + el.id : ''),
              label: (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 30)});
  }
  return out;
}"""

MOTION = r"""() => {
  const bad = [], H = document.documentElement.scrollHeight + 400, W = document.documentElement.scrollWidth + 400;
  for (const el of document.querySelectorAll('body *')) {
    const t = getComputedStyle(el).transform;
    const r = el.getBoundingClientRect();
    const nan = (t && /NaN|Infinity/.test(t)) || [r.x, r.y, r.width, r.height].some(v => !isFinite(v));
    if (nan) { bad.push('NaN in ' + el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + ' ' + t); continue; }
    if (el.getAnimations && el.getAnimations().length === 0 && t !== 'none' &&
        (r.top + scrollY > H || r.left + scrollX > W || r.bottom + scrollY < -400 || r.right + scrollX < -400))
      bad.push('escaped the page: ' + el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') +
               ' at ' + Math.round(r.left) + ',' + Math.round(r.top));
  }
  return bad.slice(0, 8);
}"""

def _changed(a, b, thresh=0.002):
    """Fraction of pixels that moved more than a hair, on a 1/4-size thumbnail."""
    from PIL import Image, ImageChops
    A = Image.open(io.BytesIO(a)).convert('L').resize((97, 211))
    B = Image.open(io.BytesIO(b)).convert('L').resize((97, 211))
    d = ImageChops.difference(A, B).point(lambda v: 255 if v > 10 else 0)
    frac = d.histogram()[255] / (97 * 211)
    return frac > thresh, frac

def pct(xs, p):
    if not xs: return 0
    xs = sorted(xs); return xs[min(len(xs)-1, int(p * len(xs)))]

def probe(path, taps=30):
    from playwright.sync_api import sync_playwright
    url = 'file://' + os.path.abspath(path)
    halts, warns, rows = [], [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={'width': 390, 'height': 844}, has_touch=True, is_mobile=True,
                            device_scale_factor=1, reduced_motion='no-preference')
        ctx.add_init_script(INIT)
        # a tap that would leave the build is caught here, never followed
        ctx.route('**/*', lambda r: r.abort() if (r.request.is_navigation_request() and
                  not r.request.url.startswith(url.split('#')[0])) else r.continue_())
        page = ctx.new_page()
        page.goto(url, wait_until='load'); page.wait_for_timeout(1200)   # idle: let the scene settle
        controls = page.evaluate(CONTROLS)
        done = 0
        for c in controls:
            if done >= taps: break
            el = page.query_selector(f'[data-feel="{c["i"]}"]')
            if not el: continue
            try:
                el.scroll_into_view_if_needed(timeout=1500)
                box = el.bounding_box()
                if not box or box['width'] < 1: continue
                page.wait_for_timeout(250)          # let scroll-linked motion stop first
                box = el.bounding_box()
                cx, cy = box['x'] + box['width']/2, box['y'] + box['height']/2
                # a control under a modal is not dead, it is unreachable: say which
                cover = page.evaluate('''([i,x,y]) => { const el = document.querySelector('[data-feel="'+i+'"]');
                    const t = document.elementFromPoint(x, y); if (!t || el.contains(t) || t.contains(el)) return null;
                    return t.tagName.toLowerCase() + (t.id ? '#' + t.id : '') + (t.className && typeof t.className === 'string' ? '.' + t.className.split(' ')[0] : ''); }''', [c['i'], cx, cy])
                if cover:
                    warns.append(f'COVERED {c["sel"]} "{c["label"]}" sits under {cover} in this state, so a tap cannot reach it')
                    continue
                base = page.screenshot()
                # ambient motion (a looping animation) would read as an answer to the tap:
                # measure it with no tap and require the tap to beat it
                idle2 = page.screenshot()
                _, ambient = _changed(base, idle2)
                t0 = time.perf_counter()
                page.touchscreen.tap(cx, cy)
                first = None
                for ms in (60, 120, 250, 400):
                    wait = ms/1000 - (time.perf_counter() - t0)
                    if wait > 0: page.wait_for_timeout(wait*1000)
                    hit, frac = _changed(base, page.screenshot(), thresh=max(0.002, ambient * 1.5 + 0.001))
                    if hit: first = ms; break
                rows.append({'control': c['sel'], 'label': c['label'], 'first_ms': first, 'ambient': round(ambient, 4)})
                if first is None:
                    halts.append(f'F1 DEAD_TAP {c["sel"]} "{c["label"]}" changed nothing on screen within {DEAD_MS} ms')
                elif first > SLOW_MS:
                    warns.append(f'F2 SLOW_ANSWER {c["sel"]} "{c["label"]}" first answered at ~{first} ms (aim under {SLOW_MS})')
                done += 1
                if not page.url.startswith(url.split('#')[0]):
                    page.goto(url, wait_until='load'); page.wait_for_timeout(600)
                    page.evaluate(CONTROLS)                  # re-tag: same page, same order
            except Exception as e:
                warns.append(f'could not tap {c["sel"]}: {str(e)[:80]}')
        # keyboard players are players: arrows and space on canvas-style builds
        if page.query_selector('canvas'):
            for k in ('ArrowLeft', 'ArrowRight', 'Space'):
                base = page.screenshot(); page.keyboard.down(k); page.wait_for_timeout(300); page.keyboard.up(k)
                if not _changed(base, page.screenshot())[0]:
                    warns.append(f'F1 KEY {k} held 300 ms changed nothing (keyboard play may be unwired)')
        page.wait_for_timeout(500)
        F = page.evaluate('() => window.__feel')
        motion = page.evaluate(MOTION)
        b.close()
    frames = [f for f in F['frames'] if f < 1000]
    p95 = pct(frames, 0.95)
    for e in dict.fromkeys(F['errors']):
        halts.append(f'F3 SCRIPT_ERROR {e[:160]}')
    if p95 > P95_WARN_MS:
        warns.append(f'F4 FRAME_PACING p95 frame {p95:.0f} ms (below 30 fps) over {len(frames)} frames')
    worst = max(F['long'] or [0])
    if worst > LONGTASK_HALT_MS:
        halts.append(f'F4 LONG_TASK a {worst:.0f} ms task froze input (floor {LONGTASK_HALT_MS})')
    for m in motion:
        halts.append(f'F5 BROKEN_MOTION {m}')
    answered = [r['first_ms'] for r in rows if r['first_ms']]
    summary = {'build': path, 'taps': len(rows), 'answered': len(answered),
               'median_first_ms': pct(answered, 0.5) if answered else None,
               'frames': len(frames), 'p50_ms': round(pct(frames, .5), 1), 'p95_ms': round(p95, 1),
               'longest_task_ms': round(worst), 'halts': halts, 'warns': warns, 'rows': rows}
    return summary

def self_test():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'canary')
    ok = True
    for f, want in (('feel-dead.html', {'F1', 'F3'}), ('feel-live.html', set())):
        got = {h.split()[0] for h in probe(os.path.join(here, f), 10)['halts']}
        good = got == want
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'} {f:<16} expect {sorted(want) or 'PASS'} got {sorted(got) or 'PASS'}")
    print('  FEEL PROBE SELF-TEST', 'PASSED' if ok else 'FAILED, the probe will not grade builds')
    return ok

def main():
    a = sys.argv[1:]
    if '--self-test' in a:
        sys.exit(0 if self_test() else 1)
    if not a or a[0].startswith('--'):
        print(__doc__); sys.exit(2)
    taps = int(a[a.index('--taps')+1]) if '--taps' in a else 30
    s = probe(a[0], taps)
    print(f"FEEL PROBE  {os.path.basename(a[0])}")
    print(f"  taps {s['taps']}  answered {s['answered']}  median first answer ~{s['median_first_ms']} ms")
    print(f"  frames {s['frames']}  p50 {s['p50_ms']} ms  p95 {s['p95_ms']} ms  longest task {s['longest_task_ms']} ms")
    for h in s['halts']: print('  HALT', h)
    for w in s['warns'][:12]: print('  WARN', w)
    if '--json' in a:
        json.dump(s, open(a[a.index('--json')+1], 'w'), indent=1)
    print('  ==', 'HALT' if s['halts'] else 'PASS')
    sys.exit(1 if s['halts'] else 0)

if __name__ == '__main__':
    main()
