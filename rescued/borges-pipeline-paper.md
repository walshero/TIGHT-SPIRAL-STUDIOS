# The Blind Librarian's Pipeline: What Borges Knew About the Problems We Keep Calling New

*Matt Walsh · Professor of English, MassBay Community College · Founder, Tight Spiral Productions · walshero@gmail.com*

*MASTER DRAFT v1 — 2026-07-03. Chronicle-shaped (~2,100 words). Founder note slots marked ‹MW: › — add ad hoc, any angle. Venue map and submission strategy in back matter. No fabricated concepts: every Borges fact is biographical or bibliographical record; every studio fact is a documented, shipped artifact. No Borges prose is quoted — his work remains in copyright, and the argument doesn't need it.*

---

In 1955, as his blindness became nearly total, Jorge Luis Borges was appointed director of the National Library of Argentina. He was given charge of roughly a million books at the moment he could no longer read one. He wrote a poem about it — about the irony of receiving the books and the darkness in the same gesture — and then he kept working for another three decades, composing in his head, dictating, revising by ear.

I have retinitis pigmentosa. I am a professor of English at a community college, and I run a small studio that builds educational games — single-file, offline, accessible-first, designed so that the version a blind student plays is the game, not an accommodation bolted onto it. I did not set out to imitate Borges. But when I look at the design decisions that made the studio work — the ones that survived contact with real students, real committees, and real AI tools — I find that every load-bearing one of them was solved, as a problem, in a handful of short stories written in Buenos Aires in the 1940s.

This essay makes one claim: the hard problems of building production pipelines in the AI era are not new problems. They are old problems wearing lanyards. A humanist who has read carefully knows which is which — and that knowledge is not decoration on a technical team. It is prior art.

‹MW: ›

## The garden: branching state

"The Garden of Forking Paths" (1941) describes a novel that is also a labyrinth: a book in which every time a character faces alternatives, the story takes all of them at once. Scholars of digital media have long treated the story as the conceptual ancestor of hypertext; it is the opening selection of the field's standard anthology, *The New Media Reader* (Wardrip-Fruin and Montfort, 2003), which is roughly the discipline's way of saying: this is where we begin.

Every branching educational game I build is a garden of forking paths with a rubric attached. The design question is never "what happens next" but "what structure holds all the nexts at once." The engineering answer turns out to be the one the makers of Zork found at MIT in the late 1970s: the world is data. Rooms, choices, and consequences live in a structure; the prose that describes them is a separate layer that reads the structure aloud. Story logic first, as a rule, before a single expensive pixel.

This month the studio codified that as law — narrative builds ship as a playable, medium-agnostic scene graph before any art lane opens — and then built the proof: a voice-only game, authored for blind players first, called *The Gaiden of Zorking Paths*. The title tips its hat in both directions. The mechanic is Borges's conceit made playable: on replay, the garden remembers the paths you did not take, and says so, out loud. Because the world is data and the voice is just a renderer, a future visual version costs almost nothing — and accessibility stops being a port and becomes a birthright.

A humanist did not need a product team to arrive at this architecture. The architecture was in the story.

‹MW: ›

## The library: generation without verification

"The Library of Babel" (1941) imagines a universe that is a library containing every possible book — every combination of characters, and therefore every true book, every false book, every refutation of every book, and every catalog, true and false, of all the others. The librarians who inhabit it are not empowered by this totality. They are ruined by it. Everything exists; nothing can be trusted; the cost has merely moved from writing to verifying.

I do not know a more precise description of the working condition of anyone using large language models in 2026. The machine will produce a plausible rubric, a plausible citation, a plausible departmental history — and somewhere in the library the false catalog sits on the shelf beside the true one, identically bound. Early in the studio's assessment work, an AI-drafted document confidently described a four-point argumentative rubric my department has never possessed. It was caught the only way such things are caught: by checking the artifact against the department's actual documents, byte for byte.

So the studio runs on a discipline Borges's librarians never got: nothing is real until verified in application. Files carry checksums. Claims carry provenance — what source, what license, verified when, by whom. The standing rule is that a confident answer inside an expert domain is a trigger to consult, not to proceed. Peer review is flawed; language models are flawed; what remains discernible is knowledge that survives being used. The library is infinite. The shelf you can trust is the one you built.

‹MW: ›

## Funes: memory without thought

"Funes the Memorious" (1942) gives us a young man who, after an accident, remembers everything — every leaf on every tree, every time he perceived it. Borges's cruel and correct observation is that Funes, possessing total recall, is thereby incapable of thought. Thinking requires abstraction, and abstraction requires forgetting: the collapse of a million particulars into one usable idea.

Every knowledge system I have watched fail in higher education — and every one I have personally over-built — failed the Funes way. The complete archive that no one can navigate. The documentation so faithful it duplicates the labor of reading the thing it documents. The AI transcript saved in full because deleting feels like loss. The studio's answer is a principle I now hold as core: knowledge lives as kernels — the small set of load-bearing truths beneath any standard — identified, verified, indexed, and folded to maximum density. Standards vary; kernels should not. The accessibility standard I follow was revised out of a draft guideline last year; the kernel beneath it, the physics of contrast and the research on legible letterforms, did not move. The kernel is what you keep. Funes is what happens when you keep everything else too.

‹MW: ›

## The Aleph: seeing everything, asking one thing

"The Aleph" (1945) is about a point in a Buenos Aires basement that contains all other points — look into it and you see everything in the universe, simultaneously, from every angle. The owner of the basement, a mediocre poet, uses this total vision to write an interminable poem describing the entire planet, acre by acre. Borges's narrator sees the Aleph too, and is shattered by it, and then — this is the part that matters — goes back upstairs and gets on with his life.

The studio holds a standing review ritual named for that basement. At the close of every working session, the whole system is looked at at once — every build, every file, every stalled lane — and the omniscient view is permitted to answer exactly one question: *why aren't builds moving?* Not "how do we perfect the system." Not the interminable poem. One diagnostic question, then back upstairs. The total view is real and it is useful, but only when it is disciplined by a single purpose; undisciplined, it produces the mediocre poet's masterwork — endless, comprehensive, and unread. Any faculty member who has served on a strategic planning committee will recognize both outcomes.

‹MW: ›

## The map: documentation the size of the territory

Borges needed only a paragraph for "On Exactitude in Science" (1946): an empire's cartographers, pursuing perfection, produce a map the exact size of the empire, point for point. The following generations find it useless and abandon it to the weather.

The studio's cross-session index is one page. It is one page on purpose, and keeping it one page is treated as maintenance work of the same seriousness as fixing a bug — because the alternative, faithfully recorded, is the map rotting in the desert with the animals living in it. Every institution I have worked in owns at least one such map.

‹MW: ›

## The turn

It would be tidy to say Borges predicted computing. He did not, and the claim isn't needed. What he did was catalog, with terrible precision, the failure modes of total systems: total branching, total text, total memory, total vision, total documentation. Those are exactly the systems the technology industry now sells, and the failure modes arrive bundled with the license.

Here is what I have come to believe, watching AI initiatives move through a resource-constrained college: the recurring institutional error is treating these as unprecedented problems requiring unprecedented purchases. They are precedented. A humanist's training — the slow reading of old texts about knowledge, memory, and labyrinths — turns out to be a working inventory of which problems are genuinely new (few) and which are old problems at new speed (most). That inventory is what a humanist brings to a pipeline: not softening, not "ethics as a garnish," but pattern recognition running about eighty years ahead of the product cycle.

Borges ran a national library he could not read, and did it by knowing, better than the sighted, how libraries actually fail. The studio's newest game is authored for the ear before the eye, by a designer whose eyes are the reason the floors exist. The pipeline works for the same reason the library did. The person who cannot take the interface for granted is the one who finds out what the system is actually made of.

For chrissake, we have been assigning these stories for decades. We might also believe them.

‹MW: ›

---
---

# BACK MATTER — venue map & submission strategy (editor's memo, not for publication)

**Genre honesty first.** "Academic paper" and Wired are different animals. What exists above is a ~2,100-word practitioner essay — the Chronicle-shaped master. Magazines (Wired, MIT TR, Atlantic) buy PITCHES, not manuscripts; peer-reviewed venues want a different apparatus entirely (that's the paper series' Papers II–IV lane, per the existing prospectus). Strategy: one master, many doors, three tiers.

**TIER 1 — full draft, submit now**
1. **Chronicle of Higher Ed (The Review)** — the named home audience. This draft's native shape. Accepts full drafts. FIRST OUT THE DOOR.
2. **Inside Higher Ed** — backup/simultaneous-adjacent lane if Chronicle passes; slightly shorter cut.
3. **Hybrid Pedagogy** — pedagogy-forward full draft; also the prospectus's Paper II venue, so sequence carefully (don't burn the relationship on the lighter piece if Paper II is the better fit).

**TIER 2 — pitch letters (150–250 words), send in parallel; pitches are not submissions, no exclusivity problem**
4. **Wired (Ideas)** — 900-word op-ed cut; angle: the blind designer and the five failure modes AI vendors resell.
5. **MIT Technology Review** — angle: accessibility-first architecture (the scene-graph/voice-renderer split) as engineering, with the Borges frame.
6. **Harvard → recommend HBR (Big Idea / AI coverage)** over Harvard Educational Review — HER is peer-reviewed, 12–18 months, wrong genre for this piece; HBR angle: why your AI team needs someone who reads. (HER stays on the list for Paper III.)
7. **The Atlantic (Technology)** — angle: Funes and the archive problem; institutional memory in the AI era.
8. **Aeon** — ideas-essay lane; Borges is native currency there; would take a 3,000-word literary expansion.
9. **Noema** — philosophy-of-technology lane; the kernel/standard distinction is their sweet spot.
10. **Fast Company** — short design-story cut: the voice-only game and accessibility-as-birthright.

**TIER 3 — hold or route to the series**
11. **EDUCAUSE Review** — governance/adoption cut; better as the AI Task Force companion piece than this essay.
12. **LA Review of Books** — the literary long cut if Aeon passes; strongest Borges scholarship adjacency.
13. **The New Atlantis** — technology-and-human-ends quarterly; slower, prestige lane; would want the expansion.
14. **Public Books** — scholar-public crossover; good second home for the LARB cut.

**Sequencing (the Aleph view, one line):** Chronicle full draft this week → four pitch letters the same day (Wired, MIT TR, HBR, Atlantic — pitches cost nothing and don't conflict) → Aeon/Noema expansion only if two pitches land or all pass. Never two simultaneous FULL-DRAFT submissions to venues that prohibit it; Chronicle and IHE — check current policy at submission, don't trust memory.

**Delegation split (standing rule — TA is MassBay-only, this is studio):** Only you: the ‹MW:› notes, the final voice pass read aloud, submission clicks. AI: venue policy checks at submission time, pitch-letter drafts (say the word), per-venue cuts. Eliminate: nothing yet.

**HITL angles to review from (your requested many-angles pass):** (1) voice — read the turn section aloud, it's the most me-imitating-you passage; (2) facts — every Borges date and the New Media Reader claim; (3) institutional exposure — the "four-point rubric" anecdote names no one but describes a real catch, confirm you want it in; (4) the "for chrissake" — it's your tic, placed once, cut it if the Chronicle version should run cleaner; (5) RP disclosure level — the essay leads with it; confirm that's the door you want to walk through in a national venue.
