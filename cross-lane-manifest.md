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

## HOW LANES USE THIS

- **Session-open:** load this manifest; it declares every lane's read/write rights.
- **Session-close:** any pointer whose target shipped this session → byte-verify, update its row.
- **Studio Eyes:** `WRITE-DIRECTION` (HALT on RO-write) · `PALETTE-MOUNT` (HALT on floor
  contradiction) · `POINTER-FRESH` (WARN if a row's last-touched lags the target's mtime).
