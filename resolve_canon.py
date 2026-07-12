#!/usr/bin/env python3
# ══════════════════════════════════════════════════════════════════
# resolve_canon.py — CANON IS COMPUTED, NOT REMEMBERED
# Tight Spiral Productions · locked 2026-07-11
#
#   python3 resolve_canon.py <filename> [--drive-id <id>]
#
#   exit 0  = lanes agree (or only one lane has it). Canon named. Safe to edit.
#   exit 1  = LANES DIVERGE. STOP. Do not edit. Do not guess. Reconcile first.
#   exit 2  = not found in any lane.
#
# WHY THIS EXISTS (each failure is from 2026-07-11, not a hypothetical):
#   · I edited v34 while canon sat at v43.
#   · I declared a shipped game "lost" after checking one lane.
#   · A Drive search returned zero while the files sat in the folder.
#   · Two sessions wrote the same 598KB trunk; one reverted the other's work.
#
# Five lines of the coherence prompt collapse into this one call. What CANNOT
# be computed — and therefore stays prose — is only:
#   (a) Matt is the authority on his own working vocabulary.
#   (b) When Matt pushes back on a machine-produced fact, the machine is the
#       suspect. Re-derive. Don't defend.
#
# A rule that can't be a check is a wish. This is the check.
# ══════════════════════════════════════════════════════════════════
import hashlib, json, os, subprocess, sys, urllib.request

REPO_RAW = "https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/"
SHELF    = "/mnt/project/"
OUTPUTS  = "/mnt/user-data/outputs/"
UPLOADS  = "/mnt/user-data/uploads/"

def h(b):
    return hashlib.md5(b).hexdigest() if b else None

def fetch_repo(name):
    """Lane 1: the repo. Canon for anything >50KB (LANE-SIZE LAW)."""
    try:
        req = urllib.request.Request(
            REPO_RAW + name,
            headers={'Cache-Control': 'no-cache'}  # raw CDN caches; bust it
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except Exception:
        return None

def fetch_local(base, name):
    p = os.path.join(base, name)
    if not os.path.isfile(p):
        return None
    try:
        return open(p, 'rb').read()
    except Exception:
        return None

def git_truth(name):
    """The repo's OWN answer, bypassing the CDN cache entirely.
    Tonight the CDN served a stale v43 for minutes after v44 landed —
    the cache lied and the POST-TICK caught it. git is authoritative."""
    for repo_dir in ('/home/claude/tsp2', '/home/claude/tsp'):
        if not os.path.isdir(os.path.join(repo_dir, '.git')):
            continue
        try:
            subprocess.run(['git', 'fetch', '-q', 'origin', 'main'],
                           cwd=repo_dir, timeout=30, capture_output=True)
            out = subprocess.run(['git', 'show', f'origin/main:{name}'],
                                 cwd=repo_dir, timeout=30, capture_output=True)
            if out.returncode == 0 and out.stdout:
                return out.stdout
        except Exception:
            pass
    return None

def resolve(name, drive_bytes=None):
    lanes = {}

    # authoritative first: git over CDN
    g = git_truth(name)
    if g:
        lanes['repo (git)'] = g
    else:
        r = fetch_repo(name)
        if r:
            lanes['repo (raw CDN — may lag)'] = r

    for label, base in (('shelf (CACHE — lags)', SHELF),
                        ('outputs (SCRATCH — evaporates)', OUTPUTS),
                        ('uploads', UPLOADS)):
        b = fetch_local(base, name)
        if b:
            lanes[label] = b

    if drive_bytes:
        lanes['drive'] = drive_bytes

    print(f"\n  RESOLVE CANON — {name}")
    print("  " + "─" * 62)

    if not lanes:
        print("  NOT FOUND in any lane.")
        print("  A zero-result is NOT evidence of absence — list the containers")
        print("  and look before you conclude it does not exist.\n")
        return 2

    hashes = {}
    for label, b in lanes.items():
        hashes[label] = h(b)
        print(f"  {label:<32} {len(b):>9,} B   {hashes[label][:12]}")

    distinct = set(hashes.values())
    print("  " + "─" * 62)

    if len(distinct) == 1:
        canon = max(lanes, key=lambda k: 0 if 'SCRATCH' in k or 'CACHE' in k else 1)
        print(f"  AGREE — all lanes identical. Canon: {canon}")
        print("  Safe to edit.\n")
        return 0

    # DIVERGENCE
    print("  ✗ LANES DIVERGE — STOP.")
    print()
    print("  Do NOT edit. Do NOT default to the newest, oldest, largest, or")
    print("  smallest. DIFF FIRST and decide from CONTENT.")
    print()
    if any('repo' in k for k in lanes):
        repo_key = next(k for k in lanes if 'repo' in k)
        print(f"  Likely canon: {repo_key} (repo is canon for files >50KB —")
        print("  the Drive/Zapier bus takes content as a tool PARAMETER, ~30-50KB")
        print("  ceiling, which is why the trunk froze for ten versions).")
    print()
    print("  Reconcile before touching this file. Two sessions writing one file")
    print("  is structural, not carelessness — one canon writes, others read.\n")
    return 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: python3 resolve_canon.py <filename>")
        sys.exit(2)
    sys.exit(resolve(sys.argv[1]))
