#!/usr/bin/env python3
"""
STUDIO EYES v3  ·  Tight Spiral Productions
===========================================
The accessibility auditor for a founder with retinitis pigmentosa.
Contrast is ARITHMETIC, not judgment. This tool is in the critical path
of every ship, so it must first prove it can be trusted.

WHAT CHANGED FROM v2 (and why)
------------------------------
v2 parsed CSS with regex and GUESSED what the browser would do. It was wrong
seven times: comments glued to selectors, @media invisible, only the first
<style> block read, grouped selectors unfindable, ancestors mis-walked,
self-painting elements ignored, and key-class collisions grounding a caption
against an unrelated progress bar.

Every one of those is the same bug: *guessing the cascade instead of asking
the engine that runs it.* There is no regex that fixes this class. So:

    v2:  read CSS text -> guess cascade -> guess ground -> compute
    v3:  RENDER PAGE   -> ASK for ground              -> compute

The middle column is where all seven bugs lived. It is deleted.
getComputedStyle does not guess. elementFromPoint does not guess. And when
text sits on a photo or a gradient, v3 SCREENSHOTS THE PIXELS UNDER THE GLYPHS
— something regex can never do, and which v2's own gate admitted it could not see.

SELF-AUDIT (the thing that makes it world-class, not merely correct)
--------------------------------------------------------------------
Every v2 bug was found by a HUMAN noticing something was off. That is the real
failure. v3 ships with a canary corpus of known-verdict traps — half of them
FALSE-POSITIVE traps: files that are CORRECT and that v2 wrongly HALTed.

    studio-eyes.py --self-test

runs before any audit. If the auditor cannot grade its own canary, IT REFUSES
TO RUN. A tool that gates the studio must first gate itself.

FLOOR 11 — CLIPPED TEXT (added 2026-09-01)
------------------------------------------
Ten floors graded the glyphs this tool could see. None asked whether the reader can
read them. Flok shipped its research card sliced through the middle for weeks with
every floor green. The measurement lives in _CLIP_BODY below, is spliced into PROBE,
and is exported as CLIP_PROBE so playthrough-agent.py can run the same arithmetic at
every state its crawler visits — because this auditor measures FIRST PAINT, and the
card that caused this floor sits behind three clicks.

USAGE
    studio-eyes.py --self-test              validate the auditor
    studio-eyes.py <file.html> [...]        audit (self-test runs first)
    studio-eyes.py --no-self-test <file>    skip (CI only; not for ship)

EXIT 0 = ship.  EXIT 1 = HALT, do not ship.
"""
import sys, os, json, base64, io, re

WCAG_TEXT = 4.5
WCAG_LARGE = 3.0
STOP_SEP_MIN = 0.12
MIN_TARGET = 44
CLIP_TOL = 2          # px of sub-pixel slack before a glyph counts as cut off
# A BOX vs A WINDOW. Both clip; only one is broken. A box was meant to hold its
# content and doesn't; a window shows a slice of something long on purpose (a feed, a
# list, a transcript). The separation is not a judgment call, it is a ratio, and it is
# not close: measured on the-console.html 2026-09-01, the broken research card held
# 76px of text in a 68px box (1.12) and the diegetic phone feed held 699px in 150px
# (4.66). Nobody designs a box to show 80% of a sentence; nobody designs a window to
# show 20% of a feed. Under 2.0 the box was meant to fit and HALTs; over it, the shape
# is a window and the finding is reported as a note instead of blocking.
# [HOUSE] — declared, not derived from any founder ruling, and it contradicts none.
CLIP_WINDOW_RATIO = 2.0

# ---------------------------------------------------------------- colour math

def lum(rgb):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def parse_rgb(s):
    m = re.findall(r'[\d.]+', s or '')
    if len(m) < 3:
        return None
    r, g, b = int(float(m[0])), int(float(m[1])), int(float(m[2]))
    a = float(m[3]) if len(m) > 3 else 1.0
    return (r, g, b, a)

def flatten(fg, bg):
    """Composite a translucent colour over its backdrop."""
    r, g, b, a = fg
    if a >= 0.999:
        return (r, g, b)
    br, bg_, bb = bg
    return (round(r * a + br * (1 - a)),
            round(g * a + bg_ * (1 - a)),
            round(b * a + bb * (1 - a)))

# ---------------------------------------------------------------- the probe
# This runs INSIDE the browser. It is the whole point: the page tells us what
# it actually painted, instead of us deducing it from source text.


# ---------------------------------------------------------------- the clip probe
# ONE CANON WRITES, OTHERS READ. This body is spliced into PROBE below AND exported
# as CLIP_PROBE, which playthrough-agent.py runs at every state its crawler visits.
# Two copies of one measurement is the failure this studio keeps paying for, so
# there is exactly one — and the crawler reads it from here or says out loud that
# it could not.
_CLIP_BODY = r"""
  // ---- CLIPPED TEXT: words the page renders and then hides behind a clip box.
  //
  // FLOOR 11, added 2026-09-01 after Flok shipped its research card unreadable and
  // every one of floors 1-10 stayed green. "Why does this work?" flipped open onto a
  // 68px box holding 85px of research: the first line was sliced through the x-height
  // and the citation was cut in half. Contrast was perfect. The touch target was
  // 340x68. The focus ring was there. NOTHING in this auditor had ever been asked the
  // one question that mattered — CAN YOU ACTUALLY READ IT — because every floor graded
  // the glyphs it could see and none looked for the glyphs that had been thrown away.
  // A tool built for a founder with retinitis pigmentosa that cannot see text
  // disappear is looking through the wrong end of itself.
  //
  // ARITHMETIC, not judgment: for every visible text node, walk up to the nearest
  // ancestor that does not paint everything inside it, and ask whether the text's
  // painted box escapes that ancestor's padding box. If it does, those pixels were
  // computed, laid out, and then discarded by the compositor. Nobody can read them.
  //
  // WHAT IS NOT A DEFECT — each of these is a false-positive trap in the canary,
  // because a gate that cries wolf is a gate people route around:
  //   - a SCROLL WINDOW (overflow auto/scroll on the escaping axis). The content is
  //     off-view but reachable; that is a window, not a clip.
  //   - a COLLAPSED DISCLOSURE (the clip box is ~0 on that axis). A closed accordion
  //     is not hiding text, it is waiting. Flok's own locked card is this shape, and
  //     the defect was in the OPEN state, never the closed one.
  //   - VISUALLY-HIDDEN text (sr-only: a 1px box, or parked off-canvas). Written for
  //     a screen reader, deliberately not painted.
  //   - DELIBERATE TRUNCATION (text-overflow other than clip). An ellipsis is a
  //     designer saying "there is more"; a hard slice says nothing at all.
  //   - anything [hidden] or aria-hidden — already declared not-for-reading.
  // A HIDDEN BACKFACE IS NOT PAINTED, and its projected box lies. On a flip card the
  // face turned away still has visibility:visible and opacity:1, and under perspective
  // its axis-aligned box is a few px WIDER than the card — which read as the front face
  // clipping itself by 2px on a card that was flipped away and invisible. Found on the
  // first crawler run after fixing the-console.html, 2026-09-01.
  // Exact, not a guess: accumulate the transform chain and read the z-component of the
  // transformed normal. rotateY(180deg) once is -1 (turned away); twice is +1 (facing
  // the reader), which is precisely how a .flip-back inside a .flip.flipped works.
  const facingAway = (el, stopAt) => {
    let p = el, seenHidden = false, m = new DOMMatrix();
    while (p && p !== stopAt) {
      const cs = getComputedStyle(p);
      if (cs.backfaceVisibility === 'hidden') seenHidden = true;
      if (cs.transform && cs.transform !== 'none') m = new DOMMatrix(cs.transform).multiply(m);
      p = p.parentElement;
    }
    return seenHidden && m.m33 < 0;
  };
  const clipBoxOf = (el) => {
    let p = el.parentElement;
    while (p) {
      const cs = getComputedStyle(p);
      if (cs.overflowX !== 'visible' || cs.overflowY !== 'visible') return { el: p, cs };
      p = p.parentElement;
    }
    return null;
  };
  const walker2 = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seenClip = new Set();
  let m;
  while (m = walker2.nextNode()) {
    const t = (m.textContent || '').trim();
    if (!t) continue;
    const el = m.parentElement;
    if (!el || seenClip.has(el)) continue;
    seenClip.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    if (el.closest('[hidden]') || el.closest('[aria-hidden="true"]')) continue;
    // SVG lays out on a viewBox, not a scroll box. This arithmetic does not describe
    // it, and every SVG label in the corpus read as clipped when it was not.
    if (el.closest('svg')) continue;
    // A CLOSED <details> is a disclosure, not a clip — same forgiveness as any other
    // collapsed drawer, and Chromium keeps its children laid out so the box math
    // otherwise reports the whole runbook as cut off.
    if (el.closest('details:not([open])')) continue;
    const box = clipBoxOf(el);
    if (!box) continue;
    // The PAGE overflowing is studio-fingers' F-VIEWPORT floor, not this one. Reporting
    // it here says nothing new and buries the real finding under one line per word.
    if (box.el === document.body || box.el === document.documentElement) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    const cr = box.el.getBoundingClientRect();
    // sr-only / off-canvas: a 1px box, or parked outside the viewport entirely.
    if (cr.width <= 4 || cr.height <= 4) continue;
    if (cr.right <= 0 || cr.bottom <= 0 || cr.left >= innerWidth) continue;
    // PARKED, not clipped: a skip link at top:-40px, or anything else pushed off the
    // top/left origin until it is summoned. Content BELOW the fold is not parked —
    // the reader scrolls to it — so only the negative side is forgiven.
    if (r.bottom <= 0 || r.right <= 0) continue;
    // clipping happens at the PADDING box, inside the borders.
    const bw = (v) => parseFloat(v) || 0;
    const cTop    = cr.top    + bw(box.cs.borderTopWidth);
    const cBottom = cr.bottom - bw(box.cs.borderBottomWidth);
    const cLeft   = cr.left   + bw(box.cs.borderLeftWidth);
    const cRight  = cr.right  - bw(box.cs.borderRightWidth);
    const scrolls = (o) => o === 'auto' || o === 'scroll';
    const overY = Math.max(r.bottom - cBottom, cTop - r.top);
    const overX = Math.max(r.right - cRight, cLeft - r.left);
    const lostY = scrolls(box.cs.overflowY) ? 0 : overY;
    const lostX = scrolls(box.cs.overflowX) ? 0 : overX;
    const lost = Math.max(lostY, lostX);
    if (lost <= 2) continue;
    if (cs.textOverflow && cs.textOverflow !== 'clip') continue;
    if (facingAway(el, box.el.parentElement)) continue;
    const nm = (e) => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string'
                 ? '.' + e.className.trim().split(/\s+/).join('.') : '');
    // MEASURE THE AXIS THAT ACTUALLY OVERFLOWED. Judging a sideways-scrolling ticker
    // by its height called a 453px-wide marquee in a 278px box a broken box.
    const vertical = lostY >= lostX;
    const boxH = Math.round(cr.height), needH = Math.round(box.el.scrollHeight);
    const boxW = Math.round(cr.width),  needW = Math.round(box.el.scrollWidth);
    const span = vertical ? boxH : boxW, need = vertical ? needH : needW;
    out.clipped.push({ text: t.slice(0, 40), sel: nm(el), by: Math.round(lost),
                       axis: vertical ? 'Y' : 'X',
                       boxH: span, needH: need, clipSel: nm(box.el),
                       // a window shows a slice of something long on purpose; a box
                       // was meant to hold what is in it. See CLIP_WINDOW_RATIO.
                       window: span > 0 && (need / span) > 2.0 });
  }
"""

# Standalone form: same arithmetic, returns just the findings. For any harness that
# has a page and wants the one question floors 1-10 never asked.
CLIP_PROBE = "() => {\n  const out = {clipped:[]};\n" + _CLIP_BODY + "\n  return out.clipped;\n}"

# ---- FLOOR 12: ESCAPED TEXT. Added 2026-10-16 after the founder's phone showed
# ELEVATOR and BASEMENT CAT walking out through the right border of their lobby
# buttons at ~140% page zoom. Floor 11 stayed green, correctly: nothing was CLIPPED.
# The box had overflow:visible, so the browser painted every glyph — straight across
# the border and off the viewport. Floor 11 asks "was any text thrown away?" This
# floor asks the other half of the question: "did any text leave its box?"
#
# ARITHMETIC: for every visible text node, walk up to the nearest ancestor that FRAMES
# it — one that paints a border or a background, or is a button. If the text's painted
# box exits that frame's padding box, or exits the viewport on the right, the text
# escaped. Measured at the padding box, inside the borders, exactly as floor 11 does.
#
# WHAT IS NOT A DEFECT: a scroll window on that axis; sr-only text; parked text
# (negative side only); a backface turned away; text-overflow other than clip; and a
# frame that is itself a window (content more than 2x the box, see CLIP_WINDOW_RATIO).
# Body and html are never the frame: a paragraph on bare paper has nothing to escape.
_ESCAPE_BODY = r"""
  const facingAway = (el, stopAt) => {
    let p = el, m = new DOMMatrix();
    while (p && p !== stopAt) {
      const t = getComputedStyle(p).transform;
      if (t && t !== 'none') { try { m = new DOMMatrix(t).multiply(m); } catch(e){} }
      p = p.parentElement;
    }
    return m.m33 < 0;
  };
  const framed = (e) => {
    const cs = getComputedStyle(e);
    if (/^(button|a|summary)$/i.test(e.tagName)) return cs;
    const bw = ['Top','Right','Bottom','Left'].some(k =>
      parseFloat(cs['border'+k+'Width']) > 0 && !/rgba\(0, 0, 0, 0\)|transparent/.test(cs['border'+k+'Color']));
    const bg = cs.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(cs.backgroundColor);
    return (bw || bg) ? cs : null;
  };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let n;
  while (n = walker.nextNode()) {
    const t = n.textContent.trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    if (el.closest('[hidden],[aria-hidden="true"],script,style,svg')) continue;
    // a closed disclosure is waiting, not hiding: Chromium still lays its body out
    const det = el.closest('details');
    if (det && !det.open && !el.closest('summary')) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    if (r.bottom <= 0 || r.right <= 0) continue;
    // a hard-edged inline run can be taller than its glyphs; measure the text itself
    const range = document.createRange(); range.selectNodeContents(el);
    const tr = range.getBoundingClientRect();
    if (tr.width < 1) continue;
    if (cs.textOverflow && cs.textOverflow !== 'clip') continue;
    // 2026-11-09: text inside a closed clipping box (a drawer at max-height:0, a 1px
    // screen-reader span) is not on screen at all, so it cannot escape anything.
    // Signal Rider v0.16's sr-only "meters per second" was HALTed as escaping its box.
    let shut = false;
    for (let q = el; q && q !== document.body; q = q.parentElement) {
      const qs = getComputedStyle(q);
      if (qs.overflow !== 'visible' && (q.clientHeight <= 1 || q.clientWidth <= 1)) { shut = true; break; }
    }
    if (shut) continue;
    let box = el.parentElement, bcs = null;
    while (box && box !== document.body) { bcs = framed(box); if (bcs) break; box = box.parentElement; }
    if (!box || box === document.body) {
      if (tr.right > innerWidth + 2) {
        out.push({ text: t.slice(0,40), sel: el.tagName.toLowerCase(), by: Math.round(tr.right - innerWidth),
                   frame: 'viewport', axis: 'X' });
      }
      continue;
    }
    const cr = box.getBoundingClientRect();
    if (cr.width <= 4 || cr.height <= 4) continue;
    if (facingAway(el, box.parentElement)) continue;
    const bw = (v) => parseFloat(v) || 0;
    const cRight  = cr.right  - bw(bcs.borderRightWidth);
    const cLeft   = cr.left   + bw(bcs.borderLeftWidth);
    const cBottom = cr.bottom - bw(bcs.borderBottomWidth);
    const cTop    = cr.top    + bw(bcs.borderTopWidth);
    const scrolls = (o) => o === 'auto' || o === 'scroll';
    const overX = scrolls(bcs.overflowX) ? 0 : Math.max(tr.right - cRight, cLeft - tr.left);
    const overY = scrolls(bcs.overflowY) ? 0 : Math.max(tr.bottom - cBottom, cTop - tr.top);
    const over = Math.max(overX, overY);
    if (over <= 2) continue;
    const vertical = overY >= overX;
    const span = vertical ? cr.height : cr.width;
    const need = vertical ? box.scrollHeight : box.scrollWidth;
    if (span > 0 && need / span > 2.0) continue;   // a window, not a box
    const nm = (e) => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string'
                 ? '.' + e.className.trim().split(/\s+/).join('.') : '');
    out.push({ text: t.slice(0,40), sel: nm(el), by: Math.round(over), frame: nm(box),
               axis: vertical ? 'Y' : 'X' });
  }
"""
ESCAPE_PROBE = "() => {\n  const out = [];\n" + _ESCAPE_BODY + "\n  return out;\n}"

# The text scales a founder with retinitis pigmentosa actually reads at. 1.0 is the
# page as authored; 1.5 and 2.0 are Safari page zoom / a large-text phone. A box
# that holds its words at 1.0 and loses them at 1.5 fails the reader it was built for.
TEXT_SCALES = (1.0, 1.5, 2.0)

def escape_halts(page, mode_label):
    """Floor 12 at every TEXT_SCALE. Page zoom is emulated the way Safari does it: the
    CSS viewport narrows to 390/scale and the page REFLOWS, so a box that fits its
    words at 1.0 has to fit them again with a third less room. Text leaving the
    viewport is only judged at the authored scale: at a narrowed viewport a fixed-width
    panel walking off the right edge is page overflow (Studio Fingers' question), not
    a word leaving its box. The viewport is restored afterwards."""
    halts = []
    for z in TEXT_SCALES:
        try:
            page.set_viewport_size({'width': int(round(390 / z)), 'height': int(round(844 / z))})
            page.wait_for_timeout(80)
            found = page.evaluate(ESCAPE_PROBE) or []
        except Exception:
            found = []
        for c in found:
            if c['frame'] == 'viewport' and z != 1.0:
                continue
            halts.append(f"ESCAPED_TEXT [{mode_label} x{z}] {c['sel']} \"{c['text'][:28]}\" leaves "
                         f"{c['frame']} by {c['by']}px on the {c['axis']} axis. "
                         f"A word outside its box is a word the reader has to chase.")
    try:
        page.set_viewport_size({'width': 390, 'height': 844})
        page.wait_for_timeout(60)
    except Exception:
        pass
    return halts

PROBE = r"""
() => {
  const out = {texts:[], targets:[], stops:[], firstScreen:null, emoji:[], tokens:{}, clipped:[]};

  // ---- every visible text node, with its REAL computed colour and the REAL
  // ---- chain of ancestors that paint behind it.
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let n;
  while (n = walker.nextNode()) {
    const t = n.textContent.trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;

    // walk up for the nearest OPAQUE painted background. The browser knows.
    const chain = [];
    let p = el;
    while (p) {
      const pcs = getComputedStyle(p);
      chain.push({
        bg: pcs.backgroundColor,
        img: pcs.backgroundImage !== 'none' ? pcs.backgroundImage.slice(0,60) : null,
        sel: p.tagName.toLowerCase() + (p.className && typeof p.className === 'string'
              ? '.' + p.className.trim().split(/\s+/).join('.') : '')
      });
      p = p.parentElement;
    }
    const fs = parseFloat(cs.fontSize);
    const bold = (parseInt(cs.fontWeight) || 400) >= 700;
    out.texts.push({
      text: t.slice(0,40),
      sel: chain[0].sel,
      color: cs.color,
      chain: chain,
      large: (fs >= 24 || (fs >= 18.66 && bold)),
      rect: {x:r.x, y:r.y, w:r.width, h:r.height},
      // THE BOX IS NOT THE TEXT. Sampling an element's border box for the pixels
      // "behind the glyphs" reads whatever shows through its rounded corners and
      // padding — on Flok's primary button that was the near-black page seen through
      // a 16px radius, reported as the darkest thing behind dark-on-mint ink and
      // HALTed at 1.1:1. A Range over the element's contents is the actual painted
      // line box, and nothing outside the text can leak into it.
      trect: (() => { const g = document.createRange(); g.selectNodeContents(el);
        const b = g.getBoundingClientRect();
        return (b.width >= 2 && b.height >= 2)
          ? {x:b.x, y:b.y, w:b.width, h:b.height}
          : {x:r.x, y:r.y, w:r.width, h:r.height}; })()
    });

    // emoji, in RENDERED text (not source) — catches JS-injected ones too
    const EM = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}\u{1F000}-\u{1F02F}]/u;
    if (EM.test(t)) out.emoji.push(t.slice(0,30));
  }

  // ---- interactive targets: real rendered box + real focus ring
  // WCAG 2.5.5 inline exception: an <a> in running prose or a footer/credit byline
  // is inline text, not a primary touch target (mirrors studio-fingers). It still
  // must show a focus ring, so it is measured for FOCUS but exempt from TOUCH_TARGET.
  const INLINE_CTX = 'p,li,dd,dt,blockquote,figcaption,footer,.foot,.credits,.credit,.byline,address,.fc-body,.prose,.bio-card,.award-card,.sec-hd';
  document.querySelectorAll('a,button,input,select,textarea,[role=button],[tabindex]').forEach(el=>{
    const cs = getComputedStyle(el);
    if (cs.display==='none' || cs.visibility==='hidden') return;
    // 2026-10-15: content of a CLOSED <details> is not rendered and cannot take focus, so it
    // read as "no focus ring" (the face's folded full shelf). Not rendered = not a target.
    if (el.checkVisibility && !el.checkVisibility()) return;
    const r0 = el.getBoundingClientRect();
    if (r0.width < 1 && r0.height < 1) return;
    // HIT AREA, NOT PAINT BOX. Added 2026-09-26: a ::before/::after, position:absolute, with a
    // negative inset widens the tap target (kireji's 36px sound chip is 46px to a thumb). The
    // Fingers gate has credited this since the Flok false positives; Eyes now reads the same
    // geometry, so the two gates cannot disagree about one button.
    // An absolute pseudo is placed against the PADDING box, inside the border. Measured on
    // kireji: inset:-5px on a 2px-bordered 36px chip is a 42px hit area, not 46.
    const cs0 = getComputedStyle(el);
    const bl = parseFloat(cs0.borderLeftWidth)||0, bt = parseFloat(cs0.borderTopWidth)||0,
          br = parseFloat(cs0.borderRightWidth)||0, bb = parseFloat(cs0.borderBottomWidth)||0;
    let hx = r0.left, hy = r0.top, hr = r0.right, hb = r0.bottom;
    for (const pe of ['::before', '::after']) {
      const ps = getComputedStyle(el, pe);
      if (ps.content === 'none' || ps.position !== 'absolute') continue;
      const T = parseFloat(ps.top), L = parseFloat(ps.left), R = parseFloat(ps.right), B = parseFloat(ps.bottom);
      if (![T, L, R, B].every(Number.isFinite)) continue;
      hx = Math.min(hx, r0.left + bl + L); hy = Math.min(hy, r0.top + bt + T);
      hr = Math.max(hr, r0.right - br - R); hb = Math.max(hb, r0.bottom - bb - B);
    }
    const r = {width: hr - hx, height: hb - hy};
    el.focus();
    const f = getComputedStyle(el);
    const ring = (f.outlineStyle !== 'none' && parseFloat(f.outlineWidth) > 0)
              || (f.boxShadow && f.boxShadow !== 'none')
              || (f.borderColor !== cs.borderColor);
    out.targets.push({
      sel: el.tagName.toLowerCase() + (el.className && typeof el.className==='string'
            ? '.'+el.className.trim().split(/\s+/)[0] : ''),
      w: r.width, h: r.height, ring: ring,
      // [LAW] WCAG 2.5.8 Inline exception, mirrors studio-fingers (2026-11-05): any target
      // that computes display:inline inside a paragraph is constrained by the line-height.
      inlineLink: (el.tagName === 'A' && !!el.closest(INLINE_CTX)) ||
        (getComputedStyle(el).display === 'inline' && !!el.parentElement && !!el.parentElement.closest('p,li,blockquote,.prose'))
    });
    el.blur();
  });
  // Focusing the controls above scrolls the page to the last one; reset to the top
  // so first-screen measurements (opening wall, image floor) see the true first paint.
  window.scrollTo(0, 0);

  // ---- TOKEN-ROLE LAW: a token is atmosphere OR text, never both.
  // Read the real stylesheets the browser assembled (not a regex over source).
  // TOKEN-ROLE LAW.
  // NOTE: the CSSOM is USELESS for this. Chromium resolves var() into a computed
  // value before it ever reaches cssText or getPropertyValue, so no token name
  // survives. The RAW <style> source is the only place --amber is still spelled
  // '--amber'. So we read the source text -- but ONLY to find token NAMES, never
  // to reason about the cascade. Grounding still comes from the renderer.
  const asText = new Set(), asDeco = new Set();
  const DECO = /^(background|background-color|background-image|fill|stroke|box-shadow|border-color|border|outline-color|outline)$/;
  let raw = '';
  document.querySelectorAll('style').forEach(el => { raw += el.textContent + '\n'; });
  raw = raw.replace(/\/\*[\s\S]*?\*\//g, ' ');          // comments lie; strip them
  // every declaration, anywhere (inside @media too -- we only want prop:value pairs)
  const declRe = /([-\w]+)\s*:\s*([^;{}]+)/g;
  let dm;
  while ((dm = declRe.exec(raw)) !== null) {
    const prop = dm[1].trim();
    const val  = dm[2];
    if (prop.startsWith('--')) continue;                 // a definition, not a use
    const m = val.match(/var\(\s*(--[\w-]+)/g);
    if (!m) continue;
    const toks = m.map(x => x.replace(/var\(\s*/, ''));
    if (prop === 'color') toks.forEach(t => asText.add(t));
    else if (DECO.test(prop)) toks.forEach(t => asDeco.add(t));
  }
  out.tokens.text = [...asText];
  out.tokens.deco = [...asDeco];

  // ---- NO OPENING WALL: what is actually on screen at first paint?
  const vis = [...document.body.querySelectorAll('*')].filter(el=>{
    const cs = getComputedStyle(el);
    if (cs.display==='none'||cs.visibility==='hidden') return false;
    const r = el.getBoundingClientRect();
    return r.width>0 && r.height>0 && r.top < innerHeight && r.bottom > 0;
  });
  const GATEWORDS = /(comfort|palette|contrast|theme|colou?r scheme|text size|font size|choose your|pick a|preference|difficulty|accessib)/i;
  const gateEls = vis.filter(el=>{
    const cls = (typeof el.className==='string'? el.className:'') + ' ' + (el.id||'');
    const txt = (el.textContent||'').slice(0,80);
    const isCtl = /^(button|select|input)$/i.test(el.tagName) || /swatch|palette|stop|comfort/i.test(cls);
    return isCtl && (GATEWORDS.test(cls) || GATEWORDS.test(txt));
  });
  // scene = meaningful prose visible on load
  const prose = vis.filter(el=>{
    if (!/^(P|H1|H2|H3|LI|BLOCKQUOTE|FIGCAPTION)$/.test(el.tagName)) return false;
    const t = (el.textContent||'').trim();
    if (t.length <= 25) return false;
    // A gate's OWN headline is not a scene. 'Choose your comfort setting' cannot
    // rescue the wall it is the title of.
    if (GATEWORDS.test(t)) return false;
    // Nor can prose nested INSIDE the gate container.
    let p = el;
    while (p && p !== document.body) {
      const cls = (typeof p.className==='string'? p.className:'') + ' ' + (p.id||'');
      if (/swatch|palette|comfort|preference|gate|settings/i.test(cls)) return false;
      p = p.parentElement;
    }
    return true;
  });
  // is a gate element in the MAIN flow (not parked in a corner)?
  const inFlow = gateEls.filter(el=>{
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' || cs.position === 'absolute') return false;   // corner control: fine
    return r.width > innerWidth * 0.25 || r.height > 60;
  });
  out.firstScreen = {gates: inFlow.length, gateTxt: inFlow.slice(0,3).map(e=>(e.textContent||'').trim().slice(0,40)),
                     prose: prose.length, proseTxt: prose.slice(0,2).map(e=>(e.textContent||'').trim().slice(0,50))};

  // ---- comfort stops: find the classes that repaint the page
  const bodyClasses = new Set();
  for (const ss of document.styleSheets) {
    let rules; try { rules = ss.cssRules; } catch(e){ continue; }
    if (!rules) continue;
    for (const r of rules) {
      if (!r.selectorText) continue;
      const m = r.selectorText.match(/body\.([\w-]+)/g);
      // A STOP IS A CLASS THAT REPAINTS. Added 2026-09-26 (kireji-pond): body.still stops
      // motion and body.fzopen stops scroll; neither is a light stop, and grading them as
      // knobs that "change nothing" HALTed a correct build three times over. Only a rule that
      // declares a paint property (background, color, or a token) makes its class a stop.
      // t10 (a real fake knob that repaints by 0.004) still HALTs: it declares background.
      let paints = false;
      for (let i = 0; i < r.style.length; i++) {
        if (/^(background|color$|filter$|--)/.test(r.style[i])) { paints = true; break; }
      }
      if (m && paints) m.forEach(x=>bodyClasses.add(x.replace('body.','')));
    }
  }
  out.stops = [...bodyClasses];

"""

# resume: the rest of the page probe, with the clip body spliced in above.
PROBE = PROBE + _CLIP_BODY + r"""
  return out;
}
"""

# ---------------------------------------------------------------- audit core

# ── the ground shot ──────────────────────────────────────────────────────────
# TWO DEFECTS THIS CLOSES, both found 2026-09-01 by putting a gradient on Flok's
# primary button and measuring what the floor said about it (1.1:1, on dark ink over
# mint that is 10:1 to any eye):
#
#   1. THE BOX WAS NOT THE TEXT. px_bg_under was handed the element's border box, so
#      it sampled whatever showed through the button's 16px rounded corners — the
#      near-black page — and called it the backdrop. Fixed by sampling `trect`, a
#      Range over the element's contents. See the probe.
#   2. THE GLYPHS WERE THEIR OWN BACKDROP. Even cropped tight, the darkest pixel
#      "behind" dark ink is the ink. Fixed here, by painting the page again with the
#      glyphs made invisible and sampling THAT.
#
# Measured on canary p10 with both fixes off, one on, and both on: 1.08 / 1.00 / 8.84.
# Neither fix is sufficient alone — the first crop hides the second defect behind a
# worse number, which is exactly why one bug masked the other for so long.
#
# Nobody had noticed because this floor shipped with a HALT canary (t03) and no PASS
# canary: the side that wrongly blocks a correct build was never once exercised.
#
# The fix is the doctrine this whole tool was rebuilt on — ASK THE RENDERER rather
# than guess. Paint the page again with the glyphs made invisible and sample THAT.
# -webkit-text-fill-color is the right instrument and `color` is not: it blanks the
# glyph fill only, so currentColor still resolves and every border, SVG and shadow
# that derives from it paints exactly as it did. Layout is untouched, so the rects
# collected from the live page still land where they landed.
GROUND_CSS = ("*,*::before,*::after{-webkit-text-fill-color:transparent!important;"
              "text-shadow:none!important;-webkit-text-stroke-width:0!important}")

def ground_screenshot(page):
    """The page as painted, minus the glyphs. One shot serves every text on it."""
    page.evaluate("""(css)=>{let el=document.getElementById('se-ground-probe');
        if(!el){el=document.createElement('style');el.id='se-ground-probe';
        document.head.appendChild(el);} el.textContent=css;}""", GROUND_CSS)
    try:
        return page.screenshot()
    finally:
        page.evaluate("()=>{const el=document.getElementById('se-ground-probe');"
                      "if(el) el.remove();}")


def px_bg_under(png_bytes, rect, dpr=1):
    """Sample the ACTUAL painted pixels behind a text box.
    This is the check the old gate confessed it could not do: text on a photo
    or a gradient. Returns the WORST-CASE (most extreme) backdrop found.
    Feed it a ground_screenshot, never a plain one — see above."""
    try:
        from PIL import Image
    except ImportError:
        return None
    im = Image.open(io.BytesIO(png_bytes)).convert('RGB')
    x, y = int(rect['x']*dpr), int(rect['y']*dpr)
    w, h = int(rect['w']*dpr), int(rect['h']*dpr)
    x, y = max(0,x), max(0,y)
    w, h = min(w, im.width-x), min(h, im.height-y)
    if w < 2 or h < 2:
        return None
    crop = im.crop((x, y, x+w, y+h))
    px = list(crop.getdata())
    if not px:
        return None
    # worst case = the two luminance extremes actually present behind the glyphs
    lo = min(px, key=lum); hi = max(px, key=lum)
    return lo, hi

def resolve_ground(chain):
    """Nearest ancestor with an OPAQUE background. No guessing — the browser
    already told us the computed backgroundColor of every ancestor."""
    acc = None
    for link in chain:
        # An image or gradient ANYWHERE in the chain means the true backdrop is
        # not a single colour. Bail to pixel sampling immediately — this is the
        # case the old gate confessed it could not see.
        if link['img']:
            return (acc or (255, 255, 255)), link['sel'], link['img']
        c = parse_rgb(link['bg'])
        if not c:
            continue
        if c[3] <= 0.001:
            continue
        if acc is None:
            acc = flatten(c, (255,255,255))
        if c[3] >= 0.999:
            return flatten(c, (255,255,255)), link['sel'], None
    return (acc or (255,255,255)), '(page)', None

def audit_page(page, path, mode_label):
    halts = []
    d = page.evaluate(PROBE)

    # -- 1. CONTRAST (computed grounds)
    shot = None
    for t in d['texts']:
        fg = parse_rgb(t['color'])
        if not fg:
            continue
        ground, gsel, gimg = resolve_ground(t['chain'])
        fgc = flatten(fg, ground)
        floor = WCAG_LARGE if t['large'] else WCAG_TEXT

        if gimg:  # text sits on an image/gradient -> MEASURE THE PIXELS
            if shot is None:
                shot = ground_screenshot(page)
            got = px_bg_under(shot, t.get('trect') or t['rect'])
            if got:
                lo, hi = got
                r = min(ratio(fgc, lo), ratio(fgc, hi))
                if r < floor:
                    halts.append(f"CONTRAST [{mode_label}] {t['sel']} \"{t['text'][:24]}\" "
                                 f"= {r:.1f}:1 on IMAGE/GRADIENT (floor {floor})")
                continue

        r = ratio(fgc, ground)
        if r < floor:
            halts.append(f"CONTRAST [{mode_label}] {t['sel']} \"{t['text'][:24]}\" "
                         f"= {r:.1f}:1 (floor {floor}, ground {gsel})")

    # -- 2. TOKEN-ROLE LAW
    dual = set(d['tokens']['text']) & set(d['tokens']['deco'])
    for tok in sorted(dual):
        halts.append(f"TOKEN_ROLE {tok} is BOTH text and decoration. "
                     f"Light may be dim; text may not. Split it.")

    # -- 3. TOUCH TARGETS + FOCUS
    for t in d['targets']:
        if (t['w'] < MIN_TARGET or t['h'] < MIN_TARGET) and not t.get('inlineLink'):
            halts.append(f"TOUCH_TARGET [{mode_label}] {t['sel']} "
                         f"{t['w']:.0f}x{t['h']:.0f}px (floor {MIN_TARGET})")
        if not t['ring']:
            halts.append(f"FOCUS [{mode_label}] {t['sel']} has no visible focus ring")

    # -- 4. EMOJI
    for e in d['emoji']:
        halts.append(f"EMOJI in rendered text: \"{e}\"")

    # -- 4b. CLIPPED TEXT (floor 11) — words rendered and then thrown away.
    # See the probe for why this floor exists and what it deliberately forgives.
    for c in d.get('clipped', []):
        if c.get('window'):
            continue          # a window, not a box — see CLIP_WINDOW_RATIO
        halts.append(f"CLIPPED_TEXT [{mode_label}] {c['sel']} \"{c['text'][:28]}\" is cut off "
                     f"by {c['by']}px inside {c['clipSel']} "
                     f"({c['boxH']}px box holding {c['needH']}px of content). "
                     f"Text that is laid out and then discarded is text nobody can read.")

    # -- 5. NO OPENING WALL
    fs = d['firstScreen']
    if fs['gates'] > 0 and fs['prose'] == 0:
        halts.append(f"OPENING_WALL first paint shows {fs['gates']} preference control(s) "
                     f"{fs['gateTxt']} and NO scene. Comfort is a corner control, never a gate.")

    # -- 6. >50% IMAGE (founder standing floor — NEVER ENFORCED UNTIL 2026-07-13)
    #
    # The postmortem named this gap out loud: ">50% IMAGE — a stated founder floor.
    # Unchecked." So it was a wish. Every game shipped without anyone measuring it,
    # and Choose Your Leader v5 shipped a text wall as a result.
    #
    # SCOPE (caught by the canary, 2026-07-13): this floor is a GAME floor. The
    # golden canary p07 is a 3-line fixture with zero art and it must still pass —
    # it exists to test contrast, not scenery. A spec, a hub, a report, and a test
    # fixture are not games and are not graded as broken ones. Tableau Sweep #1 made
    # exactly this mistake, grading a spec-log as a failed game.
    #
    # A surface declares itself a game with:  <meta name="tsp:surface" content="game">
    # Absent that tag, the floor still runs on anything that ALREADY carries scene
    # art (>=1 media element) — because a game with a picture in it is a game.
    #
    # ARITHMETIC, not judgment: on the FIRST SCREEN, sum the area of every
    # scene-carrying element — svg/img/canvas/video/picture, or any element painting
    # a background-image or gradient — and divide by the viewport. Under 50% HALTs.
    img = page.evaluate("""() => {
      window.scrollTo(0, 0);   // measure the FIRST screen, not wherever focus left us
      const vw = innerWidth, vh = innerHeight, VP = vw * vh;
      const seen = [], hits = [];
      for (const el of document.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (r.width < 8 || r.height < 8) continue;
        if (r.top > vh || r.bottom < 0 || r.left > vw || r.right < 0) continue;
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
        const tag = el.tagName.toLowerCase();
        const painted = cs.backgroundImage && cs.backgroundImage !== 'none';
        const isMedia = ['svg','img','canvas','video','picture'].includes(tag);
        if (!isMedia && !painted) continue;
        if (seen.some(s => s.contains(el))) continue;   // no double-count of children
        seen.push(el);
        const w = Math.min(r.right, vw) - Math.max(r.left, 0);
        const h = Math.min(r.bottom, vh) - Math.max(r.top, 0);
        hits.push({ tag, area: Math.max(0, w) * Math.max(0, h) });
      }
      const m = document.querySelector('meta[name="tsp:surface"]');
      return { pct: VP ? (hits.reduce((a,b)=>a+b.area,0) / VP) * 100 : 0,
               n: hits.length,
               surface: m ? m.content : '',
               top: hits.sort((a,b)=>b.area-a.area).slice(0,3).map(h=>h.tag) };
    }""")
    is_game = img['surface'] == 'game' or (not img['surface'] and img['n'] > 0)
    if is_game and img['pct'] < 50:
        halts.append(f"IMAGE_FLOOR [{mode_label}] first screen is {img['pct']:.0f}% image "
                     f"(floor 50). {img['n']} scene element(s): {', '.join(img['top']) or 'none'}. "
                     f"Scene-first is a floor, not a preference — a first paint that is mostly "
                     f"prose is a document with buttons.")

    return halts, d

# ---------------------------------------------------------------- floors 13 + 14
# Added 2026-11-08 from a founder phone screenshot of lab/en195-course.html in dark
# mode: the spiral diagram's track and one of its five stops sat at ~1.3:1 on their
# panel. Twelve floors were green on it because every floor graded GLYPHS. Nothing
# ever asked whether a line, a dot or an icon that carries meaning can be seen.
# Same screenshot: two floating corner pills (Top, Comfort) parked over the reading
# column. Nothing asked whether a fixed control covers words the reader needs.
#
# FLOOR 13 — NON-TEXT CONTRAST (WCAG 2.2 SC 1.4.11, 3:1)
#   Measured by asking the renderer, the v3 doctrine: screenshot the mark, hide the
#   mark, screenshot again. The pixels that changed ARE the mark; the same pixels in
#   the second shot ARE its ground. Opacity, filters, gradients and shadows are all
#   inside the measurement, not guessed.
#   SCOPE, arithmetic and overridable:
#     - only SVGs a reader is told about (role="img" or a <title>); aria-hidden is decor
#     - a "diagram" (<= DIAGRAM_MAX_SHAPES drawn shapes AND stroke-only lines running at
#       least half its width, the thing that connects marks) HALTs under 3:1   [HOUSE heuristic]
#     - a "scene" (more shapes) is paint, not chart: under 3:1 is an ART_VALUE advisory
#     - data-graphic="diagram" | "scene" on the <svg> overrides the count
#     - a shape painting more than FIELD_MAX of its SVG is a field (sky, hill), not a mark
#     - translucent paint (opacity < 0.6) is glaze or shadow, never graded
# FLOOR 14 — OBSCURED (WCAG 2.2 SC 2.4.11 for focus; reachability for text)
#   A fixed or sticky element HALTs when (a) at the top or the bottom of the page,
#   where no further scroll exists, it covers more than a third of a text block that
#   is not its own, or (b) a focused control is more than half hidden under it.
#   Footprint over FOOTPRINT_MAX of the phone screen is an advisory.
NONTEXT_MIN = 3.0
DIAGRAM_MAX_SHAPES = 24
FIELD_MAX = 0.15
MAX_MARKS = 30       # per graphic
FOOTPRINT_MAX = 0.08
ADVISORIES = []       # printed by main(); never change the exit code

_MARKS_JS = r"""() => {
  const out = [];
  document.querySelectorAll('[data-se-mark]').forEach(e => e.removeAttribute('data-se-mark'));
  const SH = 'circle,ellipse,rect,path,polygon,polyline,line,use';
  let n = 0;
  for (const svg of document.querySelectorAll('svg')) {
    if (svg.closest('[aria-hidden="true"]')) continue;
    const told = svg.getAttribute('role') === 'img' || svg.querySelector(':scope > title');
    if (!told) continue;
    const sr = svg.getBoundingClientRect();
    if (sr.width < 40 || sr.height < 40) continue;          // an icon inside a button is graded as the button
    const cs0 = getComputedStyle(svg);
    if (cs0.display === 'none' || cs0.visibility === 'hidden') continue;
    const shapes = [...svg.querySelectorAll(SH)].filter(s => !s.closest('defs,clipPath,mask,symbol,pattern,marker'));
    const decl = svg.getAttribute('data-graphic');
    // A diagram CONNECTS things: it carries at least one stroke-only line (a track, an
    // arrow, an axis). Scene paint is filled shapes. p08 (a 3-rect living room) is a scene.
    // ...and the line must actually travel: total stroke-only length of at least half
    // the graphic's width. A ribbon seal's 8%% flourish is ornament (measured 0.08 on
    // en195-course.html); the spiral track is 2.26, the Down the Nerve gauge 0.84.
    const vb = svg.viewBox && svg.viewBox.baseVal, vw0 = vb && vb.width ? vb.width : sr.width;
    let run = 0;
    for (const s of shapes) { const c = getComputedStyle(s);
      if ((c.fill === 'none' || s.tagName === 'line') && c.stroke !== 'none' && parseFloat(c.strokeWidth) >= 2)
        try { run += s.getTotalLength(); } catch (e) {} }
    const stroked = run >= 0.5 * vw0;
    const kind = decl || (shapes.length <= %d && stroked ? 'diagram' : 'scene');
    const sarea = sr.width * sr.height;
    let per = 0;
    for (const s of shapes) {
      if (per >= %d) break;               // cap PER graphic, so a busy hero cannot starve the diagram below it
      const cs = getComputedStyle(s);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      let op = 1, e = s;
      while (e && e !== svg.parentElement) { op *= +getComputedStyle(e).opacity; e = e.parentElement; }
      const hasFill = cs.fill !== 'none' && !/rgba\(.*,\s*0\)$/.test(cs.fill);
      const hasStroke = cs.stroke !== 'none' && parseFloat(cs.strokeWidth) > 0;
      const po = hasFill ? +cs.fillOpacity : +cs.strokeOpacity;
      if (op * po < 0.6) continue;
      const r = s.getBoundingClientRect();
      if (r.width < 2 && r.height < 2) continue;
      if (hasFill && (r.width * r.height) / sarea > 0.6) continue;  // backdrop rect
      s.setAttribute('data-se-mark', String(n)); per++;
      let label = s.tagName.toLowerCase();
      if (s.getAttribute('class')) label += '.' + s.getAttribute('class').trim().split(/\s+/).join('.');
      out.push({i: n, label, kind, svgArea: sarea,
                svgId: svg.id || (svg.querySelector('title') ? svg.querySelector('title').textContent.slice(0, 40) : 'svg')});
      n++;
    }
  }
  return out;
}""" % (DIAGRAM_MAX_SHAPES, MAX_MARKS)

def _shot_mark(page, i):
    """Two shots of one mark's neighbourhood: painted, and with the mark hidden."""
    r = page.evaluate("""(i)=>{const s=document.querySelector('[data-se-mark="'+i+'"]');
        if(!s) return null; s.scrollIntoView({block:'center',inline:'center',behavior:'instant'});
        const b=s.getBoundingClientRect(); return {x:b.left,y:b.top,w:b.width,h:b.height,
        vw:innerWidth,vh:innerHeight};}""", i)
    if not r:
        return None
    pad = 8
    x0, y0 = max(0, r['x']-pad), max(0, r['y']-pad)
    x1, y1 = min(r['vw'], r['x']+r['w']+pad), min(r['vh'], r['y']+r['h']+pad)
    if x1 - x0 < 3 or y1 - y0 < 3:
        return None
    clip = {'x': x0, 'y': y0, 'width': x1-x0, 'height': y1-y0}
    a = page.screenshot(clip=clip, animations='disabled')
    page.evaluate("(i)=>{document.querySelector('[data-se-mark=\"'+i+'\"]').style.setProperty('visibility','hidden','important')}", i)
    try:
        b = page.screenshot(clip=clip, animations='disabled')
    finally:
        page.evaluate("(i)=>{document.querySelector('[data-se-mark=\"'+i+'\"]').style.removeProperty('visibility')}", i)
    return a, b

def _mark_ratio(a_png, b_png, svg_area):
    """SC 1.4.11 grades a mark against its ADJACENT colours, so measure the mark's
    outer edge, not its belly: an outlined stop (a punched washer, a rim) is legible
    by its rim whatever its fill. Edge = the outermost ring of the mark's PAINT, where
    paint means a change of at least 40% of the strongest change, so a soft drop
    shadow (small change) is never mistaken for the edge."""
    from PIL import Image
    A = Image.open(io.BytesIO(a_png)).convert('RGB')
    B = Image.open(io.BytesIO(b_png)).convert('RGB')
    W, H = A.size
    pa, pb = A.tobytes(), B.tobytes()
    diff = [0] * (W * H)
    for i in range(W * H):
        k = 3 * i
        diff[i] = max(abs(pa[k]-pb[k]), abs(pa[k+1]-pb[k+1]), abs(pa[k+2]-pb[k+2]))
    changed = sum(1 for d in diff if d > 6)
    if changed < 12:
        return None, changed                # nothing visible changed: covered, or zero contrast
    if changed > FIELD_MAX * svg_area:
        return 'field', changed
    top = max(diff); cut = max(7, 0.4 * top)
    paint = [d >= cut for d in diff]
    edge = []
    for y in range(H):
        for x in range(W):
            i = y * W + x
            if not paint[i]: continue
            if x == 0 or y == 0 or x == W-1 or y == H-1 or not (paint[i-1] and paint[i+1] and paint[i-W] and paint[i+W]):
                edge.append(i)
    # The outermost ring is antialiased, a blend of mark and ground, so it always
    # under-reads. Grade the SECOND ring in: true paint, still at the boundary.
    es = set(edge)
    inner = [i for i in range(W * H) if paint[i] and i not in es]
    ins = set(inner)
    ring2 = [i for i in inner if (i-1 not in ins) or (i+1 not in ins) or (i-W not in ins) or (i+W not in ins)]
    if len(ring2) >= 6:
        edge = ring2
    elif len(edge) < 6:
        edge = [i for i in range(W * H) if paint[i]]
    def med(buf):
        ls = sorted((lum((buf[3*i], buf[3*i+1], buf[3*i+2])), i) for i in edge)
        i = ls[len(ls)//2][1]
        return (buf[3*i], buf[3*i+1], buf[3*i+2])
    return ratio(med(pa), med(pb)), changed

_INSTANT = ("()=>{document.documentElement.style.setProperty('scroll-behavior','auto','important');"
            "document.body&&document.body.style.setProperty('scroll-behavior','auto','important')}")
# html{scroll-behavior:smooth} turns every scrollTo into an animation: a rect read the
# next instant is mid-flight. Found 2026-11-08 on en195-course.html, where it hid the
# very spiral this floor was written for. Both floors pin scrolling to instant first.

def nontext_halts(page, mode_label):
    halts = []
    page.evaluate(_INSTANT)
    try:
        marks = page.evaluate(_MARKS_JS)
    except Exception as e:
        return [f"NONTEXT [{mode_label}] could not enumerate marks: {e}"]
    y0 = page.evaluate("()=>scrollY")
    for m in marks:
        shots = _shot_mark(page, m['i'])
        if not shots:
            continue
        r, npx = _mark_ratio(shots[0], shots[1], m['svgArea'])
        if r is None:
            # A mark that changes no pixel when hidden is either covered or the same
            # colour as its ground. Covered marks are not our business; same-colour is.
            if npx == 0 and m['kind'] == 'diagram':
                ADVISORIES.append(f"NONTEXT_GHOST [{mode_label}] {m['label']} in \"{m['svgId']}\" "
                                  f"changes no pixel when hidden: covered, or the colour of its ground")
            continue
        if r == 'field':
            continue
        if r < NONTEXT_MIN:
            msg = (f"{m['label']} in \"{m['svgId']}\" = {r:.1f}:1 against what it sits on "
                   f"(floor {NONTEXT_MIN}, SC 1.4.11)")
            if m['kind'] == 'diagram':
                halts.append(f"NONTEXT [{mode_label}] {msg}. A line or a dot that carries "
                             f"meaning is read, not glimpsed.")
            else:
                ADVISORIES.append(f"ART_VALUE [{mode_label}] {msg} — scene paint; Hitchcock "
                                  f"decides whether it is meant to recede")
    page.evaluate("(y)=>{scrollTo(0,y);document.querySelectorAll('[data-se-mark]')"
                  ".forEach(e=>e.removeAttribute('data-se-mark'))}", y0)
    return halts

_OVERLAYS_JS = r"""() => {
  const vw = innerWidth, vh = innerHeight, out = [];
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    if (el.hidden || el.closest('[hidden]')) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    if ((r.width * r.height) / (vw * vh) > 0.6) continue;      // a backdrop, not an overlay
    if (cs.position === 'sticky' && (r.bottom < 0 || r.top > vh)) continue;
    if (out.some(o => o.el.contains(el))) continue;
    out.push({el, sel: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') +
              (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '')});
  }
  window.__seOverlays = out.map(o => o.el);
  return out.map(o => o.sel);
}"""

_COVER_JS = r"""(edge) => {
  // edge: 'top' | 'bottom' | 'focus'
  const ovs = (window.__seOverlays || []).map(el => ({el, r: el.getBoundingClientRect(),
      sel: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '')}))
      .filter(o => o.r.width > 0 && o.r.height > 0 && o.r.bottom > 0 && o.r.top < innerHeight);
  const ov = (a, b) => Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) *
                       Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
  const hits = [];
  const scrollable = document.documentElement.scrollHeight > innerHeight + 4;
  const vis = r => r.bottom > 0 && r.top < innerHeight && r.width > 0 && r.height > 0;
  const blocks = [...document.querySelectorAll('p,li,h1,h2,h3,h4,dd,dt,td,th,figcaption,blockquote,label,a,button')]
      .filter(el => (el.innerText || '').trim().length > 1);
  // graded per LINE, not per block: one buried line in a two-line paragraph is a
  // buried line, whatever fraction of the block it is
  for (const el of blocks) {
    const br = el.getBoundingClientRect();
    if (!vis(br)) continue;
    const rg = document.createRange(); rg.selectNodeContents(el);
    const lines = [...rg.getClientRects()].filter(r => r.width > 12 && r.height > 6 && vis(r));
    let done = false;
    for (const o of ovs) {
      if (done) break;
      if (o.el.contains(el) || el.contains(o.el)) continue;
      const mid = (o.r.top + o.r.bottom) / 2, low = mid > innerHeight / 2;
      if (scrollable && ((edge === 'top' && low) || (edge === 'bottom' && !low))) continue;
      for (const r of lines) {
        const a = ov(r, o.r) / (r.width * r.height);
        if (a <= 0.5) continue;
        // only an overlay PAINTED above the line covers it: probe the CENTRE of the
        // intersection, since a rounded pill's corner lets the page show through
        const cx = (Math.max(r.left, o.r.left) + Math.min(r.right, o.r.right)) / 2,
              cy = (Math.max(r.top, o.r.top) + Math.min(r.bottom, o.r.bottom)) / 2;
        const top = document.elementFromPoint(Math.min(cx, innerWidth - 1), Math.min(cy, innerHeight - 1));
        if (!top || !o.el.contains(top)) continue;
        hits.push({sel: o.sel, text: el.innerText.trim().slice(0, 28), pct: Math.round(a * 100)});
        done = true; break;
      }
    }
  }
  const fp = ovs.reduce((s, o) => s + ov(o.r, {left: 0, top: 0, right: innerWidth, bottom: innerHeight}), 0)
             / (innerWidth * innerHeight);
  return {hits, footprint: fp};
}"""

def obscured_halts(page, mode_label):
    halts = []
    page.evaluate(_INSTANT)
    try:
        sels = page.evaluate(_OVERLAYS_JS)
    except Exception as e:
        return [f"OBSCURED [{mode_label}] could not enumerate overlays: {e}"]
    if not sels:
        return halts
    seen = set()
    for edge, js in (('top', "()=>scrollTo(0,0)"),
                     ('bottom', "()=>scrollTo(0,document.documentElement.scrollHeight)")):
        page.evaluate(js); page.wait_for_timeout(60)
        res = page.evaluate(_COVER_JS, edge)
        for h in res['hits']:
            k = (edge, h['sel'], h['text'])
            if k in seen: continue
            seen.add(k)
            halts.append(f"OBSCURED [{mode_label}] {h['sel']} covers {h['pct']}% of a line of "
                         f"\"{h['text']}\" at the {edge} of the page, where no scroll can "
                         f"move it out from under. Pad the page by the overlay's height.")
        if edge == 'top' and res['footprint'] > FOOTPRINT_MAX:
            ADVISORIES.append(f"FOOTPRINT [{mode_label}] fixed controls cover "
                              f"{res['footprint']*100:.0f}% of a 390x844 screen "
                              f"(advisory over {FOOTPRINT_MAX*100:.0f}%): {', '.join(sels[:4])}")
    # focus not obscured — tab every control and measure what the browser scrolled to
    n = page.evaluate("()=>document.querySelectorAll('a[href],button,input,select,textarea,[tabindex]:not([tabindex=\"-1\"])').length")
    page.evaluate("()=>scrollTo(0,0)")
    for _ in range(min(n, 120)):
        page.keyboard.press('Tab')
        got = page.evaluate(r"""() => {
          const f = document.activeElement; if (!f || f === document.body) return null;
          const r = f.getBoundingClientRect(); if (!r.width || !r.height) return null;
          for (const o of (window.__seOverlays || [])) {
            if (o.contains(f)) continue;
            const q = o.getBoundingClientRect();
            const a = Math.max(0, Math.min(r.right, q.right) - Math.max(r.left, q.left)) *
                      Math.max(0, Math.min(r.bottom, q.bottom) - Math.max(r.top, q.top));
            const t = document.elementFromPoint(Math.min(Math.max(r.left + r.width/2, 0), innerWidth-1),
                                                Math.min(Math.max(r.top + r.height/2, 0), innerHeight-1));
            if (a / (r.width * r.height) > 0.5 && t && o.contains(t))
              return {f: f.tagName.toLowerCase() + ' "' + (f.innerText || f.getAttribute('aria-label') || '').trim().slice(0, 24) + '"',
                      o: o.tagName.toLowerCase() + (o.id ? '#' + o.id : '')};
          }
          return null;
        }""")
        if got:
            k = ('focus', got['f'])
            if k not in seen:
                seen.add(k)
                halts.append(f"OBSCURED [{mode_label}] focused {got['f']} is more than half "
                             f"hidden under {got['o']} (SC 2.4.11). Add scroll-padding.")
    page.evaluate("()=>{document.activeElement&&document.activeElement.blur();scrollTo(0,0)}")
    return halts

def audit(path, no_net=True):
    from playwright.sync_api import sync_playwright
    halts = []
    external = []
    with sync_playwright() as p:
        _exe = os.environ.get('SE_CHROME')  # optional explicit chromium path
        b = p.chromium.launch(**({'executable_path': _exe} if _exe else {}))
        try:
            ctx = b.new_context(viewport={'width':390,'height':844})  # phone-width

            def on_req(r):
                u = r.url
                if u.startswith(('http://','https://')) and 'file://' not in u:
                    host = re.match(r'https?://([^/]+)', u)
                    if host:
                        external.append(host.group(1))
            ctx.on('request', on_req)

            page = ctx.new_page()
            page.goto('file://' + os.path.abspath(path), wait_until='load')
            page.wait_for_timeout(250)

            h, d = audit_page(page, path, 'default')
            halts += h
            # -- 4c. ESCAPED TEXT (floor 12), across the text scales a reader uses
            halts += escape_halts(page, 'default')
            # -- 4d. NON-TEXT CONTRAST (floor 13) and OBSCURED (floor 14)
            halts += nontext_halts(page, 'default')
            halts += obscured_halts(page, 'default')

            # -- 6. OFFLINE FLOOR
            for host in sorted(set(external)):
                halts.append(f"OFFLINE external host contacted: {host} "
                             f"(single-file, offline floor)")

            # -- 7. COMFORT STOPS: separation + each stop audited independently
            stops = d['stops']
            lums = {}
            base = page.evaluate("()=>getComputedStyle(document.body).backgroundColor")
            bc = parse_rgb(base)
            if bc:
                lums['(default)'] = lum(flatten(bc,(255,255,255)))
            for s in stops:
                page.evaluate(f"()=>{{document.body.className='{s}';}}")
                page.wait_for_timeout(80)
                sb = parse_rgb(page.evaluate("()=>getComputedStyle(document.body).backgroundColor"))
                if sb:
                    lums[s] = lum(flatten(sb,(255,255,255)))
                h2, _ = audit_page(page, path, s)
                # CLIPPED_TEXT travels with CONTRAST through the stop re-runs: a stop
                # that changes the type scale can slice a box that fit at the default.
                halts += [x for x in h2 if x.startswith(('CONTRAST', 'CLIPPED_TEXT'))]
            page.evaluate("()=>{document.body.className='';}")

            ks = list(lums.items())
            for i in range(len(ks)):
                for j in range(i+1, len(ks)):
                    (n1,l1),(n2,l2) = ks[i], ks[j]
                    if abs(l1-l2) < STOP_SEP_MIN:
                        halts.append(f"STOP_SEPARATION '{n1}' and '{n2}' differ by only "
                                     f"{abs(l1-l2):.3f} luminance (floor {STOP_SEP_MIN}). "
                                     f"A knob that changes nothing is a WALL.")

            # -- 8. DARK MODE / FORCED COLORS (where the EN195 bug hides)
            for scheme in ('dark',):
                page.emulate_media(color_scheme=scheme)
                page.wait_for_timeout(80)
                h3, _ = audit_page(page, path, f'prefers-{scheme}')
                halts += [x for x in h3 if x.startswith(('CONTRAST', 'CLIPPED_TEXT'))]
                halts += nontext_halts(page, f'prefers-{scheme}')
            page.emulate_media(color_scheme='light')
        finally:
            b.close()

    # dedupe, then order by severity. The headline defect must lead: a preference
    # gate on first paint is a WALL, and reporting its button size first buries it.
    SEV = {'OPENING_WALL':0, 'CLIPPED_TEXT':1, 'OFFLINE':2, 'EMOJI':3, 'CONTRAST':4,
           'NONTEXT':4, 'OBSCURED':4, 'TOKEN_ROLE':5, 'STOP_SEPARATION':6, 'FOCUS':7, 'TOUCH_TARGET':8}
    out, s = [], set()
    for x in halts:
        if x not in s:
            s.add(x); out.append(x)
    out.sort(key=lambda h: SEV.get(h.split()[0], 9))
    return out

# ---------------------------------------------------------------- adaptivity
# ADVISORY, not a HALT. Per the adaptive-system amendment (OS §3.1, founder ruling
# 2026-08-02): the founder's profile is the DEFAULT preset, not the only one. A build
# should hold contrast across the profiles a real user can actually select, and across
# the OS preference queries their device sets. These grade each shipped profile and
# report the gaps as advisories — so the fleet can be driven green over time, the way
# the contrast floor itself was rolled in. Promotion to HALT is a founder call.

def grade_adaptivity(path):
    from playwright.sync_api import sync_playwright
    warns = []
    with sync_playwright() as p:
        _exe = os.environ.get('SE_CHROME')
        b = p.chromium.launch(**({'executable_path': _exe} if _exe else {}))
        try:
            ctx = b.new_context(viewport={'width':390,'height':844})
            page = ctx.new_page()
            page.goto('file://' + os.path.abspath(path), wait_until='load')
            page.wait_for_timeout(250)

            def contrast_only(label):
                try:
                    h, _ = audit_page(page, path, label)
                except Exception as e:
                    return [f"ADAPTIVITY [{label}] could not grade: {e}"]
                # only CONTRAST travels across profiles; touch/emoji/image are mode-invariant
                return [x.replace('CONTRAST', 'ADAPTIVITY', 1) for x in h if x.startswith('CONTRAST')]

            # -- OS preference queries a real user's device sets --
            page.emulate_media(contrast='more'); page.wait_for_timeout(60)
            warns += contrast_only('prefers-contrast:more')
            page.emulate_media(contrast='no-preference')

            page.emulate_media(forced_colors='active'); page.wait_for_timeout(60)
            warns += contrast_only('forced-colors')
            page.emulate_media(forced_colors='none')

            # -- Comfort Kernel v2 selectable profiles. Setting a profile a page does
            #    not define is a no-op — only profiles the page actually ships grade. --
            for dl in ('dusk', 'night'):
                page.evaluate(f"()=>document.documentElement.setAttribute('data-light','{dl}')")
                page.wait_for_timeout(60)
                warns += contrast_only(f'profile:{dl}')
            page.evaluate("()=>document.documentElement.removeAttribute('data-light')")
            page.evaluate("()=>document.documentElement.classList.add('se-contrast')")
            page.wait_for_timeout(60)
            warns += contrast_only('profile:se-contrast')
            page.evaluate("()=>document.documentElement.classList.remove('se-contrast')")
        finally:
            b.close()
    seen, out = set(), []
    for w in warns:
        if w not in seen:
            seen.add(w); out.append(w)
    return out

# ---------------------------------------------------------------- self-test

def self_test(verbose=True):
    """The auditor gates itself before it gates anything else.
    Half these canaries are FALSE-POSITIVE traps: correct files that v2 wrongly
    HALTed. Crying wolf is the failure that got the tool ignored."""
    here = os.path.dirname(os.path.abspath(__file__))
    cdir = os.path.join(here, 'canary')
    exp_path = os.path.join(cdir, 'EXPECTED.json')
    if not os.path.exists(exp_path):
        print("  SELF-TEST: canary corpus missing. Refusing to run.")
        return False
    expected = json.load(open(exp_path))

    fails = []
    for c in expected:
        f = os.path.join(cdir, c['file'])
        halts = audit(f); ADVISORIES.clear()
        got = 'HALT' if halts else 'PASS'
        ok = (got == c['expect'])
        if ok and c['expect'] == 'HALT' and c['code']:
            if not any(h.startswith(c['code']) for h in halts):
                ok = False
                got = f"HALT (wrong code: {halts[0].split()[0]})"
        if not ok:
            fails.append((c, got, halts))
        if verbose:
            mark = 'ok  ' if ok else 'FAIL'
            print(f"  {mark} {c['file']:<32} expect {c['expect']:<4} got {got}")

    if fails:
        print(f"\n  SELF-TEST FAILED — {len(fails)}/{len(expected)} canaries misgraded.")
        for c, got, halts in fails:
            print(f"\n    {c['file']}  ({c['why']})")
            print(f"      expected {c['expect']}, got {got}")
            for h in halts[:3]:
                print(f"        - {h}")
        print("\n  The auditor cannot grade its own canary. IT WILL NOT AUDIT.")
        return False
    print(f"\n  SELF-TEST PASSED — {len(expected)}/{len(expected)} canaries graded correctly.")
    return True

# ---------------------------------------------------------------- cli

def main():
    args = [a for a in sys.argv[1:]]
    if '--self-test' in args:
        print("\n  STUDIO EYES v3 · SELF-TEST\n  " + "-"*46)
        sys.exit(0 if self_test() else 1)

    skip = '--no-self-test' in args
    files = [a for a in args if not a.startswith('--')]
    if not files:
        print(__doc__)
        sys.exit(2)

    if not skip:
        print("\n  STUDIO EYES v3 · self-test\n  " + "-"*46)
        if not self_test(verbose=False):
            sys.exit(1)

    do_profiles = '--no-profiles' not in args
    bad = 0
    for f in files:
        halts = audit(f)
        print(f"\n  {os.path.basename(f)}")
        if not halts:
            print("     PASS")
        else:
            bad += 1
            print(f"     HALT — {len(halts)} defect(s):")
            for h in halts[:14]:
                print(f"       {h}")
            if len(halts) > 14:
                print(f"       ... +{len(halts)-14} more")
        mine = [a for a in dict.fromkeys(ADVISORIES)]
        ADVISORIES.clear()
        if mine:
            print(f"     ADVISORY — {len(mine)} (never blocks):")
            for a in mine[:8]:
                print(f"       {a}")
        # Adaptivity is ADVISORY: it never changes PASS/HALT or the exit code.
        if do_profiles:
            warns = grade_adaptivity(f)
            if warns:
                print(f"     ADAPTIVITY — {len(warns)} advisory (not a HALT; OS §3.1 selectable profiles):")
                for w in warns[:10]:
                    print(f"       {w}")
                if len(warns) > 10:
                    print(f"       ... +{len(warns)-10} more")
            else:
                print("     ADAPTIVITY — profiles hold (advisory)")
    print(f"\n  === {bad} of {len(files)} at HALT ===\n")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
