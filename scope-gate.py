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
# `--evidence <file.json>` is a usage placeholder, not a citation. Angle brackets are the
# studio's placeholder convention in every usage line already in the trunk; a gate that
# demands `<file.json>` exist is asking the repo to hold a variable name.
SLOT = re.compile(r'<[^<>\n]{1,80}>')
# The leading dot is PART OF THE PATH. Without `\.?` this called CLAUDE.md's correct
# citation of `.claude/agents/union-rep.md` a dangling reference to
# `claude/agents/union-rep.md` - a file that does not exist, invented by the tokenizer
# eating the dot. Found 2026-08-09 by a founder-authorized write, which is the only reason
# anyone looked. A gate that manufactures the defect it reports is worse than no gate;
# studio-fingers.py shipped four of these in one afternoon.
TOKEN = re.compile(
    r'(?<![A-Za-z0-9._\-/])(\.?[A-Za-z0-9][A-Za-z0-9._\-/]{2,60}\.(?:md|py|sh|json|html|yml|yaml))')

# A citation is not dangling just because the file is not in THIS lane. FOUR LANES, NOT ONE.
# cross-lane-manifest.md names a Confluence trunk by Drive id; that file is Drive-owned and
# will never be in the repo, and calling it dangling was the gate asserting that the repo is
# the world. If the citing line also names another lane, the citation is OFF-LANE: printed,
# never counted. The address is still checkable - just not here.
OFFLANE = re.compile(r'\b(drive|dropbox|netlify|onedrive|confluence|shelf)\b', re.I)
GOOGLE_ID = re.compile(r'\b[A-Za-z0-9_-]{25,}\b')


WORKTREE = "worktree"          # grade what is ABOUT to ship, not what already shipped


def trunk_paths(ref):
    # -c -o --exclude-standard: tracked PLUS untracked-but-not-ignored. A file staged on
    # disk and about to be pushed is part of what ships, so preflight must count it as
    # present - otherwise landing a document and the citation that names it in the same
    # turn reads as a new dangling citation and halts the very fix.
    cmd = (["git", "ls-files", "-c", "-o", "--exclude-standard"] if ref == WORKTREE
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
  