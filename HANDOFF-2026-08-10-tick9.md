# HANDOFF 2026-08-10: mount tick 9, then the carried list

Lane closed at commit `6b0536be`. Belt is 8 of 8 green in the repo. One built, tested,
byte-verified thing is NOT mounted, and that is the first job next session.

## FIRST JOB: mount tick 9 on the belt (about ten minutes)

`approvals-gate.py` is landed (10220 B, md5 `e630a964`, self-test 8 of 8, corpus clean at
112 surfaces / 1 credit / 0 halts). It is NOT called by `studio-belt.sh`. A gate that is not
on the belt does not run, which is the disease this studio has fixed four times.

The belt edit was written and tested locally and did not land. It is four changes:

1. **Index line**, insert after the tick 8 line in the header comment:
   `#   9  student consent on file       approvals-gate.py       (flat, founder ruling 2026-08-10)`
2. **Tick count, computed not typed**, insert after `fail=0`:
   `TICKS=$(grep -cE '^#   [0-9]+  ' "${BASH_SOURCE[0]}")`
   Use exactly that pattern. A first attempt used `'^# +[0-9]+ +[a-z]'` and counted 8 of 9,
   because tick 3's index line reads ">50% image floor" and the pattern wanted a letter
   after the number. A computed number that is wrong is worse than a literal one.
3. **Header**, replace `all 8 ticks` with `all $TICKS ticks`. This is the only edit that is
   not insert-only, so it needs a re-seed of the file rather than a patch.
4. **The tick itself**, insert before the final summary rule. Shape it like tick 8: skip
   loud if the gate is missing, skip loud if `approvals-log.md` is missing (consent
   unreadable is never a pass), run with `APPROVALS_LOG="$BELT_DIR/approvals-log.md"`,
   `fail=1` on non-zero exit.

**Chunk any re-seed at 6000 base64 characters, not 12000.** A 12000-char payload truncated
in transit on 2026-08-09 and landed 7459 bytes against an intended 9000. The byte check
caught it; the success flag did not. Re-chunked at 6000 it landed clean three times running.

Verify by behavior, not by matching a hash from this document: belt prints `all 9 ticks`,
runs 9 of 9 green on `index.html` and `arcade.html`, and HALTs when the log entry is
removed. Both canaries were run before this handoff was written.

## WHAT LANDED THIS SESSION

- `claude/FERPA-SCOPE-RULING.md` 8685 B, commit `d0ff461a`. Founder ruling 2026-08-10 as the
  SOURCE section: do not draw from student work unless specifically authorized, and
  authorization means an entry in `approvals-log.md`. Sits above THE CHECK and above SCOPE.
- `approvals-log.md` 3024 B, commit `311e5cae`. The log the attribution standard has
  required since 2026-08-03 and that never existed. Carries no email address, no full
  surname, no quoted message text, because this repo is public.
- `approvals-gate.py` 10220 B, commits `1e446b25` / `6a04df49` / `6b0536be`.
- `studio-belt.sh` 20127 B, commit `88976ca9`. Ratchet now keyed by the git REMOTE, not the
  checkout directory. This is the big one: ticks 3, 4 and 5 were HALTing `index.html` and
  `arcade.html` on files nobody had touched, because a clone not named TIGHT-SPIRAL-STUDIOS
  missed every baseline and read carried debt as new.
- `scope-gate.py` 19720 B and belt tick 8, plus `scope-baseline.json` at debt 1.
- `claude/forking-paths-protocol.md`, `claude/founder-voice-provenance-manifest.md`,
  `claude/FUNES-LEDGER.md` (a pointer that refuses), and root
  `FORKING-PATHS-PROTOCOL.md` converted to a pointer.
- `FUNES-LEDGER.md` at 42 rows.

## CARRIED, IN THE ORDER I WOULD TAKE THEM

1. **Mount tick 9.** Above.
2. **`cross-lane-manifest.md` STANDING HALTS is stale.** All three entries were resolved on
   2026-08-08 and the section still reads as open. Anyone reading it inherits three phantom
   emergencies. Verified resolved by computation, not memory.
3. **Voice ratchet slack.** `voice-baseline.json` carries 3 dashes of unreclaimed headroom
   across 2 files. Baselines may only shrink, so it should be re-frozen. Do NOT fire
   `--init` blind: it rewrites 105 entries and could silently raise a baseline that has
   grown. Measure per file first.
4. **Last scope debt.** `claude_FUNES-CHARTER.md` cites a bare `FUNES-INDEX` name while the
   trunk holds `claude_FUNES-INDEX.md`. One line.
5. **Two sessions in one lane.** 13 commits from another TSP session landed mid-work on
   2026-08-09, one of them editing `studio-belt.sh` while this session was re-seeding it.
   Nothing was clobbered, and that was ordering luck. Second occurrence in two days. The
   lane model has RW and RO and cannot express two sessions inside one lane. Highest risk
   item on the board and the least defined. Do not open it at the end of a long session.

## ONLY MATT CAN DO THESE

- Rotate the exposed PAT. Still marked ACTIVE on `HANDOFF.md`.
- Create the Drive folder STUDENT-WORK-PROTECTED and register the ID.
- Hamish's own deploy still shows his full last name and a date. The arcade card follows the
  standard; the page it links does not, and the studio has no write access there. One email.
  Consent is settled and on file; this is presentation only.
- The GALA item on `HANDOFF.md` is marked urgent before Jul 20 and is three weeks past.
  Either it is done and the list is stale, or it is not and the list is the only thing
  that knows.

## THE PATTERN, BECAUSE IT REPEATED FIVE TIMES IN TWO DAYS

Every failure this session was a rule that named something nobody could reach, and nothing
could tell. The FERPA ruling lived in one lane and was cited from another. The standing
instructions named three files at paths that did not resolve. The attribution standard
required a log that did not exist. The manifest described resolved problems as open. The
belt's ratchet key pointed at a directory name that was not the repo. Belt tick 8 clause B
now catches the citation form of this. The others are still caught only by somebody looking.

Second pattern, same period: four times an agent typed a byte count instead of computing it
(425, 701, 175, 619). Three landed wrong-asserted. The fourth was aborted by the guard. The
arithmetic works. Read the number off the record; never type it.
