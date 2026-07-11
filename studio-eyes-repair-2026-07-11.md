# STUDIO EYES — REPAIR LOG, 2026-07-11

**Verdict: the 2026-07-05 "repair" did not take. SIX separate grounding bugs were live.
Shelf HALT count 42/57 → 20/57. Twenty-two files were blocked by an auditor that was wrong.**

---

## The presenting symptom

Confluence HALTed with 22 H1 contrast failures, all on the mobile masthead:

```
H1: [default] .mh-mark  color #fff = 1.1:1 (INVISIBLE, ground=page)
H1: [default] .mh-name  color #fff = 1.1:1 (INVISIBLE, ground=page)
...
```

By eye, the masthead is **white text on dark green** (`.mh { background: var(--pine) }`) —
high contrast, correct, shipping fine. The auditor was wrong 22 times in one file.

---

## Root cause — five bugs, not one

### BUG 1 — CSS comments glued onto selectors (THE ROOT CAUSE)

The rule parser is `([^{}]+)\{([^{}]*)\}`. It captures everything between the previous `}`
and the next `{` — **including any preceding comment**. So:

```css
/* ━━━ MASTHEAD ━━━ */
.mh { background: var(--pine); }
```

parsed with the selector key `"/* ━━━ MASTHEAD ━━━ */ .mh"` — **not `.mh`**. The key never
matched a lookup. Every descendant grounding against `.mh` fell through to the page
background and HALTed as invisible.

**Any selector preceded by a comment was silently unfindable.** In a well-commented
stylesheet — which is to say, every file in the studio — this corrupts grounding
everywhere.

*Fix:* `strip_comments()` before parsing.

### BUG 2 — only the first `<style>` block was read

`re.search(r'<style...>')` returns **one** match. Confluence has two style blocks. Every
rule in block 2+ was invisible to every check — no contrast, no stop, nothing.

*Fix:* `re.findall`, join all blocks.

### BUG 3 — at-rules broke the flat parser

Rules nested in `@media` / `@supports` were parsed with the at-rule prelude glued to the
selector (same class of failure as BUG 1). The flat brace regex cannot see nesting.

*Fix:* `strip_at_rules()` — brace-matched, recursive, unwraps to top level.

### BUG 4 — grouped selectors never split

`.mh-top,.mh-nav { ... }` was stored under the single opaque key `".mh-top,.mh-nav"`.
A background declared on a comma group was invisible to lookup.

*Fix:* `split_groups()` — explode groups so each selector is individually findable.

### BUG 5 — the ancestor walk was whitespace-only

This is the one the 07-05 repair addressed, and it fixed **descendant selectors only**:

```python
toks = sel.split()
for k in range(len(toks)-1, 0, -1):   # '.foot a' -> '.foot'  ✓
```

For a single-token selector like `.mh-name`, `toks` has length 1, so
`range(0, 0, -1)` is **empty — the loop never executes.** Zero ancestor lookup.

But `.mh-name` *is* inside `.mh` in the DOM. The relationship is a **BEM prefix**, not a
descendant combinator. No amount of string-splitting can see that. **The selector string
is not the DOM.**

*Fix:* three-stage grounding —
1. **DOM-grounded** (`build_dom_index` + `dom_ancestor_bgs`): parse the actual HTML, walk
   real parents. This is the correct answer whenever the node exists statically.
2. **BEM-prefix fallback** (`bem_prefix_chain`): for JS-injected nodes absent from the
   static tree, infer `.mh-mark → .mh` from the naming convention.
3. **String walk**: retained for descendant selectors.

---

## The honesty rule (the part that matters most)

Some elements are **JS-injected** and simply do not exist in the static HTML. Their true
background is **unknowable** by static analysis.

The old auditor grounded those against the page and reported INVISIBLE. **That is a guess
presented as a finding.** It is what manufactured the phantom-HALT flood.

New behavior:

- A failure grounded against a **resolved** background → **H1 HALT** (proven).
- A failure with **no resolvable** ground → **WARN, labeled UNGROUNDED** (suspected;
  verify by eye).

An auditor must never assert what it cannot prove. Crying wolf is worse than silence,
because it teaches the founder to ignore the alarm.

---

## One fix tried and WITHDRAWN

**Component-family grounding** — ground `.lum-poem` against its sibling `.lum-hero`
(which paints `var(--pine)`), on the theory that components paint their container.

**Unsound. Invented 20+ new false HALTs.** It grounds an element against a background it
may never sit on, and picking the "darkest sibling to be safe" reasons in the wrong
direction. Removed. The code retains a comment marking it as tried-and-rejected so it is
not reinvented.

**Lesson: an auditor must not guess. When it cannot know, it says it cannot know.**

---

## Canary (required, per TICK 4)

A gate that stops false-positiving by going blind is not repaired. Every gate repair ships
with a fixture proving it still catches the real bug:

```html
<style>
:root{ --bg:#ffffff; --ink:#111111; }
body{ background:var(--bg); color:var(--ink); }
/* a comment before the selector — the bug that started this */
.card{ background:#ffffff; }
.card .title{ color:#ffffff; }   /* white on white  -> MUST HALT */
.safe{ background:#1a4a35; }
.safe .t{ color:#ffffff; }       /* white on dark   -> MUST PASS */
</style>
```

**Result:** HALTs `.card .title` at 1.0:1 (`ground=dom:.card`). Does **not** flag `.safe .t`.
Correct in both directions.

---

## Results

| | before | after |
|---|---|---|
| Confluence H1 HALTs | 22 (all phantom) | **9 (all proven)** |
| Shelf files at HALT | 42 / 57 | **24 / 57** |

And the surviving HALTs are **real bugs the noise was hiding** — e.g.
`.sc-modal-hd color:#fff` on `--surface:#ffffff` = **1.0:1, genuinely invisible**;
`.ring-card-hd` the same. Those were always broken. Nobody could see them through
twenty-two false alarms.

---

## Files

- `studio-eyes-sweep.py` — 385 lines, repaired, canary-verified. md5 `ec24c524…`
- `os-block-truth-ticks.md` — the four ticks minted from this session.

## Still open

- **TICK 3 (reference-staleness) is not built.** Named, not enforced. Next build session.
- The nine EN195 files were "verified 0-HALT" against the **broken** auditor. That
  verification is void. **Re-sweep them before deploy.**


---

## BUG 6 — an element's own background was never checked

Found after the first five were fixed, while chasing what looked like two real warm-mode
failures in `course-river` and `workshop-wall`.

Evaluating `body.warm .tool .brasstag`, the sweep found no background on that full
selector and walked up to the ancestor `.tool` (dark `--surface`), reporting near-black
ink at **1.2:1 — INVISIBLE**.

But the element **paints itself**. The base rule `.tool .brasstag` declares
`background: var(--brass-d)`, and the warm stop redefines `--brass-d` to `#f0c357`
(light gold). True contrast: **11.6:1. Fine.**

Same story in `course-river`: `.node .due` paints itself `var(--accent2)` → warm `#9fb6cd`
(light blue). Near-black on it = **9.2:1. Fine.**

**An element's own background always wins over any ancestor.** The base rule may be
written bare (`.brasstag`) or as a descendant (`.tool .brasstag`), so the lookup matches
by *selector tail*, not by bare class.

*Fix:* stage 1b — check the element's own base rule before walking ancestors.

### The consequence, stated plainly

**The nine EN195 files were clean all along.** Mid-session I reported two of them as
carrying real warm-mode floor failures on the founder's own eyes. **That report was wrong.**
It was BUG 6 talking. Both "failures" were false positives from the same broken grounding.

This is the exact hazard TICK 4 names: a bad auditor does not just miss bugs, it
*manufactures* them, and the manufactured ones cost real time and real trust. The canary
is what caught it — a zero-HALT result on two files that had just been HALTing is a
suspicious result, and suspicious results get tested, not celebrated.

---

## Final results

| | before | after |
|---|---|---|
| Confluence H1 HALTs | 22 (all phantom) | **9 (all proven)** |
| Shelf files at HALT | 42 / 57 | **20 / 57** |
| The nine EN195 files | "verified" by a broken auditor | **genuinely clean** |

---

## TICK 3 — REFERENCE-STALENESS, now built (H6)

Institution-asserting files must carry a **source** and a **last-verified date**, in-file.
Markers are institution-specific (`islo`, `graduation competency`, `learning outcome`,
`rubric`, `norming`, `accreditation`…) — the first draft used generic words like
`outcome` and `policy` and immediately false-positived on `warriors-fantasy-arcade`, a
fantasy game. Tightened.

**Honest limit:** H6 verifies that provenance *exists*, not that it is *accurate*.
Confluence passes H6 today because it carries source and date stamps — even though its
outcome data was two revisions stale. **A stamp is a claim, not a proof.** H6 makes the
claim mandatory and visible so a human can check it; it cannot check it for you.
Catching stale-but-stamped data requires TICK 1 (count from source) and TICK 2
(authority by claim type), which are behavioral, not mechanical.

Current H6 catch on the shelf: `assignment-auditor.html`.
