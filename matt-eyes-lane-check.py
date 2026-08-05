#!/usr/bin/env python3
# MATT-EYES LANE CHECK — a "fool me once" enforcer. Tight Spiral Productions.
# Run: python3 matt-eyes-lane-check.py [dir|file]
#
# WHY THIS EXISTS (the near-miss it makes un-repeatable):
#   2026-08-04 — setting up Matt's private "parking lot" dashboard, the plan was to
#   keep personal material (creative drafts, bills, receipts, the ADA appeal) simply
#   UNLINKED from the studio face. But "unlinked" is not "private": the studio
#   deploys to GitHub Pages, so an unlinked page in a PUBLIC repo is still reachable
#   by URL and indexable. Personal bills on a public URL is unrecoverable. Funes' law:
#   a floor without an enforcer fails. So the rule is now a CHECK, not a good habit.
#
# THE RULE:
#   Any file that declares it belongs to the Matt-eyes lane is PRIVATE and may live
#   ONLY in the private Matt-eyes home repo (matt-radar). In any shared/public repo,
#   a Matt-eyes file is a LEAK => HALT before it can build/deploy.
#
#   A file is Matt-eyes if it declares, anywhere in its text, either:
#     HTML:  <meta name="tsp:lane" content="matt-eyes">
#     text:  a line   tsp:lane: matt-eyes   (markdown front-matter / marker)
#
#   HOME DETECTION — a repo is the private Matt-eyes home if EITHER:
#     * a file named `.matt-eyes-home` exists at the scan root, OR
#     * env MATT_EYES_HOME=1 (for local runs inside the home clone).
#   Home  => Matt-eyes files are allowed (this is where they belong): clean.
#   Not home (a shared/public repo) => any Matt-eyes file HALTs.
#
#   (The studio's "every page linked from the face" orphan rule needs NO Matt-eyes
#   exemption: Matt-eyes files never live in the public repo — this gate guarantees
#   it — and in the private home, the dashboard is its own face. The tension is moot.)
#
# SELF-TEST TEETH: a Matt-eyes file in a NON-home context must HALT; the same file in
#   a HOME context must pass; a plain file must be ignored in both. If any fixture
#   lies, the tool REFUSES TO CERTIFY and exits 2. An audit that lies is the disease
#   (Studio Eyes doctrine).
#
# EXIT: 0 clean · 1 HALT (a Matt-eyes file in a shared lane) · 2 self-test failure.
import re, sys, os, glob

SCAN_EXT = (".html", ".htm", ".md", ".markdown", ".txt")

# Governance docs that DESCRIBE the lane (and therefore quote its marker) are not
# themselves private content. Exempt by basename so documentation can't trip the gate.
DOC_ALLOW = ("MATT-EYES-LANE.md",)

MARKERS = (
    re.compile(r'<meta\s+name=["\']tsp:lane["\']\s+content=["\']matt-eyes["\']', re.I),
    re.compile(r'^\s*tsp:lane\s*:\s*matt-eyes\s*$', re.I | re.M),
)

def is_matt_eyes(text):
    return any(p.search(text) for p in MARKERS)

def check_one(path, is_home):
    """Return list of (level, code, msg). Only HALT when a Matt-eyes file is found
    OUTSIDE its private home."""
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except Exception as e:
        return [("HALT", "READ", f"cannot read: {e}")]
    if not is_matt_eyes(text):
        return []
    if is_home:
        return []  # belongs here
    return [("HALT", "ME1",
             "Matt-eyes (private) file in a SHARED/PUBLIC repo — personal material "
             "must live only in the private matt-radar home. Move it there; do not deploy.")]

def detect_home(root):
    if os.environ.get("MATT_EYES_HOME") == "1":
        return True
    marker = os.path.join(root if os.path.isdir(root) else os.path.dirname(root) or ".",
                          ".matt-eyes-home")
    return os.path.exists(marker)

# ---- self-test fixtures ----
ME_HTML = '<!doctype html><meta name="tsp:lane" content="matt-eyes"><body>private</body>'
PLAIN   = '<!doctype html><meta name="tsp:surface" content="game"><body>public</body>'

def _fx(text, is_home):
    import tempfile
    fd, p = tempfile.mkstemp(suffix=".html"); os.write(fd, text.encode()); os.close(fd)
    try:
        return check_one(p, is_home)
    finally:
        os.unlink(p)

def selftest():
    leak_halts = any(c == "ME1" for l, c, *_ in _fx(ME_HTML, is_home=False) if l == "HALT")
    home_ok    = not any(l == "HALT" for l, *_ in _fx(ME_HTML, is_home=True))
    plain_pub  = not any(l == "HALT" for l, *_ in _fx(PLAIN, is_home=False))
    plain_home = not any(l == "HALT" for l, *_ in _fx(PLAIN, is_home=True))
    ok = leak_halts and home_ok and plain_pub and plain_home
    if not ok:
        print("SELF-TEST FAILED — leak_halts=%s home_ok=%s plain_pub=%s plain_home=%s. "
              "REFUSING TO CERTIFY." % (leak_halts, home_ok, plain_pub, plain_home))
    return ok

def main():
    if not selftest():
        sys.exit(2)
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    home = detect_home(target)
    if os.path.isfile(target):
        files = [target]
    else:
        files = []
        for ext in SCAN_EXT:
            files += glob.glob(os.path.join(target, "**", "*" + ext), recursive=True)
        files = sorted(set(files))
    halts = found = 0
    for f in files:
        # never scan our own .git internals
        if os.sep + ".git" + os.sep in f:
            continue
        # governance docs about the lane are not private content
        if os.path.basename(f) in DOC_ALLOW:
            continue
        res = check_one(f, home)
        if is_matt_eyes(open(f, encoding="utf-8", errors="replace").read()):
            found += 1
        for level, code, msg in res:
            print(f"{level}  {code}  {f}: {msg}")
            if level == "HALT": halts += 1
    where = "PRIVATE HOME (matt-radar)" if home else "shared/public repo"
    print(f"\nMATT-EYES LANE CHECK — context: {where} · {found} Matt-eyes file(s) · {halts} HALT")
    sys.exit(1 if halts else 0)

if __name__ == "__main__":
    main()
