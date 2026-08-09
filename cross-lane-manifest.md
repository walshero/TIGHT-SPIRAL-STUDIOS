# CROSS-LANE MANIFEST
*The one table that declares what is canonical, who owns it, and who may read it.*
*Lives in the Command Center. Holds ADDRESSES ONLY — no content. Governed by
os-block-cross-lane-mount.md §12. v1 — 2026-07-10.*

**Voice-first:** say "open the manifest" in any chat.

---

## GOVERNED DOCS — canonical addresses

| doc | canonical ID / path | bytes | version | owner-lane | RW/RO by lane |
|-----|--------------------|-------|---------|-----------|--------------|
| Confluence trunk | **LATEST = Drive** `1ASstFxZrdobjUpPVK6uFMCfDYLN3yQFA` `confluence-TRUNK-v48-2026-07-14.html` (631,929 B) · repo `confluence-TRUNK.html` = **STALE v43** (598,114 B, md5 `8dcf9903`) · Drive `1034TofD…` = pointer | **v48** (Drive) · repo lags at v43 | Confluence RW | TSP: RO · **DO NOT edit repo copy — it is not canon** |
| OS canon | `tight-spiral-studio-os.md` · **repo** (canon, landed 2026-07-12) | grown to §16, reconciled 2026-08-08 | 2026-07-05 base · **all 13 os-blocks merged, see "CLOSED — OS merge" below** | TSP RW | Confluence: RO (§6.4 only) · others: RO |
| OS blocks (folded into OS §15) | `os-block-*.md` × 13 · repo | — | 07-04 → 08-07 | TSP RW | all: RO — content now lives in the OS text; files stay as the per-topic origin record |
| Visual Constitution | `tight-spiral-visual-constitution.md` | 10,141 | §13, 2026-07-04 | TSP RW | Confluence: RO · Leeder: RO · Capstone: — |
| Kernel Track | OS `tight-spiral-studio-os.md §6.4` | — | 2026-07-02 | TSP RW | Confluence: RO · Capstone: RO |
| Pipeline | `tight-spiral-pipeline.md` | 8,320 | 2026-07-02 | TSP RW | all: RO |
| Command Center | Drive `1dULxFj1fxg8sF3SF2DXGoA9B-tt1XMbQ` | — | v-live | TSP RW | all: RO |

---

## PALETTE FLOORS — mounted RO by every build at open

| lane | floor | contrast | source of truth |
|------|-------|----------|----------------|
| arcade (games) | palette-B High Lumen amber | 16.1:1 | Visual Constitution |
| Confluence | studio green `#1a4a35` | (instrument) | Confluence trunk header |

`PALETTE-MOUNT` HALT: any inline color contradicting the lane's mounted floor stops the build.

---

## REOPENED FOUNDER GATE — Confluence trunk (the 07-12 "close" was wrong)

**The 2026-07-12 resolution recorded the repo copy as canon "v44." A four-lane resolve on
2026-07-14 shows that was false on two counts:**
1. **The repo copy is v43, not v44.** Its own stamps read v43; the newest *dated* banner is
   v43 (2026-07-10). The manifest was recording a v44 that never landed in the repo.
2. **Drive is not "pointer only."** It holds a real **v48** file
   (`confluence-TRUNK-v48-2026-07-14.html`, 631,929 B) carrying four dated additive builds
   inside — v45 token-split, v46 truth-pass, v47 open-asks, v48 reliability-engine
   (all 2026-07-14). Diffed against repo: **every repo section is present + 8 more; nothing
   is lost by adopting it.** The real work was built in Drive and never pushed to the repo —
   the studio's own "built → landed → never pushed" loss pattern.

**Canon (from content, not memory): the Drive v48 is latest; the repo is a stale ancestor.**
It is **not yet promotable to repo canon** — `safe-push`'s Studio Eyes gate HALTs it. A
true-pixel sweep (headless Chromium) separated the real defects from the auditor's
mis-grounding: **8 genuinely invisible text roles fixed** (incl. two `FERPA` labels rendered
gold-on-gold, and a white-on-white progress chip) + 4 AA near-misses, all now ≥4.5:1,
verified in real pixels. Remaining Studio-Eyes HALTs (`.cab-glyph`, `.lum-*`, `.ssb-*`) are
**false positives** — the auditor grounds to `body` where the real background is dark;
those render 9–14:1. Two live `fetch()` calls (`api.anthropic.com`, a Supabase endpoint;
**no key committed**) still break the offline floor and must be gated/stripped before ship.
Staged, contrast-fixed v48 is in `outputs`; **the push is a Confluence-lane action.**

**Lane-size law (why the drift happened):** the Drive bus passes file content as a tool
parameter (~30–50 KB ceiling). A 598 KB file can never fit — so the most important file
was the one file the lanes could not move. **Any file >50 KB: canon in the REPO, pointer
in Drive.**

---

## CLOSED — OS merge (opened 2026-07-12, reconciled 2026-08-08)

The OS was **404 in the repo** until 2026-07-12 — the one doc everything defers to had
no canonical lane. Founder's call, 2026-08-08: "Reconcile." All 13 `os-block-*.md`
files are now merged into `tight-spiral-studio-os.md` §15, verified against the text
line by line, not assumed. Most (9 of 13) turned out to already be merged by an
earlier session — this table and the OS's own header just never caught up. Real
findings, both fixed:

| block | claimed | what was actually true |
|---|---|---|
| `os-block-cross-lane-mount.md` + `os-block-pointer-memory.md` | both §12 | cross-lane-mount cleanly merged as §12.1-12.8; pointer-memory's content WAS merged too, but mislabeled "### 12.7", colliding with cross-lane-mount's real §12.7. Renumbered to §12.9. |
| `os-block-preship-gate.md` | §14 | merged under §15 (not top-level §14, avoiding the OS's real, unrelated "## 14. Lane truth") - but its internal subheadings still read "§14.1"-"§14.6", confusable with the real §14 a few thousand lines away. Renumbered to 15.preship-gate.1-6. |
| `os-block-truth-ticks.md` | §11 | merged cleanly as `### 15.truth-ticks`, no internal §11 labels. This collision never actually existed in the merged text. |

The 4 newer blocks (bodyguards, fidelity-gate, aleph-fleet, aleph-diagnose-repair) were
genuinely unmerged as of 2026-08-07 and are now folded in alongside the rest, all under
`### 15.xxx`.

---


## GATES — the enforcement layer, declared 2026-08-08

*Addresses only, per this file's own rule. Added after two TSP sessions built two
different `studio-fingers.py` on the same day, neither having read this manifest — and
neither of which this manifest could have stopped, because until now it governed docs and
never named a single gate.*

**The belt is the only thing with agency.** `studio-belt.sh` (9,725 B, `02c1ff5f`) runs the
ticks; every tick BLOCKS on exit 1. **A gate that is not mounted on the belt does not run.**


> **AMENDED 2026-08-08 — read the ruling below the table before trusting a row.**

| # | tick | gate | bytes / blob | mode | owner |
|---|------|------|--------------|------|-------|
| 1 | accessibility floor | `comfort-gate.py` | 9,506 · `1db5f289` | ratchet | UNDECLARED |
| 2 | student attribution | *(in-belt)* | — | ratchet | UNDECLARED |
| 3 | >50% image + render | `preship-gate-v4.py` | 20,035 · `7d5d7b6f` | ratchet | UNDECLARED |
| 4 | founder voice | `studio-voice-gate.py` | 11,728 · `b169aaf7` | ratchet | UNDECLARED |
| 5 | entry paint | `one-thing-gate.py` | 16,873 · `7dca5f10` | ratchet | UNDECLARED |
| 6 | retired lines | `retired-lines-gate.py` | 8,134 · `99da04ae` | flat | belt lane (2026-08-08) |
| — | **NOT MOUNTED** | `studio-fingers.py` | 12,429 · `baee110d` | — | canon lane (2026-08-07) |
| — | **NOT MOUNTED · DUPLICATE** | `studio-eyes/studio-fingers.py` | 13,124 · `c504d4e2` | — | studio-eyes lane |
| — | not a tick (resolver) | `resolve-canon.py` | 38,353 · `34d58994` | — | canon lane |
| — | not a tick (write path) | `stage-push.py` | 9,230 · `4d23328c` | — | canon lane |
| — | not a tick (evidence) | `studio-eyes-sweep.py` | 15,619 · `9989f9a2` | — | UNDECLARED |
| — | not a tick (provenance) | `art-gate.py` | 3,211 · `d62c0efb` | — | UNDECLARED |

UNDECLARED is not a shrug. It is a **founder call outstanding**: a gate whose owner is not
named cannot be safely edited by any session, which is how the studio ends up with two of
them.

### RULING 2026-08-08 — ownership settled, tick 7 mounted

Founder: *"This is the belt lane."* The lane running this session owns the belt and its
gates. Every UNDECLARED above is resolved to **belt lane**. Three moves landed the same
turn, each byte-verified:

| what | file | now | commit |
|---|---|---|---|
| **tick 7 mounted** | `studio-belt.sh` 11,095 · `a54da6c8` | `studio-fingers.py` runs as a **ratchet** | `7e5798b6` |
| ratchet baseline | `fingers-baseline.json` 4,603 · `56986cc2` | 97 of 133 surfaces carry debt; **75 LAW-level failures** | `dfd1542d` |
| DARK false halt killed | `preship-gate-v5.py` 6,105 · `3696c1be` | `[data-light\|theme\|comfort\|mode]=` counts as a dark path | `d243b0af` |
| entry scope added | `retired-lines-gate.py` 9,714 · `3a3dee22` | `except_paths` + `render_only`, both optional | `99f841da` |
| vocabulary boundary armed | `retired-lines.json` 2,411 · `8e8f908b` | "studio eyes" banned on player surfaces, permitted on `studio/` | `cbbbb421` |

**`studio-fingers.py` is no longer unmounted.** The `NOT MOUNTED` marker in the table above
is superseded for the root file; `studio-eyes/studio-fingers.py` remains a live duplicate
and still needs a retire-or-merge call.

**Why the tick is a ratchet and not flat.** 97 of 133 surfaces already fail the 48px house
floor. A flat tick freezes deploy on day one over debt nobody was checking — the exact
discovery that made ticks 1/3/4/5 ratchet. `law_failures_at_baseline: 75` is recorded
separately in the baseline because those sit below **WCAG 2.5.8 AA**, not merely below house
style. That number is the one that must reach zero.

**Why the vocabulary entry is `render_only`.** The bug is a reader SEEING the internal name.
A doc that *discusses* the ban is the record, not the violation — without this flag the gate
would flag this manifest and the ledger that record it, eating its own homework. Verified on
landing: `index.html` HALT, `arcade.html` HALT, `studio/tsp-home.html` clean, source scan
clean.


### THE GAP THIS TABLE EXPOSES

The duplicate was **not a cross-lane failure.** Both sessions were TSP. This manifest's
whole model is lane-level RW/RO, and both held RW — so the rule that was supposed to
prevent this could not even express the situation. **The real hazard is two concurrent
sessions inside ONE lane**, and nothing in the studio arbitrates that.

Two checks, cheap, in preference order:

1. **A colliding basename is a HALT.** `resolve-canon.py` now records every basename held by
   more than one path and prints them by name in the Aleph pass; a single root-level path
   wins its basename, and a full path resolves exactly. Eight collide today. Before this,
   the resolver picked canon alphabetically and had been resolving `workshop-in-a-box.html`
   to a `rescued/` snapshot.
2. **A gate declares its own tick.** If a gate's header names its belt number, an unmounted
   gate is detectable by reading the gate rather than by remembering the belt.

### STANDING HALTS AGAINST THE ENFORCEMENT LAYER

- **Duplicate canon.** Two gates answer "can this be touched." Founder ruling needed on
  which is canon; the other retires.
- **`preship-gate-v5` DARK clause is false.** It greps for `prefers-color-scheme`, finds 0
  in `index.html`, and reports "no measured dark path." That file implements dark as
  `[data-light=…]` — **15 occurrences** — which is what studio doctrine requires: comfort
  is a live corner control, not an OS wall. `comfort-gate` measures real painted pixels and
  passes the same file. The gate is wrong, the file is right, and the HALT has stood since
  2026-08-03. A gate that cries wolf trains the studio to scroll past it.
- **Vocabulary boundary unenforced.** "Studio Eyes" is visible to a reader in **103 files**,
  **62 of them non-studio surfaces**, including student-facing ones. `retired-lines-gate.py`
  is the right home — it already converts a founder objection into a permanent check — but
  its entries are global. It needs one optional `except_paths` field so a name that is
  correct on `studio/` can be banned everywhere else.

---

### RULING 2026-08-09 — tick 8 mounted (scope). Read this before the GATES table above.

**The table above is amended a second time.** Tick 8 is real, mounted, and blocking.

| what | file | now | commit |
|---|---|---|---|
| **tick 8 mounted** | `studio-belt.sh` 18,641 · `12a7ac24` | `scope-gate.py` runs; header and PREFLIGHT line say **8 ticks** | `17d61f10` |
| the gate | `scope-gate.py` 16,404 · `83c1d04a` | clause A **flat**, clause B **ratchet**, self-test 14/14 | `6311c044` |
| ratchet baseline | `scope-baseline.json` 458 · `c544e56f` | **5** dangling citations across 12 governance docs | `cbf791b6` |
| the ruling it enforces | `claude/FERPA-SCOPE-RULING.md` 6,229 · `5158451d` | SCOPE section: what a sweep may RETRIEVE | `2ed2c106` |

**One gate, two clauses, one question — what does a document reach for.**
Clause **A** says do not reach past what you were asked for: no wide-corpus retrieval baked
into an artifact. Clause **B** says do not point at what you cannot touch: no governance doc
may name a file the trunk cannot reach. Split into two gates they would have *been* two
gates, and this repo grew two `studio-fingers.py` in one day by splitting a question that
was really one question.

**Measured before arming, per the 48px lesson.** Clause A is at **zero** across 587 trunk
files, so it is flat and there is no reason to ever add one. Clause B found **5** real
dangling citations, so it ratchets. Only the documents that *define* the rule may say the
forbidden query shape, and that allowlist prints on every run.

**THE FIRST CATCH, AND IT IS THE STANDING INSTRUCTIONS.** The project instructions order
every session, unprompted, to read three files at `claude/` paths. None of the three
resolves in the trunk:

```
claude/forking-paths-protocol.md          -> trunk has FORKING-PATHS-PROTOCOL.md at root
claude/founder-voice-provenance-manifest.md -> NOT IN THE REPO AT ALL. Shelf only.
claude/FUNES-LEDGER.md                    -> trunk has FUNES-LEDGER.md at root
```

Two are wrong paths for files that exist. The third — the D3/D5 founder-voice rules the
session-open protocol is told to obey — is not in the repo, so **founder voice provenance is
computable from no lane the trunk can reach.** That needs a founder call, not a patch: the
fix is either landing the document or correcting the instruction, and only one of those is
mine to make. Same shape as the FERPA ruling, closed earlier today, three more times.

*(Those three paths and the other baselined names are written inside a fenced block on
purpose. A fenced block is a quotation, not a citation, and the gate strips it before
tokenizing — otherwise naming the defect would itself trip the tick.)*

**What tick 8 does NOT cover, printed by the gate on every run rather than implied:** it
reads **artifacts**. It cannot see a query an agent types at runtime, which is the shape
that actually caused the incident. That half lives in the standing instructions and has no
arithmetic behind it yet. Snapshot trees (`rescued/`, `archive/`, `aleph-runs/`) are skipped
by design — their citations dangle because history moved on.

**Baseline is keyed to the REMOTE name, not the checkout directory.** A spoke with no
baseline of its own prints `UNMEAS` and does **not** block, because nothing is "new" when
there is no *was* — the ticks 1/3/4/5 lesson. Clause A halts everywhere regardless.

**It caught itself once.** The tick's own comment spelled the forbidden query shape, and
preflight halted the belt on the belt. Reworded rather than allowlisted.

---

## HOW LANES USE THIS

- **Session-open:** load this manifest; it declares every lane's read/write rights.
- **Session-close:** any pointer whose target shipped this session → byte-verify, update its row.
- **Studio Eyes:** `WRITE-DIRECTION` (HALT on RO-write) · `PALETTE-MOUNT` (HALT on floor
  contradiction) · `POINTER-FRESH` (WARN if a row's last-touched lags the target's mtime).
