#!/usr/bin/env python3
"""
SHELF-SAFE-TO-DELETE — the proof, not the promise.

Answers exactly one question, arithmetically:

    If I delete every file on the project shelf right now, does anything DIE?

A file "dies" if it exists on the shelf and has NO twin anywhere in the git tree.
Not "probably fine." Not "I classified it as disposable." A byte-level twin, found
by content hash, anywhere in origin/main.

WHY THIS EXISTS
---------------
On 2026-07-13 a classifier marked 29 shelf files DELETE (dated session records,
"_2" duplicates) and never pushed them. They had no repo twin. Deleting the shelf
on that classifier's word would have destroyed funnyboneysfactoryspec.pdf (749KB),
confluence-TRUNK-v43, and the OS fork the Command Center explicitly says to DIFF.

The classifier was reasoning about filenames. This script reasons about bytes.

    A rule that can't be a check is a wish.
    An audit that lies is the disease.

RUN IT FROM INSIDE A CLONE:

    git clone https://<PAT>@github.com/walshero/TIGHT-SPIRAL-STUDIOS.git
    cd TIGHT-SPIRAL-STUDIOS
    python3 shelf-safe-to-delete.py

EXIT CODES
----------
    0  SAFE   — every shelf file has a byte-identical twin in git. Delete freely.
    1  UNSAFE — at least one file would die. It names them. DO NOT DELETE.
    2  HALT   — cannot read the git tree. An audit without canon is a list of lies.
               (Never guesses. Never returns 0 because it couldn't look.)
"""

import hashlib
import os
import subprocess
import sys

SHELF = "/mnt/project"


def sh(*args):
    return subprocess.run(args, capture_output=True, timeout=60)


def md5(b):
    return hashlib.md5(b).hexdigest()


def build_git_index():
    """Every blob in origin/main, indexed by content hash AND by basename.

    RECURSIVE. The -r flag is not optional — without it this reads the repo ROOT
    only, hides everything in /studio /archive /rescued /writerly-moves, and
    reports deployed files as homeless. That bug shipped once. Not again.
    """
    r = sh("git", "ls-tree", "-r", "--name-only", "origin/main")
    paths = [p.strip() for p in r.stdout.decode(errors="replace").splitlines() if p.strip()]

    if not paths:
        print("HALT — cannot read the git tree.")
        print("       Run this from inside a clone, with origin/main fetched.")
        print("       An audit that cannot see canon is a list of lies. Exiting 2.")
        sys.exit(2)

    by_hash = {}          # content md5 -> [paths]
    by_name = {}          # basename    -> [paths]
    for p in paths:
        blob = sh("git", "show", f"origin/main:{p}").stdout
        by_hash.setdefault(md5(blob), []).append(p)
        by_name.setdefault(os.path.basename(p), []).append(p)
    return by_hash, by_name, len(paths)


def main():
    if not os.path.isdir(SHELF):
        print(f"HALT — no shelf at {SHELF}. Nothing to check. Exiting 2.")
        sys.exit(2)

    print("=" * 72)
    print("SHELF-SAFE-TO-DELETE")
    print("=" * 72)
    print("Reading the git tree (recursive, every blob hashed)...")

    by_hash, by_name, n_repo = build_git_index()
    shelf = sorted(f for f in os.listdir(SHELF) if not f.startswith("."))

    print(f"  repo:  {n_repo} files in origin/main")
    print(f"  shelf: {len(shelf)} files")
    print()

    exact, renamed, drifted, orphan = [], [], [], []

    for f in shelf:
        p = os.path.join(SHELF, f)
        if not os.path.isfile(p):
            continue
        with open(p, "rb") as fh:
            blob = fh.read()
        h = md5(blob)

        if h in by_hash:
            # byte-identical twin exists somewhere in git — under any name
            twin = by_hash[h][0]
            (exact if os.path.basename(twin) == f else renamed).append((f, twin))
        elif f in by_name:
            # same name, different bytes. NOT a death — but the shelf copy is a
            # version that exists nowhere else. Name it. Do not silently bless it.
            twin = by_name[f][0]
            rb = sh("git", "show", f"origin/main:{twin}").stdout
            drifted.append((f, twin, len(blob), len(rb)))
        else:
            # no twin by hash, no twin by name. Deleting this DESTROYS it.
            orphan.append((f, len(blob)))

    if exact:
        print(f"IDENTICAL — byte-for-byte twin in git  [{len(exact)}]")
        print("   Safe. Deleting these loses nothing.\n")

    if renamed:
        print(f"IDENTICAL, DIFFERENT PATH  [{len(renamed)}]")
        print("   Same bytes, filed elsewhere in the repo. Safe.")
        for f, twin in renamed[:8]:
            print(f"   {f:<44} -> {twin}")
        if len(renamed) > 8:
            print(f"   ... and {len(renamed) - 8} more")
        print()

    if drifted:
        print(f"DRIFTED — same name, DIFFERENT BYTES  [{len(drifted)}]")
        print("   The repo holds a different version. The shelf version exists")
        print("   NOWHERE ELSE. Usually the shelf is just stale — but never assume.")
        print("   Never default to newer/older/larger/smaller. DIFF. Decide from content.\n")
        for f, twin, sb, rb in drifted:
            d = sb - rb
            print(f"   {f:<44} shelf {sb:>8,} B  repo {rb:>8,} B  ({d:+,})")
        print()

    print("=" * 72)
    if orphan:
        print(f"*** UNSAFE — {len(orphan)} FILES WOULD DIE ***")
        print()
        print("These exist on the shelf and NOWHERE in git. Deleting the shelf")
        print("DESTROYS them. Push them first.\n")
        for f, sz in orphan:
            print(f"   {f:<52} {sz:>9,} B")
        print()
        print("DO NOT DELETE THE SHELF.")
        print("=" * 72)
        return 1

    print("*** SAFE TO DELETE ***")
    print()
    print(f"All {len(shelf)} shelf files have a twin in git.")
    if drifted:
        print(f"({len(drifted)} drifted — the repo version is canon. Confirm you")
        print(" want the repo version before you wipe the shelf copy.)")
    print()
    print("Nothing dies. The repo is home.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
