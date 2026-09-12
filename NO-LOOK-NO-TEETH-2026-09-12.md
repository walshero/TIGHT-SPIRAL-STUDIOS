# No look and no teeth are one defect

**2026-09-12 · closing the lane opened by "the response is hidden in a too small window" (2026-09-01)**

The lane fixed a card, 44 rails, a skin and three gate defects. It also kept turning up the
same thing in different costumes, five times in one day, and the fifth was mine. This is the
reconciliation the lane needs before it can close.

## The two complaints, and why they look opposed

**No look.** A gate that never measured something reports the same as a gate that measured it
and found nothing. Studio Eyes had ten floors green over text sliced through the x-height.
studio-fingers has never measured a single one of Flok's game screens. The contrast floor could
not pass *any* gradient and nobody knew, because it shipped with a HALT canary and no PASS
canary. comfort-gate is blind to `background-image` on every surface in the corpus. And the
changed-surface step I added to `floor.yml` to fix all this swallowed git's stderr, emitted an
empty list, and reported success on a merge that touched 45 surfaces.

**No teeth.** `floor.yml` has failed on every push for weeks — 1094 through 1128, unbroken.
`deploy: needs: floor`, so nothing has shipped. The playthrough sweep has reported the same
five findings on 2026-08-28, 08-31 and 09-07: **0 FIXED**. A reporter that reports forever and
changes nothing.

These read as opposite problems with opposite fixes. Measure more. Block less. Each fix makes
the other complaint worse, which is why the lane kept oscillating.

## They are the same defect at three altitudes

In every one of these cases, **an absence and a clean result are represented by the same thing.**
Silence is doing two jobs.

| altitude | the two things sharing one representation |
|---|---|
| a **finding** | "looked, found nothing" vs "did not look" |
| a **gate** | "armed and clean" vs "not mounted anywhere" |
| an **exemption** | "no debt" vs "debt carried and never printed" |

No teeth is the same collapse seen from the other end. A tick red on every push has merged
"this push broke something" with "this repo has debt" into one red, so red stopped carrying
information and everyone learned to scroll past it. That is not a separate disease. That is
overloaded silence again, wearing red instead of green.

**The rule:**

> Nothing is allowed to mean two things.
> An absence must have its own representation, and that representation is never green.
>
> - A finding has three verdicts: PASS · HALT · **DID NOT LOOK**.
> - A gate that is not mounted must say so where it would have run.
> - An exemption must print its size and its age on every run.
> - A ratchet is not leniency. It is how you keep red meaning exactly one thing.

Teeth without a baseline is permanent red, which is no teeth.
A baseline without an inventory is invisible debt, which is no look.
You need both halves or you have neither — and that is the whole reconciliation.

## The studio already ruled both halves, in separate lanes, and never joined them

This is not a new rule. It is two existing rulings that have never been in the same sentence:

- **2026-08-06, resolve-canon lane:** *"'not mounted' and 'not there' are different facts and
  must never share a return value."* That is the no-look rule, ruled and implemented — for one
  function, in one tool.
- **2026-08-08, belt lane:** *"RATCHET not flat because a tick red on every push is a tick
  everyone scrolls past."* That is the no-teeth rule, ruled and implemented — for five ticks.

Neither cites the other. So each has been violated in the other's name ever since: gates added
for thoroughness went blind, and blindness was tolerated to avoid noise.

The belt had already invented both answers and applied neither uniformly. `SKIPPED LOUD —
… this gate is BLIND. Not a pass.` exists on **3 of 12** ticks. A carried-debt announcement
existed on **1 of 11** baselines.

## What was measured on the day the lane closed

- **7,405 findings carried across 629 surface-slots in 11 baselines** — type 4,171 · voice
  2,443 · contrast 248 · fingers 194 · the rest smaller. Every one frozen 2026-08-23.
  Ten of the eleven were announced by nothing. A tick carrying 4,171 findings and a tick
  carrying none both printed `pass`.
- **The first count this session took was 4,613 — wrong low**, because it read `counts`/`files`
  and several baselines key their debt on `debt`. The measurement of the invisible debt was
  itself a no-look. That is why `carried()` reads all three keys instead of a number living in
  this document.
- **`stale-fuse.py` is the whole reconciliation, already built and mounted on nothing.** It was
  written 2026-08-17 on the founder ruling *"Go. configure with teeth."* Its docstring contains
  this lane's entire doctrine — three kinds of stored state with three different teeth, and
  *"an auditor that cries wolf trains the founder to ignore it."* Its self-test passes.
  `--verify --all` correctly exits 1. Belt references: **0**. `floor.yml` references: **0**.
  Meanwhile `canon-manifest.json` — the file that declares which gate is canon, and which the
  ledger records was once declared **backwards** — has been stale since 2026-08-27.

That is the third recorded instance of *"a gate not on the belt does not run"*, after
studio-fingers, resolve-canon and stage-push in August. The studio's failure mode is not
building the wrong thing. It is building the right thing and never mounting it.

## What this commit changes

1. **`carried()` in `studio-belt.sh`** — ticks 1, 3, 4, 5 and 7 now print what their baseline is
   carrying, how many surfaces it spans, and how old it is. Verified against the pre-edit belt
   on two surfaces: **not one verdict changed.** It adds no teeth and removes no teeth. It makes
   7,405 exemptions visible on every run, and makes the trend readable, which is the only thing
   that lets "may only shrink" ever be checked.
2. **Tick 12 mounts `stale-fuse.py`** — the rot is now printed on every run, including the two
   stale registries and all eleven drifted baselines.

## What it deliberately does not change, and why

Tick 12 **reports and does not block**, and that is the rule being applied, not dodged.
Six ticks are already red on every push. A seventh red tick on a belt nobody can get green does
not add teeth; it adds noise, and noise is exactly how this belt lost its teeth in July.

**Arm a gate green, or do not arm it.** The trigger is recorded in the tick: add `fail=1` to its
non-zero branch the day the belt can be green. Registry drift is the cheapest of the seven to clear and the fuse
prints the regenerate command for each — but `canon-manifest.json` is CURATED, and re-stamping
it to buy a green tick, without a human deciding what `nowalls.py`, `pixel-ratchet.py` and
`studio-eyes-pixel.py` are, would be manufacturing a pass. That is the founder's call, not a
side effect of closing a lane.

I state that plainly because on 2026-09-01 I wrote the no-look rule into a commit message and
broke it in the same push. A rule you apply only when it is convenient is a preference.

## The open quote, for whoever takes the next lane

**CORRECTED 2026-09-12, after this document's first version was wrong about it.**

The first version of this table said seven red ticks, put 44 surfaces under the image
floor and 84 under the voice floor, and concluded that two of them "need a founder scope
ruling". **There is no scope ruling.** Ticks 3 and 4 are GREEN in CI, 116 surfaces each.

The false numbers came from running the belt in this container, where the clone is
`.../tight-spiral-studios` and every baseline keys its debt `TIGHT-SPIRAL-STUDIOS/<file>`.
GitHub serves the same repo under any casing; the ratchet key is case-sensitive. So every
carried finding read as new debt. Same file, same gate, changing only the casing: **HALT
vs PASS.** CI checks out the canonical casing and never saw it.

That is this lane's own defect, third sign, caught inside the document written to close
the lane: a gate that cannot find its baseline does not go quiet — it cries wolf on
everything, and a gate that fires on everything has told you nothing. "Carried" and "new"
were sharing one representation. `studio-belt.sh` now adopts the baseline's casing, says
so when it differs, and says **loudly** when nothing matches instead of printing a wall of
phantom regressions that reads like a broken corpus.

### The real red set — CI run 1128, main @ `1059695`, 2026-09-07

| red tick | what is actually failing | size |
|---|---|---|
| 1 · comfort-gate | `funnybonies/index.html`, `index.html` | 2 surfaces |
| 2 · attribution | one NEW course credit carrying a year/section token | 1 line |
| 5 · entry paint | `en195-hub` · `enjambment-skins` · `floor-status` · `funnybonies/index` | 4 surfaces |
| 10 · contrast sweep | `funnybonies/index.html`, 1 failing element, baseline 0 | 1 element |
| 11 · intent | 3 builds with no `spec-source` / `audience` meta | 6 metas |
| 12 · stale-fuse | 2 registries stale since 08-27 *(reported, not armed)* | 1 human call |

**`funnybonies/index.html` is in three of the five.** `index.html` is in one more. The belt
is not red because the corpus is broken; it is red because one recent build is, plus three
entry screens, six missing meta tags and a single credit line.

Going green is a morning's work by one person. It requires **no ruling, no scope
negotiation, and no re-baselining** — which is the opposite of what the first version of
this document said, and the reason it is worth saying twice: *the estimate that says a
job is too big to start deserves the same verification as the finding that says a build
is broken.* This one was wrong because a tool measured the wrong thing quietly, which is
the sentence this whole lane is about.

Until that list is empty, every gate this lane built is worth nothing — including the
clipped-text floor that found a real defect in `choose-your-leader-v7` on 09-07 and has
sat unfixed since.
