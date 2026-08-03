#!/usr/bin/env python3
# MEDIUM-GATE CHECK — a "fool me once" enforcer. Tight Spiral Productions.
# Run: python3 medium-gate-check.py [dir|file]
#
# WHY THIS EXISTS (the error it makes un-repeatable):
#   2026-08-03 — the "Reading the Fireground" build shipped studio-drawn cut-paper
#   art for a documentary of real LODD incidents. That is the failure OS 3.2 names:
#   "jamming everything through cut-paper means the Medium Gate wasn't run, it was
#   ASSUMED." It is also a dignity breach (real firefighters died; not rendered as
#   stylized art). Funes' law: a floor without an enforcer fails. So the gate is now
#   a CHECK, not a good intention.
#
# THE RULE:
#   Every game/build surface (a file that declares <meta name="tsp:surface">) MUST
#   also declare its Medium-Gate lane: <meta name="tsp:medium" content="...">
#   with one of: licensed-photo | raster | cut-paper (or a compound starting with one).
#   Missing declaration => HALT (the gate was not run/recorded).
#
#   SOFT WATCH: a licensed-photo build that still carries inline <svg> scene art
#   (many drawn <path>/<rect> elements) => WARN — verify those are real photographs,
#   not studio-drawn scenes standing in for the subject.
#
# SELF-TEST TEETH: a good fixture (declares a lane) and a bad fixture (declares a
#   surface but no lane) run before any sweep. If the bad fixture fails to HALT or
#   the good fixture fails to pass, the tool REFUSES TO CERTIFY and exits 2.
#   An audit that lies is the disease (Studio Eyes doctrine).
#
# EXIT: 0 clean · 1 HALT (a real file failed) · 2 self-test failure (do not trust).
import re, sys, os, glob

LANES = ("licensed-photo", "raster", "cut-paper")

def meta(html, name):
    m = re.search(r'<meta\s+name=["\']' + re.escape(name) + r'["\']\s+content=["\']([^"\']*)["\']', html, re.I)
    return m.group(1).strip() if m else None

def svg_scene_weight(html):
    # crude: count drawn primitives inside inline <svg> blocks
    total = 0
    for sv in re.findall(r'<svg\b.*?</svg>', html, re.S | re.I):
        total += len(re.findall(r'<(path|rect|ellipse|circle|polygon)\b', sv, re.I))
    return total

def check_one(path):
    """Return list of (level, code, msg). level in HALT/WARN."""
    out = []
    try:
        html = open(path, encoding="utf-8", errors="replace").read()
    except Exception as e:
        return [("HALT", "READ", f"cannot read: {e}")]
    surface = meta(html, "tsp:surface")
    if surface is None:
        return out  # not a declared build surface — out of scope for this gate
    lane = meta(html, "tsp:medium")
    if not lane:
        out.append(("HALT", "MG1", "declares tsp:surface but no tsp:medium — Medium Gate not run/recorded (OS 3.2)"))
        return out
    base = lane.split()[0].split("·")[0].split("-lane")[0].strip().lower()
    if not any(lane.lower().startswith(L) or L in lane.lower() for L in LANES):
        out.append(("HALT", "MG2", f"tsp:medium='{lane}' is not one of {LANES}"))
    if "licensed-photo" in lane.lower():
        w = svg_scene_weight(html)
        if w >= 20:
            out.append(("WARN", "MG3", f"licensed-photo lane but {w} inline drawn SVG primitives — verify these are real photographs, not studio-drawn scene art"))
    return out

# ---- self-test fixtures ----
GOOD = '<!doctype html><meta name="tsp:surface" content="game"><meta name="tsp:medium" content="licensed-photo"><body>ok</body>'
BAD  = '<!doctype html><meta name="tsp:surface" content="game"><body>no lane declared</body>'

def _fx(html):
    import tempfile
    fd, p = tempfile.mkstemp(suffix=".html"); os.write(fd, html.encode()); os.close(fd)
    try:
        return check_one(p)
    finally:
        os.unlink(p)

def selftest():
    good = _fx(GOOD); bad = _fx(BAD)
    good_ok = not any(l == "HALT" for l, *_ in good)
    bad_halts = any(c == "MG1" for l, c, *_ in bad if l == "HALT")
    if not (good_ok and bad_halts):
        print("SELF-TEST FAILED — good_pass=%s bad_halts=%s. REFUSING TO CERTIFY." % (good_ok, bad_halts))
        return False
    return True

def main():
    if not selftest():
        sys.exit(2)
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    files = [target] if os.path.isfile(target) else sorted(glob.glob(os.path.join(target, "**", "*.html"), recursive=True))
    halts = warns = surfaces = 0
    for f in files:
        res = check_one(f)
        if meta(open(f, encoding="utf-8", errors="replace").read(), "tsp:surface") is not None:
            surfaces += 1
        for level, code, msg in res:
            print(f"{level}  {code}  {f}: {msg}")
            if level == "HALT": halts += 1
            else: warns += 1
    print(f"\nMEDIUM-GATE CHECK — {surfaces} build surface(s) checked · {halts} HALT · {warns} WARN")
    sys.exit(1 if halts else 0)

if __name__ == "__main__":
    main()
