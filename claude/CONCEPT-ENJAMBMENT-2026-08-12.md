# CONCEPT — ENJAMBMENT (EN195 Poetry district), 2026-08-12

*Captured the turn it was given (make-work-stick). Founder concept verbatim first;
studio findings second and labeled as such. This is a concept brief, not a build
spec — it names what the thing is, what already exists that it must absorb, and the
four design questions that have to be answered before anyone writes a line of it.*

## VERBATIM (founder)

> "working on EN195 Studio new concept: ENJAMBMENT -- inspired by the Lucy and Ethel
> chocolate assembly line episode, poems appear like ticker lines on times square
> billboards and TV news sets, and use has to cut them appropriately for easy
> traditional poems like Robert Frost. Show meter and rhyme through the game
> (trochee, iam, double dactyle etc) THROUGH the game like dance dance revolution.
> Make the setting for the game represent the context for the poem in a way that
> allows reader to feel immersed. Make the beat (bass) match the meter. Pause at
> times to let the reader see the stanza, feel the pause, let the "turn" sink in --
> the game is a base that will teach many aspects of poetry aligned with EN195
> outcomes. They don't need to learn double dactyl for this class; just know what it
> does. Students will have option to submit free verse or formal verse. The arcade
> should help them read, write, revise and respond to poetry."

## WHAT ALREADY EXISTS (this is not greenfield)

**`en195-arcade.html` already has a Poetry district and a cutting game.** Line Break
is at **v3**, rebuilt twice under founder playtest ruling on 2026-08-09:

- v5.3 ruling: *"mechanic failed because it did not create what it teaches"* — poem
  flattened to prose, scissors in hand, each cut re-forms the poem live in a verse
  card below, so enjambment is **watched** rather than described. Paste is free and
  returns the scissor; cuts blocked at zero.
- v6.2 ruling: *"WCW is crazy hard to start with; the start should be a block of prose
  and nothing else"* — trainer passage is the founder's own line (5 scissors), Williams
  is second (his own 7 breaks), entry paint is clean prose alone.

ENJAMBMENT is therefore **the promotion of Line Break into a full cabinet**, not a
second game beside it. If both ship, the Poetry district has two games teaching the
same cut, and the weaker one is the one that already passed playtest.

Also standing and binding on this build: the 08-09 rulings (3x graphics, genre
districts, feed the beings, comfort top-only), the Samorost art brief
(`claude/HANDOFF-ARCADE-ART-SAMOROST.md`), and the 08-10 feedback
(`claude/FOUNDER-FEEDBACK-EN195-ARCADE-2026-08-10.md`) whose **item 1 is precisely
this ask** — *"they should look like games... thoughtfully produced,"* not
icon-in-circle-plus-text.

## FINDINGS — four questions to answer before building (studio, not founder)

### 1. The belt and the pause are opposite pedagogies. Resolve which is the loop.
The Lucy-and-Ethel gag is **failure by acceleration** — the joke is that you cannot
keep up, and the belt wins. The concept's second half asks the opposite: *stop, let
the reader see the stanza, feel the pause, let the turn sink in.* Both are good; they
cannot both be the core loop.

**Proposed resolution (founder call needed):** the belt is the **hook**, not the loop.
The ticker accelerates to the point of comic failure — lines pile up, cuts go wrong —
and *that failure stops the belt*. The room goes quiet, the mangled stanza hangs on
the billboard, and the player gets the turn in silence. The player earns the pause by
blowing it. This is Kintsugi-native (the fracture is the data, the mend is the lesson)
and it keeps the Lucy joke intact instead of sanding it into a metronome.

### 2. DDR scoring can teach something false about scansion.
DDR rewards hitting one correct beat at one correct time. Scansion is **interpretive** —
competent readers scan the same line differently, and the ambiguity is often the
point (Frost's whole trick is a conversational voice riding a strict frame). A game
that hard-scores one stress pattern as *correct* teaches students that poems have
answer keys.

**Proposed resolution:** score the **pulse**, not the parse. The player feels/taps the
beat and the game confirms the pulse; where a line genuinely scans two ways, the game
accepts both and then *shows the difference* — plays it back one way, then the other,
and asks which one they meant. Contested lines become the best teaching moments
instead of the bug reports. Consistent with the founder's own bar: *they don't need to
learn double dactyl, just know what it does.*

### 3. Times Square neon vs. Samorost organic — a live art conflict.
The banked art direction for this arcade is Samorost: organic, hand-cut, mossy stumps,
mushrooms, drifting spores, small watching beings. The concept asks for Times Square
billboards and TV news sets — hard neon, chrome, broadcast. These do not sit in one
world by default.

**Options:** (a) the ticker is a *thing inside* the organic world — a salvaged
broadcast sign grown over with moss, glowing in the woods; (b) the setting genuinely
changes per poem (concept explicitly asks the setting to *represent the poem's
context*, which for Frost is snow and woods and fences, **not** Times Square); (c) the
neon is the machine and the poem's world is what the machine interrupts. **(b) is the
founder's own stated intent and probably resolves (a) and (c) for free** — the
billboard is the *delivery* device, the setting is the *poem's* world, and Frost's
poems get New England, not Broadway.

### 4. Frost is usable, but only through 1930.
US public domain in 2026 = published before 1931. **Clear:** *A Boy's Will* (1913),
*North of Boston* (1914), *Mountain Interval* (1916, incl. "The Road Not Taken"),
*New Hampshire* (1923, incl. "Stopping by Woods on a Snowy Evening," "Nothing Gold Can
Stay"), *West-Running Brook* (1928, incl. "Acquainted with the Night"). **Not clear:**
anything from 1931 on ("Design," 1936). The arcade's existing policy is public-domain
text, attributed in-file (WCW 1923) — this build inherits it.

Bonus: the clear list is *ideal* for the mechanic. "Stopping by Woods" is strict
iambic tetrameter with a chained rhyme (aaba/bbcb) — the rhyme scheme itself pulls the
poem forward, which is the same forward-pull the belt supplies. "Acquainted with the
Night" is terza rima and a sonnet at once. "Nothing Gold Can Stay" is eight lines and
teaches the turn in under thirty seconds.

## SCOPE NOTE (cost discipline)

The full concept — ticker, per-poem immersive settings, meter-matched bass, DDR
timing, pause/turn beats, free-verse and formal submission — is a multi-session build,
not one sitting. Suggested sequence, each shippable alone:

1. **Absorb Line Break into ENJAMBMENT's frame.** Keep the playtested scissors
   mechanic; give it the cabinet presentation 08-10 item 1 asks for. Ships the
   founder's oldest open note.
2. **Add the belt.** Ticker delivery + accelerate-to-failure + the earned pause.
   One poem ("Nothing Gold Can Stay" — eight lines, fits the frame).
3. **Add the bass.** Web Audio is already synthesized in-file in this arcade; a
   meter-matched bass pulse is cheap once the belt has a tempo.
4. **Add the settings.** Per-poem world, Samorost idiom, one poem at a time.
5. **Submission lane (free verse / formal).** Rides the existing Workshop Vending
   Machine + Supabase path; do not build a second submission mechanism.

Motion-stop, the comfort ladder, and the type floor are **not** a later pass on this
one. A timing game with an accelerating ticker and an animated setting is exactly the
build that has to hold the motion pair and the reader's enlarged base font from its
first paint — the founder plays on a phone at an enlarged base, and the studio's
accessibility-first intent is the reason the arcade exists in this shape.

## BUILT — `enjambment.html` v1, same day

Steps 1 to 3 of the sequence above are playable at `enjambment.html`, with the
three findings built in **as answers to be playtested, not as settled law**. The
belt accelerates and the poem's own turn jams it; the rest arrives at the reader's
pace; the meter round offers both real scansions of line 1 and marks neither wrong;
the setting is the poem's woods with a salvaged broadcast sign in them.

Gate state: art-gate pass, preship-gate-v5 SHIP (0 halts), studio-voice-gate SHIP,
one-thing-gate WARN. Headless playtest drives both rounds end to end in both modes
with no JS errors.

**The one open WARN is real debt, not a nit:** `SUB-50-TABLEAU`, entry tableau 0%
image. All scenery in this file is CSS, because the 2026-08-01 art ruling bars
hand-authored SVG scene art and this session has no MJ lane. one-thing-gate counts
only `img/svg/canvas/video` as a visual, so a CSS scene reads as no scene at all.
The honest fix is a real plate from the founder's own Midjourney lane, in the
Samorost idiom already banked. Until then the entry is a competent CSS scene that
the gate cannot see and will keep flagging.

**Motion stop turned out to be a second playable mode, not a setting.** The first
headless run with reduced motion produced a frozen belt: words never reached the
head, so the poem could never be cut and the turn never came. A dead game, on the
setting an RP reader is most likely to have on. The still mode is Line Break v3's
own shape, which is the strongest argument yet for the absorb-Line-Break question
below: the accessible version of ENJAMBMENT *is* Line Break, so the two cabinets
are already the same cabinet in different weather.

## OPEN — founder calls needed

- **PENDING:** Is the belt the hook (accelerate → fail → earn the pause) or the loop
  (sustained speed pressure)? Finding 1.
- **PENDING:** Setting per poem (Frost gets woods, not Times Square) — confirm the
  billboard is the delivery device, not the world. Finding 3.
- **PENDING:** Does ENJAMBMENT absorb Line Break, or do both cabinets stand?
