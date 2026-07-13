# PLAYTEST INSTRUMENT — Build Spec
**Tight Spiral Studios · single-file offline build · for an external builder with no studio context**

This document is self-contained. You do not need to know the studio, the founder, or any
prior file to build from it. Every decision is already made. Where a rule looks arbitrary,
it is a hard floor — build to it exactly; do not "improve" it. The one judgment that is NOT
yours is the final accessibility verdict (see §9): you build to spec, the founder's own eyes ratify.

Build it as one file: `playtest-instrument.html`. No external assets, no network calls, no
build step. It must open by double-click and run fully offline, on a phone, forever.

---

## 0. WHAT THIS IS

A studio-wide **playtest instrument**: a reusable rig that any of the studio's games plugs
into so playtesting is consistent and nobody rebuilds it per game. Three parts in one file:

1. **Sight / Sound / Motion** — a three-channel sensory check. A build under test is rated
   on what the eye reads, what the ear catches, and whether motion helps or distracts.
2. **"Who Are You" dashboard** — a shared player-identity panel any game can call, so player
   context is gathered once, the same way, every time.
3. **Tagged Input/Output form** — captures playtest responses. Every field that gathers data
   wears a visible **tag** stating *what* it gathers and *why*. Data is gathered only where it
   is genuinely useful, never by default.

**The one structural surprise (the novelty, required):** the form *labels its own data-gathering
moves out loud.* Most forms hide why they ask. This one annotates every input with a plain-language
tag — "gathering this because…" — so the act of collection is transparent to the person filling it.
Transparency is the mechanic, not a disclaimer bolted on.

---

## 1. HARD FLOORS — non-negotiable, all must pass

Build to every one. A build that violates any of these is not shippable, regardless of how good
the rest is.

**Data path (the most important one):**
- **On-device only. Nothing transmits. Nothing is stored across sessions. No network calls of any kind.**
- All responses live in JavaScript memory for the session and vanish on close.
- Output happens by **Carry-Out**: the person taps a button, the instrument emits a plain-text
  block, and the *person* chooses to copy it out. The instrument never sends it anywhere.
- Rationale you must respect: this is FERPA-adjacent (it may capture student playtester input).
  Until it is legally reviewed, it stays on-device. Do not add localStorage, fetch, analytics,
  cookies, or any persistence. (Note: browser storage APIs are also unavailable in this runtime —
  use in-memory state only.)

**Visibility (the founder has retinitis pigmentosa — this is the baseline, not the exception):**
- **Green is banned in any structural or primary role.** No green text, no green buttons, no
  green status fills, no green borders carrying meaning. State is carried by **position + label +
  shape**, never by color alone, and never by green. (Green is unreadable for this user.)
- Near-black ink on light paper (or full inverse), at full strength. No muted gray captions —
  differentiate secondary text by **weight or size**, never by lowering contrast.
- Large type (base ≥ 18px), 44px minimum tap targets, full keyboard navigation, visible focus
  rings, scroll-reset to the top line on every screen change, nothing hidden mid-screen or off-canvas
  at phone width.

**Comfort (3-stop, locked):**
- Provide three palettes: **Softer / Default / Warm-dark**. Warm-dark is amber-on-charcoal —
  **never pure black (#000) or pure white (#fff).**
- The comfort control is a **gold, high-contrast corner button** that cycles palettes by name.
  It is NOT a gate and NOT the first screen. Every reachable palette state must independently
  pass the visibility floor.

**Motion / engagement:**
- Default playful flourishes ON, with a **replay/re-trigger control**. Do not gate charm behind
  reduced-motion. BUT: genuine `prefers-reduced-motion` must be honored for real motion (anything
  that moves position, pulses, or animates continuously); no fast strobing ever.
- Any animation you describe, you must actually wire. No promised-but-static motion.

**Other floors:**
- **No emoji anywhere.** Ever. Use SVG shapes or text labels.
- **Provenance:** every asset (image, icon, sound) must carry a recorded legal source. Prefer
  assets you generate in-file: own SVG, and Web Audio for any sound (CC0-by-construction). No
  scraping, no "found online." If you cannot name the license, do not use the asset.
- **Single-file, offline, phone-width responsive.**

---

## 2. THE PIPELINE THIS WAS BUILT THROUGH (context for your QA, not steps for you)

The studio runs every build through a fixed pipeline. You are receiving the output of its early
stages. For your QA, the relevant ones:

- **Medium Gate:** this build is **read-clearly SVG/HTML**, not illustrative raster. Keep visuals
  legible and structural — do not push toward photorealism or decorative art.
- **Task spine:** the playtester does a real, discipline-relevant task (rate, observe, report),
  not a quiz. Rank tasks by transfer; this is an observation/judgment task.
- **Definition of Done:** §8. **The one thing it must prove (the harvest):** §10.

---

## 3. SIGHT / SOUND / MOTION — the sensory check

Three sequential channels, one decision per screen. The build-under-test is named by the playtester
up front (free text — e.g. "Choose Your Leader, opening scene").

**SIGHT screen.** Prompt: *"What did your eye go to first?"* then *"Could you read everything you
needed to?"* Capture: first-attention (free text), a legibility rating (see rating control below),
and an optional note. Tag: "gathering first-attention because the studio tests whether the eye
lands where the design intends."

**SOUND screen.** Prompt: *"Did sound help, distract, or do nothing?"* Three labeled options
(Helped / Distracted / Nothing — by **position and label, never color**) plus an optional note.
Tag: "gathering this because audio cues are easy to over- or under-use."
Include a **mute control** and respect that a playtester may have had sound off — offer a
"sound was off" path so the data isn't falsely recorded.

**MOTION screen.** Prompt: *"Did motion guide you or pull you away?"* Same three-option pattern
(Guided / Distracted / Didn't notice) plus optional note, plus a yes/no: *"Anything that looked
like it should move but didn't?"* Tag: "gathering this because promised-but-static motion is a
known studio failure mode."

**Rating control (use everywhere a rating is needed):** a 1–5 scale rendered as **five labeled,
44px+ tappable segments**, each with a visible number AND a word (1 = "couldn't" … 5 = "easily").
Selected state shown by **fill + a check shape + an aria-pressed**, never by color alone. Fully
keyboard operable, arrow-key navigable, with a clear focus ring.

---

## 4. "WHO ARE YOU" DASHBOARD — studio-wide player identity

A short, optional, reusable identity panel. The point is consistency: every game gathers player
context the same way. **Everything here is optional and skippable** — the freedom to invest effort
(or not) is a studio value; never gate progress on answering.

Fields (all optional, all tagged):
- **A name or handle to use** (free text). Tag: "so your Carry-Out is yours; stays on device."
- **What brought you here today** (free text). Tag: "context for how to read your feedback."
- **How are you feeling about this kind of thing?** — three labeled options (New to it / Comfortable
  / Skeptical), position-and-label coded. Tag: "calibrates expectations; not a test."
- **Anything I should know to read your feedback fairly?** (free text, optional). Tag: "your call
  what to share — it stays on this device."

A persistent, quiet line on every screen: **"This stays on your device. Nothing is sent. You choose
what to carry out."** This is a floor, not flavor — keep it visible.

---

## 5. TAGGED INPUT/OUTPUT FORM — the differentiator

Every input field renders with a small **tag** beneath its label: a plain sentence beginning
"Gathering this because…" The tags are the novelty. Rules:

- Tags are **always visible**, not hover-only (hover is invisible to keyboard and many low-vision users).
- Tags name a real reason. If a field has no honest "because," **cut the field** — do not invent a reason.
- Where a field is NOT gathering anything useful, do not include it. Gather only where useful.
- The tag styling: smaller and lighter-WEIGHT than the label, but **same full-contrast ink** —
  never a muted gray.

---

## 6. THE CARRY-OUT — output, on the person's terms

A single **"Carry out my playtest"** button (≥56px, gold, high-contrast, NOT at the very bottom
of a long scroll where a second monitor can hide it — place it in a sticky footer or a clearly
reachable spot). On tap:

- Assemble all in-memory responses into one **plain-text block** in a read-only textarea, pre-selected.
- Include a "Copy" button AND show the text plainly (some users copy by hand).
- Format: build-under-test name, date, the three sensory channels with ratings + notes, the
  Who-Are-You context the person provided, and a footer line: *"Emitted by the Tight Spiral
  Playtest Instrument. On-device only; this block exists because you chose to carry it out."*
- After emit, the data still only lives in memory. Closing the file discards everything.
- **No download, no mailto auto-send, no transmit.** The person copies the block by choice.

---

## 7. STRUCTURE & FLOW

- **Open on a joy-first splash**, not a gray gate and not the comfort picker. One warm line,
  a single large "Start" button, a flourish animation (wired, replayable, reduced-motion-guarded).
- Then: name the build under test → Sight → Sound → Motion → Who Are You (optional, skippable)
  → Carry-Out.
- **One decision per screen.** Scroll-reset to top on every advance. Back is always available.
- Top bar with the studio mark and the **gold comfort corner-button**.
- Never land the user on a raw text wall — every screen has a clear structure to enter by
  (a heading, a prompt, a single control).

---

## 8. DEFINITION OF DONE

Ship only when ALL are true:
- [ ] Opens offline by double-click; runs on a phone; no network calls exist in the file.
- [ ] Nothing persists or transmits; closing discards all data; Carry-Out is copy-by-choice only.
- [ ] No green in any structural/primary role; no state carried by color alone.
- [ ] All three comfort palettes pass full-contrast at every reachable state; no #000/#fff.
- [ ] No muted-gray text anywhere; secondary text differs by weight/size only.
- [ ] No emoji. Every asset has a recorded legal source (prefer in-file SVG + Web Audio).
- [ ] 44px+ targets, full keyboard nav, visible focus, scroll-reset, nothing hidden mid-screen at phone width.
- [ ] Every motion described is actually wired; reduced-motion honored for real motion; no strobing.
- [ ] Every gathering field wears a visible, honest "Gathering this because…" tag; useless fields cut.
- [ ] Who-Are-You is fully optional and never gates progress.
- [ ] The Carry-Out emits a correct plain-text block including the on-device footer line.

---

## 9. THE ONE JUDGMENT THAT IS NOT YOURS

You build to this spec. You do NOT make the final accessibility call. The founder's own eyes are
the verdict — WCAG math is the floor, not the ceiling. Build it to pass every checkbox above, then
hand it back for an eyes-on ratify. If something here trades against legibility in practice, the
founder decides, not you.

---

## 10. THE HARVEST — the one thing this build must prove

**That a data-gathering instrument can make its own collection transparent — every field saying
what it takes and why — without becoming heavier or harder to use.** If the tags make the form
feel honest rather than bureaucratic, it proved its point. That single claim is what gets recorded
when this is canonized.

---

*Spec written for handoff. Every decision pre-made per the studio's locked floors. One file:
`playtest-instrument.html`. Offline, on-device, green-free, emoji-free, Carry-Out only.*
