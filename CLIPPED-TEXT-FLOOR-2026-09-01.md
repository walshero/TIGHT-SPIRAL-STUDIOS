# The Flok research card, and what it says about Studio Eyes and Studio Fingers

**2026-09-01.** Founder report: *"In Flok, when I click why does this work, the response
is hidden in a too small window."*

Reproduced on the first try, and it is worse than "too small": the card does not just
crop the research, it **slices the first line through the x-height** and **cuts the
citation in half**. Measured on a 412x915 phone, `the-console.html` at lever 1:

| | box | content | lost |
|---|---|---|---|
| `.flip-wrap` (default) | 68px | 85px | 8px past the clip, first line and citation both cut |
| `.flip-wrap` (se-a1, 1.15x) | 68px | 85px | 10px |
| `.flip-wrap` (se-a2, 1.30x) | 68px | 94px | 23px |

Every comfort stop made it worse, which is the part that matters: the reader who most
needs the text bigger loses the most of it.

## The defect

Two causes, stacked, and both are the same mistake in different clothes — **a number
deciding how much text you get to read.**

1. `.flip{min-height:68px}` with `.flip-face{position:absolute;inset:0}`. An
   absolutely-positioned face contributes nothing to its container's height, so the
   card was sized by the SHORT face ("Why does this work?") and the long one — the
   answer — was laid out into a box that could never hold it. The card was 68px tall
   whatever the research said.
2. `#sc-train .flip-wrap{max-height:120px;overflow:hidden}`, a collapse for the locked
   state that never let go of the reveal. 120px was picked once against one font size.

**Fix.** The faces are grid-stacked into one cell, so the row is `max(front, back)` and
the text sets the box. The collapse became `0fr -> 1fr`, which animates the same way and
has no ceiling to grow into when open. The 68px floor moved off `.flip` and onto the
faces — an item carrying a min-height cannot shrink, and leaving it there broke the
collapse (see below).

Verified at 412x915, 360x640, and both comfort stops, on all five levers: nothing
clipped, collapse still 0px, flip still works by click and by Enter.

The same shape was found and fixed in `studio/elves-house.html` — absolute faces over a
96px `.flipinner`. It looks fine at 100% and pushes the answer outside the card border
on all four cards at WCAG 1.4.4's own 200% resize.

## What this says about the gates

**The bug was not missed by one gate. It was invisible to the whole belt**, and for two
different reasons that are worth keeping apart.

### Studio Eyes had no floor for it

Ten floors, all green on this file. Contrast 12:1. Target 340x68. Focus ring present.
No floor had ever asked the one question that decides whether the founder can read the
page: **is the text still there after the compositor is done?** A tool built for a reader
with retinitis pigmentosa that cannot see text disappear is looking through the wrong end
of itself.

Floor 11 (`CLIPPED_TEXT`) now measures it, with two canaries — `t13-clipped-text.html`
(the Flok card reduced to its bones) and `p09-legit-clips.html`, the false-positive trap
holding a scroll window, a closed disclosure, sr-only text and an ellipsis label. A box
and a window both clip and only one is broken; the separation is a measured ratio
(1.12 for the defect, 4.66 for Flok's own diegetic phone feed), not a judgment call.

### Both gates measure ONE STATE, and that is the deeper hole

Floor 11 **would not have caught the bug that caused it.** Studio Eyes audits first
paint; Flok's card sits behind three clicks (Clock in -> hit the target -> flip), where
it is empty and collapsed. Run the new floor against the broken build and it correctly
finds nothing.

Studio Fingers has the same hole and already knew: its `advance_past_entry` docstring
names the finding and leaves it OPEN — *"the durable fix is geometry measured at every
state the crawler in playthrough-agent.py already visits."* Its narrow door-opening
repair advanced past an entry gate on **zero of fourteen** sampled surfaces, because
every real TSP build opens with more than one control. Flok is one of them: Fingers has
never measured a single one of Flok's game screens. It reports "every hand lands" about
the hire screen.

So the fix is the one Fingers wrote down in August and nobody built. `playthrough-agent.py`
was already walking the states — up to 40 clicks, staying in-file, per build. Nobody was
measuring them. It now runs `CLIP_PROBE` at first paint and after every click that lands,
imported from `studio-eyes.py` rather than copied (one canon writes, others read; a
second copy of that arithmetic would drift from the floor it mirrors). If the import
fails the card says **CLIP FLOOR NOT RUN** — a check that went missing must not read as
a check that found nothing.

Wiring the probe in was not enough on its own. The crawler reached the training screen
in nine clicks and stood there reporting a locked card, because three things in it were
each individually reasonable and together blind:

- **It pressed each label once.** Games are made of repeated actions; Flok's card unlocks
  when the engagement meter passes its target, which takes seven or eight presses of one
  button. Now, once breadth is spent, controls that are still ANSWERING get pressed again
  (`REPEAT_MAX = 12`). One mechanical rule that reads the same on every surface — not the
  per-file recipe studio-fingers named and rejected. A repeat that changes nothing is
  exempt from DEAD BUTTON: a meter at its ceiling is finished, not dead.
- **A click that timed out burned the label anyway.** The card is `pointer-events:none`
  until the target is hit, so the one control that mattered was crossed off before the
  presses that unlocked it, and never tried again. "Not clickable in place" usually means
  "not clickable YET"; blocked controls are now retried in the same pass.
- **It measured mid-animation.** 350ms into a 500ms flip, a card's axis-aligned box
  projects a couple of px wider than the card is — which reported a correct front face
  clipping itself by 2px. It now waits for the page's own animations to settle, bounded.

Two false positives had to be closed in the floor itself before any of this was
trustworthy, and both are in the canary now: an **SVG label** (laid out on a viewBox,
not a scroll box) and a **hidden backface** (the turned-away face of a flip card still
reports `visibility:visible`, and its projected box is wider than the card). The backface
test is exact rather than heuristic — accumulate the transform chain and read the z
component of the transformed normal; one `rotateY(180deg)` is -1, two is +1.

**Against the shipped build the crawler now finds the founder's bug, unaided:** the fact
cut by 8px and the citation cut by 8px inside a 68px box, after 40 clicks with no
per-file knowledge. Against the fix it is clean.

### It caught two regressions in the fix, the same afternoon

1. The first version used `grid-template-rows:0fr` for the collapse while `.flip` still
   carried `min-height:68px`. A grid item with a min-height cannot shrink, so the locked
   card stopped collapsing to 0 and started clipping its own front face — a NEW defect,
   of exactly the class just fixed, introduced by the fix. The floor moved onto the faces.
2. The second used the implicit `auto` grid column, which sizes to the face's MAX-CONTENT,
   so "Why does this work?" pushed the card 3px past its own 340px wrap. Now
   `grid-template-columns:minmax(0,1fr)`.

Both were reported by the crawler on the next run, in states no first-paint floor can
reach. That is the whole argument for wiring it in.

## What the floor found on the rest of the corpus

First paint only, 122 surfaces (86 root + 36 `studio/`), after the false positives above
were closed. Four hits, all real, none fixed here:

- **`cliche-city.html`, `cliche-field.html`, `cliche-line.html`** — and this one is worse
  than the card that started it. `#stage` is a fixed `aspect-ratio:3/2` box with
  `overflow:hidden`, and on a 390px phone the start screen overflows it: the game's
  TITLE, its tagline and its START button are all cut off the top and bottom. The player
  sees a paragraph of rules with no title and no visible way to begin. Three games.
- **`enjambment-skins.html`** — a poem line hard-cut mid-phrase inside a 278px `.tick`
  panel with `white-space:nowrap`, no ellipsis, no scroll. By this floor's own rule
  ("an ellipsis is a promise that there is more; a hard slice says nothing at all")
  that is a defect, which is why it is deliberately not in the pass-trap canary.

Left unfixed on purpose: each needs a design call (does the stage scroll, or does the
type shrink?), and three more games is a different job from the one that was asked for.

## Still open

- **Studio Fingers still measures first paint only** for its own floors (F-TAP, F-ZOOM).
  A 20px control that only exists on screen three is still invisible to tick 7. The
  crawler is now proven as a place to measure from; the touch floors have not moved
  there yet.
- **Nothing in the belt tries WCAG 1.4.4's 200% resize.** Both flip cards were correct
  at 100% and broken at 200%; elves-house was found by hand, not by a gate.
- **Nothing runs either of these in CI, and that is the biggest one.** `floor.yml`
  invokes `studio-eyes-sweep.py` (v4, no JS) and the belt. It does NOT invoke
  `studio-eyes/studio-eyes.py`, despite `canon-manifest.json` recording that role as
  "WIRED into floor.yml this session (report mode)" — the workflow says otherwise, and
  the workflow is the truth. `playthrough-agent.py` is not invoked either. Floor 11 and
  the state crawl are real and self-tested and **nothing calls them on a push.** The
  change is two report steps beside the existing one:

      - name: STUDIO EYES v3 — JS/dynamic-state floors (report)
        run: python3 studio-eyes/studio-eyes.py --self-test
        continue-on-error: true
      - name: PLAYTHROUGH — clipped text in every state the crawler reaches (report)
        run: python3 playthrough-agent.py --dir .
        continue-on-error: true

  Left undone deliberately: a 40-click crawl across 100+ surfaces on every push is a
  standing CI cost, and cost discipline is a founder ruling, not a detail to decide
  around. Scoping it to changed files is the obvious first shape. **Founder's call.**
- **`#sc-train` claims to fit one phone screen.** It does not, and did not before this
  change: 324px of vertical overflow at 412x915, 534px at 360x640. Out of scope here,
  named so it is not lost.
