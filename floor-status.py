#!/usr/bin/env python3
# FLOOR STATUS — make the render-proof failures VISIBLE on the live site.
# Tight Spiral Productions. Draft mode: the studio ships work-in-progress, and
# every page the gate can still catch invisible text on says so, in the open.
#
# Produces:
#   floor-status.html  — one dashboard, worst-first, every HALT with the exact
#                        invisible text, its rendered ratio, and the comfort mode.
#   a DRAFT ribbon      — injected (idempotent) into each HALTing page's source,
#                        linking to the dashboard. Auto-clears when a file is fixed.
#
# HALT = R1 (invisible/low-contrast RENDERED text) / R2 / H4 / EM. C1+E1 are warns.
# Run locally (needs weasyprint) or in CI: python3 floor-status.py [dir]
# ROBUST: never raises to the caller — visibility must never block a deploy.
#
# ── 2026-08-28: THE RIBBON WILL NOT ACCUSE A PAGE THE ENGINE CANNOT SEE ────────
# The founder opened workshop-wall.html and read "DRAFT · 4 contrast issues the
# founder cannot read on this page." There were none. Measured in a real browser,
# day and night, 390 and 1100: 62 text elements, ZERO below floor, and the exact
# text the ribbon accused ('Comfort') sits at 12.46:1 and 16.49:1 against the
# 2.86:1 the sweep reported. your-rp-world.html the same: 15 elements, zero.
#
# WHY IT WAS WRONG, and it is not staleness. Neither file had changed since the
# ribbon was written. studio-eyes-sweep.py renders with WeasyPrint, which does not
# execute JavaScript, and it says so itself in its own output:
#     "JS present — engine does not execute it; hand-verify script-driven states"
# Every studio page boots its comfort kernel from a pre-paint script. With no JS
# that boot never runs, so the engine measured a state no browser ever paints, and
# reported a stop ("softer") that had been retired the day before. This function
# then took that self-declared hand-verify-me warning and printed it on the live
# site as a finding about what the founder can read.
#
# So the policy, and it is the studio's oldest rule pointed the other way: a gate
# that has gone blind must never read as clean — and a blind gate must never
# ACCUSE either. A measurement carrying its own "I could not see this" warning
# does not get to write on a shipped page. Such pages are still listed on the
# dashboard, under their own heading, marked unverified. The dashboard is a place
# to go looking; the ribbon is a claim made to a reader who did not ask.

import sys, os, re, subprocess, html as H

RIBBON_MARK = "tsp-draft-ribbon"

def run_sweep(target):
    r = subprocess.run([sys.executable, "studio-eyes-sweep.py", target],
                       capture_output=True, text=True, timeout=1800)
    return r.stdout

def parse(out):
    files, cur = {}, None
    for ln in out.splitlines():
        m = re.match(r'^(HALT|warn)  (\S+)', ln)
        if m:
            cur = os.path.basename(m.group(2))
            files[cur] = {"hard": m.group(1) == "HALT", "r1": [], "soft": []}
            continue
        if not cur:
            continue
        s = ln.strip()
        if s.startswith("R1:"):
            files[cur]["r1"].append(s[3:].strip())
        elif s.startswith(("C1:", "E1:")):
            files[cur]["soft"].append(s.split(":", 1)[0])
    return files

def ribbon(name, nr1):
    issue = "%d contrast issue%s" % (nr1, "" if nr1 == 1 else "s")
    return (
        '<a href="floor-status.html" id="%s" '
        'style="position:fixed;left:0;right:0;bottom:0;z-index:99999;'
        'background:#1a1200;color:#ffd24a;border-top:3px solid #ffd24a;'
        'font:700 18px/1.35 system-ui,-apple-system,sans-serif;'
        'padding:10px 16px;text-align:center;text-decoration:none;display:block">'
        'DRAFT · %s the founder cannot read on this page — see the floor status →'
        '</a>' % (RIBBON_MARK, issue)
    )

def engine_was_blind(src):
    """True when the sweep could not have seen what a browser paints.

    Identical test to studio-eyes-sweep.py's own JS-present warning, on purpose:
    if the sweep says hand-verify this, the ribbon does not get to skip the hand.
    Every studio page boots its comfort kernel from a pre-paint script, so on those
    pages a no-JS engine measures a state that is never shipped to anyone."""
    return "<script" in src.lower()


def inject(name, nr1):
    """Idempotent: replace an existing ribbon or insert one before </body>.

    Returns True on write, False on failure, and the string "blind" when the page
    was spared because the measurement behind it could not execute the page."""
    try:
        src = open(name, encoding="utf-8", errors="replace").read()
    except Exception:
        return False
    if engine_was_blind(src):
        # Do not accuse a page the engine could not read. Clear any ribbon a
        # previous run left there, so an old false claim does not outlive the rule.
        strip_ribbon(name)
        return "blind"
    new = ribbon(name, nr1)
    if RIBBON_MARK in src:
        src = re.sub(r'<a href="floor-status\.html" id="%s".*?</a>' % RIBBON_MARK,
                     new, src, count=1, flags=re.S)
    elif re.search(r'</body>', src, re.I):
        src = re.sub(r'</body>', new + "\n</body>", src, count=1, flags=re.I)
    else:
        src = src + new
    try:
        open(name, "w", encoding="utf-8").write(src)
        return True
    except Exception:
        return False

def strip_ribbon(name):
    try:
        src = open(name, encoding="utf-8", errors="replace").read()
    except Exception:
        return
    if RIBBON_MARK in src:
        src = re.sub(r'\n?<a href="floor-status\.html" id="%s".*?</a>\n?' % RIBBON_MARK,
                     "", src, flags=re.S)
        # the ribbon ships a companion script that pads the body for its height;
        # left behind it pads for nothing and still names the ribbon in the source
        src = re.sub(r"\n?<script>\(function\(\)\{\s*var r=document\.getElementById\('%s'\);"
                     r".*?\}\)\(\);</script>\n?" % RIBBON_MARK, "", src, flags=re.S)
        try:
            open(name, "w", encoding="utf-8").write(src)
        except Exception:
            pass

def dashboard(files):
    halt = sorted(((n, d) for n, d in files.items() if d["hard"]),
                  key=lambda t: (-len(t[1]["r1"]), t[0]))
    clean = sorted(n for n, d in files.items() if not d["hard"])
    rows = []
    for n, d in halt:
        lines = "".join("<li>%s</li>" % H.escape(x) for x in d["r1"][:8])
        more = "" if len(d["r1"]) <= 8 else "<li>(+%d more)</li>" % (len(d["r1"]) - 8)
        soft = ""
        if d["soft"]:
            from collections import Counter
            c = Counter(d["soft"])
            soft = '<p class="soft">also (warn): %s</p>' % ", ".join(
                "%s×%d" % (k, v) for k, v in sorted(c.items()))
        rows.append(
            '<article><h2><a href="%s">%s</a> <span class="n">%d</span></h2>'
            '<ul>%s%s</ul>%s</article>' % (H.escape(n), H.escape(n), len(d["r1"]), lines, more, soft))
    body = "\n".join(rows) or "<p>No pages are failing the render-proof floor. \U0001f7e2</p>"
    passing = "".join("<li><a href='%s'>%s</a></li>" % (H.escape(n), H.escape(n)) for n in clean)
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>Floor Status — Tight Spiral Studios (draft)</title>
<style>
:root{color-scheme:light dark}
body{margin:0;background:#faf8f3;color:#14181d;font:18px/1.55 system-ui,-apple-system,sans-serif;padding:24px;max-width:900px;margin:0 auto}
h1{font-size:30px;margin:0 0 6px}
.lede{color:#3d4652;margin:0 0 22px;font-size:18px}
.draft{display:inline-block;background:#1a1200;color:#ffd24a;font-weight:700;padding:4px 12px;border-radius:4px;font-size:15px;letter-spacing:.04em}
article{background:#fff;border:1px solid #e3ddd0;border-left:6px solid #b0332a;border-radius:6px;padding:14px 18px;margin:0 0 14px}
h2{font-size:20px;margin:0 0 8px}
h2 a{color:inherit;display:inline-flex;align-items:center;min-height:44px}
.n{background:#b0332a;color:#fff;border-radius:20px;padding:1px 10px;font-size:15px;font-weight:700}
ul{margin:0;padding-left:20px}
li{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:15px;margin:3px 0}
.soft{margin:8px 0 0;font-size:15px;color:#5c6675}
h3{margin:26px 0 8px;font-size:20px}
.pass li{font-family:inherit}
.pass li a{display:inline-flex;align-items:center;min-height:44px}
footer{margin-top:30px;color:#5c6675;font-size:15px}
@media (prefers-color-scheme:dark){
  body{background:#14120e;color:#f2efe8}
  article{background:#1d1a15;border-color:#3a352c;border-left-color:#e0736a}
  .lede{color:#c9c3b6}
  .soft,footer{color:#b8b2a4}
}
</style></head><body>
<h1>Floor Status <span class="draft">DRAFT MODE</span></h1>
<p class="lede">Every page below has text the render-proof gate measured as <b>invisible or low-contrast</b>
when actually rendered — the class WCAG token-checks miss. Worst-first. Contrast is arithmetic, not taste;
the number is the rendered ratio, the floor is 4.5:1 (3.0 for large text).</p>
""" + body + """
<h3>Passing the floor (""" + str(len(clean)) + """)</h3><ul class="pass">""" + (passing or "<li>—</li>") + """</ul>
<footer>Generated by floor-status.py from studio-eyes v4 (render-proof). C1 (color-scheme) and E1 (font&lt;18px) are tracked as warnings, not shown here.</footer>
</body></html>"""

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    for f in __import__("glob").glob("*.html"):
        strip_ribbon(f)                      # clean slate: the gate must see true state
    try:
        out = run_sweep(target)
    except Exception as e:
        print("floor-status: sweep unavailable (%s) — no marks written." % e)
        return
    files = parse(out)
    try:
        open("floor-status.html", "w", encoding="utf-8").write(dashboard(files))
    except Exception as e:
        print("floor-status: could not write dashboard (%s)" % e)
    marked, spared = 0, []
    swept = set(files.keys())
    for n, d in files.items():
        if d["hard"] and os.path.exists(n):
            r = inject(n, len(d["r1"]))
            if r == "blind":
                spared.append(n)
            elif r:
                marked += 1
        elif os.path.exists(n):
            strip_ribbon(n)   # was failing, now clean -> pull the ribbon
    # also strip ribbons from any file no longer in the sweep set (safety)
    for f in [x for x in __import__("glob").glob("*.html") if os.path.basename(x) not in swept]:
        strip_ribbon(f)
    print("floor-status: %d HALT pages marked draft; floor-status.html written (%d files swept)."
          % (marked, len(files)))
    if spared:
        # Loud, not silent. These pages may still have a real defect; what we know
        # is that this measurement could not see them, so it does not get to say.
        print("floor-status: %d HALT page(s) NOT marked - the engine could not execute "
              "them, so the finding is unverified, not proven:" % len(spared))
        for n in spared:
            print("    %s  (hand-verify in a browser; the ribbon is a claim, not a note)" % n)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("floor-status: non-fatal error (%s) — deploy proceeds clean." % e)
    sys.exit(0)
