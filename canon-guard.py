#!/usr/bin/env python3
"""
canon-guard.py — enforce ROLE-canon so a stale/superseded file can't be read as current.

WHY THIS EXISTS
---------------
resolve-canon.py resolves a NAME across the four lanes (repo/netlify/shelf) by md5 — the Warriors
rule (never ship the smaller stub). It CANNOT catch the class that keeps burning sessions: a role
served by the WRONG, differently-named file — the wired render-proof gate studio-eyes-sweep.py (v4)
vs the unwired studio-eyes/studio-eyes.py (v3); a wired preship-gate vN vs a newer unwired one; a
shelf index.html read as current. Those are different names, all legitimately in the repo. (Note:
which of two same-role files is canon is a DECLARATION derived from wiring + version, not an
inference from prose — declaring it backwards is itself the hazard.)

This guard reads canon-manifest.json (curated: role -> canonical + superseded) and HALTs when a
superseded file is USED or REFERENCED. Canon is DECLARED once, and INTENDED to be ENFORCED in CI.
STATUS 2026-07-26: NOW WIRED into floor.yml (this session could push the workflow; the handoff's
"needs workflow scope" claim was verified false here). It passes today (nothing declared
superseded); it bites once roles declare supersession.

HARDENED 2026-07-26 (red-team): recursive + boundary-aware ref scan (was non-recursive, code-only,
naked-substring); self-test now validates the real manifest schema AND runs the shipping scan on a
temp fixture (was synthetic-only). Prose .md/.html are intentionally OUT of the ref scan — a
filename in prose is not a live call. Residual limits (documented, WISH): indirect/`$VAR` and
`/tmp`-copy invocations, byte-identical unnamed duplicates, and accumulate-never-shed of the
manifest itself — see claude_convening-systems-2026-07-26.md (RED TEAM section).

USAGE
    canon-guard.py --self-test          gate the guard (schema + verdict + real-scan canaries; refuse on fail)
    canon-guard.py --wiring             per role, is the DECLARED canonical the WIRED one? HALT if not
    canon-guard.py --refs               scan repo for references to declared-superseded files; HALT
    canon-guard.py --workflows          YAML-parse every .github/workflows/*.yml; HALT on parse error
    canon-guard.py --check <file>       is <file> superseded for a role? print the canonical pointer
EXIT  0 clean · 1 HALT (superseded used/referenced, or unwired canonical) · 2 guard self-test failed
"""
import json, os, re, sys, glob, tempfile, contextlib, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "canon-manifest.json")
INDEX = os.path.join(ROOT, "claude_FUNES-INDEX.md")
BEGIN_MARK = "<!-- CANON:BEGIN"
END_MARK = "<!-- CANON:END -->"
STALE_DAYS = 90
# files that legitimately NAME a superseded file (the map + its own corrections); never flag these.
REF_EXEMPT = {"canon-manifest.json", "canon-guard.py", "claude_FUNES-INDEX.md",
              "claude_seat-playtesting-agents.md", "claude_cyl-playtest-table-2026-07-26.md",
              "claude_convening-systems-2026-07-26.md"}
# Recursive code/workflow/shell/js + known extensionless hooks. A live reference to a superseded
# file in any of these is a real bug. Prose (.md/.html) is deliberately excluded (a mention is not
# a call). REF_EXEMPT still applies on top of these.
REF_GLOBS = ["**/*.py", "**/*.sh", "**/*.yml", "**/*.js",
             ".github/workflows/*.yml",   # hidden dir: '**' glob skips dotdirs, so name it explicitly
             "founder-gate/*", "**/pre-push", "**/pre-commit", "**/post-*"]
# Enforce LIVE code, not the archive: a reference to a superseded file inside archived/rescued
# material is not a live bug (that code isn't running), and it is not wiring evidence either.
ARCHIVE_DIRS = {"rescued", "archive"}


def load(path=MANIFEST):
    with open(path) as f:
        return json.load(f)


def _iter_files(root):
    seen = set()
    for pat in REF_GLOBS:
        for path in glob.glob(os.path.join(root, pat), recursive=True):
            if not os.path.isfile(path):
                continue
            rel = os.path.relpath(path, root)
            if rel in seen or any(p in ARCHIVE_DIRS for p in rel.split(os.sep)):
                continue
            seen.add(rel)
            yield path, rel, os.path.basename(path)


def _mentions(text, basename):
    """A real reference to basename, not a substring of a longer name (gate.py != founder-gate.py).
    Path prefixes (/tmp/, ./) are allowed to precede; word/hyphen chars are not."""
    return re.search(r'(?<![\w-])' + re.escape(basename) + r'(?![\w-])', text) is not None


def superseded_map(manifest):
    """superseded filename (basename) -> (canonical, role, status)."""
    m = {}
    for r in manifest.get("roles", []):
        for s in r.get("superseded", []):
            m[os.path.basename(s)] = (r["canonical"], r["role"], r.get("status", ""))
    return m


def count_refs(basename, root=ROOT):
    """How many scanned files reference this basename (boundary-aware; excluding itself + exempt)."""
    n, where = 0, []
    for path, rel, b in _iter_files(root):
        if b in REF_EXEMPT or b == basename:
            continue
        try:
            if _mentions(open(path, encoding="utf-8", errors="replace").read(), basename):
                n += 1; where.append(rel)
        except Exception:
            pass
    return n, where


def check_file(name, manifest):
    sm = superseded_map(manifest)
    base = os.path.basename(name)
    if base in sm:
        canon, role, status = sm[base]
        print(f"  HALT — {base} is SUPERSEDED for role '{role}'. Canon = {canon}"
              + (f"  [{status}]" if status else ""))
        return 1
    print(f"  OK — {base} is not a declared-superseded file.")
    return 0


def scan_refs(manifest, root=ROOT):
    sm = superseded_map(manifest)
    if not sm:
        print("  (no superseded files declared — ENFORCING NOTHING here)")
        return 0
    hits = []
    for path, rel, b in _iter_files(root):
        if b in REF_EXEMPT:
            continue
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        except Exception:
            continue
        for supbase, (canon, role, _s) in sm.items():
            if b == supbase:
                continue
            for i, line in enumerate(lines, 1):
                if _mentions(line, supbase):
                    hits.append((rel, i, supbase, canon, role))
    if hits:
        print("  HALT — live references to SUPERSEDED files (fix to the canonical, or split the role):")
        for rel, i, sup, canon, role in hits:
            print(f"     {rel}:{i}  uses {sup}  ->  canon for '{role}' is {canon}")
        return 1
    print("  OK — no scanned file references a superseded file.")
    return 0


def wiring_verdict(canon_refs, sibling_refs):
    if canon_refs == 0 and any(s > 0 for s in sibling_refs):
        return "HALT"
    if canon_refs == 0:
        return "WARN"
    return "OK"


def wiring(manifest, root=ROOT):
    bad = 0
    for r in manifest.get("roles", []):
        print(f"  role: {r['role']}")
        canon = r["canonical"]
        cn, cw = count_refs(os.path.basename(canon), root)
        print(f"     [canonical] {canon}: {cn} ref(s)" + (f"  ({', '.join(cw[:4])})" if cw else "  — UNWIRED"))
        sib = []
        for s in r.get("siblings", []):
            sn, sw = count_refs(os.path.basename(s), root)
            sib.append(sn)
            print(f"     [sibling]   {s}: {sn} ref(s)" + (f"  ({', '.join(sw[:4])})" if sw else "  — UNWIRED"))
        v = wiring_verdict(cn, sib)
        if v == "HALT":
            print("     HALT — declared canonical is UNWIRED while a sibling is wired. The declaration "
                  "likely points at the wrong file (the exact error class of 2026-07-26). Re-declare from wiring.")
            bad += 1
        elif v == "WARN":
            print("     WARN — canonical unwired and no sibling wired (not-yet-wired, or a standalone/doc tool).")
        else:
            print(f"     OK — declared canonical is the wired one ({cn} ref(s)).")
    return 1 if bad else 0


# ---- the forcing loop: SSOT -> generated index -> CI checks it fresh -> decay sheds ----
def emit_index(manifest):
    """The downstream VIEW, generated from the SSOT. Hand-editing it is what rotted the old index."""
    out = [BEGIN_MARK + " — generated by `canon-guard.py --emit-index`; DO NOT hand-edit. Regenerate",
           "     when canon-manifest.json changes, or CI (`--check-index`) fails the build. -->",
           "", "| role | canonical | verified |", "|---|---|---|"]
    for r in manifest.get("roles", []):
        out.append(f"| {r['role']} | `{r['canonical']}` | {r.get('verified', '?')} |")
    out += ["", END_MARK]
    return "\n".join(out)


def _extract_block(text):
    i = text.find(BEGIN_MARK)
    j = text.find(END_MARK)
    return text[i:j + len(END_MARK)] if (i >= 0 and j >= 0) else None


def check_index(manifest, index_path=INDEX):
    """The forcing link: the committed index block MUST equal a fresh emit. Upstream change -> HALT
    until downstream regenerated. This is what makes an upstream edit NOTICEABLE."""
    want = emit_index(manifest).strip()
    try:
        have = _extract_block(open(index_path, encoding="utf-8").read())
    except Exception as e:
        print(f"  HALT — cannot read index {index_path}: {e}"); return 1
    if have is None:
        print(f"  HALT — no CANON block in {os.path.basename(index_path)}. Insert `canon-guard.py --emit-index`."); return 1
    if have.strip() != want:
        print(f"  HALT — the CANON block in {os.path.basename(index_path)} is STALE vs the manifest. "
              f"Regenerate: `python3 canon-guard.py --emit-index`, replace the block, commit."); return 1
    print(f"  OK — {os.path.basename(index_path)} CANON block matches the manifest (downstream in sync).")
    return 0


def stale(manifest, days=STALE_DAYS, today=None):
    """Decay/shed: a role not re-verified in `days` is flagged so the SSOT sheds. A NAG, not a HALT."""
    today = today or datetime.date.today()
    for r in manifest.get("roles", []):
        v = r.get("verified")
        if not v:
            print(f"  WARN — role '{r['role']}' has no 'verified' date; it can never age out. Add one."); continue
        try:
            age = (today - datetime.date.fromisoformat(v)).days
        except Exception:
            print(f"  WARN — role '{r['role']}' verified='{v}' is not YYYY-MM-DD."); continue
        if age > days:
            print(f"  STALE — role '{r['role']}' last verified {v} ({age}d > {days}d). Re-verify from wiring, or retire.")
        else:
            print(f"  ok — role '{r['role']}' verified {v} ({age}d).")
    return 0


def validate_schema(manifest):
    errs = []
    roles = manifest.get("roles")
    if not isinstance(roles, list):
        return ["'roles' is not a list"]
    names = []
    for r in roles:
        if not isinstance(r, dict):
            errs.append("a role is not an object"); continue
        nm = r.get("role"); names.append(nm)
        if not isinstance(nm, str):
            errs.append("a role is missing a string 'role' name")
        c = r.get("canonical")
        if not isinstance(c, str):
            errs.append(f"role {nm!r} is missing a string 'canonical'")
        for k in ("siblings", "superseded"):
            if k in r and not isinstance(r[k], list):
                errs.append(f"role {nm!r}.{k} is not a list")
        if isinstance(c, str) and (c in r.get("siblings", []) or c in r.get("superseded", [])):
            errs.append(f"role {nm!r}: canonical is listed in its own siblings/superseded")
    dups = sorted({x for x in names if names.count(x) > 1})
    if dups:
        errs.append(f"duplicate role names: {dups}")
    return errs


def self_test():
    # 1) the REAL manifest must be schema-valid (a malformed map silently under-enforces).
    try:
        real = load()
    except Exception as e:
        print(f"  SELF-TEST FAIL — manifest unreadable: {e}"); return 2
    errs = validate_schema(real)
    if errs:
        print("  SELF-TEST FAIL — manifest schema:")
        for e in errs:
            print("     " + e)
        return 2
    # 2) pure verdict canaries.
    if not (wiring_verdict(0, [2]) == "HALT" and wiring_verdict(3, [0]) == "OK"
            and wiring_verdict(0, [0]) == "WARN"):
        print("  SELF-TEST FAIL — wiring verdict logic."); return 2
    # 3) REAL-CODE canary: a temp tree with a planted stale ref in a SUBDIR must HALT via the
    #    shipping scan (exercises recursive glob + IO + boundary matching + verdict).
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "sub"))
        with open(os.path.join(td, "sub", "caller.sh"), "w") as f:
            f.write("#!/bin/sh\npython3 old-gate.py --run\n")
        fx = {"roles": [{"role": "canary", "canonical": "new-gate.py",
                         "siblings": ["old-gate.py"], "superseded": ["old-gate.py"]}]}
        buf = io_devnull()
        with contextlib.redirect_stdout(buf):
            refs_halt = scan_refs(fx, td)
            wire_halt = wiring(fx, td)
        # boundary: a look-alike must NOT match.
        with open(os.path.join(td, "sub", "decoy.sh"), "w") as f:
            f.write("python3 very-old-gate.py\n")   # contains 'old-gate.py' only as a substring
        with contextlib.redirect_stdout(buf):
            still = scan_refs({"roles": [{"role": "c", "canonical": "n.py",
                                          "superseded": ["old-gate.py"]}]}, td)
        if not (refs_halt == 1 and wire_halt == 1 and still == 1):
            print("  SELF-TEST FAIL — real-scan canary: subdir stale ref not caught by the shipping code.")
            return 2
    print("  SELF-TEST OK — manifest schema valid; verdict logic bites; recursive/boundary scan catches a planted stale ref.")
    return 0


def check_workflows():
    """YAML-parse every workflow file; HALT on a parse error — the gate that guards the gates.

    Born 2026-07-27: a colon-space in a floor.yml step NAME made an unquoted scalar parse as a
    nested map; the run died in 0s with 0 jobs (GitHub compiled the file and refused it). A broken
    workflow can't lint ITSELF in CI (it never runs), so the teeth are LOCAL: run this before any
    workflow push. In CI it still guards every OTHER workflow file and re-affirms parse on green.
    """
    try:
        import yaml
    except Exception as e:
        print(f"  NOTE — PyYAML absent ({e}); workflow lint skipped (CI has it). (exit 0)")
        return 0
    files = sorted(glob.glob(os.path.join(ROOT, ".github", "workflows", "*.yml")) +
                   glob.glob(os.path.join(ROOT, ".github", "workflows", "*.yaml")))
    if not files:
        print("  workflows: none found."); return 0
    bad = 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        try:
            with open(f, encoding="utf-8") as fh:
                yaml.safe_load(fh)
            print(f"  ok   {rel}")
        except Exception as e:
            bad += 1
            msg = (str(e).splitlines() or [e.__class__.__name__])[0]
            print(f"  HALT {rel} — YAML parse error: {msg}")
    print(f"\n  === workflow lint: {len(files)} file(s), {bad} broken ===")
    return 1 if bad else 0


def io_devnull():
    import io
    return io.StringIO()


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if self_test() == 2:
        return 2
    manifest = load()
    if not manifest.get("roles"):
        print("  NOTE — manifest declares NO roles: ENFORCING NOTHING (unconfigured, not 'clean').")
    if "--emit-index" in argv:
        print(emit_index(manifest)); return 0
    if "--check-index" in argv:
        return check_index(manifest)
    if "--stale" in argv:
        return stale(manifest)
    if "--wiring" in argv:
        return wiring(manifest)
    if "--refs" in argv:
        return scan_refs(manifest)
    if "--workflows" in argv:
        return check_workflows()
    if "--check" in argv:
        i = argv.index("--check")
        if i + 1 >= len(argv):
            print("  usage: canon-guard.py --check <file>"); return 2
        return check_file(argv[i + 1], manifest)
    print(__doc__.strip().splitlines()[0])
    print("  usage: --self-test | --wiring | --refs | --workflows | --check <file>")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
