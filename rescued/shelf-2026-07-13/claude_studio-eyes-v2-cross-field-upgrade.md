# Studio Eyes v2 — what other fields teach an auditor that cries wolf
*Tight Spiral Studios · drafted 2026-07-13 · cross-field synthesis for founder ratification (proposes; Matt disposes). Additive; changes no canon until locked.*
*Occasion: the "student PII CRITICAL" that wasn't. Studio Eyes flagged the Lumière award-winners showcase — published, credited student authors — as a FERPA breach. It was wrong, and it was wrong the same way the old contrast sweep was wrong: high volume, low precision, escalated to CRITICAL. Matt caught it ("Pii??"). This doc is the fix, learned from five fields that solved the same disease.*

## The diagnosis every field gave, in one line
A false positive is **not** a smaller true positive. It spends the one thing the auditor can't rebuild — the owner's willingness to believe the next alarm. **Precision is the auditor's only currency.** An alarm people learn to ignore has already failed at its only job. So the goal is not to catch everything; it is to protect the meaning of "stop."

## The five fields (each mapped to a buildable change)

| Field | The practice | The change to Studio Eyes |
|---|---|---|
| **Aviation** | TCAS splits *traffic advisory* (heads-up) from *resolution advisory* (act now); GPWS suppresses "terrain" when gear is down — context gates the alarm | Three tiers — **NOTE / ADVISORY / BLOCK** — and a `data-context` region gate (a name inside a declared `showcase`/`byline` region does not escalate) |
| **Medicine** | BI-RADS never says "cancer," it says a *category*; category 0 = "needs more info," not a verdict. PPV, not confidence, governs trust in a low-prevalence world | Split **VIOLATION** (arithmetic-proven) from **NEEDS-REVIEW** (heuristic); a per-rule base-rate `prior` so a rare-on-public finding must clear a PPV bar before it can shout |
| **Software QA** | Linters tier error/warning/info; baselines block *new* issues and grandfather old; suppression carries a *reason*, never a silent mute | A `studio-eyes-baseline.json` ratchet + inline `<!-- studio-eyes:allow RULE "reason, reviewed date, who" -->` (empty reason = ignored), every suppression logged |
| **Security / DLP** | Detection ≠ authorization. Name+email in a masthead ≠ name+grade in a record. Severity × confidence is a matrix, not a number | A **severity × confidence** pair on every finding; a **PII rule that needs a second field** (grade/ID/DOB/SSN) to escalate — a byline alone can't |
| **Manufacturing / editorial** | Poka-yoke makes the error *impossible*; the andon cord stops the line only for defined, confirmed defects; fact-checkers rank who may override what | The **Scene-First / token scaffold** designs out the contrast+emoji failure classes; a short, published **block-list**; a founder **override** on craft findings, never on the floor |

## The v2 rule model (the arithmetic — "if a rule can't be a check, it's a wish")
1. **Two axes, never fused.** Every finding carries `severity` (cost if true) and `confidence` (sure it's true). **BLOCK requires both high.** A regex-only guess is capped at low confidence and can never block a push.
2. **Two output classes.** `VIOLATION` = proven by arithmetic (computed contrast < 4.5:1, a literal emoji codepoint, an external resource *load*). `NEEDS-REVIEW` = anything semantic/inferred (looks-like-PII, design-floor heuristics, "is this a record"). **Only VIOLATION can BLOCK.** NEEDS-REVIEW reports and ships.
3. **PII done right (the fix for today's miss).** A name or email escalates **only** when it co-occurs with a *record identifier* — a grade, score, student ID, DOB, or SSN pattern — **and** sits outside a declared `data-context="showcase|byline|masthead|credits"` region **and** the page is not `class="public"`. A credited author in a public masthead → **suppress**. A name next to a grade in an internal file → **BLOCK**. The discriminator is the *second field*, not the name.
4. **Two-signal rule (double-read).** One heuristic signal caps at NEEDS-REVIEW. Escalation needs two independent signals. This alone would have killed the awards-page false CRITICAL.
5. **Baseline / ratchet.** Block only *new* findings vs a committed baseline; existing debt is WARN. Debt count can only go down. (Ends the "104 pre-existing HALTs so the gate gets disabled wholesale" death.)
6. **Suppression with provenance.** Inline allow with a *required* reason string, logged to a report — visible, countable, reviewable. Never a silent mute.
7. **Precision self-scoring (the meta-audit).** Log every finding's disposition. Compute rolling PPV per rule. **Any rule whose confirmed precision drops below a floor auto-demotes from BLOCK to NEEDS-REVIEW until it re-earns escalation.** The auditor gets a scoreboard; it can no longer cry wolf without being caught doing it.
8. **Runbook per finding.** Every finding names how to confirm, how to dismiss, and the exact fix (file, line, token, number). No runbook → cannot exceed NOTE.
9. **Poka-yoke over detection.** The Scene-First scaffold ships tokens pre-cleared for RP contrast and a font subset with no emoji glyphs — so those failure classes have nothing to fire on. Prevent, don't detect-and-nag.
10. **Andon + override hierarchy.** A short, *published* block-list (contrast arithmetic, true record-PII, emoji, external load) is the only thing that stops the line. Founder holds a logged one-line override on craft findings; **no override on the floor** — accessibility and true PII are arithmetic, not taste. (Matches studio canon: current-practice authority is Matt; floor authority is the published source.)

## Reference implementation — the corrected PII classifier (drop-in for the sweep)
```python
RECORD_ID = re.compile(r'\b(\d{3}-\d{2}-\d{4}|\b\d{7,9}\b|grade[:=]|score[:=]|GPA|DOB|date of birth)\b', re.I)
PUBLISHED_REGION = re.compile(r'data-context=["\'](showcase|byline|masthead|credits)', re.I)

def classify_pii(html, is_public_class):
    names = find_name_like(html)              # existing heuristic
    if not names: return None
    has_record_id = bool(RECORD_ID.search(html))
    in_published   = bool(PUBLISHED_REGION.search(html))
    # two-signal + context + class gate
    if has_record_id and not in_published and not is_public_class:
        return ("VIOLATION", "high", "name co-occurs with a record identifier outside a published region")
    return ("NEEDS-REVIEW", "low",
            "names present but no record identifier / inside a published byline — verify consent, do not block")
```
Run against today's file, the Lumière showcase returns **NEEDS-REVIEW / low** — a note to confirm consent, not a CRITICAL. Exactly right.

## What to ratify (founder call)
- **Adopt the tier model** (NOTE/ADVISORY/BLOCK) and the VIOLATION vs NEEDS-REVIEW split in `studio-eyes-sweep.py` + `one-thing-gate.py`, and wire it into `.github/workflows/floor.yml` so the full eyes run server-side on every push.
- **Adopt the corrected PII classifier** (two-signal + context + class gate) — this is the direct fix for the miss that started this.
- **Turn on precision self-scoring** — the scoreboard that keeps the eyes honest.
- Poka-yoke, baseline/ratchet, suppression-with-provenance, runbook-per-finding: adopt as the scaffold and CI mature.

*The lesson, kept: fire only where you'd stake the line's trust; design the rest of the errors out; let a human own everything that isn't arithmetic.*
