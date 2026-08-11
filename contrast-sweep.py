#!/usr/bin/env python3
"""CONTRAST SWEEP GATE - every route, every light mode, every element that paints text.

Born 2026-08-11 after TWO escapes in one day on the same page, both invisible to the
eyes we already had:

  1. WRONG MODE. The ladder emulated html[data-light="dusk"|"night"] and nothing else.
     Those selectors carry attribute specificity; the real @media(prefers-color-scheme:dark)
     rules do not - a media query adds no specificity - so equal-specificity base rules
     declared later in the sheet silently beat them. Card headings and price cells
     rendered near-black on a dark card (contrast 1.16) for every visitor whose phone
     was in dark mode. Three builds shipped green. The founder saw it on his phone.

  2. WRONG PAGE. The ladder only ever measured the HOME route. Every other page is
     display:none at load, so a zero-box element was skipped as "not painted" and the
     four property pages and the whole rental application had never been contrast-checked
     in any mode, ever.

So this gate walks the routes and emulates the real color schemes, and it does not carry
a selector list: anything that renders its own text gets measured. A selector list only
ever finds what someone already thought to look for.

Scope: pages that declare a dark mode (@media prefers-color-scheme, or an html[data-light]
ladder). Everything else is left to tick 1's per-file comfort gate, so this tick cannot
ambush the wider corpus with debt nobody has measured yet.

Floor: 4.5:1 against the nearest opaque ancestor background. Blocks.

Usage: contrast-sweep.py <file.html | dir> [...]
Env:   SWEEP_ROUTES  comma-separated hash routes to visit (default: the Leeder set)
"""
import os
import pathlib
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("contrast-sweep: SKIPPED LOUD - playwright absent, this gate is BLIND. Not a pass.")
    sys.exit(2)

CHROMIUM = os.environ.get("CHROMIUM_PATH", "")
ROUTES = os.environ.get("SWEEP_ROUTES", ",#/bowdoin,#/cambridge,#/perkins,#/royal,#/apply").split(",")
MODES = ["day", "dusk", "night", "system-dark"]
FLOOR = 4.5

COLLECT = r"""
() => {
  function effBg(el){
    let e = el;
    while (e) {
      const bg = getComputedStyle(e).backgroundColor;
      const m = bg.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
      if (m && (m[4] === undefined || +m[4] > 0.85)) return bg;
      e = e.parentElement;
    }
    return getComputedStyle(document.body).backgroundColor;
  }
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) continue;
    const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim())
                                  .map(n => n.textContent.trim()).join(' ');
    if (!own) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
    if (el.closest('.skip')) continue;
    out.push({tag: el.tagName.toLowerCase(),
              cls: (typeof el.className === 'string' && el.className.trim())
                     ? '.' + el.className.trim().split(/\s+/).join('.') : '',
              text: own.slice(0, 42), fg: cs.color, bg: effBg(el),
              size: parseFloat(cs.fontSize), weight: cs.fontWeight});
  }
  return out;
}
"""


def rgb(s):
    import re
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)", s or "")
    return tuple(float(m.group(i)) for i in (1, 2, 3)) if m else None


def lum(c):
    def f(x):
        x /= 255.0
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = c
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


targets = []
for arg in (sys.argv[1:] or ["."]):
    p = pathlib.Path(arg)
    if p.is_dir():
        targets += sorted(q for q in p.rglob("*.html")
                          if not any(part.startswith(".") or part in ("node_modules", "archive", "rescued")
                                     for part in q.parts))
    elif p.is_file() and p.suffix == ".html":
        targets.append(p)

halts, measured, pages = [], 0, 0
launch = {"executable_path": CHROMIUM} if CHROMIUM else {}
with sync_playwright() as pw:
    browser = pw.chromium.launch(**launch)
    for f in targets:
        src = f.read_text(encoding="utf-8", errors="replace")
        if "prefers-color-scheme" not in src and "data-light" not in src:
            continue                                     # no dark mode declared: out of scope
        routes = ROUTES if "data-nav" in src else [""]   # multi-route single-page sites only
        pages += 1
        url = f.resolve().as_uri()
        for mode in MODES:
            sys_dark = mode == "system-dark"
            ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                      color_scheme="dark" if sys_dark else "light")
            page = ctx.new_page()
            page.route("**/*", lambda r: r.abort() if r.request.url.startswith("http") else r.continue_())
            page.goto(url, wait_until="load")
            if not sys_dark:
                page.evaluate("m => document.documentElement.setAttribute('data-light', m)", mode)
            for route in routes:
                page.evaluate("h => { location.hash = h || '#/'; }", route)
                page.wait_for_timeout(320)
                for c in page.evaluate(COLLECT):
                    fg, bg = rgb(c["fg"]), rgb(c["bg"])
                    if not fg or not bg:
                        continue
                    measured += 1
                    cr = contrast(fg, bg)
                    if cr < FLOOR:
                        halts.append(f'{f} [{mode}] {route or "home"} {c["tag"]}{c["cls"]} '
                                     f'contrast {cr:.2f} {c["size"]}px/{c["weight"]} '
                                     f'"{c["text"]}" fg {c["fg"]} on {c["bg"]}')
            ctx.close()
    browser.close()

if halts:
    print("CONTRAST-SWEEP HALTS:")
    for h in sorted(set(halts)):
        print("  HALT " + h)
    sys.exit(1)
print(f"contrast-sweep: {pages} page(s), {measured} painted text elements measured across "
      f"{len(MODES)} modes - all clear {FLOOR}:1")
