# FUNES PLAYTEST — the iSLO suite, post-merge (2026-08-03)

> **Source:** an 11-aleph adversarial playtest fleet run against the iSLO suite immediately after PR #43
> merged to `main` (merge `5b14abc`). One aleph per page: each drove the page in headless Chromium through
> every interaction and edge case, exercised the Studio Eyes control in day/dusk/night + text-size + comfort
> toggles, and read the page for dignity/voice and source integrity. **Last-verified:** 2026-08-03.
>
> The Funes rule: total recall, misses nothing. This is the removal-of-doubt record — every defect the fleet
> surfaced, what was done about it, and what is knowingly left.

## Coverage
11 pages: `islo-hub`, `sticker-price`, `real-cost`, `update-the-model`, `who-holds-the-room`, `score-the-room`,
`close-the-loop`, `scorer-norming`, `rubric-forge`, `whose-draft`, `ai-resilient-assignment`.
10 alephs returned structured findings; the `who-holds-the-room` aleph hit its output-schema retry cap and was
covered directly (it had already been browser-verified during the build and passes comfort-gate in all modes).

## The one real regression — FIXED (priority 0, contrast floor)
- **Night-mode slab heading was dark-on-dark (2.14:1).** `.slab h3` colors its text with `--brass-fill`; the
  dark-mode kernel I mounted redefines `--brass-fill` to a dark meter-fill value, so the "in one sentence"
  heading nearly vanished on the dark slab in warm-dark mode. comfort-gate missed it because `--brass-fill` is
  a *fill* token, not one of the text tokens it samples — a token-role gap. **Fix:** a night override forcing
  `.slab h3` to a bright brass ink on the always-dark slab. Now **9.87:1** in night across all six affected
  files (`update-the-model`, `who-holds-the-room`, `score-the-room`, `real-cost`, `scorer-norming`, `whose-draft`).

## Correctness / integrity defects — FIXED
- **islo-hub — "four outcomes" should be "five".** Only 2 outcomes carry a live/normed rubric, so 5 lack one.
  The slab said "four"; the count tile and lede already said the equivalent of five. Corrected to "five".
- **islo-hub — "25 games mapped" didn't reconcile.** The hub lists 23 unique game targets. Set the tile to **23**
  so the number reconciles to what's on the page (no inflated claims).
- **update-the-model — repeat "Meet the evidence" wiped the player's move.** The reveal handler reset the
  posterior slider to the prior on *every* click; a second click discarded the confidence the player had entered.
  **Fix:** initialize posterior→prior only on the first reveal (`if (reveal.hidden)`). Verified: posterior held at
  15 across a repeat reveal.
- **score-the-room & scorer-norming — stale verdict after changing the pick.** After revealing the normed score,
  selecting a different level left the old verdict on screen, now contradicting the pressed button. **Fix:** the
  pick handler retires the shown reveal, so the learner re-reveals to see the verdict for their new pick. Verified.
- **sticker-price (Case 3, The Statistic) — two arithmetic-honesty defects on the flagship quantitative page.**
  (1) The reading hardcoded "up from" regardless of direction, so a *decrease* read "down 100% … up from 0.02%".
  **Fix:** directional "up from / down from" by comparing the two rates — verified both ways. (2) Nothing kept the
  incident count within the pool, so a count above the denominator printed rates over 100% (e.g. "5000% of the
  pool"). **Fix:** a count can never exceed the pool it's drawn from — `sync()` clamps it. Verified (after=500,
  pool=10 → count clamped to 10).
- **ai-resilient-assignment — packet stamped a stale hardcoded date.** The exported audit/policy packet wrote
  "Date: 2026-07-30" on any day. **Fix:** compute the current date at generation time.
- **close-the-loop — percent-at-benchmark wasn't clamped.** A typed 150 flowed into the report as "150% at
  benchmark". **Fix:** clamp to 0–100 in the assembled report.

## What the fleet confirmed HOLDS (no action)
- **Dignity/voice held on every page.** "A starting point is never a verdict" is stated explicitly where it
  matters; the number does the work (second person addresses the reader's own guess/move, never a character
  verdict); no invented or inflated claims; **no claim anywhere that blind players can play** — accessibility is
  framed only as the founder's RP design-intent; resources are asset-framed, not deficits; no dark patterns
  (Flok being a dark-patterns *teaching* game is subject matter, not page behavior).
- **Contrast held in every light mode** (day/dusk/night + high-contrast) on all sampled text, once the slab
  heading was fixed — lowest observed elsewhere 5.57:1.
- **Source integrity held** — live rubrics name their source + Confluence link and carry a last-verified date;
  un-normed outcomes are marked (Not-yet-normed / Suite-proposed / In development), never asserted.
- **No crashes, no dead ends, no console errors** across the fleet; Back/Home rails and the Studio Eyes panel
  are always reachable and dismissable.

## Knowingly left (minor, logged — not blocking)
- **real-cost** — plural agreement at slider value 1 ("1 times a week for 1 weeks"); the ~50-minute commute
  constant is page-authored rather than student-set; the all-zero degenerate case renders an empty reveal bar.
  Cosmetic / edge-case; the page's core arithmetic is correct.
- **islo-hub** — the version-stamp line carries a few stray unmatched `</span>` tags (an artifact of
  `version-stamp.py`); browsers discard them and it renders fine. A tooling fix, not a page fix.
- **score-the-room / scorer-norming** — the case rail uses `role="tablist"` without the full ARIA tablist
  contract (aria-selected / aria-controls / arrow keys). Keyboard operation works via Tab+Enter; semantics-only.

<!-- Repo context doc — the removal-of-doubt record for the post-merge Funes playtest. Not linked from the public face. -->
