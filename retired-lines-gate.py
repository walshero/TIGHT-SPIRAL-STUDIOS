#!/usr/bin/env python3
# RETIRED-LINES GATE — a founder objection is a wish until it's a check.
#
# THE BUG THIS EXISTS TO KILL (2026-08-08): CYL's original spine line was
# founder-objected on 2026-07-18, "demoted off the title screen" per
# TSP_Ledger.md -- and then kept shipping, unnoticed, on four other live
# surfaces for three weeks, because the objection lived only in a ledger
# entry a human would have to remember to re-check. Nothing was ever wired
# to actually look. This gate is that look, permanent.
#
# TWO PASSES, BOTH ZERO-TOLERANCE (no ratchet, no carried debt -- a retired
# line is not measured debt, it is a thing that must not exist):
#
#   1. RENDER SCAN (hard) -- launches every live HTML surface in a real
#      browser and checks document.body.innerText, the same text a player
#      actually reads. Catches the real bug: a retired line back on screen.
#      Blind to HTML comments and JS strings never written to the DOM --
#      correct, because a dev note documenting *why* a line was retired
#      (see choose-your-leader-v5.html's own header) is not the bug.
#
#   2. SOURCE SCAN (hard, with a citation carve-out) -- greps raw file text
#      across every *.html and *.md, including comments and specs. A spec
#      that still instructs a retired line onto a screen (cyl-full-bible.md
#      did exactly this) is a regeneration risk even though no player sees
#      it today. A line that also carries a supersession marker word
#      (superseded, retired, demoted, objected, ledger, "prior ... line")
#      is treated as the historical record it is, not a violation --
#      the same shape as the attribution tick's citation carve-out.
#
# Add a new objection: append one entry to retired-lines.json. That is the
# whole mechanism -- no code change needed for the next one.
#
# Run: python3 retired-lines-gate.py <surface.html> [<surface2.html> ...]
#      python3 retired-lines-gate.py --selftest
import json, sys, os, re, glob, pathlib

HERE = pathlib.Path(__file__).parent
DATA = HERE / "retired-lines.json"

CARVEOUT_RE = re.compile(
    r"supersed|retire|demote|object|ledger|prior[a-z ]*line",
    re.I,
)


def load_retired():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text(encoding="utf-8")).get("lines", [])


def compiled(retired):
    return [(r["id"], re.compile(r["pattern"], re.I), r["reason"]) for r in retired]


CONTEXT_WINDOW = 2  # lines of wrap-tolerance either side of a match


def source_scan(root, retired):
    """Every *.html / *.md source line (comments included) for regeneration
    risk. A hit survives only when a nearby line (+/- CONTEXT_WINDOW, to
    tolerate prose that wraps the marker onto an adjacent line) also
    carries a supersession marker -- the citation/ledger/dev-note case."""
    halts = []
    files = [
        p for p in glob.glob(os.path.join(root, "**/*.html"), recursive=True)
        + glob.glob(os.path.join(root, "**/*.md"), recursive=True)
        if not re.search(r"/(\.git|archive|rescued|node_modules)/", p)
    ]
    pats = compiled(retired)
    for f in sorted(files):
        try:
            lines = pathlib.Path(f).read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            for rid, pat, reason in pats:
                if not pat.search(line):
                    continue
                lo, hi = max(0, i - 1 - CONTEXT_WINDOW), min(len(lines), i + CONTEXT_WINDOW)
                context = "\n".join(lines[lo:hi])
                if not CARVEOUT_RE.search(context):
                    halts.append((f, i, rid, reason, line.strip()[:140]))
    return halts


def render_scan(files, retired):
    """Rendered document.body.innerText for every live surface passed in.
    Zero tolerance: a player must never see a retired line, full stop."""
    if not files:
        return []
    from playwright.sync_api import sync_playwright

    pats = compiled(retired)
    halts = []
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception:
            browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        page = browser.new_page()
        for f in files:
            if not pathlib.Path(f).is_file():
                continue
            url = pathlib.Path(f).resolve().as_uri()
            try:
                page.goto(url, wait_until="networkidle", timeout=15000)
            except Exception:
                page.goto(url, wait_until="load", timeout=15000)
            page.wait_for_timeout(200)
            text = page.evaluate("document.body.innerText || ''")
            for rid, pat, reason in pats:
                if pat.search(text):
                    halts.append((f, rid, reason))
        browser.close()
    return halts


def selftest():
    import tempfile

    ok = True
    with tempfile.TemporaryDirectory() as td:
        bad = pathlib.Path(td) / "bad.html"
        bad.write_text(
            "<html><body><h1>Title</h1>"
            "<p>You don't judge the leader. You judge what you were allowed to see.</p>"
            "</body></html>",
            encoding="utf-8",
        )
        good = pathlib.Path(td) / "good.html"
        good.write_text(
            "<html><body><h1>Title</h1><p>Trust a quote, then watch the record turn.</p></body></html>",
            encoding="utf-8",
        )
        cited = pathlib.Path(td) / "cited.md"
        cited.write_text(
            "Prior thesis line (\"You don't judge the leader. You judge what you were "
            "allowed to see.\") SUPERSEDED and retired 2026-08-08, see TSP_Ledger.md.",
            encoding="utf-8",
        )
        retired = load_retired()
        if not retired:
            print("SELFTEST FAIL: retired-lines.json is empty; nothing to test against")
            return False

        rh = render_scan([str(bad)], retired)
        if not rh:
            print("SELFTEST FAIL: render_scan missed a live retired line")
            ok = False
        rh_good = render_scan([str(good)], retired)
        if rh_good:
            print("SELFTEST FAIL: render_scan false-positived on clean copy")
            ok = False

        sh = source_scan(td, retired)
        sh_files = {pathlib.Path(f).name for f, *_ in sh}
        if "bad.html" not in sh_files:
            print("SELFTEST FAIL: source_scan missed an uncited retired line")
            ok = False
        if "cited.md" in sh_files:
            print("SELFTEST FAIL: source_scan false-positived on a cited/superseded mention")
            ok = False

    print("SELFTEST", "PASS" if ok else "FAIL")
    return ok


def main(argv):
    if "--selftest" in argv:
        return 0 if selftest() else 1

    retired = load_retired()
    if not retired:
        print("retired-lines-gate: retired-lines.json has no entries -- nothing to check")
        return 0

    root = "."
    files = [a for a in argv if pathlib.Path(a).is_file()]

    print("=" * 72)
    print(f"RETIRED-LINES GATE  ·  {len(retired)} retired line(s) on file  ·  zero tolerance")
    print("=" * 72)

    src_halts = source_scan(root, retired)
    render_halts = render_scan(files, retired)

    if src_halts:
        print(f"\n{len(src_halts)} SOURCE-TEXT hit(s) (uncited -- real regeneration risk):")
        for f, ln, rid, reason, snippet in src_halts:
            print(f"  HALT  {f}:{ln}  [{rid}]")
            print(f"        {snippet}")
            print(f"        why retired: {reason}")

    if render_halts:
        print(f"\n{len(render_halts)} RENDERED hit(s) (a player would see this today):")
        for f, rid, reason in render_halts:
            print(f"  HALT  {f}  [{rid}]")
            print(f"        why retired: {reason}")

    if not src_halts and not render_halts:
        print("\n  clean -- no retired line found live or uncited in source")

    print()
    fail = bool(src_halts or render_halts)
    print("RETIRED-LINES GATE:", "HALT" if fail else "PASS")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
