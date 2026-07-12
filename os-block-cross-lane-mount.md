# OS BLOCK — THE CROSS-LANE MOUNT (§12)

*Locked 2026-07-10 (founder voice session). The governance primitive that connects
lanes without merging them. Extracted from the Confluence↔TSP link problem and
generalized: **canon is an address, governance is a flag on that address, and the
flag is machine-enforced.** Copies go stale; pointers cannot. Remembered rules leak;
flagged ones HALT.*

---

## §12.1 The primitive

Three moves, applied to every governed document in the studio:

1. **Canon is an address, not a copy.** A lane never holds another lane's content.
   It holds a *pointer*: canonical file ID + byte-count + version + last-touched.
   A pointer is ~200 bytes and is always current; a copy is stale the moment the
   source is edited. This is the accumulator-decay rule applied at the index level.

2. **Every mount carries a write-direction flag.** `RW` (this lane owns it, may
   write) or `RO` (this lane may read only). The flag is declared once, in the
   manifest, and enforced — not remembered.

3. **The flag is machine-enforced.** Studio Eyes HALTs any session that writes to a
   doc it holds `RO`. Convention leaks; a HALT does not.

**The through-line the primitive replaces:** canon was *content copied around*;
governance was *rules people remember*. Both fail silently. The mount flips both.

---

## §12.2 The manifest — single source of truth for what's canonical

The **Cross-Lane Manifest** lives in the Command Center (which is itself now a
pointer-hub — see §12.5). Every governed doc has exactly one row:

| doc | canonical ID | bytes | version | owner-lane | last-touched |
|-----|-------------|-------|---------|-----------|-------------|

The manifest holds **no content** — only addresses. When the Confluence trunk bumps
v34→v35, one row updates; every lane that mounts it sees the new pointer next session.
No file copies, no stale duplicates, no "which one is real" fork.

**Byte-verify law:** the manifest pointer is verified on every ship of the doc it
points at (the belt already does this for the trunk). A wrong pointer is a
single-point-of-failure; the byte-check is its guard. "created:true" is never proof.

---

## §12.3 The Confluence ↔ TSP link (the first mount)

**TSP mounts Confluence:** the trunk **pointer** only (ID/bytes/version), read-only.
TSP never opens the 528KB trunk — it reads the pointer so it always knows what
"latest" is. Direction: `Confluence → TSP` is `RO`.

**Confluence mounts TSP core docs**, read-only:
- `tight-spiral-visual-constitution.md` — the green-floor legibility law
- OS §6.4 Kernel Track — Confluence's calibration ground-truth (kernels are what
  Confluence norms against)

Confluence reads these; it can never write TSP canon. Direction: `TSP → Confluence`
is `RO` both ways on the write. **Guard:** Studio Eyes HALTs if a Confluence-context
session writes to a TSP core doc, or if a TSP session writes to the trunk pointer's
target from the wrong side. Green cannot leak into a game; arcade palette cannot leak
into the instrument. The palette lock stops being a *remembered decision* and becomes
a *live constraint the build reads* (§12.6).

**Founder-confirmed doc set (2026-07-10):** Visual Constitution + Kernel Track — the
tighter assessment-only two, not the full OS. Confluence is an instrument; it needs
the floor and the ground-truth, not the whole engine.

---

## §12.4 The four other applications (all the same primitive)

**A. Silo dissolution (Leeder / Capstone / MassBay).** Each lane mounts the others'
one core doc read-only. Leeder reads the Visual Constitution (its website rebuild
passes the same floor) without touching studio canon. Capstone reads the Kernel Track
(its evidence substrate) `RO`. Silos dissolve without merging. `conversation_search`
stops being the un-silo mechanism (it was always a fallback); the manifest is.

**B. Cleared = write-locked (ship-gate teeth).** A `PANEL-CLEARED` build is `RO`
until a new gate fires. No session may edit a cleared build without re-entering the
pipeline. This is the same flag, applied to builds instead of docs — it closes the
"it's basically done, just one tweak" leak that ships un-gated edits. Clearance is a
read-only flag; only GATE 1 + GATE 2 flip it back to `RW`.

**C. Palette-as-mounted-law (§12.6).** Every build mounts its lane's palette-floor
`RO` at open and cannot override it. Studio Eyes HALTs on any inline color that
contradicts the mounted floor. Arcade-B for games, green for Confluence — read from
one governed source, not remembered per file.

**D. Memory-as-pointer (§12.7 / separate spec).** Most memory lines should be a
read-only pointer to an archive block, not the content. "MEMORY RUNS AS INDEX; OS is
the ARCHIVE" is stated architecture but currently *violated* — memory duplicates the
archive. Enforce pointer-only and the 30/30 overflow stops.

---

## §12.5 Command Center becomes a pointer-hub

The Command Center stops accumulating content and holds **only pointers** — the
Cross-Lane Manifest plus open-thread addresses. It can never go stale because it holds
no fact that lives elsewhere, only the address of where that fact lives. This is the
Drive Atlas made law: index, never archive.

---

## §12.6 Palette floor as mount (enforcement detail)

Each lane declares its palette floor once in the manifest:
- **arcade** → palette-B High Lumen amber, 16.1:1 (games default floor)
- **Confluence** → studio green #1a4a35 (instrument only)

A build reads its floor `RO` at open. Studio Eyes check `PALETTE-MOUNT`: any inline
color contradicting the mounted floor HALTs. The per-build Medium Gate still *chooses*
the lane; the mount *enforces* the choice.

---

## §12.7 Belt hooks (how this stays alive)

- **Session-open card** gains one line: *load the Cross-Lane Manifest from the Command
  Center; it declares what every lane may read and write.*
- **Session-close belt** gains one line: *any manifest pointer whose target shipped
  this session is byte-verified and its row updated.*
- **Studio Eyes** gains three checks: `WRITE-DIRECTION` (HALT on RO-write),
  `PALETTE-MOUNT` (HALT on floor contradiction), `POINTER-FRESH` (WARN if a manifest
  row's last-touched lags its target's actual mtime).
- **CLASS-TICK on process:** any session ending in a predictable "wrong lane wrote the
  wrong doc" correction mints a tighter mount rule. Adaptive Studio Eyes.

---

## §12.8 What to ignore

Do **not** build a sync engine, a database, or a merge layer. The primitive is
deliberately dumb: addresses + flags + one HALT check. The moment this grows a
bidirectional-write or auto-merge feature, it has become the thing it was built to
prevent. One canon writes; others read. That asymmetry is the whole design.
