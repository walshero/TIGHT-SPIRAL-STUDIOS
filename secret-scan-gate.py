#!/usr/bin/env python3
# SECRET-SCAN GATE — a "fool me once" enforcer. Tight Spiral Productions.
# Run: python3 secret-scan-gate.py [dir|file]
#
# WHY THIS EXISTS:
#   The 2026-08-05 account survey confirmed the repo is clean of hardcoded
#   secrets today — but "clean today, checked by hand" is not a floor. A public
#   repo (GitHub Pages) that ever commits a real token leaks it to the world,
#   cached and indexed even after deletion. Funes' law: a floor without an
#   enforcer fails. So the hand-check is now a gate.
#
# THE RULE:
#   No high-signal secret may be committed. HALT on: GitHub tokens (ghp_/
#   github_pat_), Slack tokens (xox*), AWS keys (AKIA…), OpenAI-style sk-…,
#   PEM PRIVATE KEY blocks, JSON Web Tokens (eyJhbGciOiJ… — a Supabase/JWT
#   signature), and the Supabase service_role key.
#
#   EXPLICITLY ALLOWED (public by design — not secrets):
#     * Supabase anon / publishable keys: `sb_publishable_…` and empty/paste
#       placeholders. These are meant to ship in client code WITH RLS on.
#     * base64 data: URIs (embedded images) — not credentials.
#     * Documentation that names a pattern to warn about it (DOC_ALLOW).
#
# SELF-TEST TEETH: a fake ghp_ token must HALT; a publishable key and a clean
#   file must pass. If a fixture lies, the tool exits 2 and refuses to certify.
#
# EXIT: 0 clean · 1 HALT (a real secret) · 2 self-test failure.
import re, sys, os, glob

# Docs that intentionally NAME secret patterns (to warn), so they aren't secrets.
DOC_ALLOW = ("BENCH-SETUP.md", "secret-scan-gate.py",
             "ACCOUNT-SURVEY-AND-BEST-PRACTICES.md", "DECISION-zapier-auth-lane.md")

SCAN_EXT = (".html", ".htm", ".js", ".py", ".sh", ".json", ".md", ".markdown",
            ".yml", ".yaml", ".txt", ".env")

PATTERNS = [
    ("GH-PAT",    re.compile(r'\bghp_[A-Za-z0-9]{30,}\b')),
    ("GH-PAT2",   re.compile(r'\bgithub_pat_[A-Za-z0-9_]{40,}\b')),
    ("SLACK",     re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b')),
    ("AWS",       re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ("OPENAI",    re.compile(r'\bsk-[A-Za-z0-9]{32,}\b')),
    ("PEM",       re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')),
    ("JWT",       re.compile(r'\beyJhbGciOiJ[A-Za-z0-9_-]{10,}')),
    ("SB-SERVICE",re.compile(r'service_role["\']?\s*[:=]\s*["\']eyJ')),
]

def scrub(text):
    # drop base64 data: URIs so embedded images can't false-positive
    return re.sub(r'data:[^;]+;base64,[A-Za-z0-9+/=]+', 'data:base64,<img>', text)

def check_one(path):
    try:
        text = scrub(open(path, encoding="utf-8", errors="replace").read())
    except Exception as e:
        return [("HALT", "READ", f"cannot read: {e}")]
    out = []
    for name, pat in PATTERNS:
        for m in pat.finditer(text):
            frag = m.group(0)
            if frag.startswith("sb_publishable_") or "PASTE_" in frag:
                continue
            line = text.count("\n", 0, m.start()) + 1
            out.append(("HALT", name, f"line {line}: possible {name} secret — {frag[:12]}…"))
    return out

# ---- self-test ----
BAD  = "token = 'ghp_" + "a" * 36 + "'"
PUB  = "var SB_ANON = 'sb_publishable_vVBDcyfO0700zijNHqLImw_MxKq2NeN';"
OK   = "just some clean text, no secrets here"

def _fx(text):
    import tempfile
    fd, p = tempfile.mkstemp(suffix=".js"); os.write(fd, text.encode()); os.close(fd)
    try:
        return check_one(p)
    finally:
        os.unlink(p)

def selftest():
    bad_halts = any(l == "HALT" for l, *_ in _fx(BAD))
    pub_ok    = not any(l == "HALT" for l, *_ in _fx(PUB))
    ok_ok     = not any(l == "HALT" for l, *_ in _fx(OK))
    if not (bad_halts and pub_ok and ok_ok):
        print("SELF-TEST FAILED — bad_halts=%s pub_ok=%s ok_ok=%s. REFUSING TO CERTIFY."
              % (bad_halts, pub_ok, ok_ok))
        return False
    return True

def main():
    if not selftest():
        sys.exit(2)
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    if os.path.isfile(target):
        files = [target]
    else:
        files = []
        for ext in SCAN_EXT:
            files += glob.glob(os.path.join(target, "**", "*" + ext), recursive=True)
        files = sorted(set(files))
    halts = 0
    for f in files:
        if os.sep + ".git" + os.sep in f:
            continue
        if os.path.basename(f) in DOC_ALLOW:
            continue
        for level, code, msg in check_one(f):
            print(f"{level}  {code}  {f}: {msg}")
            if level == "HALT":
                halts += 1
    print(f"\nSECRET-SCAN GATE — {len(files)} file(s) scanned · {halts} HALT")
    sys.exit(1 if halts else 0)

if __name__ == "__main__":
    main()
