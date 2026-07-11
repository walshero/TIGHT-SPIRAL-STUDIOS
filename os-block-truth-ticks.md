# OS BLOCK — TRUTH TICKS
**Locked 2026-07-11. Origin: the Confluence truth-scrub + Studio Eyes repair.**
Folds into OS §11 (standing working rules) and the Tick Rule (os-block-tick-rule.md).

---

## Why this block exists

One session produced four failures that were all the same failure wearing different clothes:
**a system asserted something it had not verified, and nothing in the pipeline caught it.**

- The file said six institutional outcomes. There are seven.
- The file named the six. They were the *wrong* six — a pre-revision set, two revisions stale.
- The auditor said twenty-two things were invisible. Twenty-two were fine.
- Claude said "the website is authoritative for vocabulary." It was not.

None of these were caught by a gate. All four were caught by the founder, by eye, in
conversation. That is a pipeline failure, not a luck failure. These four ticks close it.

---

## TICK 1 — SOURCE-COUNT

**Any claim about HOW MANY of something exists must be counted from the authoritative
source, in the same turn it is asserted, and enumerated.**

The artifact under audit is never its own reference. It is the thing being *tested*.
If a file says "six outcomes," that is the claim on trial — it is not evidence.

Applies to: outcomes, competencies, courses, panels, files, sections, roster entries,
any count that appears in a deliverable.

*Failure this prevents:* Confluence's irrigation map rendered six ISLOs and its own
aria-label asserted six. Claude reported the count as a defect without counting the
live source. Founder counted. Seven.

---

## TICK 2 — AUTHORITY BY CLAIM TYPE

**Different claims have different authorities. Do not pick one source and let it govern
everything.**

| Claim type | Authority |
|---|---|
| Counts, numbering, verbatim official text | The published source |
| Working vocabulary, current governance practice | The practitioner in the room |
| What the artifact currently does | The artifact |
| Whether the artifact is *correct* | Never the artifact |

*Failure this prevents:* Claude read "Graduation Competency" off the MassBay website and
told the founder his file's "ISLO" language was drift. It was not — the committee renamed
them two years ago. The public website was the stale artifact. The practitioner was right.
The count from that same website was correct. **One source, two claim types, two different
verdicts.** Treating a source as globally authoritative is the error.

---

## TICK 3 — REFERENCE STALENESS

**Any file carrying institutional reference data must name its source and a last-verified
date, in-file.**

Institutional reference data = outcomes, competencies, course lists, policies, rosters,
rubrics, scales, contacts.

Studio Eyes HALTs on institutional reference data with no provenance stamp.
A file that cannot say *where its facts came from and when* cannot be trusted to be current.

*Failure this prevents:* Confluence confidently rendered six outcomes MassBay abandoned two
revisions ago. Right format. Plausible names. Real-sounding. Completely wrong. Nothing in
the file or the pipeline knew the data had expired — because nothing ever asked.

This is the tick with the widest blast radius. Every institutional artifact in the studio
is exposed: the fact book, the syllabi, the course lists, the assessment corpus, the EN195
docs. Any of them may be silently stale right now.

---

## TICK 4 — THE AUDITOR IS IN THE CRITICAL PATH

**An auditor that cries wolf is worse than no auditor.** It does not merely fail to catch
bugs — it actively trains the founder to ignore its output, which disables every real
finding it will ever make.

Rules for any gate, sweep, or check in the studio:

1. **Never certify on a raw verdict without validating the verdict.** (Standing since
   2026-07-05. It was not enough — see below.)
2. **A gate must distinguish what it PROVED from what it GUESSED.** If a check cannot
   resolve the ground truth for a case, it says so and downgrades to a warning. It does
   not assert a default and call it a finding.
3. **Every repair to a gate ships with a canary** — a minimal fixture that proves the gate
   still catches the real bug it exists to catch. A gate that stops false-positiving by
   becoming blind is not repaired; it is broken in the other direction.

*Failure this prevents:* Studio Eyes was declared "repaired" on 2026-07-05. It was not.
It kept manufacturing false HALTs for six days, blocking eighteen files, and the founder
learned to distrust it. The 07-05 repair fixed *descendant* selectors and never touched
the four other ways grounding could fail.

---

## Standing consequence

**When the founder pushes back on a machine-produced fact, the machine is the suspect.**

Every one of the four failures above was found because the founder said some version of
"that doesn't look right." In all four he was correct and the system was wrong. The
correct response to founder pushback on a system's output is to *re-derive from source*,
not to defend the output or explain the system's reasoning.

---

## Wiring

- TICK 1, 2: behavioral — enforced in the session-open card and at every factual claim.
- TICK 3: mechanical — **BUILT 2026-07-11 as H6** in studio-eyes-sweep.py. HALTs any file
  asserting institutional facts without a source + last-verified date. Still owes
  floor-check.yml block-mode wiring.
  *Honest limit:* H6 verifies provenance **exists**, not that it is **accurate**. A stamp is
  a claim, not a proof — Confluence passes H6 today despite having carried two-revisions-
  stale data, because it carried stamps. Catching stale-but-stamped data needs TICK 1 + 2,
  which are behavioral.
- TICK 4: mechanical — canary fixture required in the sweep repo; the sweep's own test.
  **Canary written 2026-07-11**, lives with the sweep.


---

## TICK 5 — AUTO-DRIVE (locked 2026-07-11, founder ruling)

**Every file the studio produces writes to Drive Claude_files IN THE SAME TURN IT IS
CREATED. Not at session close. Not on request. At creation. Without being asked.**

### Why creation, not close

The close-time belt does not protect a file that dies mid-session. This session, the
corrected Confluence build sat in `/tmp` for **nine turns** — a directory that is wiped
when the chat ends — and survived only because the founder thought to ask "are these
saving automatically?" The answer was no. A session-close belt would have been too late if
the chat had ended at any point in those nine turns.

**Parked must mean saved-and-set-aside, never left-in-a-temp-directory.**

### The three clauses that make it real

1. **At creation.** A file that exists only in `/tmp` or only in the container does not
   exist. Write it the moment it is finished.
2. **Verify, never trust the receipt.** `success:true` is not proof. Byte-check every
   write. (Same rule already standing for GitHub; it applies identically here.)
3. **THE PASTE CEILING IS THE NAMED EXCEPTION.** `write_drive_file_content` takes
   `content` as a **tool parameter**, so it inherits the payload ceiling. Large files
   (Confluence at 511 KB; the 529 KB trunk) **cannot** pass through this bus.

   **Fork, mandatory:**
   - Small file → Drive bus (`write_drive_file_content`, overwrites by name, keeps file ID)
   - **Oversized file → container git-push** (no size limit), or
   - Oversized and un-pushable → **stays in outputs and is flagged LOUDLY as un-backed-up**,
     never silently

   Without clause 3 this rule fails silently on exactly the files that matter most — the
   trunks. "The most important file is the one file the lanes can't move" is a standing
   studio problem; AUTO-DRIVE must not pretend it has solved it.

### The two-lane rule, restated

Every build lands in **outputs** (the founder's save lane) **AND** Drive Claude_files (the
durable lane). This session honored only the first, and only because the founder asked.
That is the failure this tick closes.
