#!/usr/bin/env python3
# STUDIO EYES v4 — RENDER-PROOF. Tight Spiral Productions.
# Belt beat 2 runs this by name: python3 studio-eyes-sweep.py [dir|file]
#
# THE v4 THESIS: ask the engine that lays out the page, then check the paint.
# v1-v3 reimplemented a browser with regex and guessed the cascade; every
# historical bug (7 in the ledger, plus the your-rp-world lie: token gate said
# 13.23:1, iOS painted 1.17:1) traces to that guess. v4 renders each comfort
# stop at phone and desktop widths through a real CSS layout engine
# (WeasyPrint), grounds every text run against its ALPHA-COMPOSITED ancestor
# backgrounds, and cross-checks the math against rasterized pixels.
#
# HALT classes (exit 1):
#   R1  rendered contrast below WCAG AA (4.5 / large 3.0) in ANY stop at ANY width
#   R2  PAINT MISMATCH — engine ground and rasterized pixel disagree
#       (the exact class that produced the historical false certification)
#   C1  color-scheme floor — no color-scheme declaration; phone browsers in OS
#       dark mode force-darken undeclared pages and destroy computed contrast
#       (found live on device 2026-07-22, confluence-massbay-assessment.html)
#   E1  font floor — used font-size below 18px anywhere / body base below 20px
#   H4  offline break — external resource hosts
#   EM  emoji in rendered text
# WARN classes: PROPS missing (skip-link / comfort control / nav),
#   JS present (dynamic styles invisible to a no-JS engine — hand-verify),
#   focus-visible absent.
# WATCH: HORVATH lens imported from staging-area.py (gate of record there).
# E2 BLAST RADIUS: every failure reported as a class across all swept files.
#
# SELF-TEST TEETH: two embedded fixtures run before every sweep. If the bad
# fixture fails to HALT or the good fixture fails to pass, the tool REFUSES
# TO CERTIFY ANYTHING and exits 2. An audit that lies is the disease.
#
# Named limitation (printed, never silent): JavaScript is not executed.
# Class-based comfort stops are covered by static injection; styles a script
# writes at runtime are not. Hand-verify dynamic states on device.

import re, sys, os, glob, subprocess, tempfile, importlib.util, io, contextlib

try:
    from weasyprint import HTML
    import weasyprint.formatting_structure.boxes as WB
except Exception as e:
    print("EYES v4 needs weasyprint (pip install weasyprint). " + str(e)); sys.exit(2)
try:
    from PIL import Image
    HAVE_PIL = True
except Exception:
    HAVE_PIL = False

WIDTHS = (390, 1100)            # phone truth and desktop truth
FONT_FLOOR_ABS, FONT_FLOOR_BODY = 18.0, 20.0
STOP_HINTS = ("dark", "softer", "warm", "warmdark", "night", "focus", "dim")

# ---------- arithmetic ----------
def lum(rgb):
    def f(c): return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(rgb[0]) + 0.7152*f(rgb[1]) + 0.0722*f(rgb[2])

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def composite(chain, base=(1.0, 1.0, 1.0)):
    """Alpha-composite ancestor backgrounds outermost-first over base white.
    This is the background-inheritance grounding done the way paint does it."""
    dst = base
    for col in chain:
        r, g, b, a = col
        if a <= 0: continue
        dst = tuple(r*a + d*(1-a) for r, d in zip((r, g, b), dst))
    return dst

# ---------- stop discovery (regex DISCOVERS names; the engine JUDGES) ----------
def discover_stops(src):
    stops = [None]                                  # None = base stop (Day)
    for m in re.finditer(r'body\.([A-Za-z][\w-]*)\s*[{,]', src):
        c = m.group(1)
        if c not in stops and any(h in c.lower() for h in STOP_HINTS):
            stops.append(c)
    return stops

def inject(src, stop, width):
    v = re.sub(r'<body(?![\w-])', '<body class="%s"' % stop, src, count=1) if stop else src
    return ('<style>@page{size:%dpx 6000px;margin:0}</style>' % width) + v

# ---------- the render-proof core ----------
def walk_text(box, anc, out):
    if isinstance(box, WB.TextBox) and box.text and box.text.strip():
        out.append((box, list(anc)))
    for ch in getattr(box, 'children', []):
        anc.append(box); walk_text(ch, anc, out); anc.pop()

def sweep_stop(src, stop, width, name, out, px_budget):
    label = "%s@%d" % (stop or "day", width)
    try:
        doc = HTML(string=inject(src, stop, width)).render()
    except Exception as e:
        out["R1"].append("%s: engine failed to lay out (%s) — stop UNTESTED, treat as HALT" % (label, e)); return
    texts = []
    for page in doc.pages:
        walk_text(page._page_box, [], texts)
    if not texts:
        out["R1"].append("%s: zero text laid out — stop UNTESTED, treat as HALT" % label); return
    worst = {}
    for box, anc in texts:
        c = tuple(box.style['color'])
        if c[3] <= 0: continue
        fs = float(box.style['font_size'])
        fw = box.style['font_weight']
        ground = composite([tuple(a.style['background_color']) for a in anc])
        r = ratio(c[:3], ground)
        big = fs >= 24 or (fs >= 18.66 and int(fw) >= 700)
        need = 3.0 if big else 4.5
        if r < need:
            key = (round(r, 2), box.text.strip()[:28])
            worst.setdefault(key, "%s: %.2f:1 < %.1f  '%s' fs=%.0f" % (label, r, need, box.text.strip()[:28], fs))
        if fs < FONT_FLOOR_ABS:
            out["E1"].append("%s: fs %.1fpx < 18px  '%s'" % (label, fs, box.text.strip()[:24]))
    for _, msg in sorted(worst.items())[:8]:
        out["R1"].append(msg)
    if len(worst) > 8:
        out["R1"].append("%s: (+%d more failing runs)" % (label, len(worst)-8))
    # body base floor — find the actual body box by tag, not tree position
    def find_body(box):
        if getattr(box, 'element_tag', None) == 'body': return box
        for ch in getattr(box, 'children', []):
            r = find_body(ch)
            if r is not None: return r
        return None
    try:
        body = find_body(doc.pages[0]._page_box)
        if body is not None and float(body.style['font_size']) < FONT_FLOOR_BODY:
            out["E1"].append("%s: body base %.0fpx < 20px" % (label, float(body.style['font_size'])))
    except Exception:
        pass
    # R2 paint crosscheck — pixel-verify the largest OPAQUE painted grounds.
    # Sampling inside each ground box's own rect (on-canvas only) is immune
    # to off-screen elements (skip-links) and glyph noise; text color is the
    # engine's, grounds are the paint's — the pair that lied historically.
    if HAVE_PIL and px_budget[0] > 0:
        try:
            grounds = []
            def collect(box, anc):
                bg = tuple(box.style['background_color'])
                if bg[3] > 0.5 and getattr(box, 'width', 0) > 40 and getattr(box, 'height', 0) > 20:
                    if box.position_x >= 0 and box.position_y >= 0:
                        grounds.append((box.width*box.height, box, list(anc)))
                for ch in getattr(box, 'children', []):
                    anc.append(box); collect(ch, anc); anc.pop()
            for page in doc.pages:
                collect(page._page_box, [])
            grounds.sort(key=lambda t: -t[0])
            with tempfile.TemporaryDirectory() as td:
                pdf = os.path.join(td, "p.pdf"); doc.write_pdf(pdf)
                subprocess.run(["pdftoppm", "-r", "96", "-png", "-f", "1", "-l", "1",
                                pdf, os.path.join(td, "r")], check=True, capture_output=True)
                pngs = sorted(glob.glob(os.path.join(td, "r*.png")))
                if pngs:
                    im = Image.open(pngs[0]).convert("RGB"); W, H = im.size
                    for _, box, anc in grounds[:5]:
                        if px_budget[0] <= 0: break
                        sx = int(box.position_x + 8); sy = int(box.position_y + 8)
                        if sx >= W or sy >= H: continue
                        px = tuple(v/255.0 for v in im.getpixel((sx, sy)))
                        gr = composite([tuple(a.style['background_color']) for a in anc]
                                       + [tuple(box.style['background_color'])])
                        if max(abs(px[i]-gr[i]) for i in range(3)) > 0.18:
                            bg_img = str(box.style['background_image'])
                            has_img = 'gradient' in bg_img or 'url(' in bg_img
                            why = ("gradient/image ground — R1 contrast above was computed on the fallback color; hand-verify this surface"
                                   if has_img else "engine and paint disagree — hand-verify this surface")
                            out["R2"].append("%s: PAINT MISMATCH on <%s>: engine %s vs pixel %s (%s)"
                                             % (label, getattr(box, 'element_tag', '?'),
                                                tuple(round(v, 2) for v in gr), tuple(round(v, 2) for v in px), why))
                        px_budget[0] -= 1
        except Exception as e:
            out["WARN"].append("%s: pixel crosscheck unavailable (%s)" % (label, e))

# ---------- static floors ----------
def static_floors(src, name, out):
    if not re.search(r'color-scheme', src):
        out["C1"].append("no color-scheme declaration — phone OS dark mode will force-darken this page (live-device failure class, 2026-07-22)")
    vis = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', src)
    if re.search(r'[\U0001F000-\U0001FAFF\u2600-\u26FF]', vis):
        out["EM"].append("emoji in visible text")
    hosts = set(h for h in re.findall(r'https?://([^/\s"\'<>]+)', src)
                if h != "walshero.github.io")
    ext = [h for h in hosts if re.search(r'src=["\']https?://' + re.escape(h), src)
           or ("font" in h or "gstatic" in h or "cdn" in h)]
    for h in ext:
        out["H4"].append("external resource host: " + h)
    if not re.search(r'skip-link|href="#main', src, re.I):
        out["WARN"].append("PROPS missing: skip-link")
    if not re.search(r'a11y|accessib|comfort|setSkin|setStop', src, re.I):
        out["WARN"].append("PROPS missing: comfort control")
    if not (re.search(r'<nav\b', src, re.I) or re.search(r'(id|class)="[^"]*(back|home|nav)', src, re.I)):
        out["WARN"].append("PROPS missing: nav (back/home)")
    if ':focus-visible' not in src and ':focus' not in src:
        out["WARN"].append("no focus style")
    if '<script' in src:
        out["WARN"].append("JS present — engine does not execute it; hand-verify script-driven states on device")

def horvath_watch(src, out):
    for cand in ('staging-area.py', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'staging-area.py')):
        if os.path.exists(cand):
            try:
                spec = importlib.util.spec_from_file_location('staging_area', cand)
                mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    h = mod.harvest(src)
                if h.get("options", 0) == 0:
                    out["WATCH"].append("HORVATH: harvest reads 0 choices — schema-bound ({eyebrow:/{label:}); non-schema games read as 0. Loud skip, not a verdict.")
                    return
                with contextlib.redirect_stdout(buf):
                    v = mod.lens_horvath(src, h)
                out["WATCH"].append("HORVATH: %s (%d choices) — gate of record is staging-area.py" % (v, h["options"]))
            except Exception as e:
                out["WATCH"].append("HORVATH: staging-area failed to load (%s) — VERDICT UNKNOWN" % e)
            return
    out["WATCH"].append("HORVATH: staging-area.py NOT FOUND — lens not run. Loud skip.")

# ---------- per file ----------
HALT_KEYS = ("R1", "R2", "C1", "E1", "H4", "EM")

def sweep_file(path, px_budget):
    src = open(path, errors='replace').read()
    out = {k: [] for k in HALT_KEYS}; out["WARN"] = []; out["WATCH"] = []
    static_floors(src, os.path.basename(path), out)
    for stop in discover_stops(src):
        for w in WIDTHS:
            sweep_stop(src, stop, w, os.path.basename(path), out, px_budget)
    horvath_watch(src, out)
    return out

# ---------- self-test teeth ----------
FIX_BAD = """<html><head></head><body style="background:#888">
<p style="color:#999;font-size:11px">low and tiny</p>
<link rel="stylesheet" href="https://fonts.gstatic.com/x.css"></body></html>"""
FIX_GOOD = """<html><head><meta name="color-scheme" content="light dark"></head>
<body style="background:#EEF2EE;color:#17272A;font-size:20px;color-scheme:light">
<a class="skip-link" href="#main">skip</a><nav>n</nav>
<div class="comfort">c</div><style>:focus-visible{outline:2px solid #000}</style>
<p style="font-size:20px">clean twenty pixel text on chart</p></body></html>"""

def self_test():
    bad = {k: [] for k in HALT_KEYS}; bad["WARN"] = []; bad["WATCH"] = []
    static_floors(FIX_BAD, "FIX_BAD", bad)
    sweep_stop(FIX_BAD, None, 390, "FIX_BAD", bad, [0])
    good = {k: [] for k in HALT_KEYS}; good["WARN"] = []; good["WATCH"] = []
    static_floors(FIX_GOOD, "FIX_GOOD", good)
    sweep_stop(FIX_GOOD, None, 390, "FIX_GOOD", good, [0])
    bad_ok = bad["R1"] and bad["E1"] and bad["C1"] and bad["H4"]
    good_ok = not any(good[k] for k in HALT_KEYS)
    if not (bad_ok and good_ok):
        print("SELF-TEST FAILED — the teeth do not bite (bad HALTs: R1=%d E1=%d C1=%d H4=%d; good clean: %s)."
              % (len(bad["R1"]), len(bad["E1"]), len(bad["C1"]), len(bad["H4"]), good_ok))
        print("REFUSING TO CERTIFY ANYTHING. An audit that lies is the disease.")
        sys.exit(2)
    print("self-test: teeth verified (bad fixture HALTs, good fixture passes)")

# ---------- main ----------
def main():
    self_test()
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    files = sorted(glob.glob(os.path.join(target, '*.html'))) if os.path.isdir(target) else [target]
    halts = 0; blast = {}
    px_budget = [40]                                   # pixel samples across the run
    for f in files:
        r = sweep_file(f, px_budget)
        for k in ("R1", "E1"):
            for m in r[k]:
                sig = m.split("'")[0].split(":", 1)[-1].strip()[:44]
                blast.setdefault(k + " " + sig, set()).add(os.path.basename(f))
        hard = any(r[k] for k in HALT_KEYS)
        if hard: halts += 1
        if not (hard or r["WARN"] or r["WATCH"]): continue
        print("\n%s  %s" % ("HALT" if hard else "warn", os.path.basename(f)))
        for k in list(HALT_KEYS) + ["WARN", "WATCH"]:
            for m in r[k][:6]:
                print("   %s: %s" % (k, m))
            if len(r[k]) > 6: print("   %s: (+%d more)" % (k, len(r[k]) - 6))
    if blast:
        multi = {s: fs for s, fs in blast.items() if len(fs) > 1}
        if multi:
            print("\n=== E2 BLAST RADIUS — fix the CLASS across every file listed ===")
            for s, fs in sorted(multi.items()):
                print("   %s  ->  %d files: %s" % (s, len(fs), ", ".join(sorted(fs))))
    print("\n=== %d files at HALT of %d swept (render-proof, %d viewport widths per stop) ==="
          % (halts, len(files), len(WIDTHS)))
    sys.exit(1 if halts else 0)

if __name__ == '__main__':
    main()
