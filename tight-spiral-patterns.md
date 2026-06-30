# Tight Spiral Studios — Pattern Library

*Proven mechanisms graduated from the Confluence trunk (through v33) into reusable studio capital. Each pattern is paste-ready: it carries the real code, **where it goes**, **why it works**, and an **accessibility note**. Confluence is the R&D bench; patterns earn their way into this file by shipping there first. Portable by design — plain Markdown, no tool dependency.*

*Companion to the Studio OS. The OS says the rule; this file gives the recipe.*

---

## How to use this file

Every build pulls FROM here; nothing re-derives a solved problem. When a pattern proves out in a future build, fold it in (don't start a new file). Same shape as the lab cards: a live mechanism, the one knob, and one line on where it goes.

Two hard floors still sit above everything (OS §3.1): **no emoji, ever**, and **accessibility is a design floor**. A pattern that ever conflicts with those loses.

---

## 1. Overlay Frame Guarantee

**The rule (OS §3.1):** no overlay clips its own controls. A button the user can't reach is a hard fail, not cosmetic — it dead-ends the user. Must survive zoom to 200%+.

**Where it goes:** every pop-up, modal, dialog, chooser, or tour with executable buttons.

**Why it works:** an unbounded modal grows with its content and pushes the action row below the fold; on a phone or at high zoom the user scrolls but the Next/Done/Close button is already off-screen. The fix bounds the card, scrolls the *body* inside the frame, and pins header + footer so the actions never move.

**Accessibility note:** this is the single most-repeated RP failure in studio history — Confluence shipped a tour whose Next button slid off-frame at the founder's screen size (v31 fix). Once is enough. The 90vh cap, internal body scroll, and `flex-shrink:0` on the action row are non-negotiable.

```css
/* The bounded-flex overlay shell. Cap height, scroll the body, pin the rest. */
.overlay-card{
  max-width:580px; width:100%;
  max-height:90vh;                 /* never taller than the viewport */
  display:flex; flex-direction:column;
  overflow:hidden;                 /* the CARD never scrolls; its body does */
  border-radius:4px; margin:auto;
  background:var(--surface); color:var(--ink);
  box-shadow:0 16px 48px rgba(0,0,0,.4);
}
.overlay-card-hd{ flex-shrink:0; padding:1.1rem 1.35rem; }   /* pinned top */
.overlay-card-body{                                          /* the ONLY scroller */
  flex:1 1 auto; min-height:0;     /* min-height:0 lets flex children scroll */
  overflow-y:auto;
  padding:1.25rem 1.35rem; line-height:1.75;
}
.overlay-card-ft{                                            /* pinned bottom */
  flex-shrink:0; padding:.85rem 1.35rem;
  border-top:1px solid var(--border);
  display:flex; gap:.5rem; background:var(--surface-2);
}
```

```html
<div class="overlay-card">
  <div class="overlay-card-hd">…title…</div>
  <div class="overlay-card-body">…long content scrolls here…</div>
  <div class="overlay-card-ft">
    <button class="btn btn-p">Continue</button>
    <button class="btn btn-g">Close</button>
  </div>
</div>
```

**The two lines that do the work:** `min-height:0` on the body (without it, flex refuses to shrink the child and the scroll never engages) and `flex-shrink:0` on header + footer (so they hold their size and the body absorbs all overflow).

**Sticky-footer variant** (when the card is itself a scroll container rather than a flex column — e.g. a bottom sheet):

```css
.sheet{ max-height:90vh; overflow-y:auto; }
.sheet-actions{ position:sticky; bottom:0; flex-shrink:0;
  background:var(--bg); z-index:2; }   /* rides the bottom edge as content scrolls */
```

---

## 2. Radial Navigation — central-vision-first

**The rule (new, RP primitive):** one predictable shape with orbital positions beats controls scattered to the corners. Offer this as the navigation pattern for any build with more than a handful of destinations.

**Where it goes:** multi-section builds. A single fixed "Navigate" control opens a full-screen ring; every section is a large orbital node around a center "you are here" hub. Mirrors OVER existing routing — the original nav stays untouched as the assistive-tech fallback (`#rnavList` parallel links).

**Why it works:** central vision loss makes corner-scattered controls a hunt. Orbital nodes on one ring are spatially predictable: the user learns the shape once. Arrows rotate focus, Enter opens, Escape/backdrop closes, focus returns on close.

**Accessibility note:** never color-alone — each node carries glyph + label + position + `aria-current`. High-contrast and reduced-motion safe. Large targets (`min-height:3.4rem`, `8.2rem` wide). Keep the flat `<ul>` of real links present for screen readers; the wheel is the sighted-navigation layer over it, not a replacement.

```css
.rnav-overlay{
  position:fixed; inset:0; z-index:200; display:none;
  align-items:center; justify-content:center;
  background:rgba(8,20,28,.94); padding:1rem;
}
.rnav-overlay.open{ display:flex; }
body.a11y-contrast .rnav-overlay{ background:#000; }

.rnav-stage{                       /* square, viewport-bounded, never clipped */
  position:relative;
  width:min(86vmin,640px); height:min(86vmin,640px);
  max-width:96vw; max-height:86vh;
}

/* each node is a REAL button placed by JS — large target, glyph + label */
.rnav-node{
  position:absolute; transform:translate(-50%,-50%);
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  gap:.25rem; text-align:center;
  width:8.2rem; min-height:3.4rem; padding:.55rem .5rem;
  background:#13586B; color:#fff; border:2px solid rgba(255,255,255,.55);
  border-radius:14px; cursor:pointer; font:600 .92rem/1.15 inherit;
  box-shadow:0 2px 10px rgba(0,0,0,.32);
}
.rnav-node[aria-current="true"]{ outline:3px solid #ffd24a; outline-offset:2px; }
```

```javascript
/* Place N sections evenly on the ring; build a parallel real-link list for AT. */
function buildWheel(sections, stage, listEl){
  var cx=50, cy=50, R=38;                 // percentages of the square stage
  sections.forEach(function(s, i){
    var ang = (i / sections.length) * 2*Math.PI - Math.PI/2;  // start at top
    var px = cx + R*Math.cos(ang);
    var py = cy + R*Math.sin(ang);
    var b = document.createElement("button");
    b.type="button"; b.className="rnav-node";
    b.style.left=px+"%"; b.style.top=py+"%";
    b.setAttribute("data-id", s.id);
    b.setAttribute("aria-label", s.label);
    b.innerHTML='<span class="rn-glyph" aria-hidden="true">'+s.glyph+'</span>'
              + '<span class="rn-label">'+s.label+'</span>';
    b.addEventListener("click", function(){ choose(s.id); });
    stage.appendChild(b);
    // parallel real link for assistive tech — NOT optional
    var li=document.createElement("li");
    var a=document.createElement("button");
    a.type="button"; a.textContent=s.label;
    a.addEventListener("click", function(){ choose(s.id); });
    li.appendChild(a); listEl.appendChild(li);
  });
}

/* Keyboard: arrows rotate focus, Enter opens, Escape closes, focus returns. */
function onKey(e, nodes, state){
  if(e.key==="Escape"){ e.preventDefault(); rnavClose(); return; }
  if(e.key==="ArrowRight"||e.key==="ArrowDown"){
    e.preventDefault(); state.i=(state.i+1)%nodes.length; nodes[state.i].focus();
  } else if(e.key==="ArrowLeft"||e.key==="ArrowUp"){
    e.preventDefault(); state.i=(state.i-1+nodes.length)%nodes.length; nodes[state.i].focus();
  } else if(e.key==="Home"){ e.preventDefault(); state.i=0; nodes[0].focus(); }
  else if(e.key==="End"){ e.preventDefault(); state.i=nodes.length-1; nodes[state.i].focus(); }
}
```

**On open:** stash `document.activeElement`, open, focus the current section's node. **On close:** restore that focus. The wheel is a layer, not a destination — it never strands the user.

---

## 3. No Spatial Pointers in Copy

**The rule (new hard-floor copy rule):** never tell the user where a control is on screen. No "the button in the lower-left," no "the menu at the top right," no "scroll down to find." Action-based phrasing only.

**Where it goes:** every line of user-facing copy, hints, empty states, tour text, error messages.

**Why it works:** screen-location language assumes the reader can locate by position — exactly what RP makes unreliable. "Reopen the chooser" works for everyone; "reopen it from the lower-left" works only for someone who can scan the lower-left. (Confluence v32 retired a "...lower-left" hint for this reason.)

**Accessibility note:** developer-facing comments in code may use layout terms freely. This rule is about what the *user* reads.

| Don't write | Write instead |
|---|---|
| "Tap the menu in the top-right corner." | "Open the menu." |
| "The replay control is below the animation." | "Replay the animation." |
| "Scroll down to the Continue button." | "Continue when you're ready." |
| "Find the settings in the lower-left." | "Open settings." |

Name controls by what they *do*, and keep the name stable through the whole flow (OS / frontend writing: the button that says "Publish" produces a toast that says "Published").

---

## 4. Texture-Not-Color-Alone for Distinction

**The rule (WCAG 1.4.1, generalized from cut-paper):** carry visual distinction in geometry and texture, not in hue. The thing must still read apart in grayscale and under color-vision deficiency.

**Where it goes:** any set of marks the user must tell apart — chart series, nested rings, status indicators, categories, map regions.

**Why it works:** color-alone distinction fails for color-blind users and disappears in grayscale or high-contrast mode. Texture (dot / solid / diagonal / grid / stipple) and geometry (radius, nesting, shape) survive every one of those. Color is then freed for beauty and warmth instead of carrying the whole load. (Confluence v30 reworked its nested rings to carry distinct texture per ring on an expressive palette — color for beauty, texture for legibility.)

**Accessibility note:** this is the data-viz sibling of the studio's "suggest, don't simulate" art rule. It also pairs with status indicators: a status must never be color-alone — pair every state with a glyph or word (check / teardrop / dashed ring / triangle), as in the Confluence goal chips.

```css
/* SVG fill patterns: distinction that survives grayscale + CVD. Define once, reuse. */
/* <defs> goes once in your SVG: */
/*
<pattern id="tx-dot"  width="6" height="6" patternUnits="userSpaceOnUse">
  <circle cx="3" cy="3" r="1.3" fill="currentColor"/></pattern>
<pattern id="tx-diag" width="6" height="6" patternUnits="userSpaceOnUse">
  <path d="M0,6 L6,0" stroke="currentColor" stroke-width="1.4"/></pattern>
<pattern id="tx-grid" width="6" height="6" patternUnits="userSpaceOnUse">
  <path d="M0,0 H6 M0,0 V6" stroke="currentColor" stroke-width=".8"/></pattern>
*/
/* then: <circle ... fill="url(#tx-dot)"/>  — texture distinguishes, color decorates */
```

**Status pattern (never color-alone):**

```html
<span class="status status-met">     <span aria-hidden="true">✓</span> Met</span>
<span class="status status-progress"> <span aria-hidden="true">◐</span> In progress</span>
<span class="status status-notyet">   <span aria-hidden="true">○</span> Not yet</span>
<span class="status status-flag">     <span aria-hidden="true">△</span> Needs review</span>
```

(Word + glyph + color, in that priority order. "Needs review," never "flagged" — the latter carries surveillance tone.)

---

## 5. Skins as Stances — multiple visual themes over one structure

**The rule (theming pattern):** offer two or three named visual skins over a single structure, switchable from the accessibility panel. Skins change palette and feel, never layout or logic.

**Where it goes:** builds where a visual register choice is itself meaningful — a calm read vs. a high-energy read vs. a high-contrast read — or simply where the user benefits from picking the look that's easiest on their eyes.

**Why it works:** one structure, several palettes, means accessibility (high-contrast) and expression (a warm vs. cool feel) are the same mechanism, not a bolt-on. The switch lives in the a11y panel so the person who most needs it finds it where they look for accessibility, not buried in decoration. (Confluence runs Xenos / Tron / Luminocity as three skins on one accordion, v22/v24.)

**Accessibility note:** the high-contrast floor always wins — `body.a11y-contrast` overrides any skin. A skin can be pretty; it can never undercut contrast, focus rings, or legibility. Announce the change via a live region so a screen-reader user knows the skin switched.

```css
:root{ /* default skin tokens */
  --bg:#f7f6f2; --surface:#fff; --ink:#1c1c1e; --accent:#1a4a35;
}
body.skin-cool { --bg:#eef4f6; --surface:#fff; --accent:#13586B; }
body.skin-warm { --bg:#fbf6ee; --surface:#fffdf8; --accent:#8a5c00; }

/* the floor that always wins, regardless of skin */
body.a11y-contrast{ --bg:#000; --surface:#000; --ink:#fff; --accent:#fff; }
body.a11y-contrast *{ border-color:#fff !important; }
```

```javascript
function setSkin(name){
  document.body.className = document.body.className
    .replace(/\bskin-\w+\b/g,'').trim() + ' ' + name;
  // sync any duplicate toggle sets, then announce
  a11yAnnounce('Visual theme changed to ' + prettySkin(name) + '.');
}
function a11yAnnounce(msg){           // one shared live region, used everywhere
  var live = document.getElementById('a11yLive');
  if(live){ live.textContent = msg; }
}
```

```html
<!-- one polite live region near the top of <body>, reused by every announce -->
<div id="a11yLive" aria-live="polite" class="sr-only"></div>
```

---

## 6. In-File Changelog — the canonical-trunk discipline

**The rule (OS §3.3, given a format):** the source file IS the truth; everything else is archive. One trunk, edited in place, no branching. Every multi-version single-file build carries its own changelog at the very top, newest entry first.

**Where it goes:** the top of every build that will see more than one version — as an HTML comment (so it ships inside the single file and can never be separated from the code it documents).

**Why it works:** a single-file offline build has no repo, no commit history, no external record. The changelog is the *only* memory the file has. Put it anywhere but inside the file and one lost download erases the history — which nearly happened to Confluence (v18–v23 had to be reconstructed from memory at v24, the first real entry). Bump a visible version string (a header eyebrow or About box) on every ship so you can tell at a glance which build you're holding.

**Accessibility note:** none — this is process, not interface. But it protects the founder's scarcest resource (attention) by making "which version is this?" answerable in one second.

```html
<!DOCTYPE html>
<html lang="en">
<!--
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [BUILD NAME] — IN-FILE CHANGELOG
  Canonical trunk. Edit in place, no branching. Bump the version on ship.
  Newest first.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  v3 (YYYY-MM-DD)
    - WHAT CHANGED: one line per change, in plain terms.
    - WHY / SEAT: which panel seat or rule drove it (TI / RP / PM / Archivist…).
    - HOUSEKEEPING: version string bumped vN-1 -> vN.
  v2 (YYYY-MM-DD)
    - …
  v1 (YYYY-MM-DD) — first ship.
-->
```

**Entry shape that works:** name the change, name the *seat or rule* that drove it (so the reasoning travels with the change), and log the version-string bump as its own housekeeping line so it's never forgotten.

---

## 7. Tiered Depth — flOw descent

**The rule (OS §3.1, §6).** Minimal at the surface; the reader descends only as far as they want; every ring reversible. Player-chosen depth, not system-imposed (Jenova Chen's flOw: the player picks how deep to go). Used for game meta-layers ("show the engine") and governance surfaces (human-in-the-loop decision cards) alike.

**Where it goes.** Any place that must be simple for a first reader but deep for a curious one: engine/meta layers, decision surfaces, "why am I being asked this" context.

**Why it works.** A binary toggle is a switch, not a descent — it dumps everything or nothing. Rings let the surface stay bare while depth is one tap away and always climbable. Honors Scot's gate (no jargon on the surface) and the founder's one-decision-per-screen floor at once.

**Accessibility note.** Each descend/climb control is a real 44px button with `aria-expanded`; ring containers toggle `hidden`; scroll moves to the opened ring, climb returns to top. Never hide readable content behind hover.

```javascript
function wireDescend(btnId,ringId){var b=document.getElementById(btnId),r=document.getElementById(ringId);
  b.addEventListener('click',function(){var o=r.hidden;r.hidden=!o;b.setAttribute('aria-expanded',String(o));
  if(o)r.scrollIntoView({behavior:'smooth',block:'nearest'});});}
```

---

## 8. Maslow-descent — flOw levels with a brake

*Canonical home for this mechanic. The OS (§7 shorthand, §10 decision log) and any project map point here rather than restating the math — this is the one complete copy.*

**The rule (OS decision 2026-06-27).** A hierarchy the player is *pulled down* — the force acts on them (e.g. rhetoric reaching for them) — where descent is the cost and **noticing is the brake/climb**. Start at the top (own footing); the pull sinks you toward the leadable floor; catching the gap arrests the fall.

**Where it goes.** Any game where an external force acts on the player and the lesson is to *notice it acting*. First instance: Choose Your Leader.

**Why it works.** flOw's levels carry drama because descending costs something and the player has a brake. Mapping a need-hierarchy to depth turns an abstract construct (susceptibility) into a felt consequence.

**The five rungs (top = your own footing, bottom = the leadable floor).**

| Rung | Means | 
|---|---|
| 5 | Your own judgment — becoming who you could be |
| 4 | Standing, respect, a voice |
| 3 | A people, a side, a we |
| 2 | Safety — survive the threat |
| 1 | The floor — where consent stops mattering |

**The math (canonical — matches the shipping build).** Two trust readings: `t1` = blind trust (quote alone, before the record), `t2` = informed trust (after the record turns). The gap between them is the measure of noticing; you never ask the player to rate themselves.

```javascript
var delta = t1 - t2;                         // how much the record moved you
var pull  = t1 - 1;                          // more blind trust = more pull down
var brake = Math.max(0, delta);              // trusting LESS once informed = noticing
var tier  = Math.max(1, Math.min(5, 5 - pull + brake));  // start high, fall by pull, climb by brake
var noticed = delta > 0;                     // did you catch the gap at all?
```

Read it plainly: you start at the top (5). The pull subtracts how far the rhetoric reached for you. The brake adds back what you reclaimed by noticing. Clamp to 1–5. `noticed` is the yes/no the end-arc reports per scene.

**The three trauma-informed rails (law — clears the TI HALT).**
1. **Consequence lands on the force's reach, never the player's worth.** The floor copy says "this is how far rhetoric can carry a person," not "you failed."
2. **The brake is always live; naming the gap is the win even at the floor** — the floor is never a dead end (freedom to fail). If you land at the bottom but noticed on the way, the game says so plainly.
3. **The deep ending teaches** ("how far this can carry a person"), never gotchas.

**Accessibility note.** The landing tier must be announced as text, not communicated by the lit rung alone (color/fill is not a sole signal) — an `aria-live` line states "level N of 5 — [rung name]. You caught / did not catch the gap." (Pairs with §4, texture-not-color-alone.)

---

## 9. The Transfer Move — the exit invitation

*Added 2026-06-27 (McGonigal review). The pattern that keeps a game from stopping one sentence short of mattering.*

**The principle.** A skill the player practiced inside the game only counts if it fires *outside* the game. The transfer move is the bridge: on the way out, the game hands the player **one concrete, optional, real-world action** — an invitation, never homework, never a quiz, never gated. It is where post-game agency lives and where "Play. Notice. Design." actually closes: the player *designs* their own next move in real life.

**The rules.**
1. **One line. One action.** Not a list, not a worksheet. The whole game compressed into a single thing to *do*.
2. **Optional and unscored.** It is offered, not assigned. No tracking, no "did you do it," no return loop. (Tracking it would make it homework and break the invitation.)
3. **Concrete and real-world.** Names a specific situation the player will actually be in. Not "be more critical of media" (a value) but "next televised address you watch — wait eight days before you trust it" (an action in a real moment).
4. **In the house voice.** Stated flat, trusts the player, no bow. It can be quiet.
5. **Last beat, after the payoff.** It comes after the arc/result screen, on the way out the door — not mid-play, where it would interrupt the world.

**Why it's a pattern, not a CYL one-off.** Every teaching game has an outside-the-screen target behavior. The transfer move is the reusable shape of the handoff. A build that ends without one hasn't finished honoring its own teaching.

---

## 10. The Open Mode — fence the blank page

*Added 2026-06-27 (Cleese review). Not a build pattern — a process pattern, for how generation is protected from judgment.*

**The principle.** Creativity happens in the *open mode* (playful, unhurried, willing to be wrong for an afternoon) and dies in the *closed mode* (narrow, anxious, decisive). A review panel — any set of critics with the power to stop work — is pure closed mode. So generation must happen in a **fenced space where nothing can be stopped**, before any critic convenes.

**The shape.**
1. **Pipeline Stages 0–2 are panel-free of all hard powers.** No HALT, no BAIL, no SCOPE HALT until there's a draft (Stage 3).
2. **The only seat allowed in the fence is a no-power generative one** (the Possibilist — "yes, and what if it were stupid?"). Its powerlessness is the point: the open mode collapses the instant it feels judged, so the generative seat must never be able to judge.
3. **Diagnose-and-fix is closed mode** and belongs at Stage 3+. *What-if-it-were-stupid* is open mode and belongs at 0–2. **Don't let them touch.**
4. **Simplify the convening.** Most builds need five seats and a duck, not the full roster. A clutter of critics is itself an accessibility problem — the same friction as a cluttered interface.

**The failure it prevents.** Answering "the panel is all critics, the work is a little dead" by hiring *cleverer critics*. More authority is still closed mode. The fix is a protected blank page, not a better-read courthouse.

---

## Boundary — what stays in Confluence and does NOT graduate here

These are Confluence-specific and must not be pulled into general builds (they'd drag project machinery into games that don't need it):

- **ConfluenceFields / calibration-drift / score-from-anchor** — assessment-measurement substrate, project-specific.
- **The SLO Coordinator Guide and MassBay annual-report form** — institution-specific content.
- **FERPA data hooks and the FERPA HALT** — only live when real student data is in play; not a default-build concern.
- **The water/confluence house language** (tributaries, rivulets, channel) — Confluence's identity, not the studio's.

The test: a pattern graduates only if it's *mechanism* (how to keep a button reachable, how to navigate by ring, how to distinguish without color). It stays home if it's *content* (what an assessment measures, what a form requires).

---

*End of Pattern Library. Fold new proven patterns in rather than starting a new file. When in doubt, the two hard floors win: no emoji, accessibility is a design floor.*
