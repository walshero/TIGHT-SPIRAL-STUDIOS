# The 18 day deploy outage

Tight Spiral Studios · 2026-08-24 · Found while answering "is v8 pushed to studio?"

## The finding

`https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/version.json` reads:

    {"sha":"ddd5cfa1d67d5567c76d6ca9da7cb9545ea75109","ref":"main","built":"2026-08-06T18:31:34Z"}

**The live site was last deployed 2026-08-06.** Every commit since then, from every
session, has landed on main and shipped to nobody. Funnybonies v8 was only the build
that made it visible.

## Why nobody knew

`site-watch.yml` exists to catch exactly this and could not. Its freshness check runs
`git` with no checkout in the runner:

    failed to run git: fatal: not a git repository (or any of the parent directories): .git

So the staleness comparison never ran. The job tested liveness only, got HTTP 200 from an
18 day old page, and reported **success**. A watcher that cannot tell live from stale is
not a watcher. This is the same failure class the belt already names twice: a gate that
has gone blind must never read as clean.

## The chain

`floor.yml` runs `bash studio-belt.sh .` and `deploy: needs: floor`. One flat-tick HALT
anywhere in the corpus stops Pages for **every project in the repo**. Landing bytes on
main is not shipping.

## What was actually halting it

Full belt run, 2026-08-24, all 11 ticks. Ticks 1, 3, 4, 6, 7, 8, 9, 10, 11 pass.

**TICK 1 (fixed today).** Three separate causes, all cleared, 0 HALTs across 113 surfaces:
- Eight deliberately-broken canary fixtures at the repo ROOT (`*-canary-*.html`) were
  swept as corpus. The 2026-08-09 fix for this named one directory instead of the
  pattern, so it only half-landed.
- `the-break-room-v2.html` and `confluence-hub` both had correct dark palettes mounted on
  selectors comfort-gate does not drive (`html[data-comfort]`, `@media`). Mounted on
  `body.night` / `body.dusk` as well. No new palette invented.
- `confluence-hub/` is an ES-module SPA shell that paints nothing from `file://`, so every
  render gate returns "no measurable text". Excluded loudly, with the gap named: measuring
  it for real needs a served-page harness.

**TICK 2 (open).** Five lines, all governance records naming a term, none of them student
credit lines:
- `TSP_Ledger.md:377` (department co-req policy history, "Fall 2024", "2023-24")
- `confluence-TRUNK.html` x4 (governance-approved EN202 title, "effective Spring 2027")

The tick already carves out `syllabus|quoted|source|cite|policy|...`; these lines carry
none of those words. **A governance record naming a term is not a student attribution.**
Either widen the carve-out or carry them in `attribution-baseline.json`.

**TICK 5 (open).** Two entries genuinely regressed against the ratchet:
- `enjambment-skins.html` - 130 words of prose, no scene, and NO invitation at all
- `leeder/index.html` - 46 words of prose, largest visual 18% of entry

Real defects in the entry paint, in two other lanes, and NEW rather than carried.

## The structural problem, stated plainly

**A build that passes all eleven ticks cannot ship because of a course code in a ledger
file and a prose wall on a poetry page.** Funnybonies v8.1 is clean on every tick and has
been unreachable for a day; the rest of the site has been frozen for eighteen.

Coupling deploy to a corpus-wide floor means any one lane can hold every other lane
hostage, indefinitely, silently. `floor.yml`'s own comment records this argument being had
before: coupled 2026-07-14, decoupled 2026-07-28 over a near-universal 18px floor, and
re-coupled 2026-08-08. The pattern repeats because the coupling is the problem, not the
particular gate that trips it.

**Recommended: gate deploy on CHANGED FILES, keep the corpus sweep as a reporting job.**
The preflight lane already works this way and is the belt's own documented success story.
A red corpus should raise an alarm, not stop the presses.

**Tradeoff:** a page nobody touches can rot unwatched. Mitigation is the alarm, and an
alarm that actually works, which `site-watch.yml` currently does not.

**Simpler:** fix the two tick-5 entries and baseline the five tick-2 lines. Ships today,
leaves the coupling in place, and the next unrelated lane does this again.

**Advanced:** the above, plus repair the Site Watch git call so staleness is measured, plus
a hard fuse: if live sha and main sha differ for more than N hours, open an issue.

## Founder call needed

Which of the three. Nothing here is mine to decide: tick 5 is two other lanes' design work,
tick 2 is a governance-voice question, and the coupling is a governance decision this repo
has already reversed twice.
