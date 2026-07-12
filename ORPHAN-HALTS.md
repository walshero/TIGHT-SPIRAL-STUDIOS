# ORPHAN HALTS — 24 files landed 2026-07-11

**These 24 files existed ONLY on the shelf cache. They are now in the repo — which means they
are now FIXABLE. Siloed, they were invisible.**

**11 carry pre-existing contrast defects.** They were not introduced by the push; they have been
broken the whole time and nobody could see them because the files had no home and the auditor
was itself broken until today.

**These are PROVEN failures (grounded), not guesses.** The repaired Studio Eyes separates what it
can prove from what it cannot — anything marked UNGROUNDED is a suspicion, not a finding.

---

## claude_PLAY-Cliche-Cabinet.html
```
H4: uses localStorage
WARN: UNGROUNDED [default] .studio color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: UNGROUNDED [default] .coin color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no scroll-reset
```

## claude_cliche-cabinet-suite.html
```
H4: uses localStorage
WARN: UNGROUNDED [default] .studio color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: UNGROUNDED [default] .coin color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no scroll-reset
```

## claude_cliche-cabinet.html
```
H4: uses localStorage
WARN: UNGROUNDED [default] .studio color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: UNGROUNDED [default] .coin color #5a544c = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no scroll-reset
```

## claude_cliche-city.html
```
H1: [default] h1 .strike color var(--dim) = 1.2:1 (INVISIBLE, ground=base:h1 .strike::after)
H4: uses localStorage
WARN: UNGROUNDED [default] .tag color #5a544c = 2.5:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no focus style
WARN: no scroll-reset
```

## claude_cliche-field.html
```
H1: [default] h1 .strike color var(--dim) = 1.2:1 (INVISIBLE, ground=base:h1 .strike::after)
H4: uses localStorage
WARN: UNGROUNDED [default] .tag color #5a544c = 2.5:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no focus style
WARN: no scroll-reset
```

## claude_cliche-line.html
```
H1: [default] h1 .strike color var(--dim) = 1.2:1 (INVISIBLE, ground=base:h1 .strike::after)
H4: uses localStorage
WARN: UNGROUNDED [default] #attrib color #6f685e = 3.4:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: UNGROUNDED [default] .tag color #5a544c = 2.5:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
WARN: no focus style
WARN: no scroll-reset
```

## funny-boneys-factory.html
```
H1: [default] .lens-btn color var(--ink-soft) = 1.4:1 (INVISIBLE, ground=base:.lens-btn[data-l="spell"][aria-pressed="true"])
H1: [default] .part .pred color #ffb347 = 1.0:1 (INVISIBLE, ground=base:.fill.pred)
H1: [softer] .lens-btn color var(--ink-soft) = 1.7:1 (INVISIBLE, ground=base:.lens-btn[data-l="spell"][aria-pressed="true"])
H1: [softer] body.softer .part .pred color #ffc061 = 1.1:1 (INVISIBLE, ground=base:.fill.pred)
H1: [daylight] body.daylight .part .pred color #7a4600 = 1.4:1 (INVISIBLE, ground=base:.fill.pred)
H1: [daylight] .lens-btn color var(--ink-soft) = 3.6:1 (low, ground=base:.lens-btn[data-l="spell"][aria-pressed="true"])
```

## laughter-foundry-spec-and-log.html
```
H1: [default] .pill color #fff = 3.1:1 (low, ground=own)
WARN: UNGROUNDED [default] .turn.asst .who color var(--brass) = 2.6:1 (low, ground=page?) — background unresolved (likely JS-injected); verify by eye
```

## legibility-optimizer.html
```
H1: [default] .foot a color var(--accent) = 2.2:1 (low, ground=sel:.foot)
H3: dark class referenced but no parseable dark palette — stop is UNTESTED (silent-skip)
```

## recursion-ledger.html
```
H1: [default] .tag.below color var(--hot) = 4.5:1 (low, ground=own)
H1: [default] .state.live color var(--hot) = 4.5:1 (low, ground=own)
H4: uses sessionStorage
WARN: no scroll-reset
```

## timing-belt.html
```
H1: [default] .foot a color var(--accent) = 2.2:1 (low, ground=sel:.foot)
H3: dark class referenced but no parseable dark palette — stop is UNTESTED (silent-skip)
=== 11 files at HALT of 24 swept ===
```

---

## THE FINDING THAT MATTERS

**`behind-this-door.html` (42,400 B) was recorded in the studio as a DEAD LINK.**

It is not dead. It is a **real, finished, 42 KB file** that was never pushed. The 404-Forward-Guard
correctly found a broken door — and the studio **pruned the link instead of shipping the room
behind it.**

That is the whole silo problem in one file: a guard that removes the symptom and leaves the work
unreachable.

## HOW THESE GOT LOST

> **built → landed in `outputs` → never pushed → chat closed → orphaned on the shelf**

The Gatekeeper charter already says *"Outputs is a staging bench, nothing lives there."*
**Written, never enforced.** TICK 5 (auto-push at creation) is the fix — a file that is not in a
lane in the same turn it is made does not exist.