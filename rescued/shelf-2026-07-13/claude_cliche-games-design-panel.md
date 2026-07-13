# Cliché Field — Design Panel on Dynamics

*Convened to answer one question: why does this game feel like Asteroids, and what should it be instead? Four voices, argued from their published work — Eric Zimmerman (game design / meaningful play), Kurt Squire (games as designed learning), Ursula K. Le Guin (the carrier-bag theory of story), and Jared Cooney Horvath (attention & memory). These are the cases each would make from their own writing, not literal quotes. Tight Spiral Studios, 2026.*

---

## The charge

Cliché Field currently plays like Asteroids: a lone ship, free-flying, blasting objects that spawn at random and drift. Matt's instinct — "make it look a bit different, I don't like random spawning, mechanics have to align with learning" — is the whole panel in one sentence. Here's why each expert agrees, and what they'd build instead.

## Le Guin: stop telling the killer story

The Asteroids frame is what I called the *killer story* — the hero, the weapon, the thing hurled in a straight line to destroy. It is the oldest and most tired shape a narrative can take, and it is a strange shape to pour a game about *language* into, because you are asking the player to be a gunner when you want them to be a reader. A story is not a spear. A story is a **carrier bag** — a container you put things into, that holds them in relation to each other. The good version of this game is not "shoot everything that moves." It is "gather what's worth keeping, set down what isn't." The microfiction the player assembles *is* the bag. Build the whole dynamic around gathering, and let the shooting be the smaller, secondary act of setting tired things aside — not the point of the game.

## Zimmerman: make the play *meaningful* — discernable and integrated

Meaningful play has two requirements, and random spawning violates both. First, an action's outcome must be **discernable** — the player must be able to perceive what their choice did. Second, it must be **integrated** — that outcome must matter to the larger game, not evaporate. When rocks spawn at random positions on random timers, the player can't form an intention and read its result; they're reacting to noise, and noise is the enemy of meaning. Determinism isn't a limitation here, it's the *precondition* for meaning: a curated, authored field lets the player say "I am going to deal with *that* one, deliberately," and then see it happen. Every verb needs a visible consequence: reject a cliché and it should *land somewhere you can see* (the pile); keep a living line and it should *take its place in the thing you're building* (the story). Choice, consequence, both legible. That's the definition.

## Squire: the field should be *designed*, with a curve

Games teach because they are *designed experiences* — sequenced, situated, tuned. A random generator is the opposite of design; it abdicates the one thing that makes a game a teacher. Author a deck. Put more clichés early, when the player is building the recognition reflex, and thread the living lines through so the story assembles over the session as competence grows. That's a difficulty curve and a situated context in one move. And keep the stakes real but recoverable — a learner who is punished permanently for one misread stops taking the risks that learning requires.

## Horvath: the mechanic must *be* the cognitive act

I keep saying it: no memory without attention, and attention doesn't multitask. The Asteroids version splits attention three ways — fly, dodge, aim — and the *reading* loses, which means the learning loses. Collapse that. The single act I want the player to perform is: **read a phrase, judge it, commit.** So the control scheme should slow down to the speed of that judgment. Quantized, deliberate aiming — snap to a target, on a cooldown — is far better than analog twitch, because the cooldown *is* the think-time. You can't spam; you have to choose. That's not friction, that's the learning event. And keep a generative beat on the back end (recall or replace) so recognition becomes production.

---

## Decisions (built)

1. **Reframe from shooter to reader.** The ship stops free-flying. A stationary nib sits at the center of a hex arena; six lanes feed phrases inward. You are a reader at a desk, not a gunner in space. (Le Guin, Squire)

2. **Snap rotation, 60° per step, on a cooldown.** Tap turns the nib one lane (60°); two taps, 120°; three, 180°. A short cooldown between snaps makes aiming deliberate — the cooldown is the think-time. No analog spin. (Horvath, Matt's spec)

3. **Two clean verbs with visible consequences.** FIRE rejects the phrase you're facing *if* it's a cliché — it shatters and falls to a growing pile you can read. KEEP (beam) gathers it *if* it's a living line — it takes its slot in the microfiction. Fire a good line and it only bruises; keep a cliché and it's declined. Every verb's result is discernable and integrated. (Zimmerman)

4. **No random spawning — a curated deck.** An authored sequence deals phrases to lanes on a steady rhythm, clichés front-loaded, the six story fragments threaded through on a curve. Same shape every play, so outcomes are attributable to choices. (Squire, Zimmerman)

5. **Missed living lines recirculate.** A story fragment that reaches center un-kept doesn't vanish — it goes back into the deck and comes around again. You can't lose the story to a twitch. Clichés that reach center "get into print" and cost a shield. (Horvath, Le Guin)

6. **The generation beat — BUILT (2026-07-12).** Every round ends by handing the player a cliché they actually cleared and asking them to write past it in their own words: *"You cleared this cliché: 'it is what it is.' Say it fresh."* The typed line is saved to a running revisions bank (`tsp_revisions` in local storage) and the count is shown ("You've written N fresh lines so far"), so production accumulates across sessions. This is the recognition→production bridge; it appears on both the win and game-over screens, because the consolidation matters whether or not you won. (Horvath)

### Principle → mechanic

| Voice | Principle | Mechanic in Cliché Field v5 |
|---|---|---|
| Le Guin | Story is a carrier bag, not a spear | Gathering (KEEP) is the core; the microfiction is the bag |
| Zimmerman | Meaningful play = discernable + integrated | Faced-lane highlight; pile you can read; story that assembles |
| Zimmerman/Squire | Design beats randomness | Curated deterministic deck with a difficulty curve |
| Horvath | The mechanic must be the judgment | Snap-aim on a cooldown = deliberate read-judge-commit |
| Horvath/Le Guin | Recoverable stakes | Missed living lines recirculate; no permanent loss |
| Squire | Situated, sequenced experience | Front-loaded clichés, threaded fragments |
| Horvath | Recognition must become production | End-of-round "rewrite a cliché you cleared"; saved revisions bank |
