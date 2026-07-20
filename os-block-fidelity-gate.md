# OS BLOCK — FIDELITY GATE (content coherence)

STATUS: spoken floor LIVE now · arithmetic gate is THE WAY (not yet built)
OWNS: the gap between what the brief specified and what the build shipped
SITS: pipeline Stage 5, beside preship-contrast-gate.py — same HALT contract

---

## WHY THIS EXISTS

Every existing gate checks the CONTAINER — bytes, contrast tokens, nav, lanes.
Nothing checks the PAYLOAD — whether the built thing is the thing Matt saw.
Scene coherence kept failing for the same reason contrast used to: it was
JUDGED in prose by the Convening seats, never COMPUTED against a spec.
Same disease as the amber-as-text bug, same cure: turn the judgment into arithmetic.

Named failure mode this closes: SPEC-RICH, BUILD-POOR — governance ships
faster than fidelity, and the build drifts off-vision unnoticed until Matt sees it.

---

## THE THREE NAMED THINGS (the brief slots)

A pitch is not ready to build until all three are NAMED and CONCRETE:

  1. THE IMAGE  — scene anchor. The one image/moment screen 1 is about.
                  Concrete thing seen, not a mood. ("child at the radio, Oct 1962")
  2. THE VERB   — what the player can now DO that they couldn't. One verb, ≤2 taps.
  3. THE SOURCE — the named, attributed, open-license text/domain the content rests on.
                  Averaged-internet fill is a failure, not a source.

Plus one count: DECISIONS PER SCREEN. Floor is one. More than one HALTs.

Front door for these = tsp-intake.html. It emits brief.json.

---

## THE CHECK — 4 NOW

Spoken, at Convening close and before any build begins:

  "Name the image, the verb, and the source. If you can't name all three,
   you're not ready to build."

Any blank slot HALTs the build. decisions_per_screen > 1 HALTs.
This is the floor. It runs today, by memory law, no tooling.
"We don't always follow the way" — the spoken check is what keeps us honest
until the arithmetic exists.

---

## THE WAY — 1 (destination)

preship-fidelity-gate.py — reads brief.json (emitted by tsp-intake.html),
diffs it against the built HTML, same exit contract as the contrast gate:

  scene_anchor  → is the named anchor image present and >50% of screen 1?
  player_verb   → is a handler wired that delivers that verb in ≤2 taps?
  named_source  → is the source string present in the attribution/footer?
  decisions_per_screen ≤ 1 per screen, else HALT.

  exit 0 = ship · exit 1 = HALT with the missing/failing slot named.

Blocked on: the Convening emitting structured brief.json per build.
That is a founder-in-the-room build session, not a background task.

---

## DOCTRINE FIT

- IF A RULE CAN'T BE A CHECK, IT'S A WISH. Scene coherence was a wish.
  4 makes it a spoken check today; 1 makes it arithmetic.
- The fix for judgment that keeps failing is arithmetic, not more prose.
- The intake form and the fidelity gate are ONE system from both ends:
  the form collects the three; the gate checks the build against them.

---

## ARTIFACTS
  tsp-intake.html          — front door, emits brief.json (LIVE, gate-passed 11.19)
  preship-fidelity-gate.py — the way (NOT YET BUILT)
