#!/usr/bin/env python3
"""
STALE FUSE  ·  Tight Spiral Studios  ·  stored state that knows when it rotted
==============================================================================
TSP-ROLE: stored-state staleness fuse
TSP-SUPERSEDES: (none)

Founder ruling 2026-08-17: "Go. configure with teeth."

WHY THIS EXISTS
---------------
`canon-manifest.json` declared `preship-gate-v4.py` canonical for the pre-ship
role while `preship-gate-v5.py` shipped in main saying, in its own docstring, that
it superseded v4. The manifest was correct on 2026-07-26 and rotted in three weeks
without anyone doing anything wrong. The guard against reading stale files as
current was itself stale.

Then it was measured across the repo: **18 stored-state files, 0 carrying any
fingerprint of the inputs they were derived from.** Not one could answer "is the
corpus I describe still the corpus that exists?" This is not a bad file. It is a
class with eighteen members.

A file read as current with no way to know it is stale answers confidently with old
data forever. This fuse does not make anything correct. It makes wrongness LOUD,
which is the whole difference between the arcade quietly violating its own gate for
eight days and the gate saying so on day one.

THREE KINDS OF STORED STATE, AND THEY GET DIFFERENT TEETH
---------------------------------------------------------
Fusing everything identically would build an alarm that screams every session, and
an auditor that cries wolf trains the founder to ignore it (the comfort-gate
doctrine). So the fuse distinguishes what it is guarding:

  REGISTRY  - a DERIVED assertion about what is canonical right now.
              canon-manifest, canon-vocab.
              These change rarely and being wrong is expensive.
              *** DRIFT IS A HALT. ***

  POLICY    - hand-authored rules, derived from nothing.
              lane-tendrils, retired-lines, blindspots, taxonomies.
              A digest over a glob here would be theatre: no corpus change can
              make a human's ruling stale. Fused for AUDIT only, so the file is
              accounted for and its age is visible.
              *** NO DIGEST TEETH, BY HONEST DESIGN. ***

  BASELINE  - a snapshot of measured debt at one moment.
              the *-baseline files, gate-baseline, ledgers.
              Drift here is NORMAL: the corpus moved, so the snapshot aged. Halting
              on that would fire on every commit and teach everyone to ignore it.
              *** DRIFT IS REPORTED, NOT HALTED. *** What matters is that it is
              regenerable and that the drift is visible.

THE FUSE BLOCK
--------------
    "_fuse": {
      "kind":      "registry" | "baseline" | "policy",
      "mode":      "names" | "content" | "none",
      "inputs":    ["*.py", "*.sh"],       globs, or explicit paths
      "digest":    "<sha256 over the inputs>",
      "generated": "2026-08-17",
      "regen":     "canon-guard.py --refresh"   (optional, how to rebuild it)
    }

The digest is sha256 over sorted `path\0sha256(bytes)` lines for every file the
globs resolve to. The fused file never digests itself.

HONEST LIMITS, stated rather than implied:
  - The fuse proves the INPUTS moved. It cannot prove the file's CONTENT is wrong,
    and a file can be wrong the day it is written with a perfectly fresh digest.
  - Globs are declared by whoever stamps. A wrong glob makes a fuse that never
    fires or always fires; `--verify` prints the resolved input count so a glob
    matching 0 files is visible rather than silently green.
  - Renames register as drift, which is correct but can surprise.

Usage:
  stale-fuse.py --stamp <file.json> --kind registry|baseline|policy --inputs "*.py,*.sh" [--regen "..."]
  stale-fuse.py --verify <file.json> [more ...]     exit 1 if a REGISTRY drifted
  stale-fuse.py --verify --all                      every fused file in the repo
  stale-fuse.py --audit                             list stored state with NO fuse
  stale-fuse.py --selftest                          prove the teeth still bite
"""
import sys, os, json, glob, hashlib, datetime, tempfile, shutil

SELF = os.path.basename(__file__)


def _files_for(inputs, exclude):
    out = set()
    for pat in inputs:
        if any(c in pat for c in '*?['):
            for p in glob.glob(pat, recursive=True):
                if os.path.isfile(p):
                    out.add(os.path.normpath(p))
        elif os.path.isfile(pat):
            out.add(os.path.normpath(pat))
    out.discard(os.path.normpath(exclude))
    return sorted(out)


def digest_of(inputs, exclude, mode="content"):
    """
    mode="content"  every byte of every input. Right for a BASELINE, which measures
                    what the files SAY.
    mode="names"    the sorted file list only. Right for a REGISTRY OF FILES, which
                    asserts WHICH file holds a role. Editing a tool's body does not
                    change which tool is canonical; adding, removing or renaming one
                    does. Digesting contents here made the registry drift on every
                    commit that touched any script, which is a gate that cries wolf.
    """
    files = _files_for(inputs, exclude)
    h = hashlib.sha256()
    for p in files:
        h.update(p.encode('utf-8'))
        h.update(b'\0')
        if mode == "content":
            with open(p, 'rb') as f:
                h.update(hashlib.sha256(f.read()).hexdigest().encode('ascii'))
        h.update(b'\n')
    return h.hexdigest(), len(files)


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def stamp(path, kind, inputs, regen=None, today=None, mode=None):
    if kind not in ('registry', 'baseline', 'policy'):
        print("  kind must be registry, baseline or policy"); return 2
    d = load(path)
    if not isinstance(d, dict):
        print("  %s is not a JSON object; cannot carry a fuse" % path); return 2
    if mode is None:
        mode = "names" if kind == "registry" else "content"
    if kind == 'policy':
        dg, n, inputs, mode = "", 0, [], "none"
    else:
        dg, n = digest_of(inputs, path, mode)
    fuse = {
        "kind": kind,
        "mode": mode,
        "inputs": inputs,
        "digest": dg,
        "generated": today or datetime.date.today().isoformat(),
    }
    if regen:
        fuse["regen"] = regen
    d["_fuse"] = fuse
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("  stamped %-28s kind=%-8s mode=%-7s inputs=%s -> %d file(s)  %s"
          % (path, kind, mode, ','.join(inputs) or "(hand-authored)", n, dg[:12] or "no-digest"))
    if n == 0 and kind != 'policy':
        print("     WARNING: the glob resolved to 0 files. This fuse can never fire.")
    return 0


def verify(paths, quiet=False):
    halts, drifted, unfused = [], [], []
    for p in paths:
        try:
            d = load(p)
        except Exception as e:
            print("  UNPARSEABLE %s (%s)" % (p, e)); halts.append(p); continue
        fuse = d.get("_fuse") if isinstance(d, dict) else None
        if not fuse:
            unfused.append(p); continue
        if fuse.get("kind") == "policy":
            if not quiet:
                print("  POLICY  %-28s hand-authored, no inputs to drift (stamped %s)"
                      % (p, fuse.get("generated", "?")))
            continue
        dg, n = digest_of(fuse.get("inputs", []), p, fuse.get("mode", "content"))
        fresh = (dg == fuse.get("digest"))
        kind = fuse.get("kind", "baseline")
        if fresh:
            if not quiet:
                print("  FRESH   %-28s %s/%s over %d file(s)" % (p, kind, fuse.get("mode","content"), n))
        else:
            drifted.append((p, kind, fuse, n))
            tag = "STALE-HALT" if kind == "registry" else "drifted"
            print("  %-10s %-28s %s over %d file(s), generated %s"
                  % (tag, p, kind, n, fuse.get("generated", "?")))
            if fuse.get("regen"):
                print("             regenerate with: %s" % fuse["regen"])
            if kind == "registry":
                halts.append(p)
            if n == 0:
                print("             NOTE: glob resolved to 0 files, the fuse is toothless")
    return halts, drifted, unfused


def audit():
    """Stored state carrying no fuse at all: a claim with no expiry date."""
    missing = []
    for p in sorted(glob.glob("*.json")):
        try:
            d = load(p)
        except Exception:
            continue
        if isinstance(d, dict) and "_fuse" in d:
            continue
        missing.append(p)
    print("STALE FUSE - audit of stored state without a fuse")
    print("=" * 62)
    if not missing:
        print("  every stored-state file in the root carries a fuse.")
    else:
        for p in missing:
            print("  NO FUSE  %s" % p)
        print("\n  %d file(s) are claims with no expiry date." % len(missing))
    return 0


def selftest():
    """
    Live end-to-end, not a static fixture: stamp a real file over a real input,
    prove FRESH, mutate the input, prove the registry HALTs and the baseline does
    not. A gate that stops false-positiving by going blind is broken the other way.
    """
    print("STALE FUSE - selftest")
    print("=" * 62)
    tmp = tempfile.mkdtemp(prefix="fuse-selftest-")
    cwd = os.getcwd()
    ok = True
    try:
        os.chdir(tmp)
        with open("subject.txt", "w") as f:
            f.write("original\n")
        for name, kind in (("reg.json", "registry"), ("base.json", "baseline")):
            with open(name, "w") as f:
                json.dump({"note": "state"}, f)
            stamp(name, kind, ["sub*.txt"])

        h, d, _ = verify(["reg.json", "base.json"], quiet=True)
        print("  [1] unchanged        -> no halt, no drift:        %s"
              % ("OK" if not h and not d else "FAIL"))
        ok &= not h and not d

        # CONTENT changes: a baseline measures what files say, a registry of files
        # only asserts WHICH file holds a role. Editing a tool must not halt a push.
        with open("subject.txt", "w") as f:
            f.write("MUTATED\n")
        h, d, _ = verify(["reg.json", "base.json"], quiet=True)
        names = [x[0] for x in d]
        print("  [2] content edited   -> baseline drifts:          %s"
              % ("OK" if "base.json" in names else "FAIL"))
        print("  [3] content edited   -> registry does NOT drift:  %s"
              % ("OK" if "reg.json" not in names else "FAIL"))
        print("  [4] content edited   -> nothing halts:            %s"
              % ("OK" if not h else "FAIL"))
        ok &= ("base.json" in names) and ("reg.json" not in names) and not h

        # NAME-SET changes: a tool lands or is renamed. THIS is what invalidates a
        # registry, and it is the exact event that made canon-manifest.json wrong.
        with open("subject2.txt", "w") as f:
            f.write("a new tool landed\n")
        h, d, _ = verify(["reg.json", "base.json"], quiet=True)
        print("  [5] file added       -> registry HALTs:           %s"
              % ("OK" if "reg.json" in h else "FAIL"))
        print("  [6] file added       -> baseline still no halt:   %s"
              % ("OK" if "base.json" not in h else "FAIL"))
        ok &= ("reg.json" in h) and ("base.json" not in h)

        with open("empty.json", "w") as f:
            json.dump({"x": 1}, f)
        stamp("empty.json", "registry", ["nothing-matches-*.zzz"])
        print("  [7] empty-glob fuse flagged at stamp time (WARNING above)")

        dd = load("reg.json")
        print("  [8] original keys preserved:                      %s"
              % ("OK" if dd.get("note") == "state" else "FAIL"))
        ok &= dd.get("note") == "state"
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nSELFTEST: %s" % ("teeth still bite" if ok else "BROKEN"))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    if argv[0] == "--selftest":
        return selftest()
    if argv[0] == "--audit":
        return audit()

    if argv[0] == "--stamp":
        path = argv[1]
        kind = argv[argv.index("--kind") + 1] if "--kind" in argv else "baseline"
        raw = argv[argv.index("--inputs") + 1] if "--inputs" in argv else ""
        regen = argv[argv.index("--regen") + 1] if "--regen" in argv else None
        inputs = [s.strip() for s in raw.split(",") if s.strip()]
        if not inputs:
            print("  --inputs is required"); return 2
        mode = argv[argv.index("--mode") + 1] if "--mode" in argv else None
        return stamp(path, kind, inputs, regen, mode=mode)

    if argv[0] == "--verify":
        rest = argv[1:]
        if not rest or rest[0] == "--all":
            paths = sorted(glob.glob("*.json"))
        else:
            paths = rest
        print("STALE FUSE  ·  stored state that knows when it rotted")
        print("=" * 62)
        halts, drifted, unfused = verify(paths)
        if unfused:
            print("\n  %d file(s) carry no fuse (run --audit): %s"
                  % (len(unfused), ", ".join(unfused[:6]) + (" ..." if len(unfused) > 6 else "")))
        if halts:
            print("\n=== HALT: %d REGISTRY file(s) describe a corpus that has moved. ===" % len(halts))
            print("    A registry asserts what is canonical NOW. Regenerate it or")
            print("    re-stamp it deliberately; do not read it as current.")
            return 1
        if drifted:
            print("\n  %d baseline(s) drifted. Expected as the corpus moves; regenerate when convenient." % len(drifted))
        return 0

    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
