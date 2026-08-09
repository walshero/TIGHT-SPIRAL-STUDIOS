# Founder Voice Provenance Manifest

Status: this file did not exist before 2026-08-05, despite the project's own
standing instructions pointing to it as if it did ("Founder voice rules
(D3/D5) are in claude/founder-voice-provenance-manifest.md"). Checked the
GitHub repo directly on 2026-08-04: 404. Checked the project shelf: absent.
This is the first real entry, written the way the founder-canon log says a
founder log should be written from now on — at the moment of the ruling, not
dug up after. Sibling to `preship-gate-v4.py` ("Studio Eyes," verifies
founder VISION) and `studio-voice-gate.py` ("Studio Voice," verifies founder
LANGUAGE), both in the repo/shelf.

## The ruling that created this file (2026-08-05)

> "in addition to studio eyes... we need studio voice, which prioritizes
> founder language from syllabus and course schedule and handouts and
> announcements and feedback to portfolio over the years etc. No dashes like
> em dashes unless it's the founder's. The general voice here is not mine
> and needs to be closer or not have voice at all."

## D1. Primary sources outrank inference

Founder language lives in real, dated documents: syllabi, course schedules,
handouts, announcements, portfolio feedback. Where any of these exist for a
claim about how Matt actually writes, they outrank a machine's guess at his
voice, and they outrank this manifest's own prose whenever the two disagree.
This manifest is downstream of the corpus, not a replacement for it.

## D2. What's actually been checked so far (2026-08-05)

Only one primary source has been read in full for this file: the live
EN195-025 Spring 2026 syllabus (Google Doc, id
`1WQd6sexfJGmneGKbp7iTBa5I3YCvm3MweHpeJWNJLoU`). Everything below is derived
from that single document. Course schedules, handouts, announcements, and
portfolio feedback across years are named in the founder's ruling as sources
this manifest should eventually draw from and have not yet been pulled in.
That is a real gap, stated plainly, not a claim of completeness.

## D3. The em dash rule, checked against real evidence, not assumed

The founder's own syllabus was searched for em dashes before writing this
rule. Result: two, in about 2500 words. Both mark a genuine pivot, not a
decorative pause:

> "Credited attendance requires more than just showing up — it means coming
> to class prepared for the day's activities with necessary readings and
> assignments completed."

> "Some studies have shown that content warnings aren't very effective at
> reducing readers' anxiety, or that they may even increase it — more
> evidence is certainly needed."

So the rule is not "Matt never uses an em dash." It is: he uses it rarely,
and only to carry real weight — a stated consequence, a genuine turn. Machine
prose across this session's builds was using it as a comma substitute,
several times per screen, doing none of that work. That gap, not the
character itself, is what's wrong.

**Working rule:** machine-generated copy defaults to not using an em dash at
all. If a passage is Matt's own verbatim language, quote it exactly
(including any dash he wrote) and mark it as founder-verbatim so
`studio-voice-gate.py` clears it instead of flagging it. Every other em dash
in generated copy is a bug to fix, not a style choice to defend.

## D4. Other voice signals observed in the syllabus (first pass, not final)

- Direct address throughout ("you," "I"), plain and procedural, not
  performative.
- Contractions used naturally and often (it's, don't, aren't, you'll) — the
  prose is not stiff.
- Short declarative sentences carry the load; longer sentences show up for
  genuine explanation, not for effect.
- Warmth shows up as a plain, short line dropped into procedural text, not
  as sustained tone: "We want you here, and we want you to want to be here.
  So, please do your best." No ramp-up, no closing flourish — it just sits
  there and moves on.
- Analogy used sparingly and concretely, not as a rhetorical flourish: "that's
  like going to the gym and having a robot lift the weights for you."
- No AI-adjacent hedge-everything phrasing, no "let's dive in," no listicle
  cheerfulness. Headers are for navigation (a syllabus needs to be scannable),
  not a substitute for actual sentences.

## D5. What "not mine" sounds like, named plainly

The founder's complaint was not about a single punctuation mark. It's that
generated copy across this studio reads as generic AI prose wearing the
studio's color palette. The em dash was just the most checkable symptom.
The deeper fix — matching cadence, restraint, and the specific plainness
shown in D4 — is a human-ear judgment this manifest cannot make mechanically.
`studio-voice-gate.py` v1.1 only catches the one thing that can actually be
checked by machine (the dash). Everything else in D4 is a standard for a
human read, not yet a gate.

## Open, honestly

- Course schedules, handouts, announcements, and portfolio feedback (all
  named in the founder's ruling) have not been pulled into this manifest yet.
  Each would sharpen D4 past a single-document sample.
- `studio-voice-gate.py` only has one tooth. Future incidents should add
  more the way `preship-gate-v4.py` grew its teeth — one real miss, one new
  mechanical check, never a prose rule that isn't also a check.
- The founder-verbatim marking convention (`data-founder-quote`,
  `data-founder-verbatim`, or a `FOUNDER-VERBATIM` comment before a JS string)
  is new as of this file. Nothing in the existing corpus uses it yet.

---

## LANDED IN THE REPO 2026-08-09 — the status line above is finally out of date

Founder: **"Make this write lane. I auth."**

This file opens by recording that it did not exist while the standing instructions pointed
at it as if it did. That was still true four days later. Belt tick 8 (`scope-gate.py`,
armed 2026-08-09) measured the trunk and found three files named by the standing
instructions that resolved nowhere: two were wrong paths for documents that existed at repo
root, and this one was **not in the repo at all.** It lived only on the project shelf — the
lane the studio instructions call a cache that lags and is never canon.

So for four days the session-open protocol ordered every agent to obey the D3/D5 founder
voice rules from a document no agent could fetch. Founder voice provenance was computable
from no lane the trunk could reach. Every session that read the instruction, looked, found
nothing and kept going was behaving exactly as designed, which is the problem.

**Transfer method, stated because it matters.** There is no machine path from the project
shelf to disk in this sandbox. The text above was carried across by TRANSCRIPTION, not by a
byte-verified copy, so it is not blob-identical to the shelf doc the way a repo round-trip
would be. One deliberate change: a stray reference to a numbered scratch copy of the
founder-canon log was rewritten as plain prose, because naming a file that is not in the
trunk would trip belt tick 8 clause B, and a citation nobody can follow is the exact defect
this landing exists to close. Everything else is carried as written. **From this commit the
repo copy is canon and the shelf copy is a cache.**

D2 still names the real gap: one syllabus read in full, with course schedules, handouts,
announcements and portfolio feedback still not pulled in. Landing the file does not close
that. It only makes the gap readable by something other than a chat.
