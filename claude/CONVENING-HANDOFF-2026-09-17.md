# THE CONVENING — pipeline reorder handoff

Ruled in a voice session, 2026-09-17. Landed same day from the text continuation
of that session. This file is the handoff the founder asked for at the end of the
voice chat; the transcript is the primary source and this file is its landing.

---

## 1. THE DIAGNOSIS THAT FORCED THIS

The studio's gates are sensory. Studio Eyes verifies what is seen, Studio Fingers
what is touched, Studio Voice (one tooth) what is written. All three judge the
surface. None asks whether the artifact does what the founder meant it to do.

The panel exists as a spec (`panel/panel-and-aleph.spec.md`, seven seats) and the
enforcement clause exists in the Funes patch ("a thing ships only when the owning
seat signs and its gate is green"). But every seat with a script signs
automatically, and every seat without one — Coordinator on learning science,
Aleph, the game designers, the Visual Symphony Conductor — has no way to sign and
no way to block. Builds ship on the sensory gates alone.

**The bug is not missing seats. It is missing signatures — and signatures at ship
time are still too late.** Founder, verbatim:

> "I don't want shipments. It doesn't matter. Those other things don't matter if
> these things aren't there. We need to see these things so that they inform the
> drafts that I receive, so that iteration is much better."

Months of builds have missed founder vision because the seats that would catch
"this asks the player something that makes no sense" speak only when the founder
remembers to invoke them by name. The panel was a wish, in the studio's own
language.

## 2. THE PIPELINE, REORDERED

Old order: build → gate → ship → founder catches the vision miss by eye.

New order: **sentence → convene → findings → build against findings → gate → ship.**

The mechanical gates (eyes, fingers, voice, canon, contrast) are unchanged and
stay at the end. What changed: they are no longer the first place anything is
judged. The panel sits on the spec, before a line of code, and the draft is
downstream of the panel.

## 3. THE CONVENING — the routine, invocable by name

Invoked by saying **"convene"** and the name of the build. Nothing is authored
before it runs. "Full TSP treatment" now means this routine, not a phrase.

1. **The sentence.** State the build in one sentence: what the player does, and
   what the founder wants them to notice. If the sentence cannot be written, the
   Convening HALTs there. This is the founder-vision capture that has been
   missing.
2. **The standing seats answer the sentence** — each in its own voice, before any
   design exists (questions in §4).
3. **The Conductor sits whenever anything will be seen** and sets visual
   constraints before craft. This is the existing art HALT, unchanged, widened to
   its proper place in the order.
4. **Disagreement is preserved, never smoothed.** Split votes are recorded as
   dissents, in the manner of `cyl-modern/PANEL-MODERN-PERIOD-2026-08-05.md`.
5. **Findings land in one file** (`convening/<build>-CONVENING.md` in the build's
   lane), and the draft is authored against that file. A draft that arrives
   without one is out of process.
6. **Only then do the mechanical gates run.** They stay exactly as they are.

## 4. THE STANDING SEATS — five, blocking, every build

| Seat | Question it must answer on the sentence |
|---|---|
| **Coordinator** (learning science, Horvath) | What cognitive work does this ask of the player, and is it the work the founder named? |
| **Stranger** (widened: comprehension, not just visibility) | What would a first-timer think they are being asked to do, and why would they bother? Owns the C6 admission test: "Why would a stranger play this?" |
| **Osterweil** (new seat, founder-ruled this session) | The freedom-of-play test: where is the player's real choice, and what happens if they refuse the one intended? Is it play, or an exercise wearing a game's clothes? |
| **Aleph** (the one-point view) | One screen or a system? Did we relearn something the studio already knew? |
| **Studio Voice** (promoted to a seat, founder-ruled this session) | Does the prose sound like the founder or like a machine? Sourced from the real corpus (§5), not a style guess. |

Plus: **Visual Symphony Conductor** sits whenever anything is seen — which is
nearly always — but is convened by the nature of the build, not the roster.

Stranger's original brief (contrast, floors, emoji) is now arithmetic in Studio
Eyes and Studio Fingers; the seat keeps those as floors and takes comprehension
as its live question. Osterweil's seating, founder verbatim: *"I also want
Osterweil given a seat."* — *"Yes. Yes. See them."* (voice transcript; read as
"seat them"). Standing equal to Coordinator and Stranger, blocking signature.

Relation to the seven-seat ship review: the Convening does not retire it. The
ship-time seats (Engineer, Hand, Registrar, Calibrator) still govern at the end.
The Convening is the pre-authoring panel the pipeline never had.

## 5. STUDIO VOICE — rebuilt from the real corpus

Founder, verbatim: *"I have a real low bar for the uncanny valley of AI written
language."* The manifest (`claude/founder-voice-provenance-manifest.md`) names
syllabi, schedules, handouts, announcements, portfolio feedback as sources; only
one document has ever been read into it. That changes.

Sources named by the founder this session, all already in walshero
`Claude_files` (founder confirmed; do not re-copy from post):

- **MW Knowledge Base** folder — its subfolders and reports
- **The sabbatical folder**
- **The 2012 sabbatical report** — the MIT game design sabbatical in residence.
  Also Coordinator and Osterweil material in the founder's own words, and the
  documented-but-unused origin of the tight spiral itself. This closes that loop.
- **The 2018 sabbatical report**

FERPA fence rides along (`claude/FERPA-SCOPE-RULING.md`): Drive searches for
these are by **name and path, never fullText** across the teaching corpus.

## 6. THE CHECK, so this is not a wish

If a rule can't be a check, it's a wish. The Convening's check:

- The findings file is a **required input**. The build routine refuses to author
  when `convening/<build>-CONVENING.md` is absent or older than the sentence.
- Each standing seat has a **signature line** in that file. An unsigned seat is a
  HALT, exactly like a failed contrast check. Seats without scripts sign by a
  written answer; an empty answer is unsigned.
- To build next, in a Code lane: an `intent-gate`-style comparator that checks a
  draft names its Convening file and quotes its sentence verbatim. Until that
  exists, the manual check is: no findings file in the turn, no draft in the
  turn.

## 7. OPEN, HONESTLY

- The comparator in §6 is not built. Until it is, the Convening holds by
  discipline, which is the studio's known weakest material.
- Studio Voice ingestion of the §5 corpus has not run yet; this file authorizes
  it and names the fence.
- `horvath_watch` in `studio-eyes-sweep.py` already tries to load a staging
  area; whether it becomes the Coordinator's script or is retired belongs to the
  first Convening that runs.

---

*Aleph note at landing: trunk `6c7fe3e` at write time; Netlify lane BLIND from
this container (egress), Drive reachable, shelf is cache. Voice-session origin
means no file existed before this one; the transcript is the provenance.*
