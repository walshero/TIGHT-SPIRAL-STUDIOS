# INSTRUCTION WALL QUEUE — measured debt, phone width

> **Founder, 2026-08-07:** *"a wall of directions that were irrelevant and unreadable
> for my phone."* This is that defect, counted. Measured by `one-thing-gate.py` at
> **390x844**, chrome excluded: words of prose sitting above the first control you can
> actually use, and how many screens down that control sits.
>
> **Why this file exists rather than a silent baseline.** The debt is carried by the
> ratchet so the belt stays mountable, and a carried defect with no queue is a defect
> that disappears. This is the queue. It may only shrink.
>
> **Last measured:** 2026-08-07 · 74 **root-level** surfaces · **33 carry a wall**
>
> Scope note so the numbers reconcile: this queue lists root-level `*.html` only, because
> those are the surfaces with word-counts measured in the sweep. The belt's baseline
> (`one-thing-baseline.json`) covers all **131** surfaces including `studio/`, `fys/` and
> the canaries, and across that full corpus the counts are **52 `INSTRUCTION-WALL`**,
> **29 `ACTION-BELOW-FOLD`** and **4 `H-OVERFLOW`** (pages that scroll sideways at 390px).
> The baseline is authoritative; this file is the human-readable worst-first queue.

## The thresholds

- `INSTRUCTION-WALL` — more than **60 words** above the first control.
- `ACTION-BELOW-FOLD` — first control more than **1.0 screens** down.

## The queue, worst first

| words before you can act | screens to act | entry image | surface |
|---:|---:|---:|---|
| 1386 | 18.15 | 80% | `fys_fys-treasure-trove.html` |
| 301 | 2.56 | 0% | `islo-hub.html` |
| 240 | 2.79 | 56% | `old-problems-at-new-speed.html` |
| 207 | 1.42 | 0% | `advantage-intake.html` |
| 190 | 2.35 | 0% | `confluence-massbay-assessment.html` |
| 181 | 1.17 | 0% | `ai-resilient-assignment.html` |
| 174 | 1.88 | 2% | `index.html` |
| 174 | 1.28 | 2% | `who-holds-the-room.html` |
| 157 | 1.33 | 0% | `motion-specimen.html` |
| 146 | 0.86 | 0% | `review-bench.html` |
| 141 | 0.97 | 2% | `whose-draft.html` |
| 132 | 0.79 | 1% | `workshop-wall.html` |
| 131 | 0.92 | 2% | `score-the-room.html` |
| 128 | 0.97 | 2% | `scorer-norming.html` |
| 127 | 1.36 | 8% | `flash-ballast.html` |
| 118 | 0.91 | 2% | `real-cost.html` |
| 117 | 0.75 | 0% | `close-the-loop.html` |
| 116 | 0.74 | 0% | `rubric-forge.html` |
| 107 | 0.89 | 21% | `the-tell.html` |
| 106 | 0.9 | 2% | `update-the-model.html` |
| 104 | 1.21 | 7% | `sandbags.html` |
| 102 | 0.67 | 0% | `comfort-kernel-v2.html` |
| 99 | 0.81 | 2% | `sticker-price.html` |
| 99 | 0.66 | 0% | `en195-what-counts-now.html` |
| 95 | 0.97 | 0% | `workshop-in-a-box.html` |
| 95 | 0.56 | 0% | `comfort-kernel.html` |
| 91 | 0.61 | 0% | `en195-last-week.html` |
| 86 | 0.64 | 0% | `course-river.html` |
| 80 | 0.63 | 0% | `studio-aleph.html` |
| 77 | 0.83 | 17% | `play-the-semester.html` |
| 62 | 0.7 | 0% | `tsp-intake.html` |
| 44 | 1.09 | 53% | `behind-this-door.html` |
| 44 | 1.02 | 54% | `table-four.html` |

## How a row leaves this queue

Move the first real control above the fold and cut the preamble to what the player
needs *at that moment*. Directions belong attached to the action they describe, not
stacked at the front (FTUE practice, `aleph-lenses/L2.md`). Then re-run:

```
python3 one-thing-gate.py --ratchet --repo=TIGHT-SPIRAL-STUDIOS <file>
```

A repair that does not move its own gate is not done.
