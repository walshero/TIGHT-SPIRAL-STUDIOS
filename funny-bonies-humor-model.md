# FUNNY BONIES — THE HUMOR MODEL (theory, and how the game uses it)
<!-- 2026-08-02 · design foundations · founder directive: "HUMOR needs training. Introduce and utilize humor theory. What is universal, what is cultural." Grounds the game's core math (actualFor) in real humor theory so the game TEACHES humor literacy, not just calibration. Sources cited inline; web-verified 2026-08-02. -->

## THE GAP THIS CLOSES
Funny Bonies has a calibration loop (read a room, own the gap) but **no theory of what's funny** — `actualFor(gag,room)` is an arbitrary taste multiplier. That's a hollow center: the game asks players to "read the room" without modelling *why* a bit lands. This doc grounds the center in humor theory, so the number a room returns is **explainable** — and the game becomes a trainer of humor literacy.

## 1. THE THEORIES (what "funny" is)
Four load-bearing frames, cheap to state, and the game only needs the last one to *run*:
- **Incongruity** — funny is a violated expectation; a mismatch resolves in a surprising way. The **cognitive** core, and the most cross-culturally universal (brains are wired to flag the unexpected). [1000-Word Philosophy; cross-cultural research]
- **Superiority** — we laugh *down*: at misfortune, folly, the pratfall. The **social** core (schadenfreude, the banana peel).
- **Relief** — laughter discharges tension; a safe release after a build-up. The **physiological** core (timing, the pause, the pop).
- **Benign Violation (McGraw & Warren)** — the modern synthesis and the one we build on: **something is funny when a norm/expectation is *violated* AND the context makes it *benign* (safe) — both at once.** Too safe = boring; too threatening = offensive; the funny lives in the overlap. It subsumes the other three (a violation = incongruity/superiority; benignity = relief). [petermcgraw.org — "Humor Theories, the Big Three"]

**Why Benign Violation is our engine:** it's two dials, not a vibe. Every bit is a *violation of some size*; every room has a *benign threshold* (how safe it needs the violation to feel). Funny = the violation is big enough to register but stays under that room's threshold. That is literally a formula — see §4.

## 2. THE TECHNIQUES — the Onion's 11 funny filters (Dikkers)
The theories say *why* things are funny; the filters say *how* a bit is built. Scott Dikkers (founding editor of The Onion) holds that **every joke uses at least one of 11 filters** [Big Think; *How to Write Funny*]:

| Filter | What it does | Universal or Cultural |
|---|---|---|
| **Irony** | meaning is the opposite of the surface | semi (structure universal, read cultural) |
| **Character** | a funny personality acting in-character | semi |
| **Reference** | leans on shared common experience | **cultural** (needs the shared context) |
| **Shock** | taboo — sex, gross-out, transgression | **cultural** (the taboo line moves) |
| **Hyperbole** | absurd exaggeration | **universal-leaning** |
| **Wordplay** | puns, double meaning, language | **cultural / linguistic** (dies in translation) |
| **Analogy** | funny by unexpected comparison | semi |
| **Madcap** | zany physical/visual mayhem — **slapstick** | **universal** (wordless, visual) |
| **Parody** | mimics a known form in a wrong key | **cultural** (must know the original) |
| **Meta-humor** | a joke about jokes | **cultural** (needs genre literacy) |
| **Misplaced Focus** | attention on absurdly the wrong detail | semi |

(Dikkers separately catalogs **40 comedy character archetypes** — likely the source of the "~17" memory. The 11 filters are the core technique set; the archetypes are a Character sub-library for later.)

## 3. UNIVERSAL vs CULTURAL — the axis the founder asked for
The research converges cleanly [cross-cultural humor studies; Laughter and Culture, NCBI]:

**UNIVERSAL (crosses every room — the always-on floor):**
- **Incongruity / surprise** — pattern-break is cognitive, species-wide.
- **The benign-violation *structure*** itself — every culture laughs at safe transgression; only the *content* of "safe" varies.
- **Slapstick / physical comedy (Madcap)** — visual, wordless, needs no shared language. The pratfall, the boing, the pie. This is why physical comedy travels and dubbed sitcoms don't.

**CULTURAL / LINGUISTIC (room-gated — lands only where the context is shared):**
- **Wordplay** — puns ride specific words; the cleverness *is* the language, so it's lost across tongues.
- **Reference / Parody / Meta** — require a shared canon; no shared canon, no joke.
- **Shock** — the taboo line is set by the culture; edgy in one room is unremarkable or offensive in the next.
- **What counts as *benign*** — the same violation reads safe or cruel depending on power dynamics and norms [NCBI: "Benign Violations, Power Asymmetry"]. Sarcasm skews Western; some cultures favor gentle physical over mean-spirited prank.

**The one-line model:** *humor = a universal structure (incongruity held benign) wearing culture-specific clothes (which violations register, and which stay safe).* The structure is the floor; the clothes are what "reading the room" reads.

## 4. THE SYNTHESIS — the Funny Bonies Humor Model
Re-ground the game so `actualFor` computes from theory, not a magic multiplier. Two data shapes:

**Every GAG carries:** a **violation size** `v` (how big the expectation-break is, 0–10) and a **filter mix** (which of the 11 it uses), which sets its **universal share** `u` (0–1 — how much of it is physical/incongruity vs. language/reference).

**Every ROOM carries:** a **benign threshold** `b` (how safe the violation must feel to land — a jumpy cat is low; edgy web is high) and a **shared-context** vector — how much it "gets" each cultural filter (language for wordplay, canon for reference, tolerance for shock).

**The laugh (benign-violation, made literal):**
```
universal_hit = v            gated only by benignity (physical/incongruity lands anywhere safe)
cultural_hit  = v × room.getsThisFilter        (wordplay/reference land only where context is shared)
raw   = u × universal_hit + (1−u) × cultural_hit
laugh = raw × benignFit(v, room.b)      // 1 when the violation sits under the room's safe line; falls off when it's too tame OR too threatening
```
`benignFit` is the benign-violation curve: a bit that's *too safe for the room* under-lands (boring); one that's *over the room's line* over-steps (offends) — peak funny sits in the window. This makes "too tame" and "too edgy" both failures, which is truer than a linear multiplier.

### The existing cast, re-grounded (worked)
| Gag | Filters | v | u (universal) |
|---|---|---|---|
| **The Trip** (pratfall) | Madcap, Superiority | 6 | **0.9** — pure physical |
| **The Boing** (floor→trampoline) | Madcap, Incongruity | 6 | **0.85** |
| **The Flip** (pail defies up) | Incongruity, Misplaced Focus | 5 | 0.6 |
| **The Chicken** (rubber chicken from nowhere) | Reference(!), Madcap, Non-sequitur | 8 | 0.5 — the *rubber chicken* is a comedy-**reference**, so half its laugh is cultural |

| Room | benign line `b` | gets wordplay? | gets reference? | gets shock? |
|---|---|---|---|---|
| **One sleepy cat** | very low (spooks) | no (no language) | no (no canon) | no | → only **universal physical**, gently. A pun *cannot* land on a cat; a soft boing can. |
| **A room of kids** | low–mid | simple only | little | no | slapstick kills; edgy/reference bombs. |
| **Tired grown-ups** | mid–high | yes | yes | some | irony/wordplay/reference land; pure slapstick underwhelms. |
| **Strangers online** | high (edgy ok) | yes | yes (internet canon) | **yes** | shock/meta/reference/parody thrive; gentle stuff is "mid." |

**What this predicts (and teaches):** a pun bombs on the cat (no language → `cultural_hit≈0`, and `u` low) but a pratfall lands (universal). The rubber chicken kills online (gets the reference) and only half-lands on the cat (only its physical half survives). *That* is humor literacy: the player learns **why**, grounded in theory, not a mystery number.

### Bonkyard's "Sir Loin → Miss Trotter" as a worked multi-filter example
It stacks **Wordplay** (sirloin / trotter puns) + **Character** (comic pigs) + **Reference/Parody** (a love-story trope) + **Madcap** (the physical contraption). Universal base (the physics is funny to anyone) **plus** cultural top-notes (the puns reward English speakers). 168 upvotes because it lands on two layers at once — exactly the universal-floor-plus-cultural-clothes model. The lesson for us: **let a bit carry both a universal physical beat AND an optional cultural top-note**, so it floors everywhere and spikes where the context is shared.

## 5. WHAT THE GAME TEACHES (the learning science)
With the model wired in, every reveal can *explain itself*: "The pun landed 2/10 — this room has no shared language; its laugh came from the physical beat only." The game stops being a taste-guessing quiz and becomes a **humor-literacy trainer**: players internalize the universal floor, learn to spot a room's benign line, and learn which filters need shared context. "Read the room" gains a real, teachable meaning: *identify the room's benign threshold and shared-context vector, then match the bit's violation and filter mix to it.*

## 6. IMPLEMENTATION SKETCH (single-file, no new deps)
- Add `filters[]`, `v`, `u` to each `GAG`; add `b`, and a `gets{wordplay,reference,shock,...}` map to each `ROOM`.
- Replace `actualFor` with the §4 formula (still deterministic → still learnable across rounds).
- Optional reveal line: name the filter and whether its miss was *context* (cultural) or *tone* (benign line) — that's the teaching moment.
- Keeps every floor: no network, nothing stored, pure math.

<!-- MANIFEST: grounds Funny Bonies' core in humor theory (benign violation as the engine, the Onion's 11 filters as the technique set, the universal/cultural axis as the room dimension). Next: founder ranks whether to WIRE THE MODEL into actualFor now (re-grounds the four gags/rooms above and turns reveals into teaching), or to first expand the gag/room cast against this model. Authorities to cite/seat if we go deeper: Peter McGraw (benign violation), Scott Dikkers (filters), and our standing John Cleese (open-mode) lens. -->
