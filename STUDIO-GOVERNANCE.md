# STUDIO GOVERNANCE — the timing belt across five repos
*Tight Spiral Studios · adopted 2026-08-03. Hub-and-spoke: one canon writes, the others mount and run it.*

## The shape

- **Hub — `walshero/TIGHT-SPIRAL-STUDIOS`** owns the canon and the ticks. It is the only repo that WRITES governance.
- **Spokes (mount, read-only)** — `en195-apps`, `confluence-calibration-assessment-hub`, `-writerly-moves-game`, `matt-radar`. Each MOUNTS the hub at CI time and RUNS the belt against its own files. No spoke copies the gates; copying is the drift generator the studio already diagnosed. **Mount, never copy.**

## The belt — `studio-belt.sh`

One runner, all five repos. Every tick BLOCKS (`exit 1`) — agency, not a wish.

- **Tick 1 — accessibility floor** (`comfort-gate.py`): real-pixel contrast in day / dusk / warm-dark, a dark palette present, offline (no external hosts), no emoji. Matt has retinitis pigmentosa; contrast is arithmetic, not a judgment.
- **Tick 2 — student attribution standard**: a course code (`EN###`) may not sit on a line carrying a section token or a term-year (e.g. "Summer 2026"). Generic course lines ("EN195 Creative Writing (summer 6-week online)") pass; changelog dates ("2026-07-11") pass. Full-surname detection stays human/AI review — see `student-attribution-standard.md`.
- **Tick 3 — the >50% image floor + render proof** (`preship-gate-v4.py --ratchet`): founder canon C7. Ratcheted.
- **Tick 4 — founder voice** (`studio-voice-gate.py --ratchet`): the 2026-08-05 ruling, with teeth. Ratcheted.
- **Tick 5 — entry paint** (`one-thing-gate.py --ratchet`): scene-first, exactly one invitation, and the instruction wall — measured **phone-first at 390x844**, because until 2026-08-07 this was the one instrument in the studio that measured a laptop. Ratcheted.

Ticks 3-5 added 2026-08-07. Until then the belt carried two ticks and **none of the four things the founder had actually ruled on** — the image floor, the voice, the entry grammar — each of which already had a working gate in the hub that nothing ever called.

**Why 3-5 ratchet and 1-2 did not.** Measured before arming: voice HALTed 101 of 131 surfaces, entry-paint 31 of 38 builds, comfort-gate 23 of 131. A tick red on every push is a tick everyone scrolls past — that is how `floor.yml` lost its teeth in July. Today's debt is carried in hub-owned baselines; only NEW debt blocks. Baselines may only shrink. Tick 1 was given the same treatment on 2026-08-07 so the belt could be mounted on the hub at all.

Extend the belt by adding a tick here; every spoke inherits it on the next run. That is the recruitment habit with teeth.

## Two scopes — why arming needs the founder's token

The Zapier connector writes everything EXCEPT `.github/workflows/` — that path needs the `workflow` OAuth scope the grant does not carry (probed 2026-07-28: identical PUT, 404 under `.github/workflows/`, 201 at repo root). So the work splits:

- **Connector (any session, no token):** the belt, the canon, the gates. Editable forever.
- **Founder token (one-time, off-transcript):** the `.github/workflows/*.yml` stubs that call the belt, plus the cross-repo `STUDIO_SYNC_TOKEN` Actions secret. The token lives in local git config or an Actions secret — NEVER in a chat. A transcript-exposed token must be rotated; the studio already has that scar.

## Arming (founder, once)

1. Drop the workflow stub into each repo's `.github/workflows/` — the hub's reusable `belt.yml`, and each spoke's `studio-belt.yml`. Apply with your token from your Mac, or paste in the browser.
2. Turn on branch protection per repo: require the **studio belt** check to pass before merge. That is what gives the tick agency — a failing tick becomes a wall the push cannot climb.
3. (Optional, cross-repo sweep) add your token as the `STUDIO_SYNC_TOKEN` secret in the hub; the scheduled sweep fans out nightly and files an issue on any repo that drifts from canon.

## Prerequisite — MET (re-measured 2026-08-07)

~~`confluence-calibration-assessment-hub`'s default branch is a `claude/…` working branch.~~
Its default branch **is `main`**. Nothing is owed here.

## Status — RE-MEASURED 2026-08-07

**This section asserted the belt was "present and inert by design". That was false within a
day of being written, and nothing detected the drift.** Measured against live CI:

| repo | belt mounted | runs | state |
|---|---|---|---|
| `matt-radar` | yes | 6 | green (latest 2026-08-04) |
| `en195-apps` | yes | 1 | **RED since 2026-08-04**, unread for three days |
| `-writerly-moves-game` | yes | — | holds no HTML surfaces |
| `confluence-…-hub` | **no** — carried its own copied gates | — | mount pushed 2026-08-07 on `claude/mount-the-studio-belt` |
| **hub (this repo)** | **no** — `belt.yml` was `workflow_call` only, no stub | — | stub added 2026-08-07 |

Two consequences worth naming plainly:

1. **The belt was live and its failure went unread.** A tick with agency that nobody reads
   is a tick without agency.
2. **The hub was never on its own belt**, so the belt reached the three HTML surfaces the
   spokes hold between them and none of the 131 in the hub — every game included.

Also stale: the claim that workflow files are "owed to the founder's token". The **Zapier
grant** genuinely cannot write `.github/workflows/` (no `workflow` scope, probed
2026-07-28). A session container's authenticated git lane **can** — workflow files were
written and pushed that way on 2026-08-07. Keep the Zapier limitation; drop the blanket.

**Standing correction, and the reason this table has dates in it:** a status section
without a measurement date is a suspicion. Re-measure before trusting this block.
