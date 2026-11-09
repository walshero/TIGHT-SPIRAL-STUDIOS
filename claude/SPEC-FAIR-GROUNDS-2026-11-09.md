# SPEC: Fair Grounds (Lab) - 2026-11-09

A midway of critical-thinking booths. Each booth teaches one skill with one carnival mechanic.

## Founder words (primary source, verbatim)
> "I really want to imagine carnival games beyond dunk tank. EG a fact/opinion sorter that gives you strength in a strongman/bell game. Next theres a balloon darts game where the balloons are different types of fallacies and you have to correctly ID and pop what the barker prompts."
> "Let's call it Fair Grounds and start with strong man"

## Booths
| Booth | Skill | Status |
|---|---|---|
| Strongman | Checkable claim vs judgment vs both | BUILT v0.1, `lab/fair-grounds-strongman.html` |
| Balloon Darts | Spot the named fallacy in a line (barker calls it, pop the balloon whose line commits it) | Founder idea, next candidate |
| Midway Gallery | Everything at once: the runoff (`lab/dunk-o-rama.html` v1.1) | BUILT, Lab |
| Fortune Teller | Barnum statements (vague claims that fit anyone) | Proposed, not ruled |
| Hall of Mirrors | Misleading charts | Proposed, not ruled |
| Shell Game | Tracing a quote to its source | Proposed, not ruled |
| Milk Bottles | Argument structure (knock out the weak premise) | Proposed, not ruled |
| Prize booth | Tickets traded for trick cards (Writerly Moves style) | Proposed, not ruled |

## Strongman v0.1
- Eight claims per round (3 checkable, 3 judgment, 2 both), from a 34-claim town-fair bank; no repeats until the bank runs out.
- Sort by button, arrow key / 1-2-3, or swipe (left checkable, right judgment, up both).
- Each right call adds muscle; the hammer head grows. Feedback names the checkable part and the judgment part of every "both" claim.
- One swing: muscle sets the ceiling, a timing meter adds the last quarter. Only 8 of 8 can ring the bell. Low swings get a bell that is not impressed.
- Teaching line carried in two claims and the clean-round note: checkable does not mean true.

## PENDING (founder's call)
- Whether Dunk-O-Rama's runoff is renamed into Fair Grounds (for example, Fair Grounds: Midway Gallery).
- Booth order after Strongman.

## Strongman v0.2 (2026-11-09): writing rule for the claim bank
Founder, on "The fair is way too loud": "Couldn't you check decibels and town ordinance."
Rule for every judgment item: if a sharp player could name a standard (an ordinance, a policy, a measure) that makes it checkable, the item is arguable and does not ship as scored. Split it: a judgment tied to the person ("too loud to enjoy") and a checkable claim that names the standard ("breaks the town noise limit of 70 decibels after 10 p.m.").

## Strongman v0.3 (2026-11-09): screen 1 is the booth
Founder: "Strong man fails the image to text open screen ratio. We don't need content on screen 1."
Screen 1 shows the booth alone (tower, bell, barker, hammer, the puck hopping on its own) and one button, Step right up. Measured on first paint: text and controls cover 9% of a 390x844 phone, 7% of a 1280x800 desktop, 16% at large-text zoom (260x560).

## Strongman v0.4 (2026-11-09): College set
Founder: "Ok, that's the basics of the game. Now, let's create a set for college level."
- 36 claims (12 checkable, 12 judgment, 12 both) beside the 35-claim Town fair set. Same round: 3 / 3 / 2.
- Material: research findings and statistics, correlation vs cause, predictions, hedged claims, expert consensus, claims about what a source argues, interpretation of literature, value rankings.
- Bin subtitles in the College set: look it up / split it / argue it (the composition-class distinction between a fact and an arguable claim).
- Switch: menu button "Claims: ..." or "Try the college set" at the end of a round. `#college` in the URL opens straight to it. The choice is remembered.
- Rule pass: judgments avoid too, enough, unreasonable, worth, healthy; where a policy could exist (plagiarism penalties, data-sharing mandates) the feedback names it as a different, checkable claim.
