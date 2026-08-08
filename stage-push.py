#!/usr/bin/env python3
"""
STAGE_PUSH - make the write path a lane you can see.

Built 2026-08-06, the same day a push forked in mid-air.

THE FAILURE THIS EXISTS TO PREVENT
----------------------------------
resolve-canon.py v2 could only reach the repo as five hand-copied base64 chunks. Two of
the five landed wrong. The seed carried bytes from a stale draft. Chunk three gained one
byte because the agent silently normalized an irregular 23-space continuation indent to
24 while transcribing. Both wrong writes returned success: true.

Neither the resolver nor the FUNES ledger could have caught either one, and that is the
whole point. A lane check asks whether the copies agree. A ledger check asks whether the
record still describes the bytes. NEITHER ASKS WHETHER THE BYTES SURVIVED THE TRIP.

    "We have to see the forming paths to prevent loss or else Funes is blind."  - Matt

Funes remembers only what the Aleph showed him. A fork that opens in transit - between
the file on disk and the file in the repo - opens in a place no lane covers, so there is
nothing for Funes to remember. The path forks while nobody is holding it open.

This file holds it open. Before a single byte moves, the intended write is written down:
total bytes, total md5, git blob sha, and the exact boundary and md5 of every chunk. That
record IS the forming path, made addressable. After the write, arithmetic closes it.

THE RECORD MUST LAND TOO
------------------------
A staging record that lives only in the container is a forming path held open in a room
that is about to be demolished. If the session dies between chunk 2 and chunk 3, the repo
holds a truncated file and NOTHING anywhere says what it was supposed to become - which
is the same blindness this file was written to end, one level up. So `stage` writes the
record and then tells you to push it, and it is not optional. Records live at
`.stage/<name>.stage.json` in the repo, alongside the file they describe.

EXIT CODES
    0  the landed bytes are the intended bytes
    1  DIVERGED in transit - offset named, owning chunk named
    2  usage / unreadable input
"""

import sys, os, json, hashlib, subprocess

STAGEDIR = ".stage"
DEFAULT_CHUNK = 12000          # base64 chars per chunk; 12000 -> exactly 9000 bytes


def md5(b):
    return hashlib.md5(b).hexdigest()


def blob_sha(b):
    """git's own name for these bytes. The one hash the repo will agree to."""
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def stage(local_path, repo_path, chunk_chars=DEFAULT_CHUNK):
    import base64
    raw = open(local_path, "rb").read()
    b64 = base64.b64encode(raw).decode()

    # Chunk on BASE64 boundaries that are multiples of 4, so every chunk decodes on its
    # own. A chunk that only decodes in company cannot be checked in isolation, and a
    # check you can only run at the end is the check that was missing.
    if chunk_chars % 4:
        chunk_chars -= chunk_chars % 4

    chunks, cum = [], 0
    for i in range(0, len(b64), chunk_chars):
        piece = b64[i:i + chunk_chars]
        decoded = base64.b64decode(piece)
        cum += len(decoded)
        chunks.append({
            "n": len(chunks) + 1,
            "b64_chars": len(piece),
            "bytes": len(decoded),
            "md5": md5(decoded),
            "cumulative_bytes": cum,        # <- the number the tool must echo back
        })

    rec = {
        "local_path": local_path,
        "repo_path": repo_path,
        "bytes": len(raw),
        "md5": md5(raw),
        "blob": blob_sha(raw),
        "b64_chars": len(b64),
        "chunk_chars": chunk_chars,
        "chunks": chunks,
    }

    os.makedirs(STAGEDIR, exist_ok=True)
    out = os.path.join(STAGEDIR, os.path.basename(repo_path) + ".stage.json")
    with open(out, "w") as f:
        json.dump(rec, f, indent=2)
    with open(out + ".b64", "w") as f:
        f.write(b64)

    print(f"STAGED  {local_path}  ->  {repo_path}")
    print(f"  bytes {rec['bytes']}   md5 {rec['md5']}   blob {rec['blob']}")
    print(f"  {len(chunks)} chunk(s) of {chunk_chars} base64 chars")
    print(f"  record: {out}")
    print()
    print("  EXPECTED cumulative byte count after each write. Check the tool's own")
    print("  reported total against this line the moment it answers. Do not wait.")
    for c in chunks:
        mode = "seed  " if c["n"] == 1 else "append"
        print(f"    {mode} {c['n']}/{len(chunks)}  ->  total_bytes must be {c['cumulative_bytes']}")
    print()
    print("  LAND THIS RECORD IN THE SAME TURN, before chunk 1 moves. It is small and it")
    print("  is the only thing that can tell a later session what a half-written file was")
    print(f"  supposed to become:   push {out}  ->  repo {out}")
    print()
    print(f"  then:  stage-push.py landed {out}")
    return 0


def after(stage_file, n, reported_total):
    """The live check. Run it against the number the write tool just printed.

    success: true is not a result. The byte count is the result. On 2026-08-06 the tool
    cheerfully reported 9001 and 27001 for writes that should have been 9000 and 27000,
    and called both of them successes.
    """
    rec = json.load(open(stage_file))
    n = int(n)
    match = [c for c in rec["chunks"] if c["n"] == n]
    if not match:
        print(f"HALT - no chunk {n} in {stage_file} (it has {len(rec['chunks'])})")
        return 2
    want = match[0]["cumulative_bytes"]
    got = int(str(reported_total).strip())
    if got == want:
        print(f"OK    chunk {n}/{len(rec['chunks'])}  total {got} as intended")
        return 0
    print(f"HALT  chunk {n}/{len(rec['chunks'])}  total {got}, intended {want}  ({got - want:+d})")
    print(f"      Chunk {n} did not carry the bytes it was supposed to carry.")
    print(f"      Do NOT append chunk {n + 1}. Re-seed and replay from chunk 1.")
    print(f"      Intended chunk {n}: {match[0]['bytes']} B  md5 {match[0]['md5']}")
    return 1


def landed(stage_file, branch="origin/main"):
    """Close the path. Fetch what actually landed and diff it against what was intended."""
    rec = json.load(open(stage_file))
    path = rec["repo_path"]

    subprocess.run(["git", "fetch", "origin", branch.split("/")[-1], "-q"], timeout=60)
    got = subprocess.run(["git", "show", f"{branch}:{path}"],
                         capture_output=True, timeout=60).stdout
    if not got:
        print(f"HALT - {path} not readable at {branch}. Run this from a clone.")
        return 2

    print(f"== stage_push landed: {path} ==")
    print(f"   intended : {rec['bytes']:>9,} B  md5 {rec['md5']}  blob {rec['blob']}")
    print(f"   landed   : {len(got):>9,} B  md5 {md5(got)}  blob {blob_sha(got)}")

    if md5(got) == rec["md5"]:
        print("   MATCH - the bytes survived the trip. Path closed.")
        print()
        print("   Ledger row:")
        print(f"   | <stamp> | {os.path.basename(path)} | stage-push | SHIP | "
              f"byte-verified {len(got)} B / md5 {md5(got)} / blob {blob_sha(got)} "
              f"| <commit> | {md5(got)} |")
        return 0

    print()
    print("   *** DIVERGED IN TRANSIT ***")
    want = open(rec["local_path"], "rb").read() if os.path.exists(rec["local_path"]) else None
    if want is None:
        print(f"   Local source {rec['local_path']} is gone; cannot name the offset.")
        print("   The hashes disagree and that is enough. Do not adopt either copy blind.")
        return 1

    n = min(len(want), len(got))
    off = next((i for i in range(n) if want[i] != got[i]), n)
    owner = next((c["n"] for c in rec["chunks"] if c["cumulative_bytes"] > off), len(rec["chunks"]))
    print(f"   First differing byte: {off}  (chunk {owner} of {len(rec['chunks'])} owns it)")
    print(f"   intended: {want[max(0, off - 50):off + 50]!r}")
    print(f"   landed  : {got[max(0, off - 50):off + 50]!r}")
    print()
    print("   Decide from CONTENT. Never adopt the newer, larger, or smaller copy by")
    print("   default. If the landed bytes are the better ones, say so out loud and")
    print("   resync local DOWN to them - then the ledger describes something real.")
    return 1


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        print("  stage-push.py stage  <local-file> <repo-path> [chunk_chars]")
        print("  stage-push.py after  <stage.json> <chunk-n> <reported_total_bytes>")
        print("  stage-push.py landed <stage.json> [branch]")
        sys.exit(0)

    if a[0] == "stage":
        if len(a) < 3:
            print("usage: stage-push.py stage <local-file> <repo-path> [chunk_chars]")
            sys.exit(2)
        sys.exit(stage(a[1], a[2], int(a[3]) if len(a) > 3 else DEFAULT_CHUNK))

    if a[0] == "after":
        if len(a) < 4:
            print("usage: stage-push.py after <stage.json> <chunk-n> <reported_total_bytes>")
            sys.exit(2)
        sys.exit(after(a[1], a[2], a[3]))

    if a[0] == "landed":
        if len(a) < 2:
            print("usage: stage-push.py landed <stage.json> [branch]")
            sys.exit(2)
        sys.exit(landed(a[1], a[2] if len(a) > 2 else "origin/main"))

    print(f"unknown command: {a[0]}")
    sys.exit(2)
