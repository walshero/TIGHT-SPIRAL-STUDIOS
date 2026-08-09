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
    return os.path.basename(top.stdout.strip()) if top.returncode == 0 else "?"


def load_baseline(path=BASELINE):
    """A baseline belongs to ONE repo. The belt walks five, and three of them ship an
    index.html; grading a spoke against the hub's debt would call every one of that
    spoke's citations NEW and halt it on day one over debt nobody measured there. If the
    baseline names a different repo, this returns None and the caller says so OUT LOUD."""
    if not os.path.exists(path):
        return None
    rec = json.load(open(path))
    here = repo_name()
    if rec.get("repo") and rec["repo"] != here:
        print(f"   BASELINE MISMATCH - {path} was frozen for '{rec['repo']}', this is "
              f"'{here}'. Treating as NO BASELINE, loudly. Freeze one here.")
        return None
    return rec


def report(res, base):
    n_dangle = sum(len(v) for v in res["dangling"].values())
    print(f"== scope-gate: {res['ref']} ==")
    print(f"   {res['files']} files in trunk, {len(res['gov'])} governance docs scanned")
    print()

    print("-- CLAUSE A: wide retrieval baked into an artifact (FLAT, zero tolerance) --")
    if res["wide"]:
        for w in res["wide"]:
            print(f"   HALT  {w['file']}:{w['line']}  [{w['shape']}]")
            print(f"         {w['text']}")
    else:
        print("   clean - 0 wide-query shapes in trunk artifacts")
    print(f"   allowed to say it (documents that define the rule): "
          f"{', '.join(DEFINES_THE_RULE)}")
    print()

    print("-- CLAUSE B: a governance doc naming a file the trunk cannot reach (RATCHET) --")
    known = base.get("dangling", {}) if base else {}
    fresh = []
    for doc, toks in sorted(res["dangling"].items()):
        for t in toks:
            # With no baseline NOTHING is "new" — there is no was to be newer than. Calling
            # every pre-existing citation new would halt an unmeasured repo on day one over
            # debt nobody put there this push, which is the mistake ticks 1/3/4/5 already
            # made once. Unmeasured is printed as UNMEAS and does not block.
            tag = "UNMEAS" if base is None else ("known" if t in known.get(doc, []) else "NEW")
            if tag == "NEW":
                fresh.append((doc, t))
            print(f"   {tag:6s} {doc}  ->  {t}")
    if not res["dangling"]:
        print("   clean - every file named by a governance doc resolves in the trunk")
    b = base.get("count") if base else None
    print(f"   debt now {n_dangle}" + (f", baseline {b}" if b is not None else ", NO BASELINE"))
    print()

    print("-- LIMITS (this gate does not cover these; do not read silence as coverage) --")
    print("   * It reads ARTIFACTS. It cannot see a query an agent types at runtime,")
    print("     which is the shape that actually caused the incident. The runtime half")
    print("     lives in the standing instructions, not here.")
    print("   * Snapshot trees are skipped by design: " + ", ".join(GOV_SKIP_PREFIX))
    print("     Their citations dangle because history moved on; fixing them rewrites it.")
    print("   * A citation 'resolves' if the trunk holds that basename ANYWHERE. Eight")
    print("     basenames collide in this repo; resolve-canon.py owns that question.")
    print()

    if res["wide"]:
        print("HALT - a wide retrieval is baked into an artifact. Remove it.")
        return 1
    if fresh:
        print(f"HALT - {len(fresh)} NEW dangling citation(s). Either land the file it names")
        print("       or fix the citation. Do not add it to the baseline to make this quiet.")
        return 1
    if base is None:
        print("NOTE - no baseline. Freeze one with --freeze, then this becomes a ratchet.")
        return 0
    if n_dangle < b:
        print(f"PASS - and debt fell {b} -> {n_dangle}. Re-freeze so it cannot climb back.")
        return 0
    print("PASS - no wide retrieval, no new dangling citation.")
    return 0


def freeze(res, path=BASELINE):
    rec = {"repo": repo_name(), "ref": res["ref"],
           "count": sum(len(v) for v in res["dangling"].values()),
           "dangling": res["dangling"], "gov_docs": len(res["gov"])}
    with open(path, "w") as f:
        json.dump(rec, f, indent=2, sort_keys=True)
    print(f"FROZE {path}: {rec['count']} dangling citation(s) across {rec['gov_docs']} docs")
    print("This number must fall. It is debt, not a standard.")
    return 0


# ---------------------------------------------------------------- self-test
def self_test():
    """Prove it discriminates. A gate with no canary is a gate nobody has tested."""
    allset = {"a/b.md", "FORKING-PATHS-PROTOCOL.md", "resolve-canon.py"}
    byname = collections.defaultdict(list)
    for p in allset:
        byname[os.path.basename(p)].append(p)

    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"   {'PASS' if good else 'FAIL'}  {label}  (got {got!r}, want {want!r})")

    print("-- resolution --")
    chk("exact path resolves",            resolves("a/b.md", allset, byname), True)
    chk("bare basename resolves",         resolves("resolve-canon.py", allset, byname), True)
    chk("asserted path must be real",     resolves("claude/FORKING-PATHS-PROTOCOL.md", allset, byname), False)
    chk("unknown name dangles",           resolves("ghost.md", allset, byname), False)

    print("-- clause A shapes --")
    hit = lambda s: any(rx.search(s) for rx, _ in WIDE)
    chk("fullText contains caught",       hit("q=\"fullText contains 'x'\""), True)
    chk("case-insensitive caught",        hit("FULLTEXT CONTAINS 'x'"), True)
    chk("name contains is innocent",      hit("name contains 'studio-fingers'"), False)
    chk("parents fence is innocent",      hit("parents in '1AbC' and name contains 'x'"), False)

    print("-- clause B noise filters --")
    body = URLS.sub(" ", CODE.sub(" ", "see https://raw.githubusercontent.com/w/T/main/x.html now"))
    chk("URL tail not a citation",        bool(TOKEN.search(body)), False)
    body2 = URLS.sub(" ", CODE.sub(" ", "read FORKING-PATHS-PROTOCOL.md today"))
    chk("bare citation still found",      bool(TOKEN.search(body2)), True)

    print("-- governance selection --")
    chk("root CLAUDE.md is governance",   is_gov("CLAUDE.md"), True)
    chk("ruling is governance",           is_gov("claude/FERPA-SCOPE-RULING.md"), True)
    chk("snapshot is skipped",            is_gov("rescued/shelf-2026-07-13/x-CHARTER.md"), False)
    chk("html is not governance",         is_gov("index.html"), False)

    print()
    print("SELF-TEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 2


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] in ("-h", "--help"):
        print(__doc__)
        print("  scope-gate.py [ref]          scan and grade (default origin/main)")
        print("  scope-gate.py --freeze [ref]  write scope-baseline.json")
        print("  scope-gate.py --self-test     prove it discriminates")
        sys.exit(0)
    if a and a[0] == "--self-test":
        sys.exit(self_test())

    do_freeze = bool(a) and a[0] == "--freeze"
    if do_freeze:
        a = a[1:]
    ref = a[0] if a else "origin/main"

    res = scan(ref)
    if res is None:
        print(f"HALT - cannot read tree at {ref}. Run this from a clone.")
        sys.exit(2)
    sys.exit(freeze(res) if do_freeze else report(res, load_baseline()))
