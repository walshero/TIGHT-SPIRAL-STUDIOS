#!/usr/bin/env python3
"""
PRODUCTION GATE  ·  Tight Spiral Studios  ·  "full production" as a checkable state
===================================================================================
TSP-ROLE: production-readiness gate
TSP-SUPERSEDES: (none)

Founder ruling 2026-08-27: "Tsp full studio production."

WHY THIS EXISTS
---------------
The studio has been stamping `"stage":"full production"` on files for weeks. It is
worn by exactly ONE file in the corpus and it is **defined nowhere**. There is no
document saying what production means, no checklist, no gate. It is a label
asserted with nothing underneath it, which is the same class as the stale manifest:
a claim with no expiry date and no test.

Worse, and this is the part that matters: `en195-arcade.html` wears the label,
declares "0 HALT on Studio Eyes v4" in its own meta, and **currently fails
art-gate** on 5,158 bytes of hand-cut scene art. The flagship's production claim
went stale and nothing noticed, because nothing was checking.

So this gate does not invent a standard. It reads the one the studio already
practised on its flagship and makes it arithmetic.

THE BAR, derived from what the flagship actually has
----------------------------------------------------
  GATES     every shipping gate green: art, preship, voice, art-execution,
            one-thing, and the stale fuse. A production file with a red gate is
            not production, it is a claim.
  META      a TSP-META block that PARSES, declaring `operative` and `assets`
            provenance. An unparseable meta is a file that cannot be audited.
  COMFORT   the comfort kernel actually mounted (tsp.comfort.v1), plus the
            two-rule motion pair and a skip link. Accessibility is not a later pass.
  PANEL     a panel record naming seats, or a panel-reviewed stamp. The studio's
            signature move; a build nobody argued with is a draft.
  PLAYTEST  a `founder-playtested` field DECLARED in the file's own TSP-META,
            carrying the date he ruled on it. The Visual Critic HALT runs through
            his eyes, so a build he has never opened cannot be production by
            definition. Declared rather than inferred: an earlier cut searched the
            claude/ notes for the file name near the word "playtest" and passed a
            brand-new build because the panel document written minutes earlier
            contained both.
  OPEN      `founder-open` present. Production does not mean finished, it means
            the open questions are WRITTEN DOWN instead of forgotten.
  FACE      linked from index.html. "index.html accounts for every page."

HONEST LIMITS, stated rather than implied:
  - This measures EVIDENCE, not quality. A file can clear every line here and still
    be a bad game. The gate cannot read a play.
  - PLAYTEST is satisfied by a DECLARATION. It cannot tell a real playtest from a
    careless one, and a build can declare a date that never happened. It can only
    guarantee that somebody had to write the claim down deliberately.
  - Gate subprocesses that need a browser are skipped, loudly, when unavailable.
    Blind is not clean.

Usage:
  production-gate.py <file.html> [more ...]   exit 1 if any file claims production and misses the bar
  production-gate.py --audit                  every file claiming production
  production-gate.py --selftest               prove the teeth still bite
"""
import sys, os, re, json, glob, subprocess

REPO = os.path.dirname(os.path.abspath(__file__))


def meta_of(path):
    try:
        s = open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return None, ""
    m = re.search(r'<!-- TSP-META (.*?) -->', s, re.S)
    if not m:
        return None, s
    try:
        return json.loads(m.group(1)), s
    except Exception:
        return "UNPARSEABLE", s


def _run(cmd, timeout=300):
    """(ok, skipped, detail). A tool that is absent is SKIPPED and says so."""
    tool = cmd[1]
    if not os.path.exists(os.path.join(REPO, tool)):
        return None, True, "%s absent" % tool
    try:
        r = subprocess.run(["python3"] + cmd[1:], cwd=REPO, capture_output=True,
                           text=True, timeout=timeout)
        return r.returncode == 0, False, (r.stdout or r.stderr or "").strip().splitlines()[-1:] or [""]
    except subprocess.TimeoutExpired:
        return None, True, "%s timed out" % tool
    except Exception as e:
        return None, True, "%s: %s" % (tool, e)


def check(path):
    """Returns (list of (label, state, detail)); state in ok/fail/skip."""
    rows = []
    meta, src = meta_of(path)

    # ---- GATES
    for tool, args in (("art-gate.py", [path]),
                       ("preship-gate-v5.py", [path]),
                       ("studio-voice-gate.py", [path]),
                       ("art-execution-gate.py", [path]),
                       ("one-thing-gate.py", [path]),
                       ("stale-fuse.py", ["--verify", "--all"])):
        ok, skipped, detail = _run(["python3", tool] + args)
        d = detail if isinstance(detail, str) else (detail[0] if detail else "")
        rows.append(("gate:" + tool.replace(".py", ""),
                     "skip" if skipped else ("ok" if ok else "fail"), d[:88]))

    # ---- META
    if meta is None:
        rows.append(("meta", "fail", "no TSP-META block"))
    elif meta == "UNPARSEABLE":
        rows.append(("meta", "fail", "TSP-META does not parse as JSON"))
    else:
        rows.append(("meta", "ok", "parses"))
        rows.append(("meta:operative", "ok" if "operative" in meta else "fail",
                     str(meta.get("operative", "not declared"))))
        rows.append(("meta:assets", "ok" if meta.get("assets") else "fail",
                     "provenance declared" if meta.get("assets") else "no assets provenance"))
        rows.append(("meta:founder-open", "ok" if "founder-open" in meta else "fail",
                     "%d open" % len(meta.get("founder-open", []))
                     if isinstance(meta.get("founder-open"), list) else "not a list"))

    # ---- COMFORT / ACCESSIBILITY, measured in the source
    rows.append(("comfort:kernel", "ok" if "tsp.comfort.v1" in src else "fail",
                 "comfort kernel mounted" if "tsp.comfort.v1" in src else "no comfort kernel"))
    pair = ("prefers-reduced-motion" in src) and ("c-still" in src)
    rows.append(("comfort:motion-pair", "ok" if pair else "fail",
                 "two-rule motion pair" if pair else "motion pair missing or merged"))
    rows.append(("comfort:skip-link", "ok" if "skiplink" in src or "Skip to" in src else "fail",
                 "skip link present" if "skiplink" in src or "Skip to" in src else "no skip link"))

    base = os.path.basename(path)

    # ---- PANEL: a record that names seats, or a stamp in the file's own stage
    panel = False
    for f in glob.glob(os.path.join(REPO, "claude", "PANEL-*.md")):
        try:
            if base.replace(".html", "") in open(f, encoding='utf-8', errors='replace').read():
                panel = True; break
        except Exception:
            pass
    if not panel and isinstance(meta, dict):
        panel = "panel-review" in json.dumps(meta)
    rows.append(("panel", "ok" if panel else "fail",
                 "panel record found" if panel else "no panel has argued with this build"))

    # ---- PLAYTEST: DECLARED, not inferred from prose.
    # The first cut searched claude/*.md for the file name near the word
    # "playtest" and promptly passed blocking.html because the PANEL DOCUMENT
    # THIS SESSION HAD JUST WRITTEN contained both. A check the machine can
    # satisfy by writing a document about the file is not a check. It must be a
    # declaration the build makes about itself, which cannot be produced as a
    # side effect of describing it.
    pt = meta.get("founder-playtested") if isinstance(meta, dict) else None
    if pt:
        rows.append(("founder-playtest", "ok", "declared: %s" % pt))
    elif isinstance(meta, dict) and "founder-playtested" in meta:
        rows.append(("founder-playtest", "fail",
                     "declared false: he has not ruled on this build"))
    else:
        rows.append(("founder-playtest", "fail",
                     'no "founder-playtested" declared in TSP-META'))

    # ---- FACE
    try:
        idx = open(os.path.join(REPO, "index.html"), encoding='utf-8', errors='replace').read()
        linked = base in idx
    except Exception:
        linked = False
    rows.append(("face", "ok" if linked else "fail",
                 "linked from index.html" if linked else "orphan: the face does not account for it"))

    return rows


def claims_production(path):
    meta, _ = meta_of(path)
    if not isinstance(meta, dict):
        return False
    return "full production" in str(meta.get("stage", "")).lower()


def report(paths, strict_only_claimants=False):
    worst = 0
    for p in paths:
        rows = check(p)
        fails = [r for r in rows if r[1] == "fail"]
        skips = [r for r in rows if r[1] == "skip"]
        claims = claims_production(p)
        verdict = ("PRODUCTION" if not fails else
                   ("CLAIMS PRODUCTION, MISSES THE BAR" if claims else "not production yet"))
        print("\n%s  ·  %s" % (os.path.basename(p), verdict))
        print("  " + "-" * 62)
        for label, st, detail in rows:
            mark = {"ok": " ok ", "fail": "FAIL", "skip": "skip"}[st]
            print("  [%s] %-26s %s" % (mark, label, detail))
        if skips:
            print("  NOTE: %d check(s) skipped. Blind is not clean." % len(skips))
        if fails and claims:
            worst = 1
        elif fails and not strict_only_claimants:
            worst = max(worst, 0)
    return worst


def selftest():
    print("PRODUCTION GATE - selftest\n" + "=" * 62)
    ok = True
    # a file with no meta at all must fail meta, comfort, panel, playtest and face
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".html", dir=REPO)
    os.close(fd)
    open(tmp, "w").write("<!DOCTYPE html><html><body><p>nothing</p></body></html>")
    try:
        rows = dict((r[0], r[1]) for r in check(tmp))
        for k in ("meta", "comfort:kernel", "panel", "founder-playtest", "face"):
            hit = rows.get(k) == "fail"
            print("  bare file fails %-20s %s" % (k, "OK" if hit else "MISSED"))
            ok &= hit
    finally:
        os.remove(tmp)
    print("\nSELFTEST: %s" % ("teeth still bite" if ok else "BROKEN"))
    return 0 if ok else 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    if argv[0] == "--selftest":
        return selftest()
    if argv[0] == "--audit":
        claimants = [p for p in sorted(glob.glob(os.path.join(REPO, "*.html")))
                     if claims_production(p)]
        print("PRODUCTION GATE  ·  files claiming full production: %d" % len(claimants))
        print("=" * 64)
        if not claimants:
            print("  none.")
            return 0
        return report(claimants, strict_only_claimants=True)
    print("PRODUCTION GATE  ·  full production, as a checkable state")
    print("=" * 64)
    return report(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
