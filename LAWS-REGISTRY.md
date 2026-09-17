# LAWS-REGISTRY — every law names its hook, or it is a wish

Created 2026-09-17 by founder ruling, same session as THE CONVENING. The founder's
question, verbatim: *"Law, but didn't fire. That seems problematic. How can we
address systematically."*

The finding that forced this: Stage 0.5 (the disciplinary panel) was law in the OS
since July and never fired, because it was bound to a moment that exists only in
prose ("right after intake"). Nothing in the machinery ever arrives at that moment.
Contrast never has this problem because it is bound to a real event: a push.

**The principle: a law is only law when it is attached to a HOOK — a place in time
that fires without anyone remembering. A law attached to a prose moment is a wish,
structurally, however well written.**

---

## THE HOOKS — the only places in time the studio actually has

Verified this session, with evidence. A law binds to one of these or it is a wish.

| Hook | Fires | Evidence (2026-09-17) |
|---|---|---|
| **PUSH** | every push, mechanically | `belt.yml` + `floor.yml` CI; `studio-belt.sh`, 12 ticks, "every tick BLOCKS" |
| **WEEKLY** | Mondays, scheduled tasks | Aleph drift sweep 10:00 UTC, Fingers 11:00, Tableau belt 12:00, canon decay 13:00, Integrity Guard 13:00 — all read live from the scheduler today |
| **DAILY** | noon UTC | "No walls, universal home" — SUCCEEDED today |
| **SESSION-START** | every session, semi-mechanically | project instructions load mechanically; the Aleph pass (`claude/forking-paths-protocol.md`) executes by agent compliance — the load is guaranteed, the execution is not |
| **PRE-WRITE** | before a draft is authored | THE CONVENING (OS §6 0.5-A). Comparator built same day: `convening-gate.py`, audited weekly by Integrity Guard step 6b |
| **DEVICE** | when a file reaches the founder | the founder's eyes and hands — the one human hook, real but unlogged |

**Standing finding at creation: the Aleph drift sweep's last run was ABANDONED
(2026-09-14) while its four sibling sweeps SUCCEEDED.** A sweep that abandons and
is never noticed is a blind gate reading as present — this registry's first catch,
found while building it.

---

## THE REGISTRY

Status vocabulary: **WIRED** (bound to a hook, verified this session) ·
**REPORT** (wired but does not block) · **DISCIPLINE** (hook exists, enforcement
is compliance, no arithmetic) · **WISH** (no hook) · **UNVERIFIED** (not yet
censused — a status, not a shrug).

### Wired to PUSH — the belt's 12 ticks (verified in `studio-belt.sh`)

| # | Law | Check | Status |
|---|---|---|---|
| 1 | Accessibility floor (painted-pixel contrast) | `comfort-gate.py` | WIRED, flat |
| 2 | Student attribution standard | tick 2 | WIRED, ratchet |
| 3 | >50% image floor + render proof (C7) | `preship-gate-v4.py` | WIRED, ratchet |
| 4 | Founder voice — unmarked dashes (D-rules) | `studio-voice-gate.py` | WIRED, ratchet — **one tooth; corpus rebuild ruled 2026-09-17, see CONVENING handoff §5** |
| 5 | Entry paint / one invitation | `one-thing-gate.py` | WIRED, ratchet |
| 6 | Retired lines (founder bans) | `retired-lines-gate.py` | WIRED, flat |
| 7 | Touch floor, 44px, rendered | `studio-fingers.py` | WIRED, ratchet |
| 8 | Scope — what a doc reaches for | `scope-gate.py` | WIRED, A flat + B ratchet |
| 9 | Number sense / layout | `number-sense-gate.py` | WIRED, flat |
| 10 | Contrast, every route + mode | `contrast-sweep.py` | WIRED, flat |
| 11 | Intent — spec + audience declared | `intent-gate.py` | WIRED, presence ratchet |
| 12 | Stored state that rotted | `stale-fuse.py` | **REPORT — not armed.** A tick that reports and never blocks is halfway to a wish; arming it green is its own open item (belt header, 2026-09-12) |

Also on PUSH: C1 color-scheme (`c1-check.py`, `floor.yml` + `confluence-hub.yml`) — WIRED.

### Wired to WEEKLY (verified live on the scheduler)

| Law | Carrier | Status |
|---|---|---|
| The whole belt, corpus-wide | Tableau Sweep, Mondays 12:00 | WIRED — ledger lines land weekly since 2026-08-03 |
| Touch floor, corpus-wide | Fingers weekly sweep | WIRED |
| Canon decay / floors | canon decay sweep | WIRED |
| Governance integrity | Studio Integrity Guard | WIRED |
| Cross-lane canon drift | Aleph drift sweep | WIRED — **last run ABANDONED 2026-09-14; re-fired 2026-09-17; the Integrity Guard now checks sibling-sweep outcomes weekly** |
| Statute sweep — every law names its hook | Integrity Guard step 6b, Mondays 13:00 | WIRED — `statute-gate.py` + `convening-gate.py --audit`, added 2026-09-17 |

### Bound to SESSION-START (loads mechanically, executes by compliance)

| Law | Written check | Status |
|---|---|---|
| Aleph pass — hash trunk, declare BLIND lanes, diff FUNES | `forking-paths-protocol.md`, `resolve-canon.py --audit` | DISCIPLINE |
| Canon is computed — diff before editing any named file | `resolve-canon.py --check` | DISCIPLINE |
| Same-turn landing, byte-verified; connector success is never proof | `verify-push.sh` exists | DISCIPLINE — script real, invocation is memory |
| FERPA scope — name/path search, never fullText | `FERPA-SCOPE-RULING.md` THE CHECK | DISCIPLINE |
| One canon writes, others read | `cross-lane-manifest.md` | DISCIPLINE |

### Bound to PRE-WRITE (the Convening, ruled 2026-09-17)

| Law | Check | Status |
|---|---|---|
| The sentence before anything is authored | `convening-gate.py` (SENTENCE check) | WIRED — weekly audit via Integrity Guard step 6b; PRE-WRITE by invocation |
| Five standing seats sign the findings file | `convening-gate.py` against `convening/<build>-CONVENING.md` | WIRED — built, selftested and landed 2026-09-17; weekly audit via Integrity Guard; PRE-WRITE by invocation |

### Bound to DEVICE (the founder — real, unlogged)

| Law | Status |
|---|---|
| Feeling-first entry — the founder leans in before the mechanic is built | DISCIPLINE, no firing record |
| JS-driven states hand-verified (the engine does not execute JS) | DISCIPLINE |
| Art HALT — rendered pixels through the founder's eyes | DISCIPLINE |

### WISHES at census — laws with no hook (the problem class, named)

| Law | Where it lives | Cheapest honest hook |
|---|---|---|
| Medium Gate — no default medium, run at parameter time | OS §3.2; `medium-gate-check.py` exists, wiring UNVERIFIED | Convening (Conductor seat) |
| Wireframe Novelty Gate — name the one structural surprise | OS §6 | Convening |
| Spend-one-affordance close-out | OS §6 | Convening close, or a belt presence-check |
| Union Rep roll call before seating | OS §5 | Convening — a roll-call block in the findings file |
| KD! ledger append at session close | ledger header | Integrity Guard could count sessions vs. entries |
| C6 admission test — why would a stranger play this | founder canon | Convening (Stranger seat) — now assigned |
| Deferred-reskin rule (rename as-opened, never bulk) | OS header | UNVERIFIED — likely fine as DISCIPLINE |

### UNCENSUSED — scripts whose hook status is unknown (honest gap)

The repo carries ~64 gate scripts; this v1 verified the belt's 12, C1, and the
sweeps. The rest — including `canon-guard.py`, `canon-freshness.py`,
`founder-gate.py`, `approvals-gate.py`, `secret-scan-gate.py`,
`medium-gate-check.py`, `art-gate.py`, `art-execution-gate.py`,
`reply-shape-gate.py`, `pixel-ratchet.py` and siblings — are UNVERIFIED: each is
either wired somewhere this census didn't look, or is itself a wish wearing a
filename. **Censusing them is the statute sweep's first real job, not this file's.**

---

## THE SWEEP TOOTH — `statute-gate.py` (spec; Code-lane build)

Runs on the WEEKLY hook, inside the Tableau or Integrity Guard sweep:

1. Parse this registry. For every row: the named check exists on disk, and its
   hook shows a firing inside the window (CI runs for PUSH; ledger lines for
   WEEKLY; convening files for PRE-WRITE). No firing record → flag.
2. Flag any REPORT-status tick older than 30 days — report mode is a phase, not
   a destination (floor.yml's own words).
3. Advanced (second pass): grep canon docs for HALT/law declarations not present
   here, so an unregistered law cannot be written without being flagged the
   following Monday. That makes this file self-policing.
4. This registry is stored state and can rot: it takes a `stale-fuse` entry like
   the other 18 files the moment the comparator lands.

Until `statute-gate.py` exists, this file is itself DISCIPLINE — named plainly,
same as the Convening's comparator. Two builds, one Code-lane session.
