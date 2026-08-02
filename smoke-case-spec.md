# SMOKE-READ CASE + CALIBRATION HUB — SPEC

> **Provenance.** Harvested 2026-07-21 from the "firefighting" TSP chat (too full to hand off;
> content pasted into a fresh session and captured here from that paste). This is the design
> the chat locked before its sandbox died — saved so the value survives the chat. Load-bearing
> facts (NIST imagery, INSARAG/FESHE/FSRI doctrine) remain source-routed, never invented.

## THE REFRAME (the project's real shape)

Not a solo studio making a firefighter app. **A calibration-assessment layer that clips onto
existing, credentialed, open fire curricula** — filling the one hole they all share: none of
them measure *calibration* (confidence matched to evidence). That gap is the founder's actual
professional edge (assessment design). The layer is:

- **FESHE-aligned** — for accreditation-facing outcomes.
- **FSRI-adjacent** — doctrine + design reference only. **NOT an image source.**
- **NIST-sourced** — for imagery.
- **Ben-validated** — for feel (Ben Urwin, Hand seat + facilitator).

## IMAGE LANE — RESOLVED (the fetch corrected the machine's first guess)

| Source | Role | License |
|---|---|---|
| **NIST** (fire research / FIREDOC) | **The open image lane.** Full-scale compartment burns, ignition→flashover stills, side-by-side comparative burns. | **US public domain** (federal work product). Credit line Madrzykowski/NIST. Cleanest on the shelf. |
| **Ben's department photos** | Streetside-realism upgrade path. Fastest correct images. | Waits on Ben; usage-cleared by his seat. |
| **FSRI / xplorLabs** | **Doctrine + design reference, NOT liftable.** Flow-path/ventilation courses are the physics spine. | "Free to access" ≠ "free to relicense." UL Terms of Use, login-gated, reuse routes to Media Inquiries = ask permission. |

**Rule:** an FSRI still is never liftable until their Terms say so in writing. NIST is the grab.
**Honest limit on NIST:** research burns read as *laboratory*, not streetside — doctrinally
perfect for teaching the physics of the read, upgraded later by Ben's fireground photos.

## THE DELIVERABLE — TWO FACES

### 1. The case (player face) — same engine as the collapse case
- **Content:** NIST structure-fire smoke approaching flashover.
- **The read:** **VVDC** — Volume, Velocity, Density, Color of smoke.
- **The trap:** **"look away from the light"** — the eye is pulled to visible fire and misses the
  *velocity* read (the real flashover predictor). Reveal makes the player *feel* the doctrine.
- **Mechanic:** commit a read under uncertainty → confidence dial → reveal what the fire did →
  calibration score (confidence-to-evidence, not right/wrong).
- **Flashover prediction** as the load-bearing decision.

### 2. The facilitator hub (officer face) — Confluence-derived
- **Fork 1 LOCKED:** Confluence's *structure* (an outcome, a rubric, individual→group rollup, a
  dashboard) with **calibration swapped in where ISLOs sit.** Its skeleton wearing a fireground
  outcome — not a copy of Confluence.
- **The rubric IS the calibration matrix:** confidence × correctness. **High-confidence-wrong =
  the kill cell,** flagged — "the read that gets a firefighter killed."
- **Ben runs it with his crew:** each firefighter commits a read; the hub plots the crew's spread
  across the matrix; the debrief conversation ("why did four of us read high-confidence and miss?")
  is the engagement — it feeds the after-action review firefighters already run.
- **Session export** Ben keeps → becomes the Hand-seat's Layer-2 growth record.

### Fork 2 LOCKED: A now, B later without rebuild
- **A — Facilitator instrument (SHIP THIS):** no accounts, no stored roster, no FERPA-shaped data.
  Single-file, offline, station-laptop, no network. Scores/debriefs the reads happening in the room;
  exports a session summary.
- **B — Persistent hub (later):** longitudinal per-firefighter calibration trend. Needs storage,
  identity, data-governance. Build A's session-export as the seed of B's data. B first = spec-rich/
  build-poor.

## HARD FLOOR — INTRINSIC MOTIVATORS ONLY (a correctness requirement, not taste)

Extrinsic "icky engagement" **inverts the outcome** in a calibration trainer: a streak counter
rewards confidence and punishes admitting uncertainty; a leaderboard turns "I don't know / hand it
to the Specialist" (the safety answer) into the losing move. **Forbidden on both faces:** streaks,
points-as-currency, timers-as-pressure, win/lose framing, celebratory animation on "correct,"
badges, leaderboards, confetti.

**Allowed (the pull comes from the task + the profession):**
- The **reveal is the reward** — "I saw that coming" / the productive sting of "I didn't."
- **Calibration as its own mirror** — the only number on screen; framed as a mirror, not a score.
  Getting it wrong humbly scores better than getting it right arrogantly.
- The **named kill cell** — real domain stakes.
- **"Look away from the light"** — earned insight, discovery not instruction.
- **Crew debrief** as the social layer — the after-action review, never a leaderboard.
- Progress feeling = reads getting *truer* over sessions (exactly what B will one day chart).

## INHERITED FLOORS (repo-canon, arithmetic — not eyeballed)

- Ink `#0f0d0a` on paper `#f7f4ee` ≈ 17.6:1. **A color token is atmosphere OR text, never both.**
- **Warm/comfort mode text must be COOL near-white** (raise blue toward R=G=B); amber/gold is
  fill/accent only, never `color:`. (This is the exact bug that HALTed the collapse case — fixed
  from the start here.)
- No emoji. Single-file, offline. Scene-first with a live comfort corner. Screens >50% image.
- **Gate before it reaches a device:** `preship-gate-v4.py` must exit SHIP. Exit 1 = does not ship.

## ONE HONEST RUNG (Aleph discipline)

This spec is a map, not a mandate. Build the smoke case on NIST imagery + San Diego/FESHE doctrine,
get Ben's read, prove calibration lands with firefighters — *then* the FSRI-catalog ladder
(flow paths → ventilation → search → structural → WUI) is earned, not assumed. A five-rung roadmap
with zero shipped rungs is the named failure mode.
