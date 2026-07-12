# CROSS-LANE MANIFEST
*The one table that declares what is canonical, who owns it, and who may read it.*
*Lives in the Command Center. Holds ADDRESSES ONLY — no content. Governed by
os-block-cross-lane-mount.md §12. v1 — 2026-07-10.*

**Voice-first:** say "open the manifest" in any chat.

---

## GOVERNED DOCS — canonical addresses

| doc | canonical ID / path | bytes | version | owner-lane | RW/RO by lane |
|-----|--------------------|-------|---------|-----------|--------------|
| Confluence trunk | `confluence-TRUNK.html` · **repo** (canon) · Drive `1034TofDcOWwaukceHcwzsnUlsLO4yggt` = pointer only | 598,114 | **v44** (md5 `8dcf9903`) | Confluence RW | TSP: RO (pointer only) · Leeder/Capstone: — |
| OS canon | `tight-spiral-studio-os.md` · Drive `1qZBTAbluu0npTtw3NlPPXySTClI6Jnx3` | 161,666 | 2026-07-02 | TSP RW | Confluence: RO (§6.4 only) · others: RO |
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

## CLOSED FOUNDER GATE — Confluence trunk (resolved 2026-07-12)

**Resolved by repo fetch, not memory.** `raw.githubusercontent.com/.../confluence-TRUNK.html`
returns **598,114 B, md5 `8dcf9903` = v44**. Both prior candidates (v33 522,533 B and
v34 528,886 B) are **fossils**. Drive holds a pointer only. The trunk row above is now
disk-confirmed; the VERIFY flag is lifted.

**Lane-size law (why the drift happened):** the Drive bus passes file content as a tool
parameter (~30–50 KB ceiling). A 598 KB file can never fit — so the most important file
was the one file the lanes could not move. **Any file >50 KB: canon in the REPO, pointer
in Drive.**

---

## HOW LANES USE THIS

- **Session-open:** load this manifest; it declares every lane's read/write rights.
- **Session-close:** any pointer whose target shipped this session → byte-verify, update its row.
- **Studio Eyes:** `WRITE-DIRECTION` (HALT on RO-write) · `PALETTE-MOUNT` (HALT on floor
  contradiction) · `POINTER-FRESH` (WARN if a row's last-touched lags the target's mtime).
