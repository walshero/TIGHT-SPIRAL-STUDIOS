"""
tsp_browser.py — discover the authentic Chromium for the staging sandbox.

The authoring/CI environment ships a real Chromium under $PLAYWRIGHT_BROWSERS_PATH.
Tools that call `p.chromium.launch()` with no path miss it whenever the pip Playwright
version and the installed browser build differ (that mismatch is why v3 + axe read as
"no browser here" all session). This resolves the real binary so the floor checks AND the
persona playtesters run against a TRULY-RENDERED build, not source — the authentic sandbox.

    from playwright.sync_api import sync_playwright
    import tsp_browser
    with sync_playwright() as p:
        browser = tsp_browser.launch(p)   # uses the preinstalled Chromium if present
"""
import glob, os


def find_chrome():
    root = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    for pat in ("chromium-*/chrome-linux/chrome",
                "chromium_headless_shell-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(os.path.join(root, pat)))
        if hits:
            return hits[-1]   # newest build present
    return None


def launch(playwright, **kw):
    exe = find_chrome()
    if exe:
        return playwright.chromium.launch(executable_path=exe, **kw)
    return playwright.chromium.launch(**kw)   # fall back to Playwright's own resolution
