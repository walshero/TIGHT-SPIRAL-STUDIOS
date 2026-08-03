# NAMING THE CAT — a panel with agency (Saunders · Cleese · Le Guin)
<!-- 2026-08-02 · design lane · founder: "the cat needs a name. A funny name. Saunders Cleese Leguin step up; grant more agency." The instruction is двойной: pick a name, AND let the panel actually DECIDE (agency), not just advise and defer. So this is a ruling, not a menu. -->

## THE BRIEF
The cat is not décor. It is **the honest audience** — room #1, and the face in the cold-open machine — the one whose real laugh you are trying to earn. The studio's thesis lives in it: *a flat gag is a fact, not a failure.* The cat is the toughest room: it will not fake a laugh. It needs a name that is funny, and true to that.

## THE PANEL DELIBERATES (each with a real position)
- **John Cleese** opens on sound and deflation: comedy names want a plosive and a whiff of the mundane or the over-grand undercut. But he stops himself — the deeper joke is *who this cat is*. "You've built a game about the **hardest laugh in the room**. There is only one patron saint of that."
- **George Saunders** wants the humane absurdity: a small, sleepy animal carrying a dignity far too large for it. "Give the little guy the weight of someone enormous, played completely straight. That's where the tenderness and the funny both live."
- **Ursula K. Le Guin** closes it, on the true name: "A name is not a label you stick on; it is the thing's nature, spoken. What is this cat's nature? *It will not laugh.* Its true name is the name of the one who made an art of not laughing."

## THE RULING — **Buster**
After **Buster Keaton — "The Great Stone Face"** — the silent-film comedian whose entire genius was *never cracking a smile*, no matter the catastrophe around him. The panel lands here with conviction, because it does three things at once:
- **It's funny.** "Make Buster laugh." A sleepy cat named Buster, deadpan as a stone. The joke reads instantly and rewards a second look.
- **It's true (Le Guin).** The cat's nature is the withheld laugh; Buster *is* the withheld laugh, canonized. The name and the creature are one thing.
- **It's the game's whole thesis in a word (Cleese + the humor model).** Keaton's art was **physical comedy — the universal register** the humor model names as the floor that lands in any room. Trying to make *Buster* laugh is trying to earn the honest, universal laugh. The mascot and the mechanic rhyme.
- **It's humane (Saunders).** A little cat holding a giant's name, played straight.

**Runner-up, for the record:** the deadpan-banal human name (*Keith* / *Kevin*) — funnier on pure incongruity, but it carries no thesis. The panel chose meaning-that's-also-funny over funny-alone.

## WHERE THE NAME LANDS (implemented v9.1)
- Cold-open objective: **"Make Buster laugh."**
- Room #1: **"Buster, a sleepy cat."**
- The scene + reacting-face aria-labels name Buster (a signal without its subject is noise).
- Internal ids/vars (`id:"cat"`, `catFace`, `catHit`) stay — the name is for the player, not the code.

## THE STANDING SHIFT (the "more agency" part)
Per the founder's directive, advisory panels may now **make the call and ship it**, not just table options — the founder keeps veto, but the default is *decide and act*. This doc is a ruling that went straight to the build. (If Buster is wrong, one word reverts it.)

<!-- MANIFEST: the cat is named Buster (Keaton, the Great Stone Face) — funny, true, and a rhyme with the humor model's universal/physical floor. Panel exercised decision agency per founder directive; shipped in the same turn. -->
