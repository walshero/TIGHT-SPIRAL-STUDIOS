# FUNNY BONIES FACTORY — THE META-MACHINE (design)
<!-- 2026-07-29 · design lane · the P3 frontier: the thing founder-canon #5 calls "the whole reason the idea was exciting," still homeless. Design only — no build yet. -->

## THE HEART (what got dropped, and why it matters)
The original idea had two halves. The single-player half shipped: build a gag, read a room, see the gap. The other half — *the meta-machine that connects everyone's machines into one story, and a social score* — never got built, and founder-canon #5 names it as **the reason the idea was exciting**. Without it, v7 is a clean calibration trainer. With it, it becomes what you pitched: a **Rube Goldberg Laugh Factory** where your little machine is one link in a chain that spans every player.

## THE WALL (the design problem, stated honestly)
"Connect everyone into one story" and "a social score" sound like a server, accounts, a live leaderboard. The studio floors forbid all of it: **single-file, offline, zero network calls, nothing stored across sessions.** Past attempts died here — you can't have "everyone" with no network. Any honest meta-machine design has to get through this wall, not wish it away. Two cheats are banned outright:
- **No fake-live.** A baked crowd pretending to be real players is the hollow-claim failure this studio hates most ("never pretend a signup landed"). Simulated social must *say* it's simulated.
- **No silent storage.** No localStorage, no accounts, no server. The durable thing has to live somewhere the floors allow.

## THE WAY THROUGH — three moves

### 1. The reframe: the crowd was always "people like you"
The game already tells the player *"the cohort was people like you."* The meta-machine makes that literal. The "room" you read in single-player is a stand-in for **other players.** So the meta layer isn't bolted on — it's the single-player fiction, made true. You stop predicting a baked taste vector and start predicting **what real people actually did.**

### 2. The Ticket — the human is the network
The studio already has an offline transport it trusts: **carry-out.** The playtest instrument emits a text block; the person relays it. Apply it to the game:

> When you finish a round, the game emits a **Ticket** — a short code (a text string, or a `#fragment` on the URL) that encodes *your machine* (the bit you built + the room you read + your call). You hand it to someone — text it, paste it, read it aloud. They load the Ticket, and **your machine becomes a real link in their game**, your call becomes a real data point in their crowd.

No server. No storage the studio bans. **The human carries the state**, the way a physical playing card carries a game between hands. This is the studio's own "the chat is disposable, git is durable" pattern pushed to the player: *the session is disposable, the Ticket is durable, carried by a person.* It is offline, single-file, zero-network, nothing-stored — and genuinely social, because real people made those Tickets.

### 3. The House Seed — so a lone player isn't alone
A first player with no Tickets would meet an empty social world. Ship a small **authored founding crowd** — a dozen hand-made machines + calls — so there's a story to join on first launch. It is **labeled "the house crowd"**, never disguised as live. Real Tickets layer on top of it and, in the fiction, *retire the house* as real players arrive. Honest by construction.

## THE ONE STORY — the meta Rube Goldberg (mood is the marble)
This is what makes it *one story* and not a gallery of separate games. Chain the machines:

- Every machine has an **output**: how the room it played to was left — cracked-up, warmed, or cold.
- That output is the **input** to the next machine: the next player inherits a crowd already primed (or exhausted) by the last gag. Follow a sold-out room and expectations are high; follow a bomb and a small laugh is a triumph.
- So the marble that rolls between machines is the **crowd's mood.** Load a reel of Tickets and you can **watch the whole chain fire** end to end — marble → bucket → chicken → cat, then the cat's mood becomes the next machine's starting room. A Rube Goldberg machine *made of machines.*

"Connect everyone's machines into one story" = a literal chain reaction that crosses players. The reel is the story; it's playable, and it's shareable as one longer Ticket.

## THE SOCIAL SCORE — two honest numbers, never a shame-board
Founder floor: *a flat gag is a fact, not a failure.* The social score keeps that. Two axes, both **relative to the actual reel you're in**, never a fake global rank:

- **Reader:** how close your call was to what the crowd *actually* did (real other-player calls from Tickets, or the house seed until then). This is "you read the room" scaled to "you read the *crowd*." It is calibration — the studio's own moat.
- **Maker:** when your machine rides in someone else's reel, did the next players' calls say your bit *landed*? "Your bit carried the chain."

The score is a **position, not a verdict** — "you read this crowd better than most of it" is a fact about calibration, said the way norming says it, not a leaderboard designed to sting. And it is honest about its denominator: *"scored against the 14 people who've played this reel,"* never *"ranked #3 in the world."*

## THE PAYOFF — humor as a visible distribution (the moat, at meta scale)
Single-player reveals **one room's** hidden taste. The meta-machine reveals the **whole landscape**: as Tickets accumulate, the game can draw the crowd's sense of humor as a *distribution you can see* — where the laughs cluster, where you sit in it, which rooms disagree. "Make the invisible constraint visible" at scale. And note what that actually *is*: **many raters, one distribution, your position in it — that is norming.** The meta-machine isn't a bolt-on social gimmick; it's the studio's assessment moat (rater-calibration) turned into the game's endgame. The thing that made you say yes and the thing the studio is actually *for* are the same mechanic.

## PLAYER EXPERIENCE (sketch, not final)
1. Play a round as today (read the room, own the bet).
2. **"Send your machine →"** emits a Ticket (copy / share-sheet / show the code).
3. **"Load a reel →"** paste a Ticket (or open a shared `#fragment`): the sender's machine joins your factory; you can *watch the chain fire*, and now your crowd includes real calls.
4. **The floor** (the map): your position in the crowd's laugh-landscape — reader + maker — labeled with its honest denominator.
5. First launch meets the **house crowd**, clearly the house, retiring as real Tickets arrive.

## FEASIBILITY (single-file, offline — confirmed possible)
- **Ticket = base64 of a tiny JSON** (`{bit, room, call, seed, v}`), a few dozen chars; rides in a text box or `location.hash`. No network — `location.hash` and clipboard are local.
- **Reel = a list of Tickets**; the chain sim is deterministic (same math as `actualFor`, mood carried as the next room's starting temperature).
- **House seed = an authored array** in-file. **Nothing persists** unless the player carries a Ticket out — exactly the studio's carry-out floor.
- No fetch, no storage APIs, no accounts. Every floor holds.

## OPEN DECISIONS (founder)
1. **Score identity** — lead with **Reader** (calibration/norming — on-thesis), **Maker** (did your bit land — more playful), or both? I lean *both, Reader named first* (it's the moat).
2. **Ticket surface** — copy-code, native share-sheet, or `#fragment` link? (All offline. Link is the lowest-friction; code is the most honest/visible.)
3. **How literal is the chain?** Full "watch the whole reel fire" (richer, more build) vs. a lighter "your machine joined N others" (cheaper, still social). I lean start light, earn the full reel.
4. **House-crowd voice** — authored by hand, or drawn from `games-text-bank.md` (Matt's own writing, already on studio-main)? The bank is on-canon and would make the house crowd sound like the studio.

<!-- MANIFEST: design only. The wall (offline social) is cleared by the Ticket (human-relay carry-out) + a labeled house seed; the "one story" is mood-as-marble chaining machines; the social score is honest/relative and is norming in disguise. Next: founder picks the four decisions, then a thin prototype (Ticket emit + load one machine into the crowd) before the full reel. -->
