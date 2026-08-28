# RULING: LAB STATUS · 2026-08-27

**Founder's words:** *"Many games have to be placed in lab status. All the cliche
cowpath games ... put in lab not as done game."* (founder, verbatim)

## What was wrong

The face had three statuses: **Live**, **In build**, and a plain note chip. Every
playable page that was not actively being edited wore **Live**. That made "Live"
mean two unrelated things at once: *this is finished and I stand behind it*, and
*this exists and opens*.

The Cliché Cowpaths rooms are the proof. Measured this session, against the gates
the studio runs today:

| build | preship-gate-v5 halts |
|---|---|
| `cliche-cabinet.html` | 10 |
| `cliche-cowpaths.html` | 9 |
| `cliche-line.html` | 9 |
| `cliche-city.html` | 8 |
| `cliche-field.html` | 5 |

Forty-one halts across five files, font floor mostly, and all five wore the
same **Live** chip as a build that clears every gate. Nobody lied. The vocabulary
had no word for *"real, playable, on the bench, and not held to the bar."*

## The ladder, as of today

| status | what it claims | what it does NOT claim |
|---|---|---|
| **Lab** | Real, playable, opens. An experiment kept on the bench on purpose. | That it clears the gates. That it is finished. That it is being worked on. |
| **In build** | Being worked on right now, in this stretch of sessions. | That it is playable end to end. |
| **Live** | Playable end to end, gates green, and the studio stands behind it. | Full production. |
| **Full production** | The measured state in `production-gate.py`: gates, meta, comfort kernel, panel record, declared founder playtest, open questions written, linked from the face. | That it is good. The gate measures evidence, not quality. |

**Lab is not a demotion and not a graveyard.** It is the honest name for work that
taught the studio something and is being kept where it can be seen. A build in Lab
is allowed to fail the gates. That is the point of the word: a status the gates do
not have to be lied to about.

**A Lab build may not be promoted by relabelling.** It moves to Live the way any
build does: the gates go green and somebody plays it.

## Where the status is stated

Two places, and they must agree:

1. **On the face** (`index.html`): a `.c-lab` chip, cool ink on a **dashed** edge.
   Dashed so the status survives a reader who does not see the colour difference.
   The four rooms also carry a `Lab` tag in the full shelf.
2. **On the build itself**: a `.tsp-lab` chip inside the `<h1>`, beside the
   title, in the same position and to the same style floor as the version chip
   from the 2026-08-23 founder rule (20px, inherits the heading's own colour so
   it carries the heading's measured contrast on every ground the file ships).

Same reason as the version rule: a status you cannot see from the phone you are
holding is a status nobody can hold you to. A player who opens `cliche-line.html`
from a bookmark never sees the face, and until today that player had no way to
know they were looking at a bench experiment.

## Applied this session

`cliche-cowpaths.html`, `cliche-cabinet.html`, `cliche-city.html`,
`cliche-field.html`, `cliche-line.html`. Chip on the build, chip on the face,
Lab tag in the shelf. Verified: per-file preship halt counts are **identical
before and after** the stamping, so the status was added without touching what
the builds are.

## The sweep, run 2026-08-27 (the founder said it three times)

The first cut of this ruling parked the rest of the corpus as a PENDING question
for the founder. He restated the instruction twice more in the same session, which
is the answer: **"Many games have to be placed in lab status."** The sweep was run
and applied.

**Method, and its honest limits.** Every room card on the face carrying a `c-live`
chip was measured against `preship-gate-v5.py` (static, no browser, cheap) and
`art-gate.py`. `studio-voice-gate.py` was deliberately NOT used as a trigger: it
runs on a ratchet and carries debt by design, so measuring against it flat would
demote nearly the whole corpus for a reason the studio already decided to pay
down over time rather than all at once.

**Result: 33 Live-chipped surfaces measured. 25 failed a shipping gate.**

| holds Live (every gate green) | |
|---|---|
| `choose-your-leader-v7.html` · `the-compound-capstone.html` · `en195-hub.html` · `en195-arcade.html` · `enjambment.html` · `enjambment-skins.html` · `repos.html` · `workshop-wall.html` | 8 |

**19 games moved to Lab**, band on the build and chip on the face: `the-console`,
`old-problems-at-new-speed`, `choose-your-leader-full`, `choose-your-leader-v6`,
`reading-the-fireground`, `the-tell`, `soundings-TRUNK-v03`, `behind-this-door`,
`dad-energy`, `warriors-fantasy-arcade`, `how-an-idea-travels`,
`funnybonies/index`, `fys_fys-treasure-trove`, `sandbags`, `review-bench`,
`course-river`, `flash-ballast`, `play-the-semester`, `studio/play-the-studio`.

**Six surfaces failed gates and were NOT moved**, because Lab is a status for a
game and calling a runbook an experiment on the bench would be using the founder's
word for something he did not point it at: `arcade.html` and `islo-hub.html` (both
indexes), `en195.html` (a course front door), `workshop-in-a-box.html` (a kit),
`tight-spiral-runbook.html` and `studio/tight-spiral-system-map.html` (documents).
**Open for the founder:** these wear Live while failing the gates. Does the ladder
extend to non-game surfaces, or do documents need their own word?

## The flagship was fixed rather than demoted

`en195-arcade.html` failed only `art-gate`, on 5,158 bytes of hand-cut scene art,
and it had failed that way for weeks with no legal remedy short of deleting the
art. The studio-cut lane opened the same day gave it one, and the lane does not
take a marker's word for it: the art was marked `data-art-class="studio-cut"`,
its scene marked `data-scene`, and `art-execution-gate.py` **passed it** on type
dominance, cross-hatch and flat layers. The art was never the problem. The rule
that banned it had gone stale. The flagship holds Live on measurement.

## How the status mounts, and why retrofits differ

A new build carries a `.tsp-lab` chip inside its `<h1>`, beside the version chip.
That is the pattern, and `cliche-hunter.html` and the five cliché builds use it.

The 19 retrofits carry a **`.tsp-labband`** instead: a status band directly after
`<body>`. Their heading structures have nothing in common. One builds its title
from a JS template, one carries four `h1` elements, and three have **no `h1` at
all**. Rewriting the title markup of nineteen shipped games to add a label is a
large blast radius for a label. The band's colours are fixed rather than
tokenised, at 13.4:1, because these files do not share a palette and a status that
inherits an unknown token can arrive invisible.

**One defect, caught by rendering rather than by reading.** The first pass matched
`<body>` inside a prose comment in `old-problems-at-new-speed.html` and mounted
the band inside that comment, where it never rendered. Same shape as the comfort
slice that stopped one line short in the Cliché Hunter build: a pattern matched in
source is not a thing on screen. All 19 were then rendered headless and the band
confirmed present, sized and visible; 12 were clicked through to confirm the games
still respond.

## What this does not change

The cliché games' text bank is **business** clichés ("low-hanging fruit," "move
the needle," "circle back"). It is not a poetry bank, and Cliché Hunter does not
inherit it.
