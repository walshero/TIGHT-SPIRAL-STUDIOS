#!/usr/bin/env python3
"""
founder-vision.py - MENARD's instrument. Founder vision, computed against the repo.

Seat spec: claude_seat-founder-scribe.md. Built 2026-10-10.

WHY THIS EXISTS
---------------
founder-canon.md (2026-07) was one heroic sweep, written as prose. It cannot tell
you which of the founder's rulings a build now honours, ignores, or breaks, and it
cannot tell you which chats were never read. A sweep that does not log its own
coverage reads as complete. IF A RULE CAN'T BE A CHECK, IT'S A WISH.

THREE FILES, ONE DIRECTION OF TRUST  (all under founder-vision/)
-----------------------------------
utterances.jsonl  RAW. Founder turns ("H:" / "Human:") lifted from chat dumps by
                  machine, system-reminders stripped, nothing else touched.
                  Append-only, dedup by text hash. This is primary source.
coverage.json     ROSTER. Every TSP chat ever enumerated, and how deeply it has
                  been read: UNSWEPT < SUMMARY < SNIPPET < READ. Unswept chats are
                  named in every report. Silence is never agreement.
vision.jsonl      CURATED. One row per founder ruling / vision / naming / refusal.
                  Every row must cite >=1 utterance id whose text contains the
                  row's verbatim quote BYTE FOR BYTE. A row whose quote is not in
                  the raw corpus is a machine paraphrase and fails --validate.

STATUS IS COMPUTED, NEVER STORED
--------------------------------
For each vision row, against the working tree:
  CONTRADICTED  a must_not pattern hits a file in scope   (the build breaks it)
  LANDED        every path exists and every must pattern hits
  PARTIAL       some of the evidence is present
  ABSENT        none of it is present                     (vision with no build)
  UNCHECKABLE   the row carries no check                  (a wish; counted)
  SUPERSEDED    a later row names it in supersedes

USAGE
-----
  founder-vision.py ingest <dump>...           # parse recent_chats / read_conversation /
                                               #   conversation_search output
  founder-vision.py validate                   # schema + verbatim-provenance arithmetic
  founder-vision.py diff [--write]             # whole-studio report
  founder-vision.py brief <build.html>         # what the founder said that governs this
                                               #   file; exit 1 if it contradicts any
  founder-vision.py coverage                   # roster depth, unswept chats by name

EXIT  0 ok | 1 contradiction or validation failure | 2 usage
"""
import sys, os, re, json, glob, html, hashlib, fnmatch, argparse, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(ROOT, "founder-vision")
UTT = os.path.join(D, "utterances.jsonl")
COV = os.path.join(D, "coverage.json")
VIS = os.path.join(D, "vision.jsonl")
EXC = os.path.join(D, "excluded.json")   # {sha: reason}; text is never kept
LOCK = os.path.join(D, "CORPUS.lock")
# PRIVACY: every file in this repo is a public URL (.gitignore header). The raw
# corpus (utterances, coverage, excluded) is the founder's chat words and chat
# titles, so it lives in a PRIVATE lane (Drive walshero/Claude_files/founder-vision/)
# and is gitignored. Shelf holds the corpus byte-exact (project_write local_path). Only the curated vision rows and CORPUS.lock (hashes) are public.
PRIVATE = [UTT, COV, EXC]
REPORT = os.path.join(ROOT, "reports", "founder-vision-latest.md")

DEPTH = ["UNSWEPT", "SUMMARY", "SNIPPET", "PARTIAL", "READ"]
KINDS = {"ruling", "vision", "naming", "refusal", "preference", "question"}
SKIP_DIRS = {".git", "rescued", "archive", "aleph-runs", "node_modules",
             "founder-vision", "shelf-rescue-2026-09-28", "reports"}
# Files that QUOTE the founder cannot count as evidence that a build HONOURS him.
# Without this the report satisfies its own checks (found 2026-10-10: the goo row
# went LANDED because this report quoted the word "goo").
SELF_QUOTING = {"founder-vision.py", "claude_seat-founder-scribe.md", "founder-canon.md",
                "FUNES-LEDGER.md", "claude/FUNES-LEDGER.md"}
TEXT_EXT = (".html", ".md", ".js", ".py", ".json", ".css", ".txt", ".sh", ".mjs")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def h12(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def read_jsonl(p):
    if not os.path.exists(p):
        return []
    out = []
    for n, line in enumerate(open(p, encoding="utf-8"), 1):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"HALT {os.path.basename(p)} line {n}: {e}")
    return out


def load_cov():
    if os.path.exists(COV):
        return json.load(open(COV, encoding="utf-8"))
    return {"note": "Roster of TSP project chats. depth: " + " < ".join(DEPTH), "chats": {}}


# --------------------------------------------------------------------- ingest
CHAT_RE = re.compile(r"<chat url='(https://claude\.ai/chat/[0-9a-f-]{36})' updated_at='([^']+)'"
                     r"(?:[^>]*kind='(\w+)')?[^>]*>(.*?)</chat>", re.S)
FAILED_RE = re.compile(r"<!--\s*FAILED\s+(https://claude\.ai/chat/[0-9a-f-]{36})")
# Never let a credential the founder once pasted into a chat ride into the repo.
# Same patterns as secret-scan-gate.py; redacted at ingest, so no lane ever holds it.
SECRET_RES = [re.compile(p) for p in (
    r"\bghp_[A-Za-z0-9]{30,}\b", r"\bgithub_pat_[A-Za-z0-9_]{40,}\b",
    r"\bgho_[A-Za-z0-9]{30,}\b", r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b",
    r"\bAKIA[0-9A-Z]{16}\b", r"\bsk-[A-Za-z0-9_-]{32,}\b",
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    r"\beyJhbGciOiJ[A-Za-z0-9_-]{10,}[A-Za-z0-9._-]*")]


EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")


def plain(t):
    """Studio rule: no emoji, ever. Chat titles sometimes carry one; strip it."""
    return EMOJI_RE.sub("", t).strip()


def redact(t):
    n = 0
    for rx in SECRET_RES:
        t, k = rx.subn("[REDACTED-SECRET]", t)
        n += k
    return t, n


REMINDER_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
TURN_RE = re.compile(r"(?:^|\n)(H|A|Human|Assistant):[ \t]?", re.S)


def clean(t):
    t = html.unescape(t)
    t = REMINDER_RE.sub("", t)
    return t.strip()


def founder_turns(body):
    """Return the text of every Human turn in a snippet. Text before the first
    speaker label is unattributable and is dropped (could be either speaker)."""
    body = html.unescape(body)
    parts = TURN_RE.split(body)
    out = []
    # parts = [pre, label, text, label, text, ...]
    for i in range(1, len(parts) - 1, 2):
        if parts[i] in ("H", "Human"):
            t = clean(parts[i + 1])
            if t:
                out.append(t)
    return out


def load_dump(path):
    raw = open(path, encoding="utf-8").read()
    if raw.lstrip().startswith("["):
        try:
            raw = "\n".join(b.get("text", "") for b in json.loads(raw))
        except Exception:
            pass
    return raw


def ingest(paths):
    cov = load_cov()
    seen = {u["sha"] for u in read_jsonl(UTT)}
    excluded = json.load(open(EXC)) if os.path.exists(EXC) else {}
    seen |= set(excluded)
    new_u, touched, redacted = [], 0, 0
    for p in paths:
        raw = load_dump(p)
        failed = set(FAILED_RE.findall(raw))
        for url, upd, kind, body in CHAT_RE.findall(raw):
            title = plain((re.search(r"Title:\s*(.+)", body) or [None, ""])[1])
            turns = founder_turns(body)
            if kind == "read" and url in failed:
                depth = "PARTIAL"       # harvester stopped mid-chat (rate limit etc.)
            elif kind == "read":
                depth = "READ"          # whole chat paged by a harvester
            elif turns:
                depth = "SNIPPET"       # listing excerpt only
            else:
                depth = "SUMMARY"       # model-written summary only; never cited
            c = cov["chats"].setdefault(url, {"title": title, "updated_at": upd, "depth": "UNSWEPT"})
            if title and not c.get("title"):
                c["title"] = title
            c["updated_at"] = max(c.get("updated_at", ""), upd)
            if DEPTH.index(depth) > DEPTH.index(c["depth"]):
                c["depth"] = depth
            c["last_ingest"] = now()
            touched += 1
            for t in turns:
                t, k = redact(t)
                redacted += k
                s = h12(t)
                if s in seen:
                    continue
                seen.add(s)
                new_u.append({"id": "u-" + s, "sha": s, "chat_url": url, "chat_title": title,
                              "chat_updated_at": upd, "text": t, "ingested_at": now(),
                              "fidelity": "transcribed" if kind == "read" else "machine-exact",
                              "source_dump": os.path.basename(p)})
    os.makedirs(D, exist_ok=True)
    with open(UTT, "a", encoding="utf-8") as f:
        for u in new_u:
            f.write(json.dumps(u, ensure_ascii=False) + "\n")
    with open(COV, "w", encoding="utf-8") as f:
        json.dump(cov, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"ingest: {touched} chat records, {len(new_u)} new founder utterances, "
          f"roster now {len(cov['chats'])} chats, {redacted} secrets redacted")
    return 0


def exclude(uid, reason):
    """Remove a founder turn from the corpus for good (privacy, a third party's words,
    a pasted machine reply). Only the hash and the reason are kept, so re-ingest skips it."""
    rows = read_jsonl(UTT)
    keep = [u for u in rows if u["id"] != uid]
    if len(keep) == len(rows):
        sys.exit(f"HALT {uid} not in utterances.jsonl")
    exc = json.load(open(EXC)) if os.path.exists(EXC) else {}
    exc[uid[2:]] = reason
    json.dump(exc, open(EXC, "w"), indent=1, sort_keys=True)
    with open(UTT, "w", encoding="utf-8") as f:
        for u in keep:
            f.write(json.dumps(u, ensure_ascii=False) + "\n")
    print(f"excluded {uid}: {reason}")
    return 0


def mark(url, depth):
    cov = load_cov()
    if url not in cov["chats"]:
        sys.exit(f"HALT {url} is not on the roster; ingest a listing first")
    c = cov["chats"][url]
    if DEPTH.index(depth) > DEPTH.index(c["depth"]):
        c["depth"] = depth
    c["last_ingest"] = now()
    json.dump(cov, open(COV, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"{url} -> {c['depth']}")
    return 0


# ------------------------------------------------------------------- validate
REQ = ("id", "kind", "said_at", "verbatim", "utterance_ids", "subject", "principle")


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lock():
    out = {"written": now(), "lane": "project shelf founder-vision/ (utterances.jsonl, excluded.json, coverage-depth.json); Drive walshero/Claude_files/founder-vision/ holds excluded.json",
           "files": {}}
    for p in PRIVATE:
        if os.path.exists(p):
            out["files"][os.path.basename(p)] = {"sha256": sha_file(p),
                                                 "bytes": os.path.getsize(p)}
    out["utterances"] = len(read_jsonl(UTT))
    json.dump(out, open(LOCK, "w"), indent=1, sort_keys=True)
    open(LOCK, "a").write("\n")
    print(json.dumps(out, indent=1))
    return 0


def corpus_state():
    """LIVE if the private corpus is mounted and matches CORPUS.lock; else why not."""
    if not os.path.exists(UTT):
        return "NOT MOUNTED"
    if not os.path.exists(LOCK):
        return "LIVE (no lock to compare)"
    lk = json.load(open(LOCK))["files"]
    for p in PRIVATE:
        b = os.path.basename(p)
        if b in lk and os.path.exists(p) and sha_file(p) != lk[b]["sha256"]:
            return f"DIVERGED ({b} differs from CORPUS.lock; re-lock after ingest, or fetch the locked copy)"
    return "LIVE (matches CORPUS.lock)"


def validate(quiet=False):
    state = corpus_state()
    if not quiet:
        print(f"corpus: {state}")
    utt = {u["id"]: u for u in read_jsonl(UTT)}
    rows = read_jsonl(VIS)
    errs, ids = [], set()
    for r in rows:
        rid = r.get("id", "?")
        for k in REQ:
            if not r.get(k):
                errs.append(f"{rid}: missing {k}")
        if rid in ids:
            errs.append(f"{rid}: duplicate id")
        ids.add(rid)
        if r.get("kind") and r["kind"] not in KINDS:
            errs.append(f"{rid}: kind '{r['kind']}' not in {sorted(KINDS)}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}", r.get("said_at", "")):
            errs.append(f"{rid}: said_at must start YYYY-MM-DD")
        q = r.get("verbatim", "")
        found = False
        for uid in r.get("utterance_ids", []):
            u = utt.get(uid)
            if not u:
                if utt:
                    errs.append(f"{rid}: cites {uid}, not in utterances.jsonl")
            elif q and q in u["text"]:
                found = True
        if q and not found and utt:
            errs.append(f"{rid}: VERBATIM NOT IN RAW CORPUS - machine paraphrase or "
                        f"miscopy; quote must appear byte-for-byte in a cited founder turn")
        for pat in r.get("check", {}).get("must", []) + r.get("check", {}).get("must_not", []):
            try:
                re.compile(pat)
            except re.error as e:
                errs.append(f"{rid}: bad regex {pat!r}: {e}")
    for r in rows:
        for s in r.get("supersedes", []):
            if s not in ids:
                errs.append(f"{r.get('id', '?')}: supersedes unknown id {s}")
    if not quiet:
        for e in errs:
            print("FAIL", e)
        print(f"validate: {len(rows)} vision rows, {len(utt)} utterances, {len(errs)} failures")
        if not utt:
            print("PROVENANCE NOT COMPUTABLE HERE: the founder corpus is private and not mounted.")
            print("Schema only was checked. This is not a pass; mount the Drive lane and re-run.")
    return errs


# ---------------------------------------------------------------------- diff
def repo_files():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), ROOT)
            if f.endswith(TEXT_EXT) and rel not in SELF_QUOTING:
                out.append(rel)
    return sorted(out)


_cache = {}


def text(path):
    if path not in _cache:
        try:
            _cache[path] = open(os.path.join(ROOT, path), encoding="utf-8", errors="replace").read()
        except OSError:
            _cache[path] = ""
    return _cache[path]


def in_scope(files, globs):
    if not globs:
        return []
    return [f for f in files if any(fnmatch.fnmatch(f, g) for g in globs)]


def status(r, files, only=None):
    ck = r.get("check") or {}
    paths, must, mustn = ck.get("paths", []), ck.get("must", []), ck.get("must_not", [])
    scope = in_scope(files, ck.get("scope", []))
    if only is not None:
        scope = [f for f in scope if f == only]
    ev = {"paths": [], "must": [], "violations": []}
    for pat in mustn:
        rx = re.compile(pat, re.M)
        for f in scope:
            m = rx.search(text(f))
            if m:
                line = text(f).count("\n", 0, m.start()) + 1
                ev["violations"].append(f"{f}:{line} /{pat}/ -> {m.group(0)[:60]!r}")
    if ev["violations"]:
        return "CONTRADICTED", ev
    if not (paths or must or mustn):
        return "UNCHECKABLE", ev
    want = len(paths) + len(must)
    for p in paths:
        if os.path.exists(os.path.join(ROOT, p)):
            ev["paths"].append(p)
    if ck.get("each") and scope:
        # every file in scope must carry every must pattern (a ruling about ALL games)
        want = len(paths) + len(must) * len(scope)
        for pat in must:
            rx = re.compile(pat, re.M | re.I)
            for f in scope:
                if rx.search(text(f)):
                    ev["must"].append(f"/{pat}/ in {f}")
                else:
                    ev.setdefault("missing", []).append(f"{f} lacks /{pat}/")
    else:
        for pat in must:
            rx = re.compile(pat, re.M | re.I)
            hit = next((f for f in (scope or files) if rx.search(text(f))), None)
            if hit:
                ev["must"].append(f"/{pat}/ in {hit}")
            else:
                ev.setdefault("missing", []).append(f"no file in scope has /{pat}/")
    for p in paths:
        if p not in ev["paths"]:
            ev.setdefault("missing", []).append(f"path {p} does not exist")
    got = len(ev["paths"]) + len(ev["must"])
    if want == 0:
        return "LANDED", ev          # must_not only, and clean
    if got == want:
        return "LANDED", ev
    return ("PARTIAL" if got else "ABSENT"), ev


def coverage_lines():
    cov = load_cov()["chats"]
    by = {d: [] for d in DEPTH}
    for url, c in cov.items():
        by[c.get("depth", "UNSWEPT")].append((c.get("updated_at", ""), c.get("title", ""), url))
    return cov, by


def diff(write=False):
    errs = validate(quiet=True)
    rows = read_jsonl(VIS)
    files = repo_files()
    superseded = {s for r in rows for s in r.get("supersedes", [])}
    res = []
    for r in rows:
        st, ev = ("SUPERSEDED", {}) if r["id"] in superseded else status(r, files)
        res.append((st, r, ev))
    order = ["CONTRADICTED", "ABSENT", "PARTIAL", "UNCHECKABLE", "LANDED", "SUPERSEDED"]
    cov, by = coverage_lines()
    n = len(cov)
    L = [f"# FOUNDER VISION vs REPO - computed {now()}",
         "",
         "Generated by `founder-vision.py diff --write`. Do not hand-edit; re-run.",
         "Founder words below are verbatim from a cited founder turn (validate enforces it).",
         "",
         f"Corpus: {corpus_state()}",
         "",
         "## Coverage - how much of the founder record this report has actually read",
         ""]
    for d in reversed(DEPTH):
        L.append(f"- {d}: {len(by[d])} of {n} chats")
    L += ["", "READ means the agent opened the chat. SNIPPET means only the listing excerpt",
          "was seen. SUMMARY means only a model-written summary was seen; summaries are",
          "never founder words and never cited. Anything below READ is a partial witness.",
          ""]
    if errs:
        L += [f"## VALIDATION FAILURES ({len(errs)}) - rows below may be untrustworthy", ""]
        L += [f"- {e}" for e in errs] + [""]
    for st in order:
        group = [x for x in res if x[0] == st]
        L += [f"## {st} ({len(group)})", ""]
        if not group:
            L += ["(none)", ""]
            continue
        for _, r, ev in group:
            L.append(f"### {r['id']} - {r['subject']}  [{r['kind']}, {r['said_at'][:10]}]")
            L.append(f"> {r['verbatim']}")
            L.append("")
            L.append(f"Principle: {r['principle']}")
            label = {"violations": "VIOLATION", "missing": "missing", "paths": "present",
                     "must": "evidence"}
            for k in ("violations", "missing", "paths", "must"):
                for e in ev.get(k, []):
                    L.append(f"- {label[k]}: `{e}`")
            if r.get("note"):
                L.append(f"- note: {r['note']}")
            src = r.get("utterance_ids", [])
            L.append(f"- source: {', '.join(src)}")
            L.append("")
    below = sum(len(by[d]) for d in DEPTH if d != "READ")
    L += ["## NOT YET READ", "",
          f"{below} chats are below READ. They are named by `founder-vision.py coverage --list`,",
          "not here: chat titles are private and this report is a public URL.", ""]
    out = "\n".join(L) + "\n"
    counts = {st: sum(1 for x in res if x[0] == st) for st in order}
    print("FOUNDER VISION:", "  ".join(f"{k} {v}" for k, v in counts.items()),
          (f"| coverage READ {len(by['READ'])}/{n}, SNIPPET {len(by['SNIPPET'])}/{n}" if n
           else "| coverage NOT COMPUTABLE (private corpus not mounted)"))
    if write:
        os.makedirs(os.path.dirname(REPORT), exist_ok=True)
        open(REPORT, "w", encoding="utf-8").write(out)
        print("wrote", os.path.relpath(REPORT, ROOT), len(out.encode()), "B")
    return 1 if errs else 0


def brief(target):
    rel = os.path.relpath(os.path.abspath(target), ROOT)
    rows = read_jsonl(VIS)
    files = repo_files()
    superseded = {s for r in rows for s in r.get("supersedes", [])}
    hits = []
    for r in rows:
        if r["id"] in superseded:
            continue
        ck = r.get("check") or {}
        if in_scope([rel], ck.get("scope", [])) or rel in ck.get("paths", []):
            st, ev = status(r, files, only=rel)
            hits.append((st, r, ev))
    BROAD = {"*.html", "*.md", "*"}
    wide = [x for x in hits if x[0] != "CONTRADICTED"
            and BROAD & set((x[1].get("check") or {}).get("scope", []))]
    hits = [x for x in hits if x not in wide]
    print(f"FOUNDER BRIEF for {rel}: {len(hits)} rows govern this file")
    bad = 0
    order = ["CONTRADICTED", "ABSENT", "PARTIAL", "LANDED"]
    for st, r, ev in sorted(hits, key=lambda x: order.index(x[0]) if x[0] in order else 9):
        print(f"\n[{st}] {r['id']} {r['subject']} ({r['said_at'][:10]})")
        print(f"  \"{r['verbatim']}\"")
        for v in ev.get("violations", []):
            print("  VIOLATION", v)
        for m in ev.get("missing", []):
            print("  missing", m)
        bad += st == "CONTRADICTED"
    if wide:
        print("\nStudio-wide asks this file could carry (not required of it):")
        for _, r, _ in wide:
            print(f"  {r['id']} {r['subject']}")
    if bad:
        print(f"\nHALT: {bad} founder rulings contradicted by this file")
    return 1 if bad else 0


def coverage(listing=False):
    cov, by = coverage_lines()
    if listing:
        for d in DEPTH[:-1]:
            for upd, title, url in sorted(by[d]):
                print(f"{d:8} {upd[:10]}  {plain(title) or '(untitled)'}  {url}")
    for d in reversed(DEPTH):
        print(f"{d:8} {len(by[d]):4}")
    print(f"total    {len(cov):4}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd")
    a = sp.add_parser("ingest"); a.add_argument("dumps", nargs="+")
    sp.add_parser("validate")
    a = sp.add_parser("diff"); a.add_argument("--write", action="store_true")
    a = sp.add_parser("brief"); a.add_argument("target")
    a = sp.add_parser("coverage"); a.add_argument("--list", action="store_true")
    sp.add_parser("lock")
    a = sp.add_parser("exclude"); a.add_argument("uid"); a.add_argument("reason")
    a = sp.add_parser("mark"); a.add_argument("url"); a.add_argument("depth", choices=DEPTH)
    x = ap.parse_args()
    if x.cmd == "ingest":
        return ingest(x.dumps)
    if x.cmd == "validate":
        return 1 if validate() else 0
    if x.cmd == "diff":
        return diff(x.write)
    if x.cmd == "brief":
        return brief(x.target)
    if x.cmd == "exclude":
        return exclude(x.uid, x.reason)
    if x.cmd == "coverage":
        return coverage(x.list)
    if x.cmd == "lock":
        return lock()
    if x.cmd == "mark":
        return mark(x.url, x.depth)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
