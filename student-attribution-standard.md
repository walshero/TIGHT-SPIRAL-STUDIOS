# STUDENT ATTRIBUTION STANDARD — studio canon, ADOPTED
*Tight Spiral Studios · house style for crediting student-authored games on any studio surface.*
*Set by Matt, 2026-08-03. Companion to `FERPA-SCOPE-RULING.md` (which governs what is *permitted*); this governs how the studio *presents* it.*

---

## THE RULING (one line)

When the studio publishes or links a student's game, credit it **first name + last initial**, name the course **generically**, and carry **no year and no section number**.

This is a presentation standard, not a permission gate. Permission is already settled by the FERPA ruling ("published or consented student work is never FERPA; publication is consent"). This standard is the courtesy layer on top: minimal identifiable footprint, by default, every time.

---

## THE CHECK (so this is a check, not a wish)

A student credit that reaches a public studio surface (arcade card, hub link, showcase, index, README) must satisfy ALL of:

1. **Approval on file.** A student email granting permission counts as documented approval. Record it in the approvals log / ledger (student first name + last initial, game title, "email approval on file", date recorded). No approval line -> HALT, do not publish.
2. **Byline = first name + last initial only.** Form: `Firstname L.` (e.g., `Hamish K.`). A full surname in the byline -> HALT. Heuristic: the credit string carries exactly one given name and one single-letter initial; a second full capitalized name-word is the failure.
3. **Course line is generic.** Allowed: course code + plain title + modality/length descriptor — e.g., `EN195 Creative Writing (summer 6-week online)`. **Never** a 4-digit year, **never** a section number (`sec 01`, `-01`, `#01`), **never** a specific date.

Same force as a failed contrast gate: a credit that fails any of the three does not ship. Exit 1.

## HOUSE FORM (copy this shape)

```
<Game Title> — <Firstname L.> · EN195 Creative Writing (summer 6-week online)
```

## SCOPE

- Governs surfaces the **studio** owns/links: arcade, hubs, index, showcase, repo READMEs.
- Does **not** reach a student's own external deploy — the studio cannot edit a student's site. If the studio links out to a student page that itself shows a full name or a date, that is a courtesy note to raise with the student, not a studio-surface violation.
- Faculty/staff credit is unaffected (professional directory info, per the FERPA ruling).

## ENFORCEMENT

- Any publish-time or preship pass that touches a student-credited surface reads this file first.
- Proposed gate hook (offered, not yet wired): extend the preship/publish gate to fail a student credit block that contains a full surname, a 4-digit year, or a section token adjacent to the course code, and to require a matching approvals-log entry. One added check, in one place. Wiring it into the gate is a repo edit — Matt's go.

---

## FIRST APPLICATION — Barcelona Summers

- **Game:** *Barcelona Summers — a noticing game.* Author on the live deploy: full name + a `7/8/2026` date.
- **Approval:** email on file (documented approval). Log line owed.
- **Studio credit under this standard:** `Barcelona Summers — Hamish K. · EN195 Creative Writing (summer 6-week online)`
- **Caveat:** the game lives on the student's own Netlify deploy, which currently shows his full last name and a date. The studio arcade card can follow the standard, but the linked page won't unless the student trims it or the studio hosts a corrected copy. Matt's call.

---

## LEDGER LINE (recorded 2026-08-03)

```
## 2026-08-03 — DECIDED: Student Attribution Standard (studio canon, adopted)
When the studio publishes/links a student game: credit first name + last initial only, name the course generically (e.g., EN195 Creative Writing (summer 6-week online)), and carry no year and no section number. A student email granting permission = documented approval, logged in the approvals list. Presentation standard layered on the FERPA ruling (publication is consent); written as a check — a credit with a full surname, a 4-digit year, or a section token does not ship (exit 1). First application: Barcelona Summers (Hamish K.), approval on file. Standard doc: student-attribution-standard.md.
```
