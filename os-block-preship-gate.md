# OS BLOCK — THE PRE-SHIP GATE + TOKEN-ROLE LAW (§14)

*Locked 2026-07-10. Minted from a session where the founder walked a build and found
"light yellow on white — three modes, all fail." The auditor existed. Nobody ran it.
This block turns that from a tool into a practice.*

---

## §14.1 THE TOKEN-ROLE LAW (the root cause, generalized)

**Light may be dim. Text may not.**

A color token may serve as *atmosphere* (room-light, screen-rim, border, gradient,
fill) **or** as *text* — **never both.** The CYL failure was one token, `--glow`, doing
double duty: it was the warm Kodachrome rim of a 1962 television AND the color of every
caption and label. Atmosphere is *allowed* to be low-contrast — that is what makes it
atmosphere. The instant that token carries a word, the word inherits the dimness.

**Enforcement:** any token used in both a `color:` declaration and a
background/border/fill/gradient/stroke declaration is a **HALT**. Split it: give the
text its own bright token (`--label`, `--brake-ink`, `--pull-ink`) and let the
decorative token stay dim.

**Corollary — buttons:** a button surface token (`--accent`) carries only its own ink
token (`--accent-ink`). Body text never lands on a button. Pair them explicitly.

**Corollary — literals hide bugs:** a hardcoded `color:#12100a` on a var-driven
background escapes token auditing. Text colors ride tokens, always, so the gate can see
them.

---

## §14.2 THE PRE-SHIP GATE (mandatory, not optional)

`preship-contrast-gate.py` (repo root; Drive Claude_files) runs **before every
present_files, every deploy, every hand-off. No exceptions.**

```
python3 preship-contrast-gate.py <file.html>
exit 0 = PASS (safe to ship)    exit 1 = HALT (do not ship)
```

It performs three checks:
1. **WCAG per comfort mode** — every text token against every surface it actually
   lands on, in *every* mode (default / softer / warm). Floor 4.5 body, 7.0 AAA target.
2. **Dual-role tokens** (§14.1) — text riding a decorative color.
3. **No pure #fff / #000** as any token value.

**The law:** a file that has not passed the gate does not reach the founder. Not as a
draft, not as a "quick look," not as "I'll fix it after." The gate is in the critical
path or it is theater.

**Proven 2026-07-10:** the gate HALTed the CYL slice **twelve times** across two tuning
passes — catching `--glow` (the founder's bug), plus `--brake` and `--rule` dual-roles
that eye-inspection missed entirely. Final: 0-HALT, worst pair 4.76:1, all three modes.

---

## §14.3 WHY EYE-INSPECTION ALWAYS FAILS HERE

Reading hex codes and imagining the result is not auditing. Across this session the
same amber-as-text bug survived three separate "checks" by inspection and died
instantly to arithmetic. **Contrast is a computation, not a judgment.** Any claim that a
palette "passes" without a computed ratio is a guess wearing a verdict's clothes.

The founder has retinitis pigmentosa. Contrast cannot be a step someone remembers.

---

## §14.4 THE NAMED FAILURE MODE: SPEC-RICH, BUILD-POOR

Diagnosed this session, recorded so it stops recurring.

The studio ships governance faster than product. CYL v5 spec was written 2026-06-28. By
07-10 the studio had shipped a standing crew, a lab wing, a harvest engine, ten
consultants, a Drive atlas, and two OS blocks — **and zero playable CYL.** The
governance layer eats the build layer.

**The check:** at every belt close, name what a *player* can now do that they could not
before. If the answer is "nothing, but the pipeline improved," the session was
build-poor. Two consecutive build-poor belts = the next session is a build session, no
new governance permitted.

**The corrective that worked:** stop waiting for the perfect complete game. Ship a
**vertical slice** — one scene, every beat, end to end, art and sound included. Blocked
content (living-president scenes) becomes "Chapter 2, when sourced," not a ship blocker.

---

## §14.5 THE DEPLOY LANE (proven, standing)

Container git-push. Proven byte-exact twice (The Tell 07-08; CYL slice 07-10, commit
`4f25f4a`, md5 b3d129a0, 38,721 B live = local).

```
git clone https://walshero:<PAT>@github.com/walshero/TIGHT-SPIRAL-STUDIOS.git
cp <file> . && git add && git commit && git push origin main
curl raw.githubusercontent.com/.../<file>  →  md5 must match local   ← POST-TICK
```

**Order is law:** GATE (§14.2) → push → POST-TICK md5. A push without a byte-verified
fetch-back is not a ship. "Pushed" is never proof, exactly as "created:true" is never
proof.

**PAT never persists** — lives in the chat only, re-pasted per session, revocable at
GitHub → Settings → Developer settings → Fine-grained tokens. Never written to memory
or any file.

**Ship-gate still governs:** live at the URL for cold play ≠ linked from index.html.
The student front door requires GATE 1 (founder cold play) + GATE 2 (Studio Eyes).

---

## §14.6 WHAT THE GATE STILL OWES

Named honestly so it isn't mistaken for finished:
- **Render-proof.** The gate computes; it does not *look*. Text over a gradient, over
  an image, or a focus ring against a lit surface still escape it. A rasterize-and-
  inspect pass is the next tier.
- **Palette-mount enforcement (§12.6).** The manifest declares each lane's floor; the
  gate does not yet read it. Until it does, "arcade palette leaked into the instrument"
  remains possible.
- **Per-device mode.** `prefers-color-scheme: dark` and `forced-colors: active` are not
  yet simulated. The EN195 charcoal-on-black bug lives in this gap.
