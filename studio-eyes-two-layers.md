# STUDIO EYES — THE TWO LAYERS
### Studio-wide architecture. Ratified this session; first domain instance = the Pile Panel.
**One sentence:** Studio Eyes is an arithmetic floor that every build passes, plus a
per-game domain panel that only that game's experts can fill — and the two must never blur.

**As-of:** 2026-07-21. **Source:** convened from `studio-eyes-sweep.py` (the arithmetic
layer, live) + `collapse-panel-spec.md` (the first domain layer, this session).

---

## WHY TWO LAYERS

Studio Eyes today is one thing: `studio-eyes-sweep.py`, a **measurement eye**. It computes
contrast, counts external hosts, catches emoji, flags stale institutional data. It answers
questions that are *true or false by arithmetic.* That is its strength and its ceiling.

It cannot answer *"does this collapse case feel like a real pile?"* — because that is not
arithmetic, it is judgment, and judgment belongs to a credentialed human. Trying to compute
it would corrupt the one thing the arithmetic layer has: trust. An auditor that guesses is
worse than none — the sweep's own honesty rule already says so (line 372).

So Studio Eyes has two layers, and only one existed before this session.

```
STUDIO EYES
├── LAYER 1 — THE ARITHMETIC FLOOR      universal · computed · true/false
│   fires on EVERY build regardless of domain
│   = studio-eyes-sweep.py  (LIVE)
│
└── LAYER 2 — THE DOMAIN PANEL          per-game · judged · human-supplied
    fires on ONE game's cases; roster changes per game
    = collapse-panel-spec.md  (FIRST INSTANCE, this session)
```

---

## LAYER 1 — THE ARITHMETIC FLOOR  *(universal, do not touch)*

**What it holds:** things computably true or false. Contrast (WCAG AA, element-aware
grounding), the offline floor (external-host count), emoji presence, reference-staleness
(source + as-of date), file-disagrees-with-itself (version banners), focus style, scroll-reset.

**Its discipline — keep it exactly as it is:**
- **Arithmetic, not judgment.** The moment a computed check starts *deciding* instead of
  *measuring*, it stops being trustworthy. Contrast is a ratio, not an opinion.
- **A failure it can PROVE is a HALT. A failure it merely SUSPECTS is a WARN, named unproven.**
  (The 2026-07-11 honesty rule. Ungrounded ≠ invisible.)
- **Universal.** It does not know or care what the game is about. Flash fiction, collapse
  training, Choose Your Leader — same floor.

**The law:** never let domain judgment leak into Layer 1. If a check can't be arithmetic,
it is not a Layer 1 check. It is a wish, or it belongs in Layer 2.

---

## LAYER 2 — THE DOMAIN PANEL  *(per-game, human-supplied)*

**What it holds:** the judgment the arithmetic floor structurally cannot reach. Whether a
case is *honest*, not merely *legible*. Supplied by seats — and the seats are specific to
the game's domain.

**The pattern is studio-wide. The roster is per-game.**
- Collapse training convenes the Engineer, the Hand, the Coordinator (+ founder floors).
- A flash-fiction game convenes craft and reader-response seats.
- Choose Your Leader convenes historians and media theorists.
- **Each game gets its own panel spec. The pattern is reusable; the roster is not.**

**Every domain panel, whatever the game, shares three floor-seats** — the founder's, always
present because they are Studio Eyes' own values, not the domain's:
- **The Calibrator** — does the scoring measure confidence-to-evidence, or luck?
- **The Stranger** — does it render, read, and ship under the accessibility floor? (This seat
  is Layer 1's human face: it *invokes* the arithmetic sweep and refuses to ship on exit 1.)
- **Aleph** — one case or a system? Is the studio finishing or spec-chasing?

The **domain seats** on top of those floors are what change per game, and they are the ones
that **cannot be played by the machine.** They author facts. The machine only records what
they rule.

---

## THE SHARED MECHANIC — what makes both layers "Studio Eyes"

Two different substrates (arithmetic vs. judgment), one identical discipline. This is the
through-line that makes them one organ and not two unrelated tools:

| | Layer 1 (arithmetic) | Layer 2 (domain) |
|---|---|---|
| **Halts** | on a computed failure (contrast < 4.5, external host, emoji) | on an unauthored fact (a probability with no author, a stale frame) |
| **Shows the diff** | the failing token pair + its ground | the seat + the claim + the gap |
| **Never invents** | ungrounded → WARN, not a guessed HALT | missing fact → names who owes it, never fabricates it |

Both halt. Both show the diff. Neither invents. That triad *is* Studio Eyes.

---

## HOW A BUILD PASSES STUDIO EYES

1. **Layer 1 runs first, automatically.** `studio-eyes-sweep.py` on the file. Exit 1 = the
   build does not reach a human, full stop. Arithmetic is the gate; no judgment overrides it.
2. **Layer 2 runs per-case, once Layer 1 is green.** The game's domain panel passes over each
   case in seat order. Any seat HALT stops the case, shows the diff, names the owed fix.
3. **A build that clears both is *honest and legible*** — not merely one or the other.

The order matters: a case that isn't legible can't be meaningfully judged for domain honesty,
because the Stranger seat can't read it either. Arithmetic floor first, always.

---

## HOW LAYER 2 GROWS — provenance is the content

The domain layer is **not coded.** It is **populated by real practitioners, attributed.**

Every heuristic the Hand seat applies to collapse case #2 is a piece of judgment a real
firefighter gave on case #1 — captured, attributed, dated, reusable. "No responder would
trust that crack" becomes a check the Hand seat carries forward. The seat's vision is the
**accumulated, attributed judgment of named experts** — never scraped, never invented.

This is the Borges thesis wearing the studio's own tools: the de-attributed alternative is
the machine guessing what an expert thinks. Studio Eyes Layer 2 is the opposite of that by
construction. The panel that grows from Ben Urwin's review carries Ben's name on its
heuristics, with the date he gave them.

**Mechanism:** the case's feedback-export loop *is* the Layer 2 growth path. A practitioner
reviews a case, the export routes each note to a seat, and the studio records the note as a
new attributed heuristic for that seat. Review is how the domain eye learns to see.

---

## WHAT THIS IS NOT

- **Not a rewrite of the sweep.** Layer 1 stays exactly as it is. This spec adds a layer
  above it; it changes nothing below.
- **Not new studio furniture that fires everywhere.** Layer 2 is per-game. Collapse seats
  never fire on a flash-fiction build.
- **Not a substitute for the real experts.** The domain seats let a design self-check
  *before* the humans arrive. They do not replace the humans. Three collapse seats still
  demand credentialed people before any case ships to a trainee.
- **Not a place for wishes.** If a proposed check is neither computable (Layer 1) nor ownable
  by a named seat (Layer 2), it is not a Studio Eyes check. It is prose. There are already
  ~30 rules; the answer to a miss is more arithmetic or a named seat, never more prose.

---

## THE STUDIO-WIDE PAYOFF

This is why B was worth doing before the case: **every future game now inherits the pattern.**
When the next game needs domain judgment, it doesn't reinvent — it writes its own panel spec
against this architecture, reuses the three floor-seats verbatim, and swaps the domain roster.
The collapse case becomes the first *proof* of the pattern, not a one-off. Studio Eyes stops
being "the contrast script" and becomes what its name always implied: the studio's whole way
of seeing — measured where it can be, judged where it must be, attributed always.
