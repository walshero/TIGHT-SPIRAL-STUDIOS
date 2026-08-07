# OS BLOCK — The Aleph Fleet (agentic assessment)

*Supersedes the operational half of `os-block-aleph-diagnose-repair.md`, which stays as
the origin record. Three lenses became five, the merge became arithmetic, and the loop
grew a memory. 2026-08-07.*

**One job:** turn a build into a ranked, evidence-backed, *tracked* defect list — and make
the tools sharper every time they miss.

---

## What was wrong with the old Aleph

It worked twice and both times it worked **by hand**. That is the whole problem: a
protocol executed by a person is a protocol that ends when the session ends.

| hole | what it cost |
|---|---|
| **Agreement was judgement.** Three lenses, three vocabularies, no shared keys — so merging meant a human reading three lists. | The merge could not be re-run, compared, or trusted a week later. |
| **The feedback tooth was a sentence.** "Harden the gate that missed it" had nowhere to live. | It happened once (2026-07-26), was forgotten, and the same class of miss recurred twice more — comfort-gate blind to fill-tokens-used-as-text (08-03), studio-eyes-sweep blind to text inside a viewBox (08-07). |
| **There was no iteration.** Findings landed in a dated markdown file. | Nothing knew if a defect was new, old, fixed, or back. |
| **Nothing assessed learning.** Three lenses asked *does it work*, *does it play*, *does the message land*. | On teaching games, the thing they exist to do was the one property no lens measured. |
| **The wall-detector measured a laptop.** `one-thing-gate.py` ran at 1280x800 while every other instrument ran the phone. | The founder's actual complaint — "a wall of directions, unreadable for my phone" — was invisible to the gate built to catch walls. |

---

## THE FIVE LENSES

Run them independently. Independence is the point: agreement between blind lenses is
signal, agreement between briefed-together lenses is echo.

| | lens | question | brief |
|---|---|---|---|
| **L1** | TSP tools | what do the gates say, run literally? | `aleph-lenses/L1.md` |
| **L2** | Play | does it play, **on a phone**? | `aleph-lenses/L2.md` |
| **L3** | Media | does the message land? | `aleph-lenses/L3.md` |
| **L4** | Aesthetic | does it read as one made thing? | `aleph-lenses/L4.md` |
| **L5** | Learning science | does anyone actually learn? | `aleph-lenses/L5.md` |

L4 and L5 are new. L4 was a sub-clause of L3 and deserved its own eyes in a studio whose
canon is that the image carries the idea. L5 did not exist at all.

**The briefs are files, not prose in a prompt.** A lens re-derived each run produces runs
that cannot be compared. Hand the aleph the brief.

---

## THE SHARED VOCABULARY

`aleph-taxonomy.json`. Every aleph returns a **key** from it. That single constraint is
what turns the merge from judgement into a count.

Five groups: `floor` (L1-owned, mechanical) · `play` · `media` · `aesthetic` · `learning`.

A key is a **defect class** — never a fix, never a score. Add one only when a real
finding has nowhere to go. **Never rename one**: the ledger keys history by it.

---

## THE SYNTHESIS

`python3 aleph-fleet.py --synthesize <run-dir>`

- **Agreement** = how many *distinct lenses* named the same key on the same surface.
  `***` three or more, fix first. `**` two. `*` one — real, but a hypothesis.
- **Worst severity wins** a cluster.
- **Findings get stable ids** — hashed over surface + key + anchor, deliberately *not*
  over the prose, so an aleph rewording a defect does not mint a new finding.
- **`passed` is load-bearing.** A key neither found nor passed reads as **not looked at**,
  and the synthesis says so. Silence never scores as clean.
- **Malformed input is rejected, not dropped.** A broken aleph is a lens that did not
  report; it is never a pass.

---

## THE FEEDBACK TOOTH, MADE DURABLE

**When any non-L1 lens names a `floor` key that L1 did not, the gate has a hole.**

The harness writes it to `aleph-blindspots.json` with a status — `open` until the gate
grows the tooth, then `hardened`. It cannot be forgotten between sessions any more,
because it is a file with a counter on it.

Repair the **tool**, not just the file. Then re-run the gate's self-test. This is the
ratchet applied to the diagnostics themselves: every escaped defect becomes a permanent
new check.

---

## ITERATION

`aleph-ledger.json` is the memory. Every run diffs against it:

- **NEW** — first sighting.
- **REPEAT** — seen before, still there. Carries `runs_open`; a defect open across many
  runs is a decision the studio is making by not deciding.
- **REGRESSED** — was fixed, came back. The most serious state on the board.
- **FIXED** — was open, now absent. The ratchet moved.

Run with `--commit` to record. Without it, nothing is written — a dry run is safe.

---

## THE PHONE IS BINDING

The founder reads on a phone and has retinitis pigmentosa. A layout comfortable at
1280px and a wall at 390px **is a wall**. Every lens assesses the phone first; the wide
screen is measured too, but the phone decides.

`one-thing-gate.py` now measures 390x844 *and* 1280x800, and the phone-side findings
carry the higher severity. It also measures the thing that actually matters for an
instruction wall — not words on screen, but **words above the first control** and
**screens-to-first-action**, with chrome (comfort control, nav rail, skip link)
excluded, because furniture sitting at y=0 was masking the measure.

---

## HOW TO RUN IT

1. `python3 aleph-fleet.py --lenses` — see the fleet.
2. Run **L1 yourself**: `bash studio-belt.sh .` plus the gates in `aleph-lenses/L1.md`.
   Write its findings as JSON.
3. Seat **one aleph per lens per surface** (L2–L5). Hand each its brief file and the
   schema from `aleph-fleet.py --schema`. They must not see each other's output.
4. Collect the JSON into a run dir.
5. `python3 aleph-fleet.py --synthesize <dir>` — read it. Then `--commit`.
6. **Repair in confidence order**: unanimous blockers → clean logic bugs → safe minors →
   structural/voice changes last, and those get surfaced to the founder rather than
   unilaterally rewritten. Authored craft is his.
7. **Re-verify each fix against the gate that caught it.** A repair that does not move
   its own gate is not done.
8. **Harden every open blind spot**, then re-run that gate's self-test.

---

## WHAT THIS DOES NOT DO

It does not decide. It does not rewrite voice. It does not judge fun — that is the
founder, and clearing the mechanical rubble before his taste is spent is the entire
point of the fleet. Twenty cold plays become one review.
