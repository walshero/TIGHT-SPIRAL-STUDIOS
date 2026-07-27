# THE BENCH — FULL DESIGN REVIEW: Funny Boney's Factory
<!-- convened 2026-07-27 · founder verdict: "art failing on sight; the game is failing, it's overwhelming and convoluted" · PM: David Noonan -->

**Object:** `funny-boneys-factory.html` (v6 cold open + tap-fired chain).
**Panel:** Eric Zimmerman · Filament Games · No Crusts Interactive · Apple Arcade.
**PM (chair):** David Noonan. **Convened by:** founder, who called it failing on sight.

---

## VERDICT (unanimous)

**This is a deck of good ideas wearing the costume of a game. The core verb never
reaches the player's hand.** The studio's own copy says *"you are guessing what a
crowd will find funny — that guess is the whole game"* — and then the game makes
the guess for you (`pred:62` is printed on every card). Around that hollow center
sit four teaching systems (an epistemic Spellcaster/Coder/Storyteller reskin, a
polling-method seminar, a Glass-Engine robotics/agriculture thesis, a five-stop
comfort control), stacked on one ever-growing scroll where screens never replace —
they append. The founder's two words are just an accurate description of the build:
**overwhelming** (6–7 abstractions before the first laugh) and **convoluted** (no
single legible action). It would not clear the Apple Arcade front door.

---

## THE CONVERGENT RULING (all four lenses, independently)

> **Cut to one loop, one screen at a time — and give the player the bet.**
>
> The play path becomes exactly: **tap the machine → pick a gag + a crowd → enter
> YOUR prediction → watch the crowd (the cat's face) land it or not, against your
> guess → go again.** Screens *replace*, they do not stack. Everything else — the
> lens toggle, the polling lesson, the engine essay — leaves the play surface.

Noonan carries this as the single blocking item. It is the intersection of all four
reviews: the game only becomes a game when the player owns the number they are
calibrating, and it only becomes legible when each screen holds one decision.

---

## THE PANEL'S READ (findings → checks)

| # | Finding (whose lens) | Becomes |
|---|---|---|
| 1 | **The player never predicts — the bet is pre-filled** (`pred:62/48/78/55` hardcoded). The one action the copy calls "the whole game" is a label you read, not a choice you make. (Zimmerman, Filament — both: *fatal*) | **CHECK:** delete the hardcoded `pred`; the player drags a "% who'll laugh" slider before Show. That is the bet. · build · **blocking** |
| 2 | **Screens append, never replace.** `.hidden` toggles inside one scroll — the scene, lens bar, and rail persist above every panel; it grows into a worksheet. (Apple Arcade — structural) | **CHECK:** Scene / Build / Result become full-viewport states that swap in place; the rail is the only persistent chrome. · build · **blocking** |
| 3 | **The "actual" is editable after the reveal.** Flipping the poll method re-runs `surveyThrough()` with a live `Math.random()` — the truth you calibrate against moves every time you touch it, post-hoc. (Zimmerman) | **CHECK:** lock the RNG + the crowd's actual *before* the reveal; poll-method becomes a later unlock, not a post-hoc dial. · build |
| 4 | **Concept overload before the first laugh** — lens toggle + How-vs-Step + 5-stop rail + 4 named gags + pre-printed bets + 4 audiences + Show. Six to seven abstractions, zero laughs, and the "laugh" is a 3×10 grid of tiny faces. (Filament, Apple Arcade) | **CHECK:** cut the epistemic toggle from the play path; defer the polling lesson and the engine to post-round unlocks. · build |
| 5 | **Art fails on sight — one good hand, everything else a worse one.** The hero machine is charming line-art; the gag icons are a purple dot / a flat dash / clip-art pail; the crowd is a spreadsheet of 30 dimmed faces; the gap is a KPI card. (No Crusts) | **CHECK:** redraw the 4 gags in the hero's exact hand; make the crowd the **cat's expression** (you already own the art); show the gap as physical distance, not bar meters. · art · **blocking** |
| 6 | **"Recalibrate" changes nothing** — `recalibrate()`→`goBuild()`; the next bench is byte-identical, no memory of the miss surfaced. The loop is a circle, not a spiral. (Zimmerman) | **CHECK:** round N+1 shows round N's miss; the crowd or gag set shifts so the recalibration has something to bite. · build |
| 7 | **The hook and the loop are two different games.** The cold-open is a physical cause-and-effect toy (tap → chicken drops → cat laughs); "Step in" abandons it for a card-picker with a bar chart. You never build the machine you were shown. (Filament) | **WISH→CHECK (stretch):** let the pick/predict happen *on the machine* so the toy and the loop are one object. · build (after 1–2) |
| 8 | **Two Home buttons + fixed chips collide with content.** A second injected "⌂ Home" overlaps the bench title; Home/Comfort sit on top of the crowd and poll copy mid-screen. (all) | **CHECK:** one Home; chrome never overlaps live content (falls out of #2 once screens swap). · build |

---

## WORTH KEEPING (the seed — build *from* this, don't decorate the mess)

- **The cold-open machine + tap-to-fire chain.** Unanimous. The one place beauty, joy,
  and a clear verb already coexist. It is the studio's identity. The rebuilt game
  should live *inside* this object, not leave it at "Step in."
- **"Who you show it to changes what lands"** — situated humor via hidden audience
  taste vectors. The one idea with real design meat. Currently inert because the bet
  ignores the audience; wire the live prediction to it and it becomes the spine.
- **The single gap number ("20 points off")** — a clean, honest readout. Keep the
  display; give it a real bet to read, on its own uncluttered screen.
- **"Failure is diagnostic"** — the honest-grey flat face instead of punishing red.
  Right emotional design. Keep the stance; make the player earn the verdict.

---

## NAMED WISHES (good ideas, wrong layer — filed, not lost)

- **The epistemic lens** (Spellcaster/Coder/Storyteller). A real thought, but it's a
  reskin that changes nothing mechanically and triples the reading on screen one. A
  later-version idea, not MVP furniture.
- **The adaptive-polling thesis** (the 3-method seminar). The buried real lesson —
  earns its way in *after* the player has felt one gap land, not before.
- **The Glass Engine** (make invisible constraints visible → robotics/agriculture).
  The payoff, not the onboarding. Unlock it after a successful recalibration.
- **Assemble-the-machine.** Let the player build the contraption they're shown — the
  strongest way to fuse the hook and the loop (finding #7).

---

## THE REBUILD SHAPE (Noonan's target for the next build)

Four states that **replace** each other, one decision each:

1. **The machine** — tap fires the chain, cat laughs. (Already built. This is the door.)
2. **Set it up** — pick one gag (drawn in the hero's hand) + one crowd. One screen.
3. **Call it** — one slider: *how many of this crowd laugh?* The bet is the player's.
4. **The room** — the crowd (the cat's face, or a small honest crowd) lands it or
   doesn't; one gap number; "go again." The miss carries into the next call.

Everything the four teaching systems wanted to say is still sayable — as unlocks that
arrive *after* the loop is fun, or not at all. Make the game first. Teach second.

<!-- MANIFEST: this is a review, not an implementation. Findings #1, #2, #5 are the
three blocking items (own the bet · screens replace · art coheres). The rest are
build/art rows that fall out once those three land. Re-convene The Bench when the
rebuilt loop exists, and re-run both standing axes (physics, immediacy) on it. -->
