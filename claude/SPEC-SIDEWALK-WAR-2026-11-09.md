# SPEC: Sidewalk War v0.1 (LAB), 2026-11-09

Build: `lab/sidewalk-war.html`. Single file, offline, studio-cut art.

## Founder ask (verbatim)

"Create an ant warfare simulation slash strategy game that teaches players how real ants work in real habitats. Artwork must meet animata studios and don't say no."

## The sentence

The player steers a pavement ant colony through its chemistry (scent trails, alarm calls, colony emphasis) and notices that no ant gives orders: trails, nestmate recognition, and crowd size make the war.

## Medium gate

Real-time strategy on a canvas. The habitat is the one most players walk over: a garden bed, a concrete sidewalk with expansion cracks, a lawn edge. Pavement ants (Tetramorium immigrans) were chosen because their sidewalk wars are real, common in spring, and well studied.

## Art direction (named before the first pixel)

"Animata" in studio canon (claude/WORKSHOP-VENDING-MACHINE-SPEC.md) means real-time digital puppetry rooted in shadow-puppet theatre: a live, rigged, moving thing, not a still image. Combined with the studio's Lumino City paper-set bar:

- Each ant is a rigged shadow puppet: five body parts (head, mesosoma, petiole, postpetiole, gaster; Myrmicinae have the two-node waist), elbowed antennae, six two-segment legs walking an alternating tripod gait, a rim light, a cast shadow.
- The set is cut paper: hand-cut jagged edges, fibre noise, double shadows, warm light as material from the upper left, vignette.
- Pointed cut-paper bean leaves, no lollipop shapes.
- Colonies read by shape as well as colour: amber round dot (yours) and pale dash (rival), the field researcher's paint mark. Territory reads by pattern: hatching (yours) and dots (rival).

## Domain rep: research first, then gaps

| Mechanic | Source | Status |
|---|---|---|
| Trail recruitment, positive feedback | van Oudenhove et al. 2012, J. Chem. Ecol. 38: 802-809 | sourced |
| Trail evaporation, faster in heat | same | sourced |
| Nestmate recognition by cuticular hydrocarbons | Sano, Bannon & Greene 2018, J. Insect Behav. | sourced |
| Fight decision depends on recent nestmate contact and crowd size | Greene, SICB 2013 abstract 49.2; Hoover et al. 2016, Current Zoology 62: 277-284 | sourced |
| Ritual push-of-war, few deaths, wars show colony size | Plowes 2008 via Sano et al. 2018 | sourced |
| Some ants recruit instead of fighting; wars form in about 30 min | Sano et al. 2018, citing Hoover 2016 and Plowes 2008 | sourced |
| Monomorphic workers, no soldier caste; older workers forage and defend | Wikipedia, AntWiki | sourced |
| Honeydew, seeds, insects, human food | AntWiki; MacGown & Whitehouse (MEM) | sourced |
| 2017 split from T. caespitum | Wagner et al. 2017, Myrmecol. News 25: 95-129 | sourced |
| Summer nuptial flight | AntWiki sexual records; Wikipedia | sourced |
| Wars mostly spring and early summer | field observers (tightloop.com 2021; Something's Crawling in My Hair 2023) | observation, labelled |
| Rain washes trails | none found | STUDIO INVENTION, labelled in game |
| 1 ant drawn = 20 workers; 1 day = about a week | none | STUDIO STAGING, labelled in game |
| Brood timings | general life cycle only | STUDIO STAGING, labelled in game |

## Player verbs

1. **Scent trail** (tap): paints a trail from the nest to the spot and sends three ants. Ants still forage on their own without it.
2. **Alarm call** (unlocks at the first meeting with the rival): paints alarm scent and raises the colony's turnout.
3. **Colony emphasis**: Forage, Brood (faster larva feeding, more eggs, fewer ants outside), Muster (more ants out, alarm scent weighted).
4. Notes and Pause.

Keyboard: arrows move a reticle, Enter taps, T and A pick tools, 1 to 3 set emphasis, N opens notes, Space pauses.

## Win state

Twelve days, then the summer flight. Queens = stored food, colony size, ground held, garden bonus. The celebration is the alates rising from the nest, proportional to the count; no fanfare on a loss (WIN-STATE research rule 5).

## Seats (inline, cost-scoped)

- Horvath (learning): each note fires on the event it explains, not on a timer, except the two orientation notes.
- Osterweil (freedom of play): the colony plays itself; the player nudges. No wrong tap.
- Stranger: brief on top, one verb at entry, Alarm call unlocks later.
- Studio Eyes / Fingers: run via preship; results in the ledger row.

## Open founder calls

- Sound: none in v0.1. Studio Ears seat should audition a war murmur and a flight sound.
- A second species (Lasius neoniger, the cornfield ant, shares New England lawns) as a v0.2 rival.
- Is the garden bonus the right victory weight?
