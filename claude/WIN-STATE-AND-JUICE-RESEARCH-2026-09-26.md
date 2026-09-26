# WIN STATES, JUICE AND THE LEAP VOICE — studio research, 2026-09-26
<!-- source: founder, 2026-09-26: "Do some research on pleasing win states in games, like throwing in casino slot sounds etc give me options" then "Make this research persist in studio memory" | owner: mwalsh | status: RESEARCH (canon for design calls; the founder picks per build) | audition: archive/kireji-audition.html (retired after the founder's picks) -->

**One sentence:** celebrate in proportion to the win, only on real success, and never so loudly that the player loses sight of what they did.

This file is where the studio looks before choosing any win sound, reward effect or animated word. It is research, not a ruling. The founder's picks per build are recorded in that build's ledger rows.

---

## What the evidence says

| Finding | What it means for a TSP build | Source |
|---|---|---|
| Juicy feedback motivates mainly through **curiosity**, which predicted both enjoyment and time played. Success-dependent, amplified feedback built **competence**. | Vary celebrations a little so players wonder what comes next; attach big feedback to real success, not to every tap. | Kao et al., "How does Juicy Game Feedback Motivate?", CHI 2024 — https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf |
| Amplified effects **reduced effectance**: when effects cover the action, players can't tell what their action caused. The authors warn of "too much of a good thing." | The celebration must never hide the thing the player just did (the caught line, the smashed cliché). | same |
| Animated words (onomatopoeia and meaningful words) did not slow players down; **words plus particles** rated highest for appeal; meaningful words beat gibberish; water-themed effects best conveyed wetness. | The や works best as a real word with a splash of particles, not as decoration alone. | "Juicy Text: Onomatopoeia and Semantic Text Effects", ICMI 2024 — https://arxiv.org/html/2512.13695v1 |
| Visual embellishment changes how players feel about a game, not only how it looks. | Effects are a design decision with measurable weight, owned by a seat, not polish added at the end. | Hicks et al., "Juicy Game Design", CHI PLAY 2019 — https://dl.acm.org/doi/abs/10.1145/3311350.3347171 |
| On multiline slot machines, winning sounds made players **remember winning more often than they did**, including "losses disguised as wins" (paying back less than the bet while playing a win jingle). Players preferred the machine with sound on. | Casino sounds work by distorting memory of success. In a learning game that is a false signal about the player's own skill. Use only on a true win, never on a near miss or a partial one. | Dixon et al., Journal of Gambling Studies 2014 — https://link.springer.com/article/10.1007/s10899-013-9411-8 ; summary — https://uwaterloo.ca/news/what-does-winning-sound-you |
| The Mario coin is two square-wave notes a fourth apart (B5 to E6): short, bright, rising. | A tiny rising interval is the cheapest clear "yes." | Super Mario Wiki — https://www.mariowiki.com/Coin_(sound_effect) |
| Peggle's final peg slows time and swells into "Ode to Joy": a single, rare, over-the-top moment. | Save the biggest celebration for the rarest win, once. | https://en.wikipedia.org/wiki/Peggle |

## The ladder this implies (default for TSP games, founder may override)

1. **Each right call:** a tiny chime (W1 in the audition). Success only.
2. **A finished unit** (a poem): a short in-scale cascade (W2).
3. **A finished chapter** (a season): a bigger moment (W4).
4. **The ending, once:** the rarest, largest moment (W5 or W6), and it should carry the game's meaning — in Kireji, "water's sound."
5. **Never:** a celebration on a wrong answer, a near miss dressed as a win, or effects that cover the player's own action.

## The leap voice (Kireji)

- A synthesized voice reads as uncanny to the founder, whose bar for machine voice is low. A recorded human voice (the founder's, or a student's with written permission and attribution) is the strongest option; the audition page records one.
- Excited speech rises in pitch and widens its range; nervous speech trembles quickly and sinks. v5.2.4 applied this and the founder still found it weird on 2026-09-26, which is itself evidence for the recording route.

## Checks, not wishes

These are the parts of this research that can become arithmetic, for the Senses pass (`studio-senses/`):

- **Success-only:** every celebration sound fires only after a success state. The evidence crawl already logs the sounds each click makes; Ears can compare them against the game's announced outcome.
- **No occlusion:** during a celebration, the element the player acted on stays visible. This is measurable from state screenshots.
- **Proportion:** celebration loudness rises with the size of the win. Ears already measures level.

None of these is built yet. They are recorded here so the next Senses pass can make them real rather than adding prose rules.

## Audition page

`archive/kireji-audition.html` (retired 2026-09-26 after the founder picked voice C as YAH, や option 1 filled and following the frog with echoes, and W6; the page failed the belt's night-mode, image and entry checks and was never meant to last): five synthesized leap voices (A–E), record-your-own (F), five や effects, six win moments (W1–W6), all offline, levels balanced to within about 8 dB, contrast SHIP, Eyes PASS, Fingers 0 HALT.
