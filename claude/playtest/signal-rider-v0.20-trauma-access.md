# Signal Rider v0.20: Trauma-informed and access seat

Played at 390x844 in headless Chrome: warm-up, the default week to a fade, the checkpoint, the end card and the replay. Also an all-stress week under reduced motion to a fade and the "survival shortcut fired first" ending, plus a check of what the calm road deals. Steering was scripted. Evidence is in `sr-table/trauma-access/`; scripts are in `/home/claude/sr-scripts-ta/`.

## 1. What works (keep)

- **The scene comes first.** The first screen is the ride plus a one-line hint, with no wall (`01-cold-load.png`).
- **The copy does not blame.** The fade card and the alarm ending both say "That is the body protecting you, not a failure." The end card myth line says spines grow back. The pantry card says "Using them is support, not failure." The tray says "Use a week like yours, or any week. Nothing is saved," which lets players keep a distance (SAMHSA 2014, "empowerment, voice and choice"). The Library lists 988.
- **Recovery is already a real mechanic at the cortex.** In an all-stress week the greens still show up, and on the last leg they grew back 2 spines (`stress-log.txt`).
- **The arithmetic floors hold.** All HUD, banner, toast and replay text is 11.9:1 to 18.1:1. Both full-screen flashes are below the WCAG 2.3.1 general-flash threshold: the luminance change is 0.06 and 0.01, against a 0.10 threshold, and #ff4fa3 is not "saturated red" (0.51, where saturated means 0.8 or more). Reds and greens differ in shape as well as color. Every flash is also spoken.
- **One-handed steering works.** You can hold either half of the screen or drag anywhere (line 619).

## 2. Top findings, ranked

**1. The calm road still deals rent, hunger and loneliness as obstacles.**
- **Seen:** the calm road dealt 15 red cubes covering all 10 stress cards, including `rent`, `food` and `alone` (`calm.py` output). The cause is line 239: an empty choice falls back to the full red deck. A week with only supports does the same. The tray and the Library promise "Choose the calm road to ride with no week."
- **Why:** this breaks SAMHSA's "trustworthiness and transparency" and "choice" principles. MassBay's Institute of Trauma and Resiliency names "flexibility and choice" and content warnings as core practices ([MassBay ITR FAQ](https://www.massbay.edu/institute-of-trauma-resiliency/faq)). Carello and Butler (2014, *Journal of Trauma & Dissociation*) warn that teaching about trauma can retraumatize when exposure isn't controlled.
- **Fix:** when a stress card was not chosen, deal a blank rough cube ("A hard moment", no icon). The gameplay stays the same, including the 3-bad canon.
- **Size:** S.

**2. Life circumstances still count as the player's mistakes (open since Horvath 11-06).**
- **Seen:** the all-stress fade card reads "Pink blocks hit you 3 times: Rent due, Skipped meals, Feeling alone" (`22-stress-fade.png`). The HUD label is "Hits", and the warm-up says "You dodged a stress cube" (line 995). The message is: dodge poverty with skill, and it's on you when you don't.
- **Why:** Harvard's Center on the Developing Child defines tolerable stress as stress that is *buffered by supportive relationships*, not avoided. Crum, Salovey and Achor (2013, *JPSP*) show that the mindset a person holds about stress changes their outcomes. Juul (*The Art of Failure*, 2013) describes game failure as felt personal inadequacy. That is fine for a skill, but not for being food-insecure.
- **Fix, within canon:**
  - Relabel the HUD "Hits" as "Load".
  - Open the fade card with "Three heavy things at once. Any nerve would stall here."
  - Rename the list "What you carried".
  - Always deal each Money-and-basics or Time red cluster with a matching green one lane over (pantry, if-then plan), so help exists in the mechanic, not only in the text.
- **Founder ruling needed:** should week cubes count toward the 3? Horvath proposed that only frayed bands and missed landings count.
- **Size:** S for the copy, M for the pairing.

**3. Damage never heals by itself.**
- **Seen:** `bandT` changes only on a hit or a green, and on checkpoint restore (lines 289-291, 343). There is no decay. The Library says stress effects come "back when the stress passes."
- **Why:** Radley et al. (2005, *Experimental Neurology*) found that stress-induced spine loss reversed after the stress stopped. Arnsten (2009) makes the same point. The ride teaches that damage is permanent unless you earn greens.
- **Fix:** after 4 s with no new bad, ease `bandT` back toward `band0` at about 0.03/s and draw the stripes thinning ("knitting"). That gives pressure-and-relief pacing for free.
- **Also fix (transparency):** two lines still say greens "do not change your speed" or "Nothing in the ride speeds you up" (lines 104 and 148). Since v0.16 greens surge.
- **Size:** S.

**4. The tray teaches positive stress, but the ride doesn't let you play it.**
- **Seen:** the tray says a test is "positive stress: you rise to them". On the ride, every red does the same harm.
- **Why:** Jamieson et al. (2010, *JESP*; 2012, *JEP: General*) found that reappraising arousal as fuel improved test scores and cardiovascular response.
- **Fix:** a single-event red (weight 1) hit within 3 s of taking a green becomes a surge, labeled "Rose to it". That adds a risk-and-reward routing choice, which helps engagement.
- **Size:** M. UNPROVEN that players will notice the combo without a cue.

**5. The outside-event pictures can't be read during the ride.**
- **Seen:** the cube icons are drawn #d9e2ee on #6dff8a (1.02:1) and on #ff4fa3 (2.33:1) (`contrast.txt`, line 1106). The picture becomes legible only after a hit, in the top banner. The founder ruling says the picture comes first, then what happens to the nerve.
- **Fix:** draw each icon on a dark disc inside the cube (#14301f gives 10.9:1, #3a1830 gives 11.9:1), the way the tray's `cubeSvg` already does.
- **Size:** S.

**6. For the RP reader, flashes land about 10 degrees from the spark.**
- **Seen:** the effect banner sits at the top, about 380 CSS px above the spark. On a 64 mm-wide phone at 35 cm that is about 10 degrees, which is the edge of a 20-degree field (`05-ride-effect-1.png`). `placeMsgs` deliberately puts text "where the ball is not".
- **Seen:** alarm spines (#ff4f7a) against thinking spines (#ff4fa3) measure 1.04:1, so only their shape tells them apart, on the leg where the game asks you to "steer against the pull."
- **Seen:** the "Wrong shape" and "Missed" labels are 5.8 to 6.7:1, below the 7:1 target.
- **Fix:**
  - Put a one-word echo ("Load", "Clear") next to the spark, radially *outside* the tube, which is never in the incoming path.
  - Give the alarm spines a dark fill with a white outline.
  - Change the labels to #ff8fc4 (8.3 to 9.7:1).
- **Size:** S.

**7. The lightning ignores reduced motion.**
- **Seen:** `spawnBolt` runs at (0.9 + 3·stress + 4·dim) per second, up to about 8/s, plus 2 per bad (lines 478 and 536). The link lightning jitters every frame (line 547). Neither respects `reduce` or Glow. Bolts are visible in a run captured with `reduced_motion='reduce'` (`21-stress-leg4-4.png`).
- **Why it may matter:** at peak, the bolts alive at once may come close to the WCAG flash-area limit on a phone. UNPROVEN either way.
- **Fix:** add a Settings row "Lightning: on / few / off", with "few" under reduced motion, and a hard cap of 3 bolts per second. That makes 2.3.1 pass by construction.
- **Size:** S.

**8. Some controls are hard to reach with one thumb.**
- **Seen:** "Skip replay" sits at the top, around y=195 (`12-replay.png`). The Studio link exits mid-ride with no confirmation.
- **Fix:** move Skip to the bottom, and show the Studio link only on sheets.
- **Size:** S.

## 3. The one change first

Finding 1: no unchosen life-event pictures on the calm road or in support-only weeks. It is small, it can be checked (count the red card ids on the calm road; it should be 0 named stressors), and it fulfils a promise the game already makes in writing. Fixes 2 and 3 then build on a ride the player can trust.

## 4. Wishes (no honest check this cycle)

- Campus supports beside 988 (MassBay counseling, the pantry). The links need verifying.
- A peer-support verb: call a friend who clears one band (SAMHSA).
- A warmer voice for the stress lines. A low, fast "Nobody to text back" may land cold.
- A one-line content note before the tray (MassBay ITR).
- A live playtest with an RP reader and with students facing basic-needs insecurity. A bot cannot measure how a picture feels.
