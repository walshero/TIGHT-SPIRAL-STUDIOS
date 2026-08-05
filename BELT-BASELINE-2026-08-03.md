# STUDIO BELT — baseline dry-run (2026-08-03)
*Read-only. What the belt would catch across the five repos TODAY, before it is armed. Arm over a clean baseline, or ratchet the known debt — never arm blind over a backlog (floor.yml learned this the hard way in July).*

## Coverage this run
- **Hub — `TIGHT-SPIRAL-STUDIOS`:** accessibility floor already enforced by `floor.yml` (ratchet, armed 2026-07-14). Belt tick 2 (attribution) is clean on the shipped surfaces checked — the arcade credit is generic ("Hamish K. · EN195 Creative Writing (summer 6-week online)").
- **`en195-apps` (public):** swept in full. Result below.
- **`confluence-calibration-assessment-hub`, `-writerly-moves-game`, `matt-radar` (private):** the read-only proxy refused the clone (no interactive auth for private repos), so a full belt run is pending. The connector confirms all three exist and are push-enabled; each will produce its baseline on its first CI run once the workflow is applied, or from a token-clone on your Mac.

## `en195-apps` — HALT (1 surface)
`voice-slop/index.html`
- **Tick 1 — offline floor: HALT (real).** The page loads an external host, `fonts.googleapis.com`. The studio floor is single-file / offline / no external hosts. Fix: inline or self-host the font, then it clears.
- **Tick 2 — attribution: PASS** (after the calibration below).

## Belt calibration made this run
Tick 2 first flagged a legitimate SOURCE citation — *"Policy text quoted from the Summer 2026 EN195 syllabus (M. Walsh)"* — because it names a term next to a course code. That is provenance, not a student credit. Tick 2 now excludes citation/provenance lines (`syllabus`, `quoted`, `source`, `cite`, `policy`, `licen`, "per the", "from the", "note"). Real student-credit violations — a byline carrying a section token or a term-year — still HALT (verified against a fabricated "Section 02, Summer 2026" credit). A tick that cries wolf has negative agency; this keeps it honest without weakening the real catch.

## Recommended order before arming
1. Fix `voice-slop/index.html`'s external font so `en195-apps` starts green.
2. Reset `confluence-calibration-assessment-hub`'s default branch to `main` (currently a `claude/…` working branch).
3. Apply the workflow stubs with your token (`workflow-stubs/belt.yml` → hub `.github/workflows/`; `workflow-stubs/studio-belt.yml` → each spoke). Flip on the hub's Actions access ("Accessible from repositories owned by walshero") so private spokes can call the reusable belt.
4. Turn on branch protection per repo (require the **Studio Belt** check). That is the moment the ticks gain agency.
5. Optional: add your token as the `STUDIO_SYNC_TOKEN` Actions secret for a scheduled cross-repo sweep.

Tip: if a repo carries pre-existing debt you can't fix immediately (like the font above), arm it in report-mode first — same ratchet pattern `floor.yml` uses — so the belt reports without freezing the repo.
