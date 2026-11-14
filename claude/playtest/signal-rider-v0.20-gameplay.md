# Signal Rider v0.20: Gameplay seat (game feel, difficulty, flow, core loop)

2026-11-14. Played lab/down-the-nerve.html at 390x844 in headless Chrome. Five scripted runs: skilled autopilot (default week), human-like autopilot (250 ms reaction lag, about 2 s look-ahead; default week and maximum-stress week), idle (no input, through a fade and a checkpoint return), and a leg-4 stress landing captured beat by beat. Screenshots and logs are in sr-table/gameplay/. Scripts are in /home/claude/gp-scripts/. Bots see the game state exactly, so anything they suggest about how hard it is for humans is marked UNPROVEN.

## 1. What works (keep)

- **Failure is cheap.** Checkpoints sit at each leg's halfway mark and at every relay, so a fade costs about 18 s at most. One tap brings you back with hits reset (idle-default-fade-0.png). This matches Juul's case that failure feels fair when it is quick to recover from and the player can see why it happened (Juul, *The Art of Failure*, 2013).
- **Hits read clearly.** A hit drops speed from about 75 to 21 m/s, the hit box fills, and a band flash plays (idle-default-ride-hit2.png). A warning sound plays at 2 hits.
- **Each landing beat gets a crisp verdict:** Match, Half, Wrong shape, or Missed, plus a progress arc. That is the immediate feedback flow needs (Csikszentmihalyi, *Flow*, 1990).
- **Hidden assist.** Each hit lowers cruise speed by 10% (floor 72%), and it creeps back over time. That is dynamic difficulty the player never sees, the approach Hunicke (2005, ACE) argues for.
- **Scene first.** The warm-up is about 20 s with two pickups, and the tube moves before any text.
- **Spatial audio** (the landing beacon and pickup sounds are panned left or right) is a real help for low vision.

## 2. Top findings, ranked

**F1. Hold and keyboard steering go the opposite way from drag steering. (S)**
- **Saw:** with "Tube stays still" on, holding Right moves the spark to the left (dir-c-still-before.png, then dir-d-still-after-right.png). With the default rolling view, holding Right slides the world to the right, so you end up left of what you were aiming at (dir-a-before.png, dir-b-after-right.png).
- **Code:** hold and keys use `run.theta+=steer*2.7*dt`, but drag uses `run.theta-=dx*0.012`. The two touch modes disagree with each other.
- **Why it matters:** game feel starts with the input-to-response mapping (Swink, *Game Feel*, 2008). A control that moves the opposite way breaks natural mapping (Norman, *The Design of Everyday Things*).
- **Fix:** flip the sign on hold/keys, then check both views. Whether players experience the rolling view as inverted is UNPROVEN; the still view is inverted beyond doubt.
- Check: flip the sign and run a cold test with 3 people, both views · build seat · 2026-11-17.

**F2. The tube is straight about 90% of the ride, and the pacing is one flat drone. (M)**
- **Saw:** I rebuilt the curve-easing code for 12 generated layouts. Curves run at full strength on only 5% of the track and above half strength on 8%.
- **Cause:** about 16 bands and 37 to 39 pickups per ride put an event every 10.5 to 12.4 units (median), roughly 1.7 s. The easing needs 14 clear units to reach full curve, so curves almost never get room.
- **Why it matters:** the founder wanted bends that change the background, kept to clear stretches. The current layout leaves no clear stretches. Even spacing also removes the rhythm of tension and release. Smith et al. (2009, "Rhythm-based level generation for 2D platformers," FDG) build levels from rhythm groups with rests between them. Thumper and Audiosurf are built on exactly that phrasing.
- **Fix:** lay each leg out as phrases: 2 or 3 dense sets, then a 28-unit breather (about 4.3 s, two bars at 112 BPM) held free for an S-bend and a backdrop shift. Line the sets up with the music's phrase boundaries.
- Check: at least 25% of track above half curve strength, and no event within 10 units of any curve peak · build seat · 2026-11-19.

**F3. The landing puzzle is a left-or-right guess, and stress makes it easier. (M)**
- **Saw:** I simulated `reachPick`. On a 5-spine face, 100% of beats target an adjacent spine (1.26 rad away). The player only decides which neighbor.
- On the 2-spine stressed face, 67% of beats target the spine you are already on, so you just hold.
- **Why it matters:** decision time grows with the number of choices (Hick, 1952), and movement time grows with distance (Fitts, 1954). With 2 choices and mostly no movement, the hard week's landing asks less of the player. That runs against "real work, slight puzzle" and against "fewer pads = harder." Right now stress shows up only as a longer landing and the pull toward the shortcut.
- **Fix, part 1:** show the next messenger beside the current one (a one-beat preview) so the player plans a two-step route.
- **Fix, part 2:** draw targets from every spine in reach, including spines two away.
- **Fix, part 3:** on the stressed face, every target is the far spine, against the pull. Fewer places then means more travel under pressure, never a free hold.
- Check: no beat targets the current spine, and with stress the mean steering distance per beat goes up · build seat · 2026-11-19.

**F4. On the stressed face, the spines are hidden at the moment that decides the landing. (S)**
- **Saw:** at beat 0 the two thinking spines sit behind the key disc and its closing ring; only slivers show at the right (stress-leg3-beat0.png). The alarm stars sit beside the spark.
- An idle rider drifted into the shortcut in 3 beats (stress-leg3-final.png).
- **Cause:** the stressed gap is 5.5 units against 4 normally, so the face starts farther away and smaller. The key disc (radius about 42 px) and its closing ring (44 to 87 px) cover a spine ring of about 47 px.
- **Why it matters:** the founder has RP, and a target the player cannot see is not a puzzle (studio floor: no hunting).
- **Fix:** move the key to a slot above the face, or start the stressed face at the normal depth.
- Check: spine ring is never occluded on any beat (pixel probe) · build seat · 2026-11-17.

**F5. An attentive player meets almost no challenge, and nothing invites a repeat. (M) UNPROVEN for humans.**
- **Saw:** the lagged bot finished the maximum-stress week (2 spines, very wide bands, strong pull) with 0 hits; it took one green and dodged every pink. The idle rider faded at unit 157 of leg 1.
- So difficulty runs from trivial to failing, and the "every bad widens bands" spiral never touches a good player.
- The end card shows elapsed ms, and greens do lower it, but it is never framed as something to beat.
- **Why it matters:** flow needs challenge that rises with skill. Chen (2007, "Flow in games (and everything else)," *CACM*) argues for letting players choose their difficulty through in-game choices. Personal-best goals tie to engagement (Martin, 2006, *British Journal of Educational Psychology*). That is competition with yourself, which fits the trauma-informed floor.
- **Fix, part 1:** chained greens stack the surge (1.3x, then 1.45x, then 1.6x), held until you miss a green or take a bad. That is the founder's "accelerator" turned into a risk you choose.
- **Fix, part 2:** the end card shows "your best: N ms" for this session only.
- Check: run 5 cold players and log hits and replays per session · founder · 2026-11-24.

**F6. Rule text still says greens do not change speed. (S)**
- **Saw:** the legend in the tray's "How the ride works" says "They do not change your speed." The Library says "Nothing in the ride speeds you up" and "Line up with a lit spine to land."
- **Why it matters:** this contradicts the v0.16 accelerator and lock-and-key rules. Flow needs clear goals (Csikszentmihalyi, 1990).
- **Fix:** rewrite the three lines.
- Check: grep finds none of the three strings · build seat · 2026-11-16.

## 3. The one change I'd make first

F1: flip the hold and keyboard steering sign. It is a one-character fix, and every other feel note depends on it. Measuring curve, density, or landing difficulty on a control that may be inverted measures the wrong thing. After that, F2's phrase layout, because it brings back the curves and the rhythm together.

## 4. Wishes

- WISH: a 60 to 80 ms ease-in on hold-steering (Swink's attack curve). Needs a human feel test, so no honest check this cycle.
- WISH: place obstacles from the music clock, so sets land on beats (Audiosurf model).
- WISH: haptic tick on hits and matches through navigator.vibrate, where the device supports it.
- WISH: a ghost of the last run on "Ride the same week" (echoes Osterweil seat item 6).
