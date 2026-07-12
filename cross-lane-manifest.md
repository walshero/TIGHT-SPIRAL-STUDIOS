# CROSS-LANE MANIFEST
*The one table that declares what is canonical, who owns it, and who may read it.*
*Lives in the Command Center. Holds ADDRESSES ONLY — no content. Governed by
os-block-cross-lane-mount.md §12. v1 — 2026-07-10.*

**Voice-first:** say "open the manifest" in any chat.

---

## GOVERNED DOCS — canonical addresses

| doc | canonical ID / path | bytes | version | owner-lane | RW/RO by lane |
|-----|--------------------|-------|---------|-----------|--------------|
| Confluence trunk | `confluence-TRUNK.html` · Drive **VERIFY** (memory carried v33 `1ndzTmSRubSHpoUagt5Gr2VKAFt6eQJ0X`; shelf shows **528,886 B = v34**) | 528,886 | **v34** | Confluence RW | TSP: RO (pointer only) · Leeder/Capstone: — |
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

## OPEN FOUNDER GATE (blocks manifest v1 → v1-verified)

**Confluence trunk version fork.** Memory's last live probe (2026-07-05) found Drive =
**v33** (522,533 B, ID `1ndz…`). The shelf copy read this session = **528,886 B**, which
your locked ruling ties to **v34 / c0b655fc**. Two possibilities:
- Drive was refreshed to v34 since the 07-05 probe (manifest is correct as written), **or**
- Drive is still v33 and the v34 pointer needs the real Drive ID once saved.

**Next action:** one Drive probe on the `Confluence — Build Versions` folder
(`1ylU3uDeC16UZtYo-mqeSGyXFHyGEkztM`) confirms the live ID + byte-count. Until then the
trunk row is marked **VERIFY**. Everything else in the manifest is disk-confirmed.

---

## HOW LANES USE THIS

- **Session-open:** load this manifest; it declares every lane's read/write rights.
- **Session-close:** any pointer whose target shipped this session → byte-verify, update its row.
- **Studio Eyes:** `WRITE-DIRECTION` (HALT on RO-write) · `PALETTE-MOUNT` (HALT on floor
  contradiction) · `POINTER-FRESH` (WARN if a row's last-touched lags the target's mtime).
