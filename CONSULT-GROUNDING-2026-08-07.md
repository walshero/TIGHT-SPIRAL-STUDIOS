# GROUNDING PACKET — six-month consultation, 2026-08-07

*Everything below was **measured today against live bytes**, not recalled. Funes' rule:
an unstamped claim is a suspicion. Where canon and measurement disagree, the measurement
is here and the doc is flagged stale.*

**Scope honesty, stated once:** the Claude project chats are **not reachable** from the
session that produced this packet. No connector exposes them. What stands in for them is
their distillate in this repo — `TSP_Ledger.md` (97 KB), the `SESSION-*` and `HANDOFF-*`
records, `FUNES-PLAYTEST-*`, and `rescued/shelf-2026-07-13/`. Any panel finding that
would need the chats themselves must say so rather than infer.

---

## 1. What the studio is

- **Phase:** proof of concept. Roughly two months of studio work; git holds the recent
  consolidation.
- **The bet:** ~**9:1 engine over assets**. The studio is the engine; individual builds
  are downstream deliverables.
- **The moat:** the quality layer — Studio Eyes (render), Studio Fingers (touch), the
  ratchet. CI-grade enforcement of *craft*, not just code. Few solo studios have this.
- **The constraint that pays:** single-file offline HTML. Portable, no build chain, ships
  to Pages, ages well.
- **The founder:** retinitis pigmentosa. Phone-primary. One step at a time. The mechanical
  half is delegated by default; founder rulings, creative calls and voice are not.

## 2. The architecture as it actually stands

**Five repos, hub and spoke.** Hub `TIGHT-SPIRAL-STUDIOS` owns canon and ticks. Spokes
`en195-apps`, `confluence-calibration-assessment-hub`, `-writerly-moves-game`,
`matt-radar` mount the belt at CI time. **Mount, never copy** — a copied gate is a drift
generator.

**Corpus:** 131 HTML surfaces in the hub. The four spokes hold **three surfaces between
them.** The games live in the hub.

**The belt, as of today:** five ticks, up from two.

| tick | gate | mode |
|---|---|---|
| 1 accessibility floor | `comfort-gate.py` | ratchet |
| 2 attribution standard | inline | flat |
| 3 image floor + render | `preship-gate-v4.py` | ratchet |
| 4 founder voice | `studio-voice-gate.py` | ratchet |
| 5 entry paint | `one-thing-gate.py` | ratchet |

**Cold Start (locked 2026-07-13, law):** canon is computed, not remembered. A four-file
resident shelf; everything else fetched from git and dropped. The four: the OS, the
Command Center, the lane registry pair, and Cold Start itself. Rationale is explicitly
accessibility — four files is a shelf an RP reader can scan; two hundred is a wall.

## 3. Canon that measurement contradicts — three stale claims

`STUDIO-GOVERNANCE.md` (adopted 2026-08-03) says:

1. **"the belt is present and inert by design"** — **false.** `studio-belt.yml` has run
   **6 times on matt-radar** (latest green, 2026-08-04) and **once on en195-apps**
   (failed 2026-08-04, red ever since, nobody acted). The belt has been live for three
   days and its failure went unread.
2. **"confluence's default branch is a `claude/…` working branch, not `main`"** —
   **false.** It is `main`. The prerequisite is already met.
3. **"the connector cannot write `.github/workflows/`; owed to the founder's token"** —
   stale for this lane. Workflow files were written and pushed from a session container
   today. The Zapier-grant limitation is real; the blanket claim is not.

**This is the pattern worth the panel's attention**: the studio's governance doc described
a state of the world that stopped being true within a day, and nothing detected the drift.

## 4. What today's work measured

- **The wall detector measured the wrong screen.** `one-thing-gate.py` ran at 1280x800
  while every other instrument ran the phone. Corrected to phone-binding.
- **Instruction walls:** across 131 surfaces — **52 `INSTRUCTION-WALL`**, **29
  `ACTION-BELOW-FOLD`**, **4 `H-OVERFLOW`** (sideways scroll at 390px). Worst:
  `fys-treasure-trove` at 1386 words / 18 screens before the player can act.
- **Two gates were silently dead.** `playthrough-agent.py` and `studio-fingers.py` both
  failed on a Chromium build drift, printed an error, continued — reading downstream as
  "nothing found". Same shape as the WeasyPrint exit-2 that rubber-stamped the corpus for
  weeks. Both fixed; the playthrough agent immediately found 3 dead buttons.
- **A corpus-wide blind spot, open:** `studio-fingers.py` probes at load, and TSP games
  are `.screen{display:none}` with controls built by JS on transition. **Every control
  after the entry screen, in every multi-screen game, has never been touch-measured.**
- **Nothing assessed learning.** Three Aleph lenses asked does-it-work, does-it-play,
  does-the-message-land. On teaching games, whether anyone learns was unmeasured until
  today.
- **First five-lens run** (`the-tell.html`): 30 defects, 5 blockers. The learning lens
  found the verdict is `mine.card===preset.card` — a string compare. The student's written
  reasoning is never read; the commit gate is three characters.

## 5. The studio's own strategic read (SWOT, 2026-08-02)

**Strengths:** machine-enforced craft quality; single-file offline as a paying constraint;
theory-grounded pedagogy; governance depth and an honesty brand; accessibility as an
authentic driver.

**Weaknesses:** the system optimizes around one profile; governance is **veto, not
optimization** — it can say a build isn't broken, not that it's good; no per-user
adaptivity; **no external proof point**; **single point of judgment = bottleneck and bus
factor**; sprawl (60 live pages, 131 HTML, two months, one person).

**Threats:** accessibility monoculture as liability; **the moat is also a treadmill**
(every page is standing maintenance); attention burnout; AI-art trust; "beautiful engine,
no proof".

**Named next moves:** teach the gates adaptivity (grade each shipped profile, not one
theme); **land one legible PoC win** so month three has evidence, not just engine.

## 6. Standing founder rulings the panel must not re-litigate

- Faculty emails, published student work and the Confluence pages are fine to share.
  Settled. Not a privacy question.
- **No invented or inflated claims.** If it isn't in the founder's docs, don't write it.
- **No claim that blind players can play the games.** There is no playtest behind it. The
  defensible framing is the founder's RP and an accessibility-first design *intent* —
  never an outcome claim.
- **Pull back on disclaimers.** Say the thing plainly; caveat only when load-bearing.
- Git/Pages is the primary lane. Netlify is one-off sharing only.
- Canon is the repo. The shelf is a cache and it lags.
- WCAG AA is the floor; the founder profile is the **default preset**, not a universal
  wall (amendment 2026-08-02).
