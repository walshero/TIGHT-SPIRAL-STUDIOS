# POST-MORTEM: Studio Eyes
## Why the auditor kept lying, and what it costs to make it world-class

Date: 2026-07-13
Author: Claude (Tight Spiral Productions)
Status: DIAGNOSIS COMPLETE — rebuild specified below

---

## 1. THE FAILURE, STATED PLAINLY

Studio Eyes is the studio's contrast auditor. It exists because Matt has
retinitis pigmentosa and **contrast cannot be a judgment call**. It is the one
tool in the critical path of every ship.

**It has been wrong, in a new way, roughly every time anyone has looked at it.**

Seven distinct bugs, all found by a human noticing something was off — never by
the tool noticing itself:

| # | Date | Bug | What it did |
|---|------|-----|-------------|
| 1 | 07-11 | Comments glued to selectors | `/* MASTHEAD */ .mh {}` parsed the comment AS PART OF the selector. Any rule preceded by a comment was invisible. |
| 2 | 07-11 | At-rules not unwrapped | Anything inside `@media` was unparseable. |
| 3 | 07-11 | Only first `<style>` block read | Everything after the first block: unseen. |
| 4 | 07-11 | Grouped selectors not split | `.a,.b{background:x}` — neither `.a` nor `.b` was findable. |
| 5 | 07-11 | Ancestor-chain grounding | `.foot a` grounded against the page, not `.foot`. |
| 6 | 07-11 | Element's own base rule ignored | Walked to ancestor before checking whether the element paints itself. |
| 7 | 07-13 | Key-class collision | `.part .pred` (a caption) grounded against `.fill.pred` (a progress bar). `.lens-btn` base text grounded against its own `[aria-pressed]` background — two states that never coexist. |

Every one of these produced **FALSE HALTS** — the tool screaming that working,
legible files were invisible.

---

## 2. THE REAL COST — AND IT IS NOT THE BUGS

The bugs are symptoms. Three compounding costs:

**COST 1 — It trained the founder to distrust it.**
The source code says this out loud, in bug 1's own comment:
> *"manufactured false HALTs that trained the founder to distrust the auditor."*

An auditor you don't trust is worse than no auditor. You stop reading its output.
You start overriding it. And then the ONE time it is right, you override that too.

**COST 2 — It nearly made me break working files.**
Tonight, Studio Eyes told me six things about Funny Boney's were INVISIBLE.
If I had obeyed it, I would have "fixed" a hand-tuned 12:1 button down to
something worse, in a file that was already correct. **The auditor was one step
from becoming the thing that introduces the bug.**

**COST 3 — Nine EN195 files sat frozen for days.**
Memory records it: they were "stuck as fixed-but-not-deployed" because a broken
auditor was flooding false positives while masking real bugs. Days of a
resource-constrained professor's life, spent servicing a tool that was wrong.

---

## 3. ROOT CAUSE — WHY IT KEEPS HAPPENING

**Studio Eyes reimplements a browser, badly, with regex.**

Every single bug in that table is the same bug wearing a different hat:

> *The tool is guessing what the browser would do, from the text of the CSS,
> using pattern-matching — instead of asking something that actually knows.*

- Comments? A real CSS parser handles them. Regex doesn't.
- `@media`? A real cascade handles it. Regex doesn't.
- Which ancestor grounds this text? **The DOM knows. Regex guesses.**
- Is `.lens-btn` pressed or unpressed? **The renderer knows. Regex cannot.**

There is no clever regex that fixes this class. Every patch narrows one gap and
opens another, because the underlying model — "CSS is a string I can pattern-match" —
is false. CSS is a **cascade evaluated against a tree**.

**This is the deepest finding in this document. The tool is built on the wrong
primitive.** Bug 8 is already in there. So is bug 9.

---

## 4. THE SECOND FAILURE: IT ONLY CHECKS ONE THING

Even a perfect contrast checker would be an incomplete Studio Eyes.

Tonight's sweep of the live repo: **26 of 31 files HALT.** Not because they're
broken — because the **Token-Role Law** was invented *after* they shipped. That
is a real finding, and the tool surfaced it. Good.

But look at what Studio Eyes **cannot** see, all of which are named studio law:

- **NO OPENING WALL** — is the first painted screen a scene, or a preference gate?
  *(The Tell shipped this exact bug. The law exists. The tool cannot check it.)*
- **>50% IMAGE** — a stated founder floor. Unchecked.
- **NO EMOJI EVER** — trivially checkable. Not checked.
- **SINGLE-FILE / OFFLINE** — no external hosts. Not checked.
- **Focus rings on every interactive** — WARNs, never HALTs.
- **44px touch targets.** Unchecked.
- **Text over an image or gradient** — the gate itself admits it "computes, it
  does not LOOK." A caption on a photo escapes entirely.
- **`prefers-color-scheme: dark` / `forced-colors: active`** — unsimulated. The
  known EN195 charcoal-on-black bug lives precisely in this gap.

**Studio Eyes checks one law out of ten, and gets that one wrong seven times.**

---

## 5. WHY THIS ONE IS WORTH DOING RIGHT

Everything else in the studio is downstream of this tool.

The pre-ship gate is mandatory. The ship gate depends on it. GATE 2 *is* Studio
Eyes. If it's unreliable, **every certification the studio has ever issued is
unearned** — including tonight's.

And the standing lesson is already written in memory, from the last time:

> *"Never certify a file passing on a raw sweep verdict without validating the
> sweep itself. The auditor is in the critical path and must be trustworthy
> before it gates."*

We keep re-learning it because we keep patching instead of rebuilding.

**More prose will not fix this. `IF A RULE CAN'T BE A CHECK, IT'S A WISH.`
The answer to a lying auditor is not a better-written auditor. It is an auditor
that cannot lie — because it stops guessing and starts measuring.**

---

## 6. THE REBUILD — STUDIO EYES v3

### The one change that kills all seven bugs at once

**Stop parsing CSS. Start rendering the page.**

Load the file in a real headless browser. Ask the browser — which is the ground
truth, the same engine Matt's phone runs — for the **computed style** of every
element, in every comfort stop, at every viewport.

```
OLD:  read the CSS text  ->  guess the cascade  ->  guess the ground  ->  compute
NEW:  render the page    ->  ASK for the ground ->  compute
```

That middle column is where all seven bugs lived. **Delete the middle column.**

- Comments? Gone — the browser already stripped them.
- `@media`? Gone — the browser already resolved it.
- Grounding? **`getComputedStyle` and `elementFromPoint` do not guess.**
- `[aria-pressed]` states? **Toggle the attribute, re-measure. Actually click it.**
- Text on a gradient or a photo? **Screenshot the pixels under the glyphs and
  measure the worst case.** This is not possible with regex. It is trivial with a
  renderer.

### What it must check (the full floor, not one tenth)

Ten checks, each a HALT, each mechanical:

1. **CONTRAST** — every text node vs its *actually rendered* background, in every
   stop. Including text over images/gradients (sample the real pixels).
2. **TOKEN-ROLE LAW** — no token is both text and decoration.
3. **STOP SEPARATION** — comfort stops differ ≥0.12 luminance. A knob that changes
   nothing is a wall.
4. **NO OPENING WALL** — screenshot the **first paint**. If it contains
   palette/comfort/preference controls and no scene: HALT.
5. **IMAGE RATIO** — measure painted image area vs total. <50%: HALT.
6. **NO EMOJI** — scan rendered text. Any: HALT.
7. **OFFLINE** — intercept every network request during load. Any external host: HALT.
8. **FOCUS VISIBLE** — tab through every interactive. No visible ring: HALT.
9. **TOUCH TARGETS** — measure every control's rendered box. <44px: HALT.
10. **FORCED COLORS / DARK MODE** — re-run 1–9 under `prefers-color-scheme: dark`
    and `forced-colors: active`. This is where the EN195 bug is hiding.

### The check that makes it *world-class*, not just correct

**IT MUST AUDIT ITSELF.**

Every bug in that table was found by a human. That is the actual failure.

Ship Studio Eyes v3 with a **canary corpus** — a directory of tiny HTML files
with *known, deliberate* defects and *known, deliberate* correct cases:

- a file where text sits on a `@media`-only background
- a file where a button's pressed and unpressed states differ
- a file with a comment before every rule
- a file with white-on-white (must HALT)
- a file with hand-tuned 12:1 buttons (must **PASS** — this is the false-positive trap)
- a file that opens on a comfort gate (must HALT)
- a file with a caption over a photo (must sample pixels)

**`studio-eyes --self-test` runs the canary before it audits anything.**
If the auditor cannot correctly grade the canary, **it refuses to run.**

A tool that gates the studio must first gate itself. There is already a
`studio-eyes-canary.html` on the shelf — the idea existed. It was never wired
into the critical path.

### What to ignore

- **Do not** write a better regex. There is no better regex.
- **Do not** add more rules to the OS. There are ~30. The tool is the rule.
- **Do not** hand-fix the 26 HALTing files first. Fix the tool, then run it once
  and fix the class in a single pass. **CLASS-TICK, not instance.**

---

## 7. THE HONEST TRADE

**Cost:** Studio Eyes v3 needs a headless browser (Playwright). That is a real
dependency, and the current tool's one virtue is that it is a single dependency-free
Python file.

**Why pay it:** The dependency-free version *has been wrong seven times and cost
days*. A tool that is convenient and lies is not cheaper. It is more expensive,
and the bill arrives as Matt's time and Matt's trust.

**Simpler alternative:** keep the regex sweep as a fast pre-filter, and gate ONLY
on the renderer. Rejected — two auditors that disagree is worse than one that's
right. Kill the regex.

**Portability preserved:** it stays a single script, runs offline, no service,
no subscription. Playwright is durable, standard, and not going anywhere.

---

## 8. NEXT ACTION

Build Studio Eyes v3 on Playwright, canary-first:

1. Write the canary corpus (the trap cases above)
2. Build v3 to pass the canary — **the canary is the spec**
3. Run v3 across all 31 live files
4. Fix the class (Token-Role Law + whatever else it surfaces) in one pass
5. Wire `--self-test` into `floor-check.yml` so the auditor is gated on every push

**Then** playtest. Not before.
