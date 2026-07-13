# Tableau Sweep — Report
*Weekly read-only entry-paint audit (the "run the belt on all games" loop, ratified 2026-07-12). One file per name; this report is replaced each run, not dated-copied.*
*Run: 2026-07-13 · scheduled, unattended · Gate: `claude/one-thing-gate.py` @ 1280×800 headless Chromium · Doctrine: `claude/tableau-gate-and-room-2026-07-12.md`.*
*Read-only: no game was edited, nothing published. The gate emits moves; fixes are Matt's go, one game at a time.*

> **FILE-COLLISION NOTE (needs Matt).** The scheduled order told this sweep to "update or write `claude/studio-guard-report.md`." That file is already owned by a *different* weekly sweep — the **Studio Integrity Guard** (public-web FERPA probe), which is currently holding a standing **CRITICAL** there (named-student PII live on GitHub Pages, Run #34). Overwriting it would have destroyed that finding. Per studio law ("ONE CANON WRITES, OTHERS READ"), this sweep did **not** touch that file and writes here instead. Recommend the routine's step-4 target be corrected to this filename.

## Bottom line
Swept **21 builds**. **3 PASS · 2 WARN · 16 SHIP-BLOCK.** The gate exited 1 (ship-block present). **Zero emoji on any entry, studio-wide** — the no-emoji floor holds everywhere, cleanly. The block count is real but partly an artifact of scope: several swept surfaces are *hubs, course pages, a decision-lab, and a spec-log*, not scene-first games, and the gate currently grades them by game rules (see Growth Habit below).

**Worst offender (by the gate's arithmetic):** `laughter-foundry-spec-and-log.html` — a 197-word wall, 5 co-equal invitations, 5 competing controls, 0% entry image. (It is a spec/log surface, not a core game — see caveat.)
**Worst among core playable games:** the four text-walls — `choose-your-leader-full`, `convergence-card-engine`, `sandbags-joy`, `flash-ballast` — each opens on prose with no scene.
**Already fixed on the shelf:** `cliche-field.html` still ships the old two-button entry (SHIP-BLOCK), but `cliche-field-v6.html` PASSES — the fix exists; the plain-named file just lags. Promote v6 over it.

## Full table (ranked: SHIP-BLOCK → WARN → PASS)

| Build | Verdict | Entry img | Primary invites | Controls | Prose words | Emoji | Top finding | Surface |
|---|---|---|---|---|---|---|---|---|
| laughter-foundry-spec-and-log | SHIP-BLOCK | 0% | 5 | 5 | 197 | 0 | CRIT wall + HIGH 5 invites | spec/log |
| dark-stop-lab | SHIP-BLOCK | 0% | 5 | 5 | 127 | 0 | CRIT wall + HIGH 5 invites | decision-lab |
| convergence-card-engine | SHIP-BLOCK | 0% | 2 | 2 | 112 | 0 | CRIT wall + HIGH 2 invites | game |
| choose-your-leader-full | SHIP-BLOCK | 0% | 2 | 2 | 110 | 0 | CRIT wall + HIGH 2 invites | game |
| sandbags-joy | SHIP-BLOCK | 11% | 2 | 3 | 109 | 0 | CRIT wall + HIGH 2 invites | game |
| flash-ballast | SHIP-BLOCK | 0% | 1 | 6 | 106 | 0 | CRIT wall + clutter | game |
| en195-last-week | SHIP-BLOCK | 0% | 1 | 5 | 42 | 0 | CRIT wall + clutter | course page |
| en195-what-counts-now | SHIP-BLOCK | 0% | 1 | 5 | 42 | 0 | CRIT wall + clutter | course page |
| warriors-fantasy-arcade | SHIP-BLOCK | 0% | 0 | 21 | 23 | 0 | HIGH no invite + 21 controls | arcade hub |
| funny-boneys-factory | SHIP-BLOCK | 43% | 2 | 7 | 85 | 0 | HIGH 2 invites + clutter | game |
| behind-this-door | SHIP-BLOCK | 13% | 2 | 4 | 36 | 0 | HIGH 2 invites + clutter | game |
| en195-hub | SHIP-BLOCK | 13% | 2 | 4 | 33 | 0 | HIGH 2 invites + clutter | course hub |
| cliche-field | SHIP-BLOCK | 86% | 2 | 2 | 51 | 0 | HIGH 2 invites (v6 fixes) | game |
| PLAY-Cliche-Cabinet | SHIP-BLOCK | 0% | 0 | 3 | 40 | 0 | HIGH no invite | launcher |
| cliche-cabinet-suite | SHIP-BLOCK | 0% | 0 | 3 | 40 | 0 | HIGH no invite | suite launcher |
| cliche-cabinet | SHIP-BLOCK | 0% | 0 | 3 | 40 | 0 | HIGH no invite | launcher |
| the-compound-capstone | WARN | 0% | 1 | 5 | 34 | 0 | WARN img + clutter | game/capstone |
| confluence-console | WARN | 32% | 1 | 4 | 32 | 0 | WARN img + clutter | tool/console |
| cliche-city | PASS | 93% | 1 | 2 | 154 | 0 | clean: one scene, one invite | game |
| cliche-line | PASS | 93% | 1 | 2 | 108 | 0 | clean: one scene, one invite | game |
| cliche-field-v6 | PASS | 55% | 1 | 3 | 34 | 0 | clean: one scene, one invite | game |

*Note: prose-word count is entry-viewport visible text; the two passing canvas games (city/line) show high word counts inside their start card but still PASS because a full-bleed canvas scene fills >90% of the entry — the wall rule only fires when the visual is under 20%.*

## What passes, and why it matters
The three PASSes — `cliche-city`, `cliche-line`, `cliche-field-v6` — all share one shape: **the game surface (a canvas scene or a majority-image SVG) fills the entry, with exactly one primary CTA.** That is the target pattern. Every SHIP-BLOCK is a departure from it: they open on an HTML title card, a menu, or a document instead of the game.

## Failure-class tally (the arithmetic behind the Growth Habit)
Three classes each recur far past the 3-build trigger:

1. **Menu/title-first entry — invitation count ≠ 1 (HIGH): 13 of 21 builds.** Four open with *zero* primary CTA (the cabinet launchers, warriors-arcade); nine open with *two or more* co-equal CTAs. The one-thing floor is the single most-violated rule on the shelf.
2. **Text wall, no scene (CRITICAL): 8 of 21 builds.** Opens on ≥42 words of prose with under 20% entry image.
3. **Control clutter — >3 controls before the player acts (WARN): 11 of 21 builds.** Peak: warriors-fantasy-arcade at 21 controls on entry.
4. **Sub-50% entry image (WARN): 17 of 21 builds.** Only the four canvas/majority-image games clear it.

Clean win: **emoji = 0 across all 21.** The no-emoji floor needs no attention.

## GROWTH HABIT — proposals for ratification (drafted, NOT self-adopted)
The recurring classes are already *caught* by the gate — so the growth move is not "add a check that exists." The distortion the data reveals is upstream: **the gate grades a course hub, a launcher, a decision-lab, and a spec-log by the same scene-first rules it applies to a game.** That inflates the block count and buries the real game findings. Two proposals, Matt's call at a belt close (RED stays gated; drafting is GREEN):

**Proposal 1 — SURFACE-TYPE split in the gate (a new line, tied to a check).**
Give `one-thing-gate.py` three rubrics keyed off a one-line `<meta name="tsp:surface" content="game|hub|doc">` tag (default `game`):
- **game** — scene-first, exactly one CTA, ≥50% entry image (current rules).
- **hub/launcher** — many nav links are fine, but still demand *one* primary CTA (the "start here" door) + a masthead image; don't fire the "wall" on a menu.
- **doc/spec-log** — exempt from wall/CTA entirely; only the no-emoji and contrast floors apply.
This is arithmetic, not prose: the tag is a check, and it stops the gate crying "wall" at things that are correctly documents. It would move ~6 of the 16 blocks (cabinet launchers, en195 pages, laughter-foundry spec-log, dark-stop-lab) out of "broken game" and into their right rubric.

**Proposal 2 — seat a "Scene-First Scaffold" as studio default (a new standard, tied to the passing pattern).**
The three PASSes prove the pattern works. Propose a shared entry-screen scaffold — full-bleed scene ≥50%, one primary CTA, comfort/nav demoted to corner controls — that every new or rebuilt game *starts from*, so builds are born passing instead of being audited into compliance. This is the constructionist "low floor" made literal: the scaffold is the floor.

## Move lists (per SHIP-BLOCK game — for the belt, when Matt greenlights)
Ranked by return. Each is a re-order, not a rewrite:
- **cliche-field** → retire the plain file; promote **cliche-field-v6** (already passes). One move, highest ROI.
- **funny-boneys-factory** → lead with the one CTA ("Step in"); demote "How this plays" to discovered; move the 7 top-bar knobs to a corner; grow the entry SVG past 50%. (This is the First-Bite move list, still owed.)
- **convergence-card-engine / choose-your-leader-full / sandbags-joy / flash-ballast** → open on the game scene, not the prose card; collapse the prose to one line under the scene; pick one CTA.
- **behind-this-door / en195-hub** → choose one primary door; demote the second CTA + palette/back controls to corners.
- **warriors-fantasy-arcade** → the 21-control grid is the whole entry; front it with one "Start" and let the grid be the second screen.
- **cabinet launchers (cliche-cabinet, -suite, PLAY-)** → add one primary "Play" CTA; or re-tag as `hub` under Proposal 1.

## Method note
Staged all 21 builds from the project shelf to `/root/sweep/games/` (the lane the standing loop names). Ran `one-thing-gate.py` unmodified in logic (added only a machine-readable `gate-results.json` sidecar for this report). Repo lane could not be diffed — `raw.githubusercontent.com` returned `PROVENANCE_REQUIRED` unattended (same wall the Integrity Guard hits); the Ledger append is based on the freshly-read shelf copy and is additive-only. Two large suite files (`PLAY-Cliche-Cabinet`, `cliche-cabinet-suite`) were staged via a scaffold-plus-blob transcription and verified to decode; their entry metrics match the plain `cliche-cabinet` launcher, consistent with a shared shell. No canonical game edited; no deploy/publish/send.
