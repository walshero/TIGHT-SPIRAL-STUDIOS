#!/usr/bin/env python3
"""
SCOPE_GATE - what a document reaches for.

Built 2026-08-09, the day claude/FERPA-SCOPE-RULING.md was found to exist in exactly one
lane while FUNES-MEMORY-PATCH.md cited it by name from another.

THE TWO FAILURES THIS EXISTS TO CATCH
-------------------------------------
CLAUSE A - REACHING TOO FAR.
An errand hunting a studio FILE ran `fullText contains 'studio-fingers'` against all of
Google Drive and got three students' course portfolios back, because "floor" matched
"floor-to-ceiling windows." The control is arithmetic, not judgment: a name-contains query
has no reach into a document body, so it CANNOT return a student's paragraph. This clause
cannot watch a runtime query - see LIMITS - but it can stop a wide query from being BAKED
INTO an artifact, where it would be copied forward forever.

CLAUSE B - NAMING WHAT YOU CANNOT REACH.
The project instructions order every session to read claude/forking-paths-protocol.md,
claude/founder-voice-provenance-manifest.md and claude/FUNES-LEDGER.md. On the day this
gate was written, NONE of the three resolved in the trunk. A rule that names a file nobody
can fetch is a wish wearing a gate's clothes, and it fails silently and forever: the
session reads the instruction, cannot find the file, and proceeds. That is precisely how
the FERPA ruling went unread twice in one day by the agent whose enforcement clause names
it. THE CITATION IS THE GATE'S OWN HOMEWORK, so this clause grades it.

WHY ONE GATE AND NOT TWO
Both clauses ask the same question about reach: A says do not reach past what you were
asked for, B says do not point at what you cannot touch. This repo grew two studio-fingers
gates in one day by splitting a question that was really one question. Not doing that again.

RATCHET, NOT FLAT (clause B)
Clause B starts with real debt. A tick that is red on every push is a tick everyone learns
to scroll past - the belt's own lesson from ticks 1/3/4/5. Baseline freezes today's
dangling citations; NEW ones halt, and the baseline is the number that must reach zero.
Clause A is FLAT zero-tolerance: it is at zero today and there is no reason to ever add one.

EXIT CODES
    0  no wide query baked in, no new dangling citation
    1  HALT - clause A hit, or clause B debt above baseline
    2  usage / unreadable input / self-test failure
"""

import sys, os, re, json, subprocess, collections

BASELINE = os.environ.get("SCOPE_BASELINE", "scope-baseline.json")

# ---------------------------------------------------------------- clause A
# Query shapes that reach into document BODIES across a whole corpus. Matched as source
# text, so a spec, a script, or a saved Zap all count the same.
WIDE_GREP = [
    (r"fullText[[:space:]]+contains", "Drive fullText"),
    (r"q[[:space:]]*=[[:space:]]*[\"']fullText", "Drive q=fullText"),
    (r"has:attachment[[:space:]]+OR", "unbounded Gmail OR sweep"),
]
# Same shapes as Python regex, for the self-test canary only. git grep is the real reader.
WIDE = [
    (re.compile(r'fullText\s+contains', re.I),      "Drive fullText"),
    (re.compile(r'\bq\s*=\s*["\']fullText', re.I),  "Drive q=fullText"),
    (re.compile(r'has:attachment\s+OR\b', re.I),    "unbounded Gmail OR sweep"),
]

# The documents that DEFINE the rule must be allowed to SAY the forbidden string, or the
# gate eats its own homework - the same lesson retired-lines-gate.py learned as render_only.
# This list is printed on every run. It is not a quiet exemption.
DEFINES_THE_RULE = [
    "claude/FERPA-SCOPE-RULING.md",
    "FUNES-LEDGER.md",
    "scope-gate.py",
    "scope-baseline.json",
]

# ---------------------------------------------------------------- clause B
GOV_HINTS = ("PROTOCOL", "MANIFEST", "RULING", "CHARTER", "PATCH", "CONTRACT")
GOV_NAMES = {"CLAUDE.md", "COLD-START.md", "LANE-REGISTRY.md", "HANDOFF.md",
             "PROJECT-INSTRUCTIONS-paste-block.md"}
# Snapshots are history, not live rules. Their citations dangle by design and fixing them
# would rewrite the past. STATED, not silently dropped - printed under LIMITS.
GOV_SKIP_PREFIX = ("rescued/", "archive/", "aleph-runs/")

URLS = re.compile(r'https?://\S+|\b[\w.-]+\.(?:com|org|net|io|edu|dev)/\S*', re.I)
CODE = re.compile(r'```.*?```', re.S)
TOKEN = re.compile(r'\b([A-Za-z0-9][A-Za-z0-9._\-/]{2,60}\.(?:md|py|sh|json|html|yml|yaml))\b')


WORKTREE = "worktree"          # grade what is ABOUT to ship, not what already shipped


def trunk_paths(ref):
    cmd = (["git", "ls-files"] if ref == WORKTREE
           else ["git", "ls-tree", "-r", "--name-only", ref])
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if out.returncode:
        return None
    return [p for p in out.stdout.split("\n") if p.strip()]


def read(ref, path):
    """Bytes, then a lossy decode. The trunk holds binaries; a gate that dies on a PNG is
    a gate that does not run, which is the same as no gate."""
    if ref == WORKTREE:
        try:
            return open(path, "rb").read().decode("utf-8", "replace")
        except OSError:
            return ""
    out = subprocess.run(["git", "show", f"{ref}:{path}"],
                         capture_output=True, timeout=120)
    if out.returncode:
        return ""
    return out.stdout.decode("utf-8", "replace")


def grep(ref, pattern):
    """One pass over the whole tree per shape, -I so binaries are skipped by git itself.
    587 `git show` calls took longer than the belt's whole budget; this takes one.
    In worktree mode git greps the checkout, so an unpushed wide query is caught BEFORE
    it lands — which is the only moment the catch is worth anything."""
    cmd = ["git", "grep", "-n", "-I", "-E", "-i", pattern]
    if ref != WORKTREE:
        cmd.append(ref)
    out = subprocess.run(cmd, capture_output=True, timeout=180)
    if ref == WORKTREE:
        hits = []
        for line in out.stdout.decode("utf-8", "replace").splitlines():
            path, _, rest = line.partition(":")
            num, _, body = rest.partition(":")
            if path and num.isdigit():
                hits.append((path, int(num), body.strip()[:120]))
        return hits
    hits = []
    for line in out.stdout.decode("utf-8", "replace").splitlines():
        head, _, text = line.partition(":")           # strip "ref:"
        path, _, rest = text.partition(":")
        num, _, body = rest.partition(":")
        if path and num.isdigit():
            hits.append((path, int(num), body.strip()[:120]))
    return hits


def resolves(token, allset, byname):
    """Same rule the resolver uses: an exact path is never ambiguous; otherwise a bare
    basename resolves if the trunk holds that basename anywhere."""
    if token in allset:
        return True
    if "/" in token:
        return False                      # a path was asserted; it must be the real one
    return os.path.basename(token) in byname


def is_gov(path):
    if path.startswith(GOV_SKIP_PREFIX):
        return False
    if not path.endswith(".md"):
        return False
    base = os.path.basename(path)
    up = path.upper()
    return base in GOV_NAMES or any(h in up for h in GOV_HINTS)


def scan(ref="origin/main"):
    paths = trunk_paths(ref)
    if paths is None:
        return None
    allset = set(paths)
    byname = collections.defaultdict(list)
    for p in paths:
        byname[os.path.basename(p)].append(p)

    wide = []
    for pattern, label in WIDE_GREP:
        for path, num, body in grep(ref, pattern):
            if path in DEFINES_THE_RULE or os.path.basename(path) in DEFINES_THE_RULE:
                continue
            wide.append({"file": path, "line": num, "shape": label, "text": body})

    dangling, gov = collections.defaultdict(list), []
    for p in paths:
        if not is_gov(p):
            continue
        gov.append(p)
        body = URLS.sub(" ", CODE.sub(" ", read(ref, p)))
        seen = set()
        for m in TOKEN.finditer(body):
            t = m.group(1)
            if t in seen:
                continue
            seen.add(t)
            if not resolves(t, allset, byname):
                dangling[p].append(t)

    return {"ref": ref, "files": len(paths), "gov": sorted(gov),
            "wide": wide, "dangling": {k: sorted(v) for k, v in dangling.items()}}


def repo_name():
    """The REMOTE's name, not the checkout directory's. This clone is called 'tsp-repo';
    the repo is TIGHT-SPIRAL-STUDIOS. Keying a baseline to a directory name means the same
    repo cloned twice grades as two repos, which is how baselines quietly stop applying."""
    r = subprocess.run(["git", "remote", "get-url", "origin"],
                       capture_output=True, text=True, timeout=60)
    if r.returncode == 0 and r.stdout.strip():
        return os.path.basename(r.stdout.strip().rstrip("/")).removesuffix(".git")
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, timeout=60)
    return os.path.basename(top.stdout.s