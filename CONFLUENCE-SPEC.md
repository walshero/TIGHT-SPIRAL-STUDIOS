# CONFLUENCE — LANE SPEC & COLD-START
*v2 · 2026-07-23 · One repo. Confluence is a **lane** inside*
*`walshero/TIGHT-SPIRAL-STUDIOS` (public), not a separate repo. This is the*
*durable memory a chat can't hold. Canon is git; everything below is computed.*

---

## 0 · HOW TO USE THIS

Paste-block: `CONFLUENCE-PROJECT-PASTE.md`. Because the repo is **public**, a
project/phone session can fetch this spec and the gates straight from git —
`raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/<path>`. No shelf
dependency. Only Claude Code / CI fires the gates and lands to git.

---

## 1 · WHAT CONFLUENCE IS

Confluence is the MassBay **assessment + calibration** lane: where student work
goes, how artifacts read against outcomes, how consistently faculty score them.
It is **its own entity — as a lane, not a repo.** Its files live in the one repo
and it holds RW over them; other lanes mount them RO.

Three artifacts, all in this repo:

| artifact | what | path | state |
|---|---|---|---|
| **calibration-hub SPA** | role-adaptive app: sessions, rubrics, scoring, inter-rater reliability | `confluence-hub/` | built, C1-fixed, C1-gated |
| **massbay companion** | single-file "where student work meets the world" | `confluence-massbay-assessment.html` | **gate-green** |
| **trunk** | the ~600 KB Confluence trunk | `confluence-TRUNK.html` | HALTs — baselined debt; founder call to fix |

---

## 2 · THE LANE LAW

- **Confluence owns its files RW** (`confluence-hub/`, `confluence-*.html`).
  Other lanes read/gate them but don't edit them. No two truths.
- The cross-lane manifest is the address book; it already models Confluence as a
  lane. One repo makes that literal.

---

## 3 · THE FLOORS EVERY PAGE MUST CLEAR  *(acceptance form)*

Each floor is a **check**, run from the repo root.

- [ ] **C1 — color-scheme declared** (`<meta>` + per stop). *`c1-check.py` — works on the SPA too.*
- [ ] **R1 — rendered text contrast ≥ 4.5** (≥ 3.0 large), every stop, every width. *`studio-eyes-sweep.py`.*
- [ ] **Token-role law** — a color is atmosphere or text, never both. *`preship-gate-v4.py`.*
- [ ] **Warm-ink** — warm-mode text is cool near-white; amber/gold is fill only. *preship + sweep (H-HUE).*
- [ ] **Font floor** — 20 px body, 18 px absolute min. *sweep (E1).*
- [ ] **Comfort stops** — Day / Softer / Night, set pre-paint, corner control. *`confluence-hub/css/comfort-stops.{css,js}`.*
- [ ] **A11y** — skip-link, visible focus, working nav; no emoji in text.
- [ ] **Self-contained** — no external hosts; offline.

---

## 4 · GATES & CI (one repo — no vendoring)

Gates live at repo root and are shared by the whole studio: `c1-check.py`,
`preship-gate-v4.py`, `studio-eyes-sweep.py`.

- **`floor.yml`** (existing) sweeps root-level `*.html` and ratchets — the
  companion + trunk are covered here; the trunk is baselined debt.
- **`confluence-hub.yml`** (new) gates `confluence-hub/` — the SPA is a subdir,
  so the root sweep never sees it; C1 covers the shell (render-proof can't,
  because the SPA is JS-driven).

There is **no `studio-kernel/`, no pin, no sync** — one repo means the gates are
simply *here*. (That apparatus was scaffolding for the retired two-repo split.)

---

## 5 · THE PANEL — mapped to assessment

Seven seats govern a Confluence artifact before it ships; the panel names the
seat that owes a missing fact, it never invents one.

1. **Engineer** — every reliability/agreement figure is computed from real
   scores, not a guess wearing a decimal.
2. **Hand** — a faculty rater who has lived with a borderline call; the artifact
   teaches doubt, not false certainty.
3. **Coordinator** — ISLOs / AAC&U VALUE / NECHE, **sourced, not remembered.**
4. **Registrar** — every student artifact has a source + as-of date + FERPA standing.
5. **Calibrator** *(founder seat)* — the score measures confidence-matched-to-
   evidence, not "were you right."
6. **Stranger** *(non-negotiable floor)* — contrast is arithmetic; §3 floors;
   readable by a first-timer; no emoji.
7. **Aleph** — one screen or a system? Anti spec-rich/build-poor. In Confluence
   Aleph also asks: **"did we relearn something the studio already knows?"** —
   if yes, it's a gate, not a note.

*(Full seat text: `collapse-panel-spec.md`, the domain-general source.)*

---

## 6 · CURRENT STATE  *(computed 2026-07-23)*

- **SPA** (`confluence-hub/`): role-adaptive (4 roles, Home/Back/breadcrumbs,
  design system). **C1 fixed**; C1 gate ok; boots 0 console errors. Stubs still
  toast-only: scoring persistence, New session, Close & publish, Send reminders,
  New/Approve/Edit rubric, Settings save.
- **Companion**: gate-green (preship SHIP; sweep 0 HALT + pixel crosscheck). Only
  unprovable-by-machine element = JS initial theme → the founder's on-device GATE 1.
- **Trunk**: HALTs (C1, `--pine-lt` 4.08, `--gold-border` warm-ink, 'Tour' 4.19,
  250+ sub-18px) — **baselined**, so it doesn't block. Also lane-drift: shelf has
  reported a v48 (631,929 B) newer than git — reconcile by content before trusting.

---

## 7 · BUILD DIRECTION  *(the 1+2+3; each ships through §3)*

- **A · Functional (stateful).** Wire the SPA stubs to client-side state:
  scoring records, progress + agreement recompute live, status persists.
- **B · Real MassBay content.** True ISLOs / VALUE rubrics / programs; no invented
  people — positions or a real roster only.
- **C · New surfaces.** Session wizard, rubric builder, norming/discrepancy view,
  export. *(Aleph gates against speccing C before A ships.)*

---

## 8 · OPEN FOUNDER CALLS

- **Trunk fix** (Confluence-lane RW): apply the companion-proven pattern, re-gate,
  land. Removes it from the ratchet baseline (the ratchet only shrinks).
- **Trunk lane-drift**: which trunk is canon — git 611,046 or shelf v48 631,929?
  Decide by content.
- **Retire the old repo**: `confluence-calibration-assessment-hub` (private) is
  now redundant; archive it once this lands.

---

## 9 · WORKING DISCIPLINE

- **Canon is computed, not remembered.** Fetch git; verify md5; decide from content.
- **Land the same turn.** Push, fetch back, match the hash — or it doesn't exist.
- **A rule that can't be a check is a wish.** New floor → new gate tooth.
- **Gates run in CI.** A regression fails the build (the ratchet only turns one way).
