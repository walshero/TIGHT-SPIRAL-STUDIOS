# HANDOFF
**Last written 2026-07-14. REPLACED, never appended. History lives in git.**
**Canon: `raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/HANDOFF.md`**

---

## THE ONE THING — 90 seconds, and it unblocks everything

**The GitHub PAT lacks the `Workflows` scope. Until it has it, the studio has ZERO
enforcement points that cannot be skipped.**

Everything else landed today. `floor.yml` could not — git refuses workflow files without
that scope.

> github.com → **profile picture, top right** → Settings → scroll to the **bottom** →
> Developer settings → Personal access tokens → **Fine-grained tokens** → your token →
> Permissions → Repository permissions → **Workflows** → *Read and write* → scroll to the
> **bottom** → **Update token** (green button; it does not save without it).

⚠ **"Workflows" is alphabetically BELOW "Webhooks."** Easy to scroll past on a phone.

Paste the token, say **"arm it."** One push.

---

## THE TEETH AUDIT — the disease, finally measured

```
30 imperative rules across 10 OS blocks
 7 executable enforcers, 53 HALT paths between them
 0 enforcement points that cannot be skipped
```

**Zero.** Every gate runs only if the agent REMEMBERS to run it.

The access-control literature names what is missing: a **Policy Enforcement Point** — a
chokepoint every request must physically pass through. **A policy without a PEP is not a
policy. It is a document.**

**Gawande is harsher:** killer items only, **5–9 per pause point**. Past nine you get *"the
illusion of a checklist while guaranteeing selective attention failures."* TSP has **30** —
3.3× working memory. That is why six rules watched the v34 clobber and **only the arithmetic
one fired.**

**The one gate that runs without a human was disarmed** — `floor.yml`, `continue-on-error:
true`, three days. Its own comment: *"A gate that does not block is not a gate."* Disarmed
over **104 HALTs**; the corpus now has **23**. *Audit mode is a phase, not a destination.*
The reason expired; the exception outlived it.

**SHIPPED: `ratchet.py`** — arms the gate without freezing the site. Baselines the 23,
**blocks anything new.** Debt can only shrink; a fixed file leaves the baseline **forever**
and can never quietly regress. Both canaries pass. **It refuses.**

---

## STUDIO EYES — BUG 7. It was serving false passes.

Built the ratchet, ran a canary, **it failed.** White-on-white at **1.1:1** sailed through.

**The blindness was in Studio Eyes.** The ground walk checks the selector, the base rule, DOM
ancestors, BEM prefixes, descendant strings — **and never checks `body`.** Text sitting
directly on the page background finds no ancestor, falls to `page?`, and is **downgraded from
HALT to WARN.** The auditor **measured the defect correctly** and filed it as a suspicion.

**TICK 4 predicted this in writing:** *"a gate that stops false-positiving by becoming blind
is not repaired; it is broken in the other direction."* It was. **Body is not a guess. It is
the cascade.**

**Fix surfaced 8 more files: 15 → 23.** They were never passing. **They were invisible** — on
a corpus built for a founder with retinitis pigmentosa.

---

## THE FERPA OVER-FIRE — I was wrong. Reverted.

**I pulled the 598 KB Confluence canon trunk off the public site over a false CRITICAL.**
Scanned, found 18 `@massbay.edu` addresses and 7 Lumière contributor names, called it a breach.

**Founder ruling, now in memory:**
> **MassBay faculty names and emails are PUBLIC DIRECTORY INFORMATION.**
> **Student writing published in Lumière is PUBLISHED WORK — attribution is the POINT.**
> *A litmag that hides its writers is not a litmag.* **Features, not leaks.**

**REVERTED byte-exact.** `confluence-TRUNK.html` md5 `8dcf9903` = canon v44, 598,114 B.
`massbay-fact-book-word.docx` restored. **Nothing lost.**

**Correctly pulled, stays pulled:** `claude-project-instructions.md`,
`chatgpt-pro-instructions.md` — **the pipeline IP, the subject of the Borges paper, published
for free.**

⚠ **STANDING: the Integrity Guard has pushed this same false CRITICAL across NINE runs since
07-12.** TICK 4: *an auditor that cries wolf is worse than no auditor — it trains the founder
to ignore it, disabling every real finding it will ever make.* **Correct its PII definition or
it fires forever.** True scope: unpublished student work, grades, enrollment, advising notes,
gradebook/SIS. Nothing else. `.gitignore` now says this in plain language.

---

## THE ADVANTAGE LANE — new client, shipped

**James Power**, Advantage Relocation Inc. — advantagenyc.com · 917-686-9830 ·
james@advantagenyc.com. Manhattan rentals, executive + international, REBNY. **Tenant-side
only, no landlord tie-ins** — which after the FARE Act is the only legally clean way to take
a fee from a renter in NYC.

**He wrote the spec himself,** in caps, on his own site:
> *"We know what to show, but more importantly our experience tells us WHAT NOT TO SHOW!!"*

The filter is his whole value, and it only fires once he is on the phone with you.

**SHIPPED:** `advantage-intake.html` · 35,352 B · commit `d2727c7` · gate exit 0 · ratchet 0
regressions.
**LIVE:** `walshero.github.io/TIGHT-SPIRAL-STUDIOS/advantage-intake.html`
*(container egress blocks github.io — could not verify the 200 from inside. Tap it.)*

**The Tension Bar.** Six controls; the market answers. **Opens on the collision** — a doorman
one-bedroom at an out-of-town number, the trap the data says everyone walks into.

**The number that carries the product** (MNS, May 2026): non-doorman 1BR asks **$4,310**;
with a doorman, **$5,840**. **$1,530/month — ~$18,400/year — for a lobby.**

**The collab app (James + Nathan):** they can already text. A text cannot carry the client's
**constraint-state**. So it rides in the **URL fragment** — everything after `#` is never sent
to a server. Tap the link in iMessage, land inside the exact bar the client saw. No database,
no account, no storage, nothing to breach. Round-trip verified; malformed hashes fail clean.

**COMPLIANCE — load-bearing:**
- **Never show a unit.** DCWP forbids conditioning access to identifiable inventory on being
  hired. **State, never stock.**
- **The page measures; it does not counsel.** Unlicensed software may not advise on a NY lease.
- **Flat project fee. Never per-lease.** Confirm with a NY RE attorney before any comp
  touching a transaction.
- **`guarantorRateConfirmed: false`** — the 90% guarantor figure does NOT render until James
  confirms it. Shows *"ask James."* A blank is honest.

**THE ASK TO JAMES — do not lead with it.** Neighborhood multipliers were **invented** and sat
beside a real citation block, which made them *look* sourced. Deleted; `hoodSpread: null` plus
a written refusal is in the data block. **Open by showing him the doorman number and asking if
it matches what he sees.** If he says "that's low," he has corrected you for free.

---

## THE ALEPH FINDING — bigger than any build

**You have built this engine four times.**

| Build | The invisible constraint it makes visible |
|---|---|
| **Confluence** | Courses × outcomes. **Dry cells.** Called "the actual product." **Unbuilt.** |
| **Choose Your Leader** | *"You judge what you were allowed to see."* |
| **The Console** | The levers move; the telemetry shows what they cost. |
| **Advantage** | The constraints collide; the tradeoff names itself. |

**One engine, four faces.** Advantage is the first with a paying client attached — and **its
data block is already isolated.** Same file, different data block, and you have **Confluence's
I-P-A map.**

---

## OPEN — carried forward

- **`os-block-bodyguards.md` (`d4c670e`) FORKED an existing block.**
  `os-block-bodyguard-gates.md` (07-04) already had the ≥75% rule and the adversarial seat.
  **I wrote it without checking the shelf — the Aleph failure, committed while writing a block
  about enforcement.** Merge them.
- **Advantage is a doorless room.** URL works; navigation does not. Held: direct-link only.
  **Do not build a storefront for a client who has not walked in.**
- **The three questions still unanswered:** (1) how two licensed agents co-advise through the
  app; (2) **the competitive SWOT — not researched.** Instinct: nobody does the tradeoff-reveal
  because every other player is a *listing* business and **cannot afford to tell you what not
  to buy.** Unverified. (3) TSP's niche assets: **accessibility-as-arithmetic** (no NYC
  brokerage has run a contrast gate on a client tool; HR with ADA obligations will care), the
  **collision engine**, and **the assessment spine** — *you norm raters before they score*,
  which is the same operation as norming a client before they tour. No broker has that.
- **FOUR LANES, not three:** repo · **Netlify** (`relaxed-gaufre-a0c223.netlify.app` — Dad
  Energy v2.1 lives ONLY here, no backup) · Drive · shelf. **A zero-result search is not
  evidence of absence** — it lied twice today (the canary was in `/studio`, not root).
- **The finishing problem stands.** Borges paper: finished, unsent. Diagnose mode: built,
  parked. **Advantage: now live at a URL nobody has been sent.**

---

## NEXT SESSION — IN ORDER

1. **Arm `floor.yml`.** One PAT scope, one push.
2. **Correct the Integrity Guard's PII definition.**
3. **Merge the two bodyguard blocks.**
4. **THE FORK THAT IS YOURS:** send Advantage to James, **or** point the engine at Confluence's
   I-P-A map. Same engine. One has a friend and a possible check; the other is the thing
   MassBay is waiting on and that you have called "the actual product" three times.
   **I cannot tell you which debt you would rather carry.**
