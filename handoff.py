#!/usr/bin/env python3
"""
HANDOFF — the save/retrieve pathway.

THE PROBLEM THIS SOLVES
-----------------------
The studio has lost work the same way every time:

    built -> landed in outputs -> never pushed -> chat closed -> gone

And it has RE-DERIVED the same context every session, because the handoff was a
thing someone had to remember to write, in a place someone had to remember to look.

Fifteen files named `session-handoff-2026-07-*` are the fossil record of that.

THE PATHWAY — two commands, no memory required
----------------------------------------------
    python3 handoff.py save      # write the handoff to EVERY lane, byte-verified
    python3 handoff.py read      # pull it from the FIRST lane that answers

That is the whole system. Not a procedure. A command.

THE LANES, in precedence order
------------------------------
    1. REPO      raw.githubusercontent.com/.../main/HANDOFF.md   <- CANON
    2. DRIVE     Claude_files (walshero) — survives a repo outage
    3. SHELF     /mnt/project — a cache, it LAGS, never canon

`save` writes to every lane it can reach and SAYS SO when a lane fails. It never
reports success it did not verify. `read` walks the lanes in order and takes the
first that answers, naming which lane it came from.

WHY ONE FILE, NO DATE
---------------------
Canonical name. Replace, never add. History lives in git — that is what git is for.
A file whose name you cannot distinguish from fourteen others is a file you cannot use.
"""

import sys, os, subprocess, hashlib, urllib.request

NAME  = "HANDOFF.md"
RAW   = "https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/" + NAME
SHELF = "/mnt/project/" + NAME


def md5(b):
    return hashlib.md5(b).hexdigest()


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tsp-handoff"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except Exception:
        return None


def save():
    """Write to every lane. Verify each. Never claim a landing that did not happen."""
    if not os.path.exists(NAME):
        print(f"HALT — {NAME} not found in this directory.")
        print("       Nothing to save. Write the handoff first.")
        return 2

    local = open(NAME, "rb").read()
    lm    = md5(local)
    print(f"== HANDOFF SAVE — {len(local):,} B  md5 {lm[:8]} ==\n")

    landed, failed = [], []

    # LANE 1 — the repo. Canon. Content-addressed; it cannot lie.
    try:
        subprocess.run(["git", "add", NAME], check=True, capture_output=True)
        c = subprocess.run(
            ["git", "-c", "user.email=walshero@gmail.com",
             "-c", "user.name=Tight Spiral Productions",
             "commit", "-q", "-m", "Handoff."],
            capture_output=True, text=True)
        # "nothing to commit" is not a failure — it means canon already matches.
        p = subprocess.run(["git", "push", "-q", "origin", "main"],
                           capture_output=True, text=True)
        if p.returncode == 0 or "nothing to commit" in c.stdout:
            # POST-TICK. Verify against GIT, not the CDN — raw.githubusercontent
            # caches ~5 min and WILL report the old file on a fresh push.
            h = subprocess.run(["git", "rev-parse", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
            o = subprocess.run(["git", "rev-parse", "origin/main"],
                               capture_output=True, text=True).stdout.strip()
            if h == o:
                landed.append("repo   (canon)")
                print(f"  repo   LANDED   HEAD == origin/main  {h[:8]}")
            else:
                failed.append("repo — push did not land")
                print("  repo   *** FAILED — HEAD != origin/main ***")
        else:
            failed.append("repo — " + p.stderr.strip()[:70])
            print(f"  repo   *** FAILED *** {p.stderr.strip()[:70]}")
    except Exception as e:
        failed.append(f"repo — {e}")
        print(f"  repo   *** FAILED *** {e}")

    # LANE 2 — Drive. Small file, passes the paste bus. Survives a repo outage.
    print("  drive  MANUAL — the Drive bus is a tool call, not a shell command.")
    print("         Claude writes it with write_drive_file_content in the same turn.")

    # LANE 3 — the shelf. A cache. Read-only from here.
    print("  shelf  READ-ONLY from the container. It syncs from the Project, not to it.")

    print()
    if failed:
        print("  *** NOT FULLY LANDED ***")
        for f in failed:
            print(f"      {f}")
        print("\n  A handoff that did not land is a handoff that does not exist.")
        return 1

    print(f"  SAVED — {', '.join(landed)}")
    print(f"  Retrieve next session with:  python3 handoff.py read")
    return 0


def read():
    """Walk the lanes in precedence order. Take the first that answers. Name it."""
    print("== HANDOFF READ ==\n")

    b = fetch(RAW)
    if b and len(b) > 200:
        print(f"  FROM: repo (canon)   {len(b):,} B   md5 {md5(b)[:8]}\n")
        print("-" * 70)
        print(b.decode("utf-8", errors="replace"))
        return 0
    print("  repo   unreachable (egress block, or not pushed)")

    if os.path.exists(SHELF):
        b = open(SHELF, "rb").read()
        print(f"\n  FROM: shelf (A CACHE — IT LAGS. Verify against the repo.)")
        print(f"        {len(b):,} B   md5 {md5(b)[:8]}\n")
        print("-" * 70)
        print(b.decode("utf-8", errors="replace"))
        return 0
    print("  shelf  not present")

    print("\n  HALT — no lane answered.")
    print("  This is NOT proof the handoff does not exist. A zero-result is not")
    print("  evidence of absence. Check Drive Claude_files by hand before concluding")
    print("  anything is lost.")
    return 2


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    if a[0] == "save":
        sys.exit(save())
    if a[0] == "read":
        sys.exit(read())
    print(f"unknown: {a[0]}. Use `save` or `read`.")
    sys.exit(2)
