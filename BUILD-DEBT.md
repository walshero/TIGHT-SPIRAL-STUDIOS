# BUILD-DEBT.md — the governance rate-limiter

**One job:** stop the studio from shipping governance faster than product.

The named failure mode (already in memory): **SPEC-RICH, BUILD-POOR.** Every
session ends cleaner and adds one more rule, and that *feels* like progress. It
isn't. A player gained nothing.

This file makes the anti-rabbit-hole rule itself a check. "If a rule can't be a
check, it's a wish" — here is the check.

---

## THE RATIO RULE (the only rule in this file)

> **No session may add a governance artifact — a rule, an OS block, a seat, a
> gate, a tick, a script — unless the PRIOR session shipped a player-facing
> capability.**

Governance is rate-limited by shipping. Debt must be paid before more is drawn.

- **Ship** = a player/student/institution can now DO something they could not do
  before, AND it passed the ship gate (GATE 1 founder cold phone play → GATE 2
  Studio Eyes), AND it rendered on Matt's actual device.
- **Governance** = anything in the meta-layer: rules, OS blocks, seats, gates,
  ticks, sweep scripts, manifests, canon docs.
- A spec is **not** a ship. A parked artifact is **not** a ship. "Basically done"
  is **not** a ship.

---

## SESSION-OPEN CHECK (fires with the three seats)

Read the last two lines below. If the most recent line is `GOV` and the one
before it is not `SHIP`, then **THIS SESSION BUILDS. Full stop.** No new
governance until a capability ships.

## SESSION-CLOSE LOG (one line, append-only, newest at bottom)

Format: `DATE | SHIP or GOV | what a player can now do (or what governance was added)`

```
2026-07-19 | GOV | added BUILD-DEBT.md ratio rule. DEBT +1. Next session owes a build.
2026-07-19 | SHIP | preship-gate-v4.py render-proof teeth: the gate now catches the class where a screen passes at 13:1 and renders unreadable on Matt's retina (opacity floor + RP warm-hue floor). A builder can no longer ship a gold-on-unpainted screen the old gate green-lit. Canaried: your-rp-world HALTs, viscosity SHIPs. DEBT paid.
```

---

## SUNSET CLAUSE (Chesterton's Fence, inverted)

Before adding any governance artifact, remove one that never fired. Any rule,
seat, or gate that has not triggered in 5 logged sessions is archived to
`governance-attic/`. A rule nobody runs trains everyone to ignore the ones that
matter.

---

## WHY THIS IS THE FORCING FUNCTION

Memory already says NEXT SESSION OWES A BUILD. This file is that sentence with
teeth: it survives the chat, it fires at open, and it blocks the reflex that
keeps winning — ending the session with a tidier OS instead of a played game.

Borrowed from: Kanban WIP limits (cap governance-in-progress), Scrum Definition
of Done (DONE = rendered on Matt's phone, not gate exit 0).
