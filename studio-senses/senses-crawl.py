#!/usr/bin/env python3
"""
STUDIO SENSES · THE EVIDENCE CRAWL                      Tight Spiral Productions
-----------------------------------------------------------------------------
Founder direction 2026-09-26 (option 5): paired agent personas plus a recorded
human playtest that grades the seats. Everything downstream reads THIS crawl.

ONE CANON WRITES, OTHERS READ. Eyes (Layer 2, Hitchcock), Fingers, Horvath, Ears,
the sighted persona and the ear persona all used to be silent because nothing ever
showed them the rendered game. This crawler plays the build ONCE and writes an
evidence bundle; every sense reads the bundle and none of them re-crawls, so they
cannot disagree about what happened.

What it records, per click and per new state:
  screenshot (sighted persona only)       states/NN.png
  accessibility tree (ear persona only)   states/NN.aria.txt
  controls with real rendered boxes       manifest.json  (Fingers)
  visible text + aria-live announcements  manifest.json  (Horvath, ear persona)
  every audio source started, with its    manifest.json  (Ears)
    context state and time since the
    first trusted gesture
  output level at the speaker, measured   manifest.json  (Ears)
    by an analyser spliced in front of
    the AudioDestinationNode
  navigator.vibrate calls                 manifest.json  (Ears, cross-channel)
  a cold keyboard walk: Tab order from    manifest.json  (ear persona)
    load, before any click

The bundle is stamped with the build's md5. Every seat verdict and every prediction
downstream carries that stamp, so a verdict on an old build reads STALE, never PASS.

It measures. It does not judge. Exit 0 always (reporter, like playthrough-agent.py).

Usage:
  python3 studio-senses/senses-crawl.py <build.html> [--out DIR] [--clicks N]
"""
import sys, os, json, hashlib, re, time, argparse

VIEWPORT = {"width": 400, "height": 840}      # matches Studio Eyes and the playthrough agent
SETTLE_MS = 450
TAB_WALK = 40
# The play loop never presses the sound control: a crawl that muted itself on click one
# (it did, first run) would grade a silent game. mute_test() exercises it separately.
SOUND_CTL = re.compile(r'\b(sound|mute|unmute|audio|volume)\b', re.I)

HOOK = r"""
(() => {
  const L = window.__senses = {ev: [], gest: null, vib: [], meters: [], peak: 0,
                                rmsMax: -120, win: [], ctx: 0};
  const T = () => performance.now();
  const log = (k, x) => L.ev.push(Object.assign({k, t: T()}, x || {}));
  ['pointerdown','mousedown','touchend','click','keydown'].forEach(e =>
    addEventListener(e, ev => { if (ev.isTrusted && L.gest === null) { L.gest = T(); log('gesture', {type: e}); } }, true));
  if (navigator.vibrate) { const v = navigator.vibrate.bind(navigator);
    navigator.vibrate = (p) => { log('vibrate', {p: JSON.stringify(p)}); try { return v(p); } catch (e) { return false; } }; }
  const wrapCtx = (C) => C && class extends C { constructor(...a) { super(...a); L.ctx++; log('ctx', {state: this.state}); } };
  if (window.AudioContext) window.AudioContext = wrapCtx(window.AudioContext);
  if (window.webkitAudioContext) window.webkitAudioContext = wrapCtx(window.webkitAudioContext);
  if (window.AudioNode) {
    const meters = new WeakMap(), oc = AudioNode.prototype.connect;
    AudioNode.prototype.connect = function (dest, ...r) {
      if (window.AudioDestinationNode && dest instanceof AudioDestinationNode) {
        let m = meters.get(dest.context);
        if (!m) { m = dest.context.createAnalyser(); m.fftSize = 2048; oc.call(m, dest); meters.set(dest.context, m); L.meters.push(m); }
        return oc.call(this, m, ...r);
      }
      return oc.call(this, dest, ...r);
    };
    const os = AudioScheduledSourceNode.prototype.start;
    AudioScheduledSourceNode.prototype.start = function (...a) {
      log('src', {node: this.constructor.name, loop: !!this.loop, state: this.context.state,
                  ahead: Math.max(0, (a[0] || 0) - this.context.currentTime)});
      return os.apply(this, a);
    };
  }
  if (window.HTMLMediaElement) {
    const op = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function () {
      log('media', {src: (this.currentSrc || this.src || '').slice(0, 80), muted: this.muted, vol: this.volume});
      return op.apply(this, arguments);
    };
  }
  const buf = new Float32Array(2048);
  setInterval(() => {
    let pk = 0, ss = 0, n = 0;
    for (const m of L.meters) { m.getFloatTimeDomainData(buf);
      for (let i = 0; i < buf.length; i++) { const x = Math.abs(buf[i]); if (x > pk) pk = x; ss += buf[i] * buf[i]; n++; } }
    if (!n) return;
    const rms = 20 * Math.log10(Math.sqrt(ss / n) + 1e-9);
    if (pk > L.peak) L.peak = pk;
    if (rms > L.rmsMax) L.rmsMax = rms;
    L.win.push([Math.round(T()), +rms.toFixed(1), +pk.toFixed(3)]);
    if (L.win.length > 4000) L.win.shift();
  }, 100);
  const seen = new WeakMap();
  const scanLive = () => document.querySelectorAll('[aria-live],[role=status],[role=alert]').forEach(el => {
    const t = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 200);
    if (t && seen.get(el) !== t) { seen.set(el, t); log('live', {text: t}); }
  });
  new MutationObserver(scanLive).observe(document, {subtree: true, childList: true, characterData: true});
})();
"""

CONTROLS_JS = r"""
() => {
  const sel = 'button, a[href], [role=button], input, select, textarea, [tabindex]:not([tabindex="-1"])';
  const out = [];
  for (const el of document.querySelectorAll(sel)) {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    if (r.width < 1 || r.height < 1 || cs.visibility === 'hidden' || cs.display === 'none') continue;
    if (el.closest('[hidden],[aria-hidden=true]')) continue;
    if (el.disabled || cs.pointerEvents === 'none' || el.getAttribute('aria-disabled') === 'true') continue;  // v2: inert until earned
    // HIT AREA, not paint box. A ::before/::after with position:absolute and a
    // negative inset widens the tap target (kireji's 36px sound chip is 46px to a
    // thumb). Reading the paint box here is the exact false positive the retired
    // root studio-fingers.py shipped on Flok. Union the pseudo extents in.
    // offsets are against the PADDING box (inside the border): kireji's inset:-5px chip measured 42px, not 46
    const bl = parseFloat(cs.borderLeftWidth)||0, bt = parseFloat(cs.borderTopWidth)||0,
          bR = parseFloat(cs.borderRightWidth)||0, bB = parseFloat(cs.borderBottomWidth)||0;
    let hx = r.x, hy = r.y, hr = r.right, hb = r.bottom;
    for (const pe of ['::before', '::after']) {
      const ps = getComputedStyle(el, pe);
      if (ps.content === 'none' || ps.position !== 'absolute') continue;
      const t = parseFloat(ps.top), l = parseFloat(ps.left), rr = parseFloat(ps.right), bb = parseFloat(ps.bottom);
      if ([t, l, rr, bb].every(Number.isFinite)) {
        hx = Math.min(hx, r.x + bl + l); hy = Math.min(hy, r.y + bt + t);
        hr = Math.max(hr, r.right - bR - rr); hb = Math.max(hb, r.bottom - bB - bb);
      }
    }
    const vis = (el.innerText || el.value || '').trim().replace(/\s+/g, ' ');
    const name = (el.getAttribute('aria-label') || vis || el.getAttribute('title') || '').slice(0, 60);
    out.push({name, visible: vis.slice(0, 60), tag: el.tagName.toLowerCase(), id: el.id || '',
      cls: (el.className && el.className.baseVal === undefined ? el.className : '').toString().slice(0, 40),
      pressed: el.getAttribute('aria-pressed'), href: el.getAttribute('href') || '',
      chrome: !!el.closest('.se-chrome,.se-rail,[data-studio-chrome]'),
      scrollable: el.scrollHeight > el.clientHeight + 20 && /(auto|scroll)/.test(cs.overflowY),
      x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), hw: Math.round(hr - hx), hh: Math.round(hb - hy),
      inView: r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth});
  }
  return out;
}
"""


def md5(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def signature(controls, text, titles=''):
    # v2.1 (2026-10-13, seat finding): headings and titles are part of a state's identity.
    # Grouping by controls alone folded Flok's promotion cards 2-4 into card 1, so no seat saw them.
    heads = ' '.join(sorted({c['name'] for c in controls if c['inView']})) + '#' + titles
    pressed = ' '.join(f"{c['name']}={c['pressed']}" for c in controls if c['pressed'] is not None)
    return hashlib.md5((heads + '|' + pressed).encode()).hexdigest()[:12]


def level(page, ms=900):
    page.wait_for_timeout(ms)
    w = page.evaluate("() => window.__senses.win.slice(-5)")
    return max((x[1] for x in w), default=None)


def mute_test(page):
    """Find the sound control in the CURRENT state, press it, measure the speaker,
    press it again, measure again. A mute is only a mute if the level drops."""
    ctls = [c for c in page.evaluate(CONTROLS_JS) if SOUND_CTL.search(c['name'])]
    r = {"found": bool(ctls), "control": ctls[0]['name'] if ctls else None}
    if not ctls:
        return r
    c = ctls[0]
    r['before_dbfs'] = level(page, 300)
    page.mouse.click(c['x'] + c['w'] / 2, c['y'] + c['h'] / 2)
    r['after_press_dbfs'] = level(page)
    c2 = next((x for x in page.evaluate(CONTROLS_JS) if SOUND_CTL.search(x['name'])), c)
    r['label_after'] = c2['name']
    page.mouse.click(c2['x'] + c2['w'] / 2, c2['y'] + c2['h'] / 2)
    r['after_second_press_dbfs'] = level(page)
    return r


def mute_oneshot(page, ctl, action):
    """2026-10-13. For a sound that plays only when one action is pressed: press the action
    and measure, press the sound control and press the action again (must be silent),
    press the control back and press the action again (must sound)."""
    ax, ay = action['x'] + action['w'] / 2, action['y'] + action['h'] / 2
    cx, cy = ctl['x'] + ctl['w'] / 2, ctl['y'] + ctl['h'] / 2
    r = {"found": True, "control": ctl['name'], "kind": "oneshot", "action": action['name']}
    page.mouse.click(ax, ay); r['before_dbfs'] = level(page, 450)
    page.mouse.click(cx, cy); page.wait_for_timeout(150)
    page.mouse.click(ax, ay); r['after_press_dbfs'] = level(page, 450)
    page.mouse.click(cx, cy); page.wait_for_timeout(150)
    page.mouse.click(ax, ay); r['after_second_press_dbfs'] = level(page, 450)
    return r


def crawl(build, out, clicks):
    from playwright.sync_api import sync_playwright
    os.makedirs(os.path.join(out, 'states'), exist_ok=True)
    stamp = md5(build)
    url = 'file://' + os.path.abspath(build)
    external = []
    man = {"build": os.path.basename(build), "md5": stamp,
           "sha256": hashlib.sha256(open(build, 'rb').read()).hexdigest(), "viewport": VIEWPORT,
           "crawled": time.strftime('%Y-%m-%dT%H:%M:%S%z'), "tool": "senses-crawl.py v2",
           "states": [], "steps": [], "tab_walk": [], "external_requests": external}
    with sync_playwright() as p:
        # DEVICE POLICY, corrected 2026-09-26 after the founder heard it on a phone: with
        # 'user-gesture-required' headless Chromium let the AudioContext run before any touch,
        # so E1 HALTed kireji for a sound no phone ever plays. 'document-user-activation-required'
        # is what a phone does: sound waits for a touch. The machine was the suspect.
        b = p.chromium.launch(args=['--autoplay-policy=document-user-activation-required'])
        ctx = b.new_context(viewport=VIEWPORT, device_scale_factor=2, has_touch=True)
        ctx.add_init_script(HOOK)
        page = ctx.new_page()

        def route(r):
            u = r.request.url
            if u.startswith(('file:', 'data:', 'blob:', 'about:')):
                return r.continue_()
            external.append(u[:120]); return r.abort()
        page.route('**/*', route)
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)[:200]))
        page.goto(url); page.wait_for_timeout(1200)

        # cold keyboard walk, before any click: what the ear player meets first
        for i in range(TAB_WALK):
            page.keyboard.press('Tab')
            f = page.evaluate("""() => { const a = document.activeElement; if (!a || a === document.body) return null;
                return {name: (a.getAttribute('aria-label') || a.innerText || a.value || a.title || '').trim().replace(/\\s+/g,' ').slice(0,60),
                        tag: a.tagName.toLowerCase(), id: a.id || ''}; }""")
            man['tab_walk'].append(f)
        # A Tab press is a trusted gesture and gives the page sticky activation, which
        # would let audio start "before a gesture" on the reload and hide an ambush.
        # So the play crawl gets a FRESH context: a cold browser, as a first player has.
        ctx.close()
        ctx = b.new_context(viewport=VIEWPORT, device_scale_factor=2, has_touch=True)
        ctx.add_init_script(HOOK)
        page = ctx.new_page(); page.route('**/*', route)
        page.on('pageerror', lambda e: errors.append(str(e)[:200]))
        page.goto(url); page.wait_for_timeout(1200)

        seen_sigs = {}
        clicked = {}
        dead = {}          # v2: clicks on a label that changed nothing
        left = []          # v2: taps that tried to leave the build

        def capture(tag):
            # v2: wait for smooth scrolling to settle, or every box is read mid-flight and
            # the next tap lands on empty space (Flok "Start over", 2026-10-13).
            for _ in range(20):
                y1 = page.evaluate("scrollY"); page.wait_for_timeout(90)
                if page.evaluate("scrollY") == y1: break
            controls = page.evaluate(CONTROLS_JS)
            text = page.inner_text('body')[:5000]
            titles = page.evaluate("()=>[...document.querySelectorAll('h1,h2,h3,.title,[role=heading]')].filter(e=>e.offsetParent).map(e=>e.innerText.trim()).join('|').slice(0,300)")
            sig = signature(controls, text, titles)
            if sig in seen_sigs:
                return seen_sigs[sig], controls, text, False
            n = len(man['states'])
            png = f"states/{n:02d}.png"; aria = f"states/{n:02d}.aria.txt"
            page.screenshot(path=os.path.join(out, png))
            try:
                snap = page.locator('body').aria_snapshot()
            except Exception as e:
                snap = f"(aria snapshot unavailable: {e})"
            with open(os.path.join(out, aria), 'w') as f:
                f.write(snap)
            man.setdefault('screens_seen', [])
            for sid in page.evaluate("()=>[...document.querySelectorAll('.screen,[data-screen]')].filter(e=>e.offsetParent||getComputedStyle(e).display!=='none').map(e=>e.id||e.dataset.screen||'')"):
                if sid and sid not in man['screens_seen']: man['screens_seen'].append(sid)
            scr = page.evaluate("()=>{const e=[...document.querySelectorAll('.screen,[data-screen]')].find(e=>getComputedStyle(e).display!=='none'&&e.offsetParent);return e?(e.id||e.dataset.screen||''):''}")
            man['states'].append({"n": n, "sig": sig, "reached_by": tag, "png": png, "aria": aria, "screen": scr,
                                  "controls": controls, "text": text[:2500],
                                  "headings": page.evaluate("()=>[...document.querySelectorAll('h1,h2,h3')].filter(h=>h.offsetParent).map(h=>h.innerText.trim()).slice(0,8)")})
            seen_sigs[sig] = n
            return n, controls, text, True

        cur, controls, text, _ = capture('cold load')
        for step in range(clicks):
            # v2, 2026-10-13: STAY IN THE BUILD. v1's first tap on Flok was the studio's own
            # "Studio" link at the top; the whole bundle became the home page and the
            # arcade, and every seat would have reviewed the wrong game. Never follow a
            # link to another document; never tap the studio chrome (Studio / Cabinet /
            # Back / Home), which is the same on every build and is Fingers' job anyway.
            cands = [c for c in controls if not c.get('chrome')
                     and not (c['href'] and not c['href'].startswith('#'))
                     and c['tag'] not in ('input', 'textarea', 'select')
                     and not SOUND_CTL.search(c['name'])]   # Ears tests the mute on its own
            # least-DEAD first: a game's core verb is often the same button tapped many
            # times (Flok's levers). v1 quit any label after 3 clicks, so a 5-lever game
            # stalled on lever 1. Now a label is retired after 3 clicks that changed nothing.
            cands.sort(key=lambda c: (dead.get(c['name'], 0), clicked.get(c['name'], 0), not c['inView'], c['y'], c['x']))
            if not cands:
                man['steps'].append({"n": step, "dead_end": True, "state": cur}); break
            c = cands[0]
            if dead.get(c['name'], 0) >= 3:
                break
            clicked[c['name']] = clicked.get(c['name'], 0) + 1
            # v2: a control whose centre is off screen gets scrolled to first, as a thumb
            # would, and the scroll is logged for Fingers (needs_scroll is a finding).
            vh = VIEWPORT['height']; cy = c['y'] + c['h'] / 2
            needs_scroll = cy < 4 or cy > vh - 4
            if needs_scroll:
                page.mouse.wheel(0, cy - vh / 2); page.wait_for_timeout(350)
                fresh = [k for k in page.evaluate(CONTROLS_JS) if k['name'] == c['name']]
                if fresh: c = dict(fresh[0], scrollable=c.get('scrollable'))
            before_ev = page.evaluate("() => window.__senses.ev.length")
            t_click = page.evaluate("() => performance.now()")
            try:
                # v2: a scrollable control's verb is the swipe, not the tap (Flok lever 2
                # is an infinite feed). Wheel over it, the way a thumb would drag it.
                if c.get('scrollable'):
                    page.mouse.move(c['x'] + c['w'] / 2, c['y'] + c['h'] / 2)
                    page.mouse.wheel(0, 700)
                else:
                    page.mouse.click(c['x'] + c['w'] / 2, c['y'] + c['h'] / 2)
            except Exception as e:
                man['steps'].append({"n": step, "label": c['name'], "error": str(e)[:120]}); continue
            page.wait_for_timeout(SETTLE_MS)
            ev = page.evaluate(f"() => window.__senses.ev.slice({before_ev})")
            prev_text = text
            if not page.url.startswith(url.split('#')[0]):
                left.append({"n": step, "label": c['name'], "to": page.url[-80:]})
                page.goto(url); page.wait_for_timeout(1200)
            nxt, controls, text, new = capture(f"step {step}: {c['name']}")
            if text == prev_text:
                dead[c['name']] = dead.get(c['name'], 0) + 1
            man['steps'].append({
                "n": step, "label": c['name'], "from": cur, "to": nxt, "new_state": new,
                "needs_scroll": needs_scroll,
                "t_click": round(t_click), "box": [c['x'], c['y'], c['w'], c['h']],
                "text_changed": text != prev_text,
                "oneshot_sounds": [e for e in ev if e['k'] == 'src' and not e['loop']][:12],
                "loops_started": sum(1 for e in ev if e['k'] == 'src' and e['loop']),
                "media": [e for e in ev if e['k'] == 'media'],
                "live": [e['text'] for e in ev if e['k'] == 'live'],
                "vibrate": [e['p'] for e in ev if e['k'] == 'vibrate']})
            cur = nxt
            if man['steps'][-1]['oneshot_sounds'] and 'mute_test_oneshot' not in man:
                snd = [k for k in controls if SOUND_CTL.search(k['name']) and k['inView']]
                same = [k for k in controls if k['name'] == c['name'] and k['inView']]
                if snd and same:
                    man['mute_test_oneshot'] = mute_oneshot(page, snd[0], same[0])
                    text = page.inner_text('body')[:5000]
        # v2 COVERAGE. A crawl that never reached the game's own screens is SHALLOW, and
        # SHALLOW is printed, never PASS. Screens = the build's [id^=sc-] sections or
        # [data-screen] / .screen elements; reached = shown at any captured state.
        man['left_build'] = left
        man['mute_test'] = mute_test(page)
        s = page.evaluate("() => ({gest: window.__senses.gest, ctx: window.__senses.ctx, peak: window.__senses.peak, rmsMax: window.__senses.rmsMax, win: window.__senses.win, ev: window.__senses.ev})")
        man['audio'] = {"first_gesture_ms": s['gest'], "contexts": s['ctx'], "peak_linear": round(s['peak'], 4),
                        "rms_max_dbfs": round(s['rmsMax'], 1), "level_windows": s['win'][-600:],
                        "pre_gesture_sources": [e for e in s['ev'] if e['k'] in ('src', 'media')
                                                and (s['gest'] is None or e['t'] < s['gest'])],
                        "sources_total": sum(1 for e in s['ev'] if e['k'] == 'src'),
                        "media_total": sum(1 for e in s['ev'] if e['k'] == 'media')}
        man['page_errors'] = errors
        man['screens_secondary'] = page.evaluate("()=>[...document.querySelectorAll('[data-secondary]')].map(e=>e.id||e.dataset.screen||'').filter(Boolean)") if page.url.startswith(url.split('#')[0]) else []
        man['screens_total'] = page.evaluate("()=>[...document.querySelectorAll('.screen,[data-screen]')].map(e=>e.id||e.dataset.screen||'').filter(Boolean)") if page.url.startswith(url.split('#')[0]) else []
        b.close()
    with open(os.path.join(out, 'manifest.json'), 'w') as f:
        json.dump(man, f, indent=1)
    return man


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('build'); ap.add_argument('--out'); ap.add_argument('--clicks', type=int, default=60)
    a = ap.parse_args()
    out = a.out or os.path.join('reports', 'senses', os.path.splitext(os.path.basename(a.build))[0])
    m = crawl(a.build, out, a.clicks)
    print(f"SENSES CRAWL  {m['build']}  md5 {m['md5']}")
    print(f"  states {len(m['states'])} · steps {len(m['steps'])} · audio sources {m['audio']['sources_total']}"
          f" · page errors {len(m['page_errors'])} · external requests {len(m['external_requests'])}")
    tot, seen = m.get('screens_total', []), [x for x in m.get('screens_seen', []) if x in m.get('screens_total', [])]
    if tot:
        verdict = 'FULL' if len(seen) == len(tot) else 'SHALLOW'
        print(f"  coverage {verdict}  {len(seen)}/{len(tot)} screens reached: {', '.join(seen)}"
              + ('' if verdict == 'FULL' else f"  (never reached: {', '.join(x for x in tot if x not in seen)})"))
    if m.get('left_build'):
        print(f"  left the build {len(m['left_build'])}x and came back (a link escaped the filter)")
    print(f"  bundle -> {out}/manifest.json")


if __name__ == '__main__':
    main()
