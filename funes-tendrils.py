#!/usr/bin/env python3
# FUNES TENDRILS — loose ends down every forking path. Tight Spiral Productions.
# Run: python3 funes-tendrils.py [repo-dir]        (advisory: reports, exits 0)
#      python3 funes-tendrils.py --gate [repo-dir]  (CI: exits 1 if loose ends)
#
# WHY THIS EXISTS (the loss shape it makes visible):
#   Every loss this studio has suffered has ONE shape:
#       built -> landed in a branch/worktree/outputs -> STALL -> never merged -> gone.
#   A "stall" is any interruption: context compaction, session resume, an MCP
#   connector flap, a user interrupt, a chat that just ended. Work strands on a
#   fork and no one walks back down it.
#
#   2026-08-04 proved it live: the ENTIRE studio-wide governance lane sat 194
#   commits behind main on a stale handoff branch — invisible until someone
#   thought to look. Funes (the studio's memory discipline) forgets nothing, but
#   memory without a WALK is just a pile. This is the walk: after every stall,
#   send tendrils down all forking paths and surface what did not land.
#
# WHAT IT WALKS (per repo):
#   1. Working tree      — uncommitted changes (the freshest loose end).
#   2. Current branch    — commits ahead of upstream (built, not pushed).
#   3. All branches      — local + remote, ahead/behind main (unmerged = stranded;
#                          far-behind = stale base, the handoff-branch trap).
#   4. Worktrees         — extra worktrees that may hold uncommitted work.
#   5. Staging dirs      — outputs/ , scratch/ , tmp/ with files (nothing lives there).
#   6. Orphan pages      — *.html the face (index.html) does not link. "No orphans."
#
# It never guesses and never deletes. It reports. In --gate mode a loose end fails
# the build; by default (and as a session-start hook) it only reports, so a stall
# can never be silently inherited.
#
# EXIT: advisory -> always 0 · --gate -> 1 if any loose end · 2 if not a git repo.
import subprocess, sys, os, glob, re

def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root, *args],
                           capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def is_repo(root):
    return git(root, "rev-parse", "--is-inside-work-tree")[0] == 0

def main_ref(root):
    for cand in ("origin/main", "main", "origin/master", "master"):
        if git(root, "rev-parse", "--verify", "--quiet", cand)[0] == 0:
            return cand
    return None

def count(root, rng):
    rc, out, _ = git(root, "rev-list", "--count", rng)
    return int(out) if rc == 0 and out.isdigit() else None

def report(root):
    """Return (list_of_loose_end_lines, list_of_note_lines)."""
    loose, notes = [], []

    # 1. working tree
    _, dirty, _ = git(root, "status", "--porcelain")
    if dirty:
        n = len(dirty.splitlines())
        loose.append(f"[working tree] {n} uncommitted change(s) — commit or stash before the next stall")

    # 2/3. branches vs main
    mref = main_ref(root)
    cur = git(root, "rev-parse", "--abbrev-ref", "HEAD")[1]
    # unpushed on current branch
    if git(root, "rev-parse", "--verify", "--quiet", "@{u}")[0] == 0:
        ahead = count(root, "@{u}..HEAD")
        if ahead:
            loose.append(f"[unpushed] '{cur}' is {ahead} commit(s) ahead of its upstream — push before the chat closes")
    if mref:
        # every branch (local + remote), ahead/behind main
        rc, out, _ = git(root, "for-each-ref", "--format=%(refname:short)",
                         "refs/heads", "refs/remotes/origin")
        seen = set()
        for br in out.splitlines():
            if br in (mref, "origin/HEAD") or br.endswith("/HEAD"):
                continue
            base = br.split("/", 1)[-1] if br.startswith("origin/") else br
            if base in ("main", "master"):
                continue
            key = base
            ahead = count(root, f"{mref}..{br}")
            behind = count(root, f"{br}..{mref}")
            if ahead is None:
                continue
            if ahead > 0 and key not in seen:
                tag = "STRANDED" if behind and behind > 50 else "unmerged"
                extra = f", {behind} behind — STALE BASE, do not fast-merge" if behind and behind > 50 else ""
                loose.append(f"[{tag}] {br}: {ahead} commit(s) not in {mref}{extra}")
                seen.add(key)

    # 4. worktrees
    rc, out, _ = git(root, "worktree", "list")
    wl = [l for l in out.splitlines() if l.strip()]
    if len(wl) > 1:
        notes.append(f"[worktrees] {len(wl)} worktrees active — extra checkouts can hide uncommitted work:")
        for l in wl:
            notes.append("    " + l)

    # 5. staging dirs that should be empty
    for d in ("outputs", "scratch", "tmp"):
        p = os.path.join(root, d)
        if os.path.isdir(p):
            files = [f for f in glob.glob(os.path.join(p, "**", "*"), recursive=True) if os.path.isfile(f)]
            if files:
                loose.append(f"[staging] {d}/ holds {len(files)} file(s) — nothing lives in a staging dir; land or delete")

    # 6. orphan pages (the face links every page)
    face = os.path.join(root, "index.html")
    if os.path.isfile(face):
        try:
            idx = open(face, encoding="utf-8", errors="replace").read()
        except Exception:
            idx = ""
        # gate fixtures are deliberately unlinked (same exclusion the eyes use)
        FIXTURES = ("comfort-gate-canary-",)
        orphans = []
        for h in sorted(glob.glob(os.path.join(root, "*.html"))):
            b = os.path.basename(h)
            if b == "index.html" or b.startswith(FIXTURES):
                continue
            if b not in idx:
                orphans.append(b)
        if orphans:
            loose.append(f"[orphan pages] {len(orphans)} page(s) not linked from index.html: "
                         + ", ".join(orphans[:12]) + (" …" if len(orphans) > 12 else ""))

    return loose, notes

def main():
    args = [a for a in sys.argv[1:] if a != "--gate"]
    gate = "--gate" in sys.argv[1:]
    root = args[0] if args else "."
    root = os.path.abspath(root)
    if not is_repo(root):
        print(f"FUNES TENDRILS — {root} is not a git repo; nothing to walk.")
        sys.exit(2 if gate else 0)

    loose, notes = report(root)
    print("=" * 68)
    print("FUNES TENDRILS — loose ends down every forking path (post-stall sweep)")
    print("=" * 68)
    if loose:
        print(f"\n  {len(loose)} LOOSE END(S) — work that did not land:")
        for l in loose:
            print("   • " + l)
    if notes:
        print()
        for n in notes:
            print("  " + n)
    if not loose and not notes:
        print("  Git lanes clean. Every fork accounted for; nothing stranded.")

    # UNWALKED LANES — the blind-gate lesson (belt tick 5) applied to memory:
    # a lane this script cannot reach must be named LOUDLY, never silently
    # implied clean. Losses have never been git-only (v48 trunk in Drive,
    # 194-commit stranded governance lane, un-harvested chats). Registry:
    # lane-tendrils.json. Session-connector lanes are walked at session close
    # by a live session (CLAUDE.md); human-only lanes are walked by discipline.
    lreg = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lane-tendrils.json")
    if os.path.isfile(lreg):
        try:
            import json
            lanes = json.load(open(lreg, encoding="utf-8")).get("lanes", [])
            unwalked = [l for l in lanes if l.get("reach") != "mechanical-ci"]
            if unwalked:
                print(f"\n  {len(unwalked)} LANE(S) THIS SWEEP CANNOT WALK — blind is not clean:")
                for l in unwalked:
                    print(f"   ◦ [{l['reach']}] {l['lane']}")
                print("    Session-connector lanes: walk from a live session at close"
                      " (CLAUDE.md session-close sweep). Human-only lanes: harvest"
                      " before the chat dies; the shelf is a cache, not a lane.")
        except Exception as e:
            print(f"\n  WARN: lane-tendrils.json unreadable ({e}) — lane blindness is now itself invisible. Fix it.")
    else:
        print("\n  WARN: lane-tendrils.json missing — the unwalked-lane roster is gone. Fix it.")

    print("\n  Funes forgets nothing. Walk each one before the next stall inherits it.")
    sys.exit(1 if (gate and loose) else 0)

if __name__ == "__main__":
    main()
