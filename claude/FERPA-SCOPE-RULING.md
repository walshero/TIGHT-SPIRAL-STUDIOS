# FERPA SCOPE — founder ruling, LOCKED. Stop the false flag.

**Verbatim, Matt, 2026-07-29 (recorded on the 29th recurrence):**
> "MassBay email addresses and published student work is never FERPA."

**Authority:** this is a policy / current-practice call, and Matt is the authority — he
teaches it, sits on academic standards, grade appeals, and ISLO assessment, and administers
FERPA in practice. The machine is not the authority. **When a sweep's FERPA flag disagrees
with this ruling, the machine is wrong. Do not defend the flag. Dismiss it.**

---

## THE CHECK (so this is a check, not a wish)

A FERPA flag may fire **only** when ALL of these are true:
1. a **named, identifiable student** is
2. tied to a **non-public education record** — a grade, score, GPA, disciplinary record, an
   **unpublished** graded artifact identifiable to that student, or an ID/SSN —
3. **without consent.**

A FERPA flag **NEVER** fires on:
- **Faculty / staff `@massbay.edu` (or any institutional) email addresses** — public
  professional directory information.
- **Published or consented student work** — lit-mag pieces, portfolios the student or program
  published, anything the student put into the world. **Publication is consent.**
- **Student names alone, roster entries, or seat labels** in a public or directory context.

## WHY THIS KEEPS RECURRING (the real defect)

The Integrity Guard and past sweeps trigger on the **mere presence** of `@massbay.edu` or a
student name and escalate to CRITICAL. **That trigger is wrong and is the bug.** Presence of an
institutional email is not evidence of a protected record. Remove the trigger.

## ENFORCEMENT

- **Funes and the Integrity Guard read this file before emitting any FERPA verdict.**
- A FERPA flag that does not meet all three conditions of THE CHECK **does not ship** — same
  force as a failed contrast gate. Exit 1.
- To raise FERPA, a sweep must name **the specific student** and **the specific non-public
  record.** "Emails present" / "names present" is **auto-dismissed**, silently, every time.

## DE-ESCALATION (kills the old framing)

Whether colleagues' emails sit on a public repo is, at most, a tidiness or courtesy preference
for Matt to decide on his own timeline. **It is never labeled FERPA, never CRITICAL, never an
emergency.** Prior briefs that called it "FERPA CRITICAL" were the false positive this ruling
closes.

**Recurrence count at ruling: 29. The recurrence was the defect. This closes it.**

---

# SCOPE — what a sweep may RETRIEVE

**Amendment, 2026-08-09, at recurrences 30 and 31. Founder direction: "Yes, build."**

THE CHECK above governs when a flag may **fire**. It says nothing about what a sweep may
**pull**. Those are two different questions, and the second one is where this file was
silent. A flag is a verdict about data you already hold. Scope is about whether you had any
business going and getting it.

## THE INSTANCE

Hunting for a studio file, the agent ran Google Drive `search_files` with
`fullText contains 'studio-fingers'`. Drive answered with five documents: three student
course portfolios and a short story, names attached, course codes EN195 and EN210, several
paragraphs of student prose dragged into the transcript. The token that matched was
**"floor"** — as in *floor-to-ceiling windows*. Nobody asked for student work. The errand
asked for a filename and the tool answered with a teaching corpus, because full-text search
does not know the difference between a file and a body.

## THE SCOPE CHECK

When the target is a **file**, search by **name and path. Never `fullText`.**

That is the whole control, and it is arithmetic rather than judgment: a `name contains`
query has no reach into a document body, so it cannot return a student's paragraph. There
is nothing to weigh.

1. Looking for a studio file → `name contains '<file>'`, or `parents in '<folder-id>'`.
2. Genuinely need body text → fence it first. Scope to `walshero/Claude_files` and its
   children by folder id, **then** full-text inside that fence.
3. `fullText` across all of Drive is **out of scope for studio errands, always.** Drive
   holds the teaching corpus. A studio errand has no business reading it.
4. If a wide query already ran and returned student prose: **drop it.** Not quoted, not
   summarized, not carried into a later turn, not written to a lane. Say the query was too
   wide, narrow it, run the narrow one.

Same rule shape everywhere else the studio reaches: Gmail, Dropbox, Netlify, the shelf. Ask
for the file by its name. Do not ask a corpus what it contains and then read the answer.

## THE VERDICT STILL DOES NOT CHANGE

A wide query is a **tool-usage defect** — the agent's, not the institution's. Adding SCOPE
does not license re-escalation, and nothing in this section reopens anything DE-ESCALATION
closed. It stands without exception: **never labeled FERPA, never CRITICAL, never an
emergency.** The correct report is one line — *that search was too wide, here is the
narrower one* — followed by the narrower one.

## THE PROCESS FAILURE, WHICH IS THE WORSE HALF

On 2026-08-09 the agent raised FERPA **twice without reading this file**, and called it
"the one I'd not leave sitting." ENFORCEMENT above requires reading this file **before**
emitting any FERPA verdict, and DE-ESCALATION forbids exactly that framing. Recurrences
**30 and 31**, on a ruling made at 29.

The ruling was not wrong. It did not need amending. It needed reading.

**THE READING IS THE GATE.** Any agent, sweep, or seat about to say the word FERPA fetches
this file first and states THE CHECK before it states anything else. No fetch, no verdict.
An agent that escalates FERPA without a fetch has produced a **process halt about itself**,
not a finding about the studio.

## LANE NOTE

Until this amendment, this file lived in exactly one lane — the project shelf — while
`FUNES-MEMORY-PATCH.md` §5 cited it by name from the repo. A gate document reachable from
only the lane the studio instructions call "a CACHE that LAGS, never canon" is a rule
nobody can compute. It now lands in the repo at `claude/FERPA-SCOPE-RULING.md`, and that
citation resolves.

**Recurrence count at amendment: 31.**
