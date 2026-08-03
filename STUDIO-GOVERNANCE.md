# STUDIO GOVERNANCE — the timing belt across five repos
*Tight Spiral Studios · adopted 2026-08-03. Hub-and-spoke: one canon writes, the others mount and run it.*

## The shape

- **Hub — `walshero/TIGHT-SPIRAL-STUDIOS`** owns the canon and the ticks. It is the only repo that WRITES governance.
- **Spokes (mount, read-only)** — `en195-apps`, `confluence-calibration-assessment-hub`, `-writerly-moves-game`, `matt-radar`. Each MOUNTS the hub at CI time and RUNS the belt against its own files. No spoke copies the gates; copying is the drift generator the studio already diagnosed. **Mount, never copy.**

## The belt — `studio-belt.sh`

One runner, all five repos. Every tick BLOCKS (`exit 1`) — agency, not a wish.

- **Tick 1 — accessibility floor** (`comfort-gate.py`): real-pixel contrast in day / dusk / warm-dark, a dark palette present, offline (no external hosts), no emoji. Matt has retinitis pigmentosa; contrast is arithmetic, not a judgment.
- **Tick 2 — student attribution standard**: a course code (`EN###`) may not sit on a line carrying a section token or a term-year (e.g. "Summer 2026"). Generic course lines ("EN195 Creative Writing (summer 6-week online)") pass; changelog dates ("2026-07-11") pass. Full-surname detection stays human/AI review — see `student-attribution-standard.md`.

Extend the belt by adding a tick here; every spoke inherits it on the next run. That is the recruitment habit with teeth.

## Two scopes — why arming needs the founder's token

The Zapier connector writes everything EXCEPT `.github/workflows/` — that path needs the `workflow` OAuth scope the grant does not carry (probed 2026-07-28: identical PUT, 404 under `.github/workflows/`, 201 at repo root). So the work splits:

- **Connector (any session, no token):** the belt, the canon, the gates. Editable forever.
- **Founder token (one-time, off-transcript):** the `.github/workflows/*.yml` stubs that call the belt, plus the cross-repo `STUDIO_SYNC_TOKEN` Actions secret. The token lives in local git config or an Actions secret — NEVER in a chat. A transcript-exposed token must be rotated; the studio already has that scar.

## Arming (founder, once)

1. Drop the workflow stub into each repo's `.github/workflows/` — the hub's reusable `belt.yml`, and each spoke's `studio-belt.yml`. Apply with your token from your Mac, or paste in the browser.
2. Turn on branch protection per repo: require the **studio belt** check to pass before merge. That is what gives the tick agency — a failing tick becomes a wall the push cannot climb.
3. (Optional, cross-repo sweep) add your token as the `STUDIO_SYNC_TOKEN` secret in the hub; the scheduled sweep fans out nightly and files an issue on any repo that drifts from canon.

## Prerequisite

`confluence-calibration-assessment-hub`'s default branch is a `claude/…` working branch, not `main`. Reset it to `main` before the belt runs, or the belt judges the wrong HEAD.

## Status

Belt runner and this doc: landed via connector (dormant — nothing runs them until the workflow stubs are applied). Workflow stubs + branch protection + secret: owed to the founder's token. Until then the belt is present and inert by design.
