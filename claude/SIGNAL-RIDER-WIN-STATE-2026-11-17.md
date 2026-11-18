# Signal Rider: win-state proposal, 2026-11-17
<!-- source: founder 2026-11-17 20:30 "That gameplay was decent, but there needs to be some visual reward as a win state. What would Osterweil turkle Hitchcock suggest ?" | build at time: v0.23 (e249f9f3) | canon: claude/WIN-STATE-AND-JUICE-RESEARCH-2026-09-26.md | status: PENDING founder pick -->

**Now:** reaching the thinking cortex plays a bell and the end card appears at once. There is no visual payoff.

## Seats
- **Hitchcock (composition, timing):** the pull-back. The tube opens, the camera pulls out, and the whole route you rode lights up in one shot, fingertip to spinal cord to thalamus to cortex. Hold the image about 3 s with no text, then raise the card. Suspense, then release, with no words over the picture.
- **Osterweil (meaning):** the reward is the system finishing its job. The touch becomes a perception: a picture of what you felt resolves (a friend's hand, a cat's fur). Let the player drift in the lit cortex for a few seconds before the card (freedom to linger).
- **Turkle (evocative object):** give the player something that is theirs. This ride's week grows a one-off Brainbow neuron whose branches and spines are the ones you earned and kept. You see it again on the end card, and each week grows a different one.

## Studio canon that binds
- The ending is the rarest and largest moment, and it carries the game's meaning.
- Temple bell (W6) is the founder's pick for the sound.
- Never a celebration on a near miss.
- No effects covering the player's own action.

## Chair recommendation
One combined moment of about 6 s:
1. Pull-back across the lit route (Hitchcock).
2. The cortex blooms into your neuron (Turkle).
3. The touch resolves to its picture (Osterweil).
4. Temple bell, then the end card.

The alarm ending gets its own calm visual (the alarm glows and settles; "the body protecting you"), never a "lose" screen.

## Founder pick, 2026-11-17 20:32: "1." Built as v0.24 (`claude/signal-rider-build-v24.py`)
**The cortex ending runs about 6.5 s, and a tap skips it:**
1. The camera rides the bright signal head and pulls back from 3x to the full route. The route draws as a five-strand Brainbow bundle, fingertip to cortex, and each relay flashes as it passes.
2. Your neuron blooms in the cortex, with the temple bell at 2.4 s.
3. A ripple at the fingertip is answered by the neuron's pulse.
4. "You felt it." appears at 5.2 s and is spoken.

**The alarm ending runs about 4.6 s:** the route lights to the sensory cortex, the alarm swells pink, then settles into a slow amber breath. "Your alarm answered first." appears at 3.6 s.

**Throughout:** the HUD and messages hide during the ending. The end card shows your neuron. Reduced motion: no camera move, a 2.6 s version.

**Verified:**
- A full hard-week ride triggered the ending from the real finish (timeline 0 to 6.3 s, then the card).
- Frame strips of both endings were checked for composition, fit and the hidden HUD.
- No page errors. Contrast gate SHIP.

**Held:** Osterweil's "a picture of what you felt" (a hand, fur) is a line of words, not a drawing. A drawn object would need its own art pass to clear the studio's no-uncanny bar.
