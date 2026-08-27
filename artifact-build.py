#!/usr/bin/env python3
"""
ARTIFACT BUILD  ·  Tight Spiral Studios  ·  the publish lane's one transformation
=================================================================================
TSP-ROLE: artifact publish transform
TSP-SUPERSEDES: (none)

WHY THIS EXISTS
---------------
A Claude Artifact wraps the file it is given in its OWN skeleton:

    <!doctype html> <head>…</head> <body>   [ your content here ]   </body>

So a file that ships its own `<!DOCTYPE>`, `<html>`, `<head>` and `<body>` gets
those stripped at publish time, and **everything living inside that `<head>` is
stripped with them**. For every game in this studio that means the entire
`<style>` block and the pre-paint comfort boot script. The published page then
renders with no stylesheet and no boot: black, inert, no data.

That is exactly what shipped on 2026-08-27. `blocking.html` was published whole,
opened black, and the founder had to report it. The file was verified; the
DELIVERY was not. Same shape as the raw.githubusercontent links given earlier the
same day, which served `text/plain` and so showed source rather than a playable
page: in both cases the artifact that arrived was never checked, only the artifact
that was sent.

WHY A GENERATOR AND NOT TWO COPIES
-----------------------------------
The obvious fix is to keep a hand-maintained `blocking.artifact.html` beside
`blocking.html`. That is a second copy of a game, and a second copy is a second
place to drift, which is the failure this repo spent 2026-08-17 documenting
(`claude/FINDING-STALE-STATE-CLASS-2026-08-17.md`). The derived files are
gitignored on purpose. **The source is canon; the artifact build is a lane.**

WHAT IT DOES, AND NOTHING MORE
------------------------------
Removes the document skeleton and the two `<meta>` tags the runtime supplies
itself. It does not touch a single byte of the style, the script, the markup or
the TSP-META block, because the games are already gate-verified and any edit here
would be an unreviewed change to a shipped build.

HONEST LIMITS:
  - It assumes one skeleton per file, which is true of every studio single-file
    build and would silently mangle a document containing a nested one.
  - It does not verify the result renders. `--check` does that, and the publish is
    not done until `--check` has passed under a simulated wrapper.

Usage:
  artifact-build.py <file.html> [more ...]    write <name>.artifact.html
  artifact-build.py --check <file.html> ...   build, wrap as the runtime does, and
                                              render headless in light AND dark
"""
import sys, os, re, pathlib

SKELETON = (
    (r'^\s*<!DOCTYPE[^>]*>\s*', '', re.I | re.M),
    (r'<html[^>]*>\s*', '', re.I),
    (r'\s*</html>\s*$', '', re.I | re.M),
    (r'<head>\s*', '', re.I),
    (r'\s*</head>\s*', '\n', re.I),
    (r'<body>\s*', '', re.I),
    (r'\s*</body>\s*', '\n', re.I),
    (r'<meta charset[^>]*>\s*', '', re.I),
    (r'<meta name="viewport"[^>]*>\s*', '', re.I),
)


def build(src):
    out = pathlib.Path(src).with_suffix('').as_posix() + '.artifact.html'
    s = open(src, encoding='utf-8').read()
    for pat, rep, flags in SKELETON:
        s = re.sub(pat, rep, s, count=(0 if 'meta' in pat else 1), flags=flags)
    leftover = [t for t in ('<!doctype', '<html', '<head>', '<body>') if t in s.lower()]
    open(out, 'w', encoding='utf-8').write(s)
    print("  built %-34s %7d bytes  leftover skeleton: %s"
          % (out, len(s), ", ".join(leftover) if leftover else "none"))
    if leftover:
        print("     WARNING: skeleton survived. Do not publish this.")
    return out, not leftover


def check(paths):
    """Render each build inside a simulated runtime wrapper, light and dark."""
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("  playwright unavailable (%s). Blind is not clean: NOT verified." % e)
        return 1
    import tempfile
    ok = True
    for src in paths:
        out, clean = build(src)
        if not clean:
            ok = False; continue
        body = open(out, encoding='utf-8').read()
        wrapped = ('<!doctype html>\n<head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width, initial-scale=1">'
                   '<style>*{margin:0;padding:0;box-sizing:border-box}</style></head>\n'
                   '<body>\n' + body + '\n</body>')
        fd, tmp = tempfile.mkstemp(suffix='.html'); os.close(fd)
        open(tmp, 'w', encoding='utf-8').write(wrapped)
        try:
            with sync_playwright() as p:
                try:
                    b = p.chromium.launch()
                except Exception:
                    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
                for scheme in ('light', 'dark'):
                    pg = b.new_page(viewport={'width': 390, 'height': 844}, color_scheme=scheme)
                    errs = []
                    pg.on('pageerror', lambda e: errs.append(str(e)))
                    pg.goto(pathlib.Path(tmp).as_uri())
                    pg.mouse.move(5, 5)
                    pg.wait_for_timeout(600)
                    bg = pg.eval_on_selector('body', 'e=>getComputedStyle(e).backgroundColor')
                    before = pg.evaluate("(document.body.innerText||'').trim().length")
                    styled = pg.evaluate("!!document.querySelector('style')")
                    # a page with no stylesheet, or no text, is the black-on-open failure
                    good = styled and before > 20 and bg not in ('rgba(0, 0, 0, 0)', 'transparent')
                    print("    %-22s %-5s bg=%-22s text=%-4d styled=%s %s%s"
                          % (os.path.basename(out), scheme, bg, before, styled,
                             "OK" if good else "FAIL", (" errs=%s" % errs) if errs else ""))
                    ok &= good and not errs
                    pg.close()
                b.close()
        finally:
            os.remove(tmp)
    print("\nARTIFACT BUILD: %s" % ("renders under the wrapper" if ok else "NOT SAFE TO PUBLISH"))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__); return 0
    if argv[0] == '--check':
        return check(argv[1:])
    print("ARTIFACT BUILD")
    bad = 0
    for f in argv:
        _, clean = build(f)
        bad += (0 if clean else 1)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
