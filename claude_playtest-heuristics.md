# PLAYTEST HEURISTICS — the standing regression ledger

*The Playtest Table re-runs these FIRST on every player-facing build (`claude_seat-playtesting-agents.md`, improvement D). "Provenance is the content" (`studio-eyes-two-layers.md`): each firing check is dated, attributed to the persona that caught it, and carried forward. A catch on build N is a standing check on build N+1. No emoji; every row is a yes/no check.*

## How to use
Before a build reaches the founder's cold play, walk this list. Each row = a question with a yes/no answer. A NO is a Ledger-A HALT-class check for that build. Add a row whenever a new persona catch fires; never delete a row (retire with a dated note if a class is proven impossible).

## The ledger (newest catches appended)

| # | check (answer yes to pass) | class | first caught | persona |
|---|---|---|---|---|
| H1 | Are the scene's "tap the room" affordances REAL in-scene hotspots (not text chips in a panel under a static picture)? | presentation | 2026-07-26 · CYL v5 | Cold Newcomer, RP, Mobile, Craft |
| H2 | Does every referenced object stay visible in PORTRAIT (no `preserveAspectRatio="slice"` amputating edges; referenced objects inside the safe band)? | mobile / a11y | 2026-07-26 · CYL v5 | Mobile-One-Hand |
| H3 | Is the core verb reachable in the first screen / first touch (no title+prelude wall before it)? | entry | 2026-07-26 · CYL v5 | Cold Newcomer |
| H4 | Is there NO dead code promising a feature the build doesn't render (e.g. an orphaned "descent" rig, unused icon set, computed-but-never-shown tier)? | integrity | 2026-07-26 · CYL v5 | Cold Newcomer, Craft |
| H5 | Is a selected/pressed state signalled by MORE than hue (inset check / solid fill / inset border), never color alone? | RP / a11y | 2026-07-26 · CYL v5 | RP Reader |
| H6 | Is atmosphere motion (glow flicker, pulse) OFF by default / opt-in, so it never glares an RP reader? | RP / a11y | 2026-07-26 · CYL v5 | RP Reader |
| H7 | Are orientation labels and source lines ≥1rem and not tiny-uppercase-tracked (size, not just contrast)? | RP / a11y | 2026-07-26 · CYL v5 | RP Reader |
| H8 | For a pre/post instrument: is the "blind" reading LOCKED once the record/reveal is seen (no Back-path overwrite after exposure)? | measurement integrity | 2026-07-26 · CYL v5 | Craft/Reception |
| H9 | Does the pre-reveal framing avoid telegraphing the reveal (no "reach" line that manufactures the delta the record will spring)? | honesty | 2026-07-26 · CYL v5 | Craft/Reception |
| H10 | Does the reveal operate on the quality the player actually rated (reconsolidation), not swerve to an un-rated adjacent fact? | craft / reception | 2026-07-26 · CYL v5 | Craft/Reception |
| H11 | Are all interactive targets ≥44px AND reachable one-handed (not stranded in top corners); is `env(safe-area-inset)` handled? | mobile / a11y | 2026-07-26 · CYL v5 | Mobile-One-Hand |

## Standing PASSES (do not re-litigate unless the build changes them)
- Instrument fairness for pre/post: identical wording blind vs post; ipsative to the player's own prior; no grade, no gotcha. (CYL v5, Craft — PASS 2026-07-26.)
- Focus ring present and consistent; sound opt-in/off-by-default; nav present every screen; scroll resets on screen change; token-role law (no text on atmosphere). (CYL v5 — PASS 2026-07-26.)
