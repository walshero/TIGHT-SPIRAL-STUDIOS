# STUDIO FORWARD GUARD
*The enforcement layer for Tight Spiral Studios. Written 2026-07-11. Portable Markdown.*
*The studio was rule-rich and enforcer-thin — written gates nobody runs. This turns each gate into a running agent. This is the teeth on the gears.*

**Companion to:** `tsp-delegation-charter.md` (who may act) — this doc is *what watches and when*.

---

## THE SHAPE OF A GUARD

Every guard is four fields, no more:

- **GATE** — the rule it enforces.
- **SCAN** — what it looks at, and when it fires.
- **ACT** — what it does with a finding.
- **ESCALATE** — what it hands to Matt instead of acting.

**Iron rule for all guards:** guards *audit and report*. They never deploy, delete, publish, or send. Cosmetic fixes below the auto-fix wall may be applied at belt close and logged; everything above the wall escalates. A guard that could publish or delete on its own is not a guard, it's a hazard.

---

## THE GUARDS

### 1. INTEGRITY GUARD — scheduled, unattended (weekly)
The one that runs while you sleep. Stood up as a scheduled task 2026-07-11.
- **GATE:** link integrity + FERPA floor + Visual Constitution §13.
- **SCAN:** every public URL for 200/404; the repo/public pages for emails, student/faculty names, rosters; emoji, green-outside-Confluence, contrast; confirms sensitive files stay 404.
- **ACT:** ranks findings (PII = CRITICAL, broken public link = HIGH, cosmetic drift = LOW), overwrites `studio-guard-report.md`, appends one line to the TSP Ledger, pushes a summary to your phone.
- **ESCALATE:** any PII exposure surfaces immediately, not at week's end.

### 2. SOURCING GUARD — in-session, event-driven (on any claim entering a build)
The gear that connects to recursive research.
- **GATE:** nothing unsourced ships. Real figures, quotes, stats, dates — held until each has a verified, dated, sourced record.
- **SCAN:** every factual/real-figure claim in a build in progress.
- **ACT:** dispatches a recursive-research agent (the `deep-research` engine) to assemble the sourced record → returns a **draft for your HITL edit** → holds the claim out of any public build until you sign.
- **ESCALATE:** real-figure political content is RED regardless of sourcing — you clear it, never an agent.

### 3. CANON GUARD — in-session, event-driven (on save / handoff)
- **GATE:** one canonical file per name, no drift. (Kills the v33/v34 and triple-`Claude_files` class of problem.)
- **SCAN:** byte-count + content-head after every save; version ambiguity; duplicate folders.
- **ACT:** reports divergence, proposes the single canonical, flags "needs phone-canonization" where the phone copy is truth.
- **ESCALATE:** which file is canonical = founder gate.

### 4. WIP GUARD — belt-time
- **GATE:** max two builds in stages 4–6; one graduation per run.
- **SCAN:** counts active builds at every belt close.
- **ACT:** blocks a third from advancing; names the queue.
- **ESCALATE:** none — this one just holds the line.

---

## THE RECURSION (why "gears," not "checklist")

```
build in progress
      │
  SOURCING GUARD flags an unsourced claim
      │
  → deep-research agent  (fan-out search · fetch · verify · cite)
      │
  → sourced draft  →  YOU edit (HITL)  →  claim clears the gate
      │
  → build ships  →  belt logs it  →  Ledger records the sourced record
      │
  next build inherits the record — the studio gets more sourced over time, not less
```

The guard doesn't just say "no." It sends research to *earn the yes*, and the earned record is kept. That is the self-propagating loop you asked for.

## THE AUTO-FIX WALL

- **Below (auto-fixable at belt, logged):** muted-ink tokens, pre-ban green on old builds, dead internal anchors, stale dates in changelogs.
- **Above (never auto — RED):** anything touching student data, publishing to public web, real-figure content, canon choice, money, external comms.

## STATUS

- Integrity Guard: **LIVE** (scheduled weekly, read-only, reports to phone + Ledger).
- Sourcing / Canon / WIP Guards: **ON in-session** — followed on every build in any chat, per this spec.
- Next: first live run of the recursion loop on a real pending claim, on Matt's go.
