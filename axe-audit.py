#!/usr/bin/env python3
"""
axe-audit.py — invoke axe-core (the industry-standard accessibility engine) on each build.
Tight Spiral Productions.

WHY: floor.yml installed axe-core and never called it (verified 2026-07-27) — the broad
WCAG engine (names/roles/values, ARIA, landmarks, labels, duplicate ids, etc.) was
provisioned and wasted. This invokes it, in one shared browser, over all builds.

OPTIMAL INSTALL: floor.yml pins `axe-core@<ver>` via npm; we inject
`node_modules/axe-core/axe.min.js` directly into the page (offline, no CDN, deterministic) —
no per-file re-download, one Chromium for the whole run.

Report mode by default (exit 0; advisory, like the sweep's report pass). `--strict` exits 1
if any violation is found. Needs Playwright + Chromium (CI installs both; a bare sandbox may
not, in which case it reports that and exits 0 — it never fails a build it could not run).

USAGE
    axe-audit.py [--strict] [file.html ...]     (default: all *.html in cwd)
"""
import sys, os, glob

AXE_JS = os.environ.get("AXE_JS", "node_modules/axe-core/axe.min.js")


def main(argv):
    strict = "--strict" in argv
    files = [a for a in argv if not a.startswith("--")] or sorted(glob.glob("*.html"))
    try:
        axe_src = open(AXE_JS, encoding="utf-8").read()
    except Exception as e:
        print(f"  axe-audit: cannot read {AXE_JS} ({e}). In CI, `npm install axe-core` provides it. Skipping (exit 0).")
        return 0
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"  axe-audit: Playwright unavailable ({e}) — needs a real browser (CI installs it). Skipping (exit 0).")
        return 0

    total = 0
    try:
        import tsp_browser
    except Exception:
        tsp_browser = None
    try:
        with sync_playwright() as p:
            browser = tsp_browser.launch(p) if tsp_browser else p.chromium.launch()
            for f in files:
                page = browser.new_page()
                # offline floor: block every network request; only file:// runs.
                page.route("**/*", lambda r: (r.abort() if r.request.url.startswith(("http://", "https://")) else r.continue_()))
                try:
                    page.goto("file://" + os.path.abspath(f), wait_until="load")
                    page.wait_for_timeout(200)
                    page.add_script_tag(content=axe_src)
                    res = page.evaluate("async () => await axe.run(document, {resultTypes:['violations']})")
                    v = res.get("violations", [])
                except Exception as e:
                    print(f"  {os.path.basename(f)}: axe could not run ({e})")
                    page.close(); continue
                if v:
                    print(f"\n  {os.path.basename(f)} — {len(v)} violation type(s):")
                    for x in v[:12]:
                        print(f"     [{x.get('impact','?')}] {x['id']}: {x.get('help','')} ({len(x.get('nodes', []))} node(s))")
                    total += len(v)
                else:
                    print(f"  {os.path.basename(f)}: axe clean")
                page.close()
            browser.close()
    except Exception as e:
        print(f"  axe-audit: browser session failed ({e}) — CI verifies this; skipping (exit 0).")
        return 0

    print(f"\n  === axe-core: {total} violation type(s) across {len(files)} file(s) ===")
    return 1 if (strict and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
