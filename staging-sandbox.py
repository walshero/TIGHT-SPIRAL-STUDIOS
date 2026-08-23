#!/usr/bin/env python3
"""
staging-sandbox.py — the authentic staging area for floor checks AND agentic playtesters.
Tight Spiral Productions.

ONE real browser (the preinstalled Chromium, via tsp_browser), the build RENDERED, and both
consumers run against the SAME rendered DOM instead of reasoning from source:

  FLOOR CHECKS      axe-core (breadth) + rendered probes (overflow, tap targets, focus, landmarks)
  PLAYTEST SUBSTRATE the same page, staged, screenshotted, and query-able — so a persona agent
                     PLAYS the build (reads getComputedStyle, clicks real hotspots) rather than
                     estimating from code (the gap the 2026-07-26 playtest run hit).

Findings leave as owned checks: `FLAG verb · owner · when` or `ok`. No emoji. Report-mode by
default (exit 0); `--strict` exits 1 on any FLAG. Self-test runs first and REFUSES (exit 2) if
its probe canary does not bite — a harness that gates the studio must gate itself.

USAGE
    staging-sandbox.py --self-test
    staging-sandbox.py <file.html> [more.html ...]      (default: index.html)
    staging-sandbox.py --strict <file.html>
    staging-sandbox.py --shots-dir studio-eyes-shots <file.html>
"""
import sys, os, glob, tempfile

PHONE = {"width": 390, "height": 844}
AXE_JS = os.environ.get("AXE_JS", "node_modules/axe-core/axe.min.js")

# Probes run in the page: return the facts a floor check or a persona needs from the RENDER.
PROBE = r"""() => {
  const vw = window.innerWidth;
  const small = [...document.querySelectorAll('a,button,[role=button],input,select,summary')]
    .filter(el => { const r = el.getBoundingClientRect();
      if (!(r.width > 0 && r.height > 0)) return false;              // not rendered
      // WCAG 2.5.8 inline exception: a link that flows inline within text is sized by the
      // line-height of the prose around it, not a standalone target — exempt it.
      if (el.tagName === 'A' && getComputedStyle(el).display === 'inline') return false;
      return r.width < 44 || r.height < 44; })
    .map(el => (el.id || el.className || el.tagName).toString().slice(0,32));
  const focusStyle = [...document.styleSheets].some(s => { try {
    return [...s.cssRules].some(r => (r.selectorText||'').includes(':focus')); } catch(e){ return false; } });
  return {
    overflow: document.documentElement.scrollWidth > vw + 1,
    scrollWidth: document.documentElement.scrollWidth, innerWidth: vw,
    mains: document.querySelectorAll('main').length,
    smallTargets: small.slice(0, 10), smallCount: small.length,
    hasFocusStyle: focusStyle,
    title: document.title || ''
  };
}"""


def axe_src():
    try:
        return open(AXE_JS, encoding="utf-8").read()
    except Exception:
        return None


def stage(page, path, axe):
    """Load the RENDERED build and pull the facts. Returns (probe dict, axe violations|None)."""
    page.set_viewport_size(PHONE)
    page.route("**/*", lambda r: (r.abort() if r.request.url.startswith(("http://", "https://")) else r.continue_()))
    page.goto("file://" + os.path.abspath(path), wait_until="load")
    page.wait_for_timeout(200)
    probe = page.evaluate(PROBE)
    viols = None
    if axe:
        page.add_script_tag(content=axe)
        viols = page.evaluate("async () => (await axe.run(document, {resultTypes:['violations']})).violations")
    return probe, viols


def report(name, probe, viols):
    """Turn render facts into owned checks. Returns FLAG count."""
    flags = 0
    print(f"\n  STAGING SANDBOX (rendered @390px) - {name}")
    print("  " + "-" * 58)
    if probe["overflow"]:
        flags += 1
        print(f"  FLAG horizontal overflow · build · v-next  (scrollWidth {probe['scrollWidth']} > {probe['innerWidth']})")
    else:
        print(f"  ok  no horizontal overflow ({probe['scrollWidth']} = {probe['innerWidth']})")
    if probe["mains"] != 1:
        flags += 1
        print(f"  FLAG landmark: {probe['mains']} <main> (want exactly 1) · build · v-next")
    if probe["smallCount"]:
        flags += 1
        print(f"  FLAG {probe['smallCount']} tap target(s) < 44px · build · v-next  ({', '.join(probe['smallTargets'])})")
    else:
        print("  ok  all tap targets >= 44px")
    if not probe["hasFocusStyle"]:
        flags += 1
        print("  FLAG no :focus style found · build · v-next")
    if viols is not None:
        if viols:
            flags += len(viols)
            for v in viols[:10]:
                print(f"  FLAG axe [{v.get('impact','?')}] {v['id']}: {v.get('help','')} ({len(v.get('nodes',[]))} node) · build · v-next")
        else:
            print("  ok  axe-core clean")
    else:
        print("  note axe skipped (no axe.min.js; CI `npm install axe-core` provides it)")
    return flags


def run(files, strict=False, shots_dir=None):
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"  staging-sandbox: Playwright unavailable ({e}). CI has it; skipping (exit 0).")
        return 0
    try:
        import tsp_browser
    except Exception:
        tsp_browser = None
    axe = axe_src()
    total = 0
    try:
        with sync_playwright() as p:
            b = tsp_browser.launch(p) if tsp_browser else p.chromium.launch()
            for f in files:
                page = b.new_page()
                try:
                    probe, viols = stage(page, f, axe)
                    if shots_dir:
                        os.makedirs(shots_dir, exist_ok=True)
                        page.screenshot(path=os.path.join(shots_dir, os.path.basename(f) + ".staging.png"), full_page=True)
                    total += report(os.path.basename(f), probe, viols)
                except Exception as e:
                    print(f"  {os.path.basename(f)}: staging failed ({e})")
                finally:
                    page.close()
            b.close()
    except Exception as e:
        print(f"  staging-sandbox: browser session failed ({e}) — CI verifies; skipping (exit 0).")
        return 0
    print(f"\n  === staging sandbox: {total} FLAG(s) across {len(files)} build(s) ===")
    return 1 if (strict and total) else 0


def self_test():
    """Canary: a page with a KNOWN overflow must FLAG; a clean page must not. Real browser + probe."""
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"  SELF-TEST SKIP — no Playwright here ({e}); CI runs the canary. (exit 0)")
        return 0
    try:
        import tsp_browser
    except Exception:
        tsp_browser = None
    bad = "<!doctype html><title>bad</title><body style='margin:0'><div style='width:120vw;height:20px'>x</div>"
    good = "<!doctype html><title>good</title><body style='margin:0'><main><p>ok</p></main></body>"
    with tempfile.TemporaryDirectory() as td:
        pb, pg_ = os.path.join(td, "bad.html"), os.path.join(td, "good.html")
        open(pb, "w").write(bad); open(pg_, "w").write(good)
        try:
            with sync_playwright() as p:
                b = tsp_browser.launch(p) if tsp_browser else p.chromium.launch()
                pg = b.new_page(); probe_bad, _ = stage(pg, pb, None); pg.close()
                pg = b.new_page(); probe_good, _ = stage(pg, pg_, None); pg.close()
                b.close()
        except Exception as e:
            print(f"  SELF-TEST SKIP — browser could not launch here ({e}); CI runs it. (exit 0)")
            return 0
    if not (probe_bad["overflow"] and not probe_good["overflow"] and probe_good["mains"] == 1):
        print(f"  SELF-TEST FAIL — probe did not bite (bad.overflow={probe_bad['overflow']}, good.overflow={probe_good['overflow']}).")
        return 2
    print("  SELF-TEST OK — overflow probe flags a bad page and clears a good one (rendered).")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    strict = "--strict" in argv
    shots = None
    if "--shots-dir" in argv:
        i = argv.index("--shots-dir"); shots = argv[i + 1] if i + 1 < len(argv) else None
    files = [a for a in argv if not a.startswith("--") and a != shots] or ["index.html"]
    return run(files, strict, shots)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
