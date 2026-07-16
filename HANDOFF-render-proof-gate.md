# HANDOFF — RENDER-PROOF THE GATE, THEN SWEEP THE CORPUS
**Written 2026-07-16, after the founder read a screen the gate passed at 13:1 and could not see it.**

---

## THE ONE THING

**The pre-ship gate certifies color-token PAIRS. It never checks whether the surface
actually PAINTS. A screen can pass at 13:1 and render at 1.17:1 on the founder's device.**
Build the teeth that catch that, run the whole game corpus through the staging area, produce
the HALT list. This is a BUILD session — enhance the gate, do not write more prose rules.

---

## THE PROOF (today, with the founder's own retina)

`your-rp-world.html`, warm-dark comfort mode, Screen 1. Founder screenshot on iPhone:
the light-gold body text was **unreadable** — washed, smearing, near-invisible.

The arithmetic, computed live:

| What was measured | Ratio | Verdict |
|---|---|---|
| Gate's claim: warm body ink `#e4d8c2` on warm paper `#151210` | **13.23:1** | PASS (what the gate saw) |
| Reality on the founder's screen: same ink on the WHITE iOS sheet `#ffffff` | **1.41:1** | INVISIBLE |
| Warm heading `#f6ecda` on that same white | **1.17:1** | INVISIBLE (1.0 = identical colors) |

Both numbers are true. The gate measured text on its DARK home surface. The **device
rendered text on WHITE**, because the page background did not paint opaque — the light-gold
text sat on the white in-app-browser sheet showing through. (Confirming detail: the previous
chat message was visible bleeding through the top of the game screen. The game was not opaque.)

**Two stacked failures:**
1. **Gold-as-text in warm mode** — token-role law broken. Gold is atmosphere; it became text.
2. **The full-page background did not paint** — so light text landed on white, not on `--paper`.

The gate is structurally blind to #2. It has no concept of "does this surface actually
cover the viewport." That is the class to kill.

---

## THIS IS ALREADY IN MEMORY, UNFIXED

> *"Studio Eyes structural blind spot: the gate reads only the DEFAULT palette and reports
> 'every mode' — a bug can pass three checks while only one mode was actually tested."*

Written down. Never built. Today it cost a screen the founder couldn't read. The founder's
words: *"This happens all the time... these failures are regular and need addressing."*
He is right. The enhancements (flip_check, image_floor, nav_floor) have partial teeth;
the opacity/render class has NONE.

---

## THE TEETH TO BUILD (in order)

1. **OPACITY TOOTH — the one that caught today.**
   Every full-screen section (`.stage`/`.screen`/`.scene`) must resolve to an OPAQUE
   background in EVERY comfort mode, or HALT. Check: does `body` OR the section declare a
   solid (non-transparent, non-gradient-only) background that covers the viewport? A section
   whose only background is `transparent`/inherited-from-nothing = HALT. Light text on an
   unpainted surface is the whole bug.

2. **PER-MODE HAND-VERIFY — stop trusting the default-palette read.**
   The gate reads `:root` and reports "every mode." It is LYING about warm. Force each
   comfort stop (`body.warm`, `body.softer`, `html[data-comfort=...]`) as its own full
   palette and measure text-on-actual-surface independently. Report per mode, never merged.

3. **RENDER-PROOF, NOT TOKEN-PROOF.**
   The gate does string arithmetic on CSS tokens. It must reason about background
   INHERITANCE: if a text element's nearest painted ancestor is white (or unset), measure
   against THAT, not against the token the author hoped applied. This is the `own_bg` /
   ancestor-walk logic from studio-eyes-sweep.py — port its grounding discipline into the
   pre-ship gate, which currently has none.

4. **HUE FLOOR FOR RP (founder's eyes, not WCAG).**
   Gold/amber-on-dark can measure 13:1 and still smear for an RP reader. Warm-mode TEXT must
   be cool near-white at full strength; warm/amber tokens are fills and accents ONLY, never
   `color:`. This is the token-role law, enforced per-mode. WCAG is the floor; the founder's
   retina is the verdict — and today WCAG passed while the retina failed.

---

## THE RUN

Once the teeth exist: **stage the entire game corpus through enhanced Studio Eyes.** Every
HTML game with a comfort mode is a suspect for the opacity + warm-mode class. Produce one
HALT list, ordered worst-first. Expect this to catch a lot — the founder says these failures
are regular, and the arithmetic today says he is right.

Corpus lives across the four lanes (repo canon, Drive Claude_files, shelf, Netlify). Resolve
canon per file before judging — do not sweep stale shelf copies and report ghosts.

---

## THE FILE THAT TRIGGERED THIS

`your-rp-world.html` (Stage 1 RP intake-game, 38,638 B) is in outputs, gate-passed but
FOUNDER-REJECTED on warm mode. It must be rebuilt with the opacity fix + warm-mode cool-white
ink BEFORE it ships anywhere. It is the first customer of the new teeth. Do not ship it on
the old gate's say-so.

---

## STANDING

- **When the founder pushes back on a machine-produced fact, the machine is the suspect.**
  The gate said 13:1. The founder said "unseeable." The founder's retina was right and the
  gate was wrong. Re-derive from what the DEVICE renders, not what the token claims.
- **A gate that certifies a screen the founder cannot read is worse than no gate** — it
  manufactures false confidence. Same lesson as the Studio Eyes cry-wolf repair, other
  direction: this one cries "all clear" over a real failure.
- **PAT still expired.** This handoff reached the repo via the no-PAT Zapier GitHub lane
  (`github_create_or_update_file`). Container git-push remains dead until the PAT is rotated.
