# Flok claims audit — PROPOSAL, awaiting founder approval

**Date:** 2026-10-17 · **Build:** `the-console.html` (Flok v35) · **Status:** PENDING. Nothing in the game has changed.
**Asked for (founder, by voice):** every Flok source must pass the CRAAP test; replace the 1950s research; tighten any claim that overreaches; founder approves wording before anything ships.

**CRAAP** = Currency, Relevance, Authority, Accuracy, Purpose. "Read" says how much of each source was checked this session.

## Summary
| Card | Current source | CRAAP | Proposed source |
|---|---|---|---|
| 1 Surprise likes | Skinner, *Science and Human Behavior* (1953) | FAIL: currency (73 years); claim "most persistent" not in it | Lindström et al., *Nature Communications* (2021) |
| 2 Infinite scroll | "Stopping-cue research"; Harris, U.S. Senate (2019) | FAIL: no study named; Senate testimony is advocacy (purpose), not research | Rixen et al., *Proc. ACM HCI* / MobileHCI (2023) |
| 3 Streak | Kahneman & Tversky, Prospect Theory (1979) | WEAK: currency; loss aversion is real but moderated (Mrkva et al. 2020); says nothing about streaks | Silverman & Barasch, *Journal of Consumer Research* (2023) |
| 4 Red dot | Montag et al. (2019); Mark et al. (2016) | FAIL on accuracy: "fires anticipatory dopamine" is not measured in either; Montag is a theory review | Kushlev, Proulx & Dunn, CHI (2016); Fitz et al., *Computers in Human Behavior* (2019) |
| 5 Seen receipts | Cialdini, *Influence* (2001) | WEAK: popular book, general reciprocity, nothing on read receipts | Hoyle et al., CHI (2017) |

## Card by card

### 1. Surprise likes (lever `vrr`)
- **Now (fact):** "Unpredictable rewards drive the most persistent checking — the same schedule that makes slot machines compulsive."
- **Now (task line):** "...Unpredictable payoffs are the strongest hook."
- **Problem:** the source is from 1953, and "most persistent" and "strongest" are superlatives no source here supports.
- **Proposed fact:** "Likes work like rewards. Across more than a million posts, people posted more when likes came fast and less when they slowed: the same reward learning that steers an animal looking for food."
- **Proposed cite:** Lindström et al., *Nature Communications* (2021)
- **Proposed task line:** "...Unpredictable payoffs keep people checking."
- **Evidence:** >1 million posts, >4,000 users, plus an experiment (n = 176) showing likes causally shape posting. *Read: abstract and summaries.* The paper does not test variable-ratio schedules, so the slot-machine comparison is dropped rather than re-cited.

### 2. Infinite scroll (lever `scroll`)
- **Now:** "Take away the bottom of the page and people keep going past the point they meant to stop. The missing stop-cue is the trick."
- **Problem:** "past the point they meant to stop" is not measured in the cited sources, and the citation names no study.
- **Proposed fact:** "An endless feed never gives you a place to stop. In a week of logged sessions, people mostly left because something outside the app pulled them away, or because they got bored, not because the feed ran out."
- **Proposed cite:** Rixen et al., *Proc. ACM HCI*, MobileHCI (2023)
- **Evidence:** a one-week field study, 46 adults, 6,605 logged sessions. Quote: "most reasons to break SM sessions were not related to the app but the user's general context." *Read: full paper summary.* Limit: small sample, and it is observational; it did not test removing infinite scroll.

### 3. Don't-lose-it streak (lever `streak`)
- **Now:** "Losing hurts more than gaining feels good. 'Don't break your streak' turns that into a daily pull."
- **Proposed fact:** "A streak gives her something to lose. Across seven studies, people treated keeping a logged streak alive as a goal in itself, and an unbroken streak brought them back more than a broken one."
- **Proposed cite:** Silverman & Barasch, *Journal of Consumer Research* (2023)
- **Evidence:** the authors' own words: "consumers consider maintaining a logged streak to be a meaningful goal in and of itself." *Read: abstract.* Loss aversion still holds as background (Mrkva et al., *Journal of Consumer Psychology*, 2020: real, larger when people know less), but the streak paper is the direct evidence.

### 4. Red-dot alerts (lever `notify`)
- **Now:** "A waiting red dot fires anticipatory dopamine. Constant interruption also lowers attention and raises stress."
- **Problem:** no human study measures dopamine from a notification badge. A search turned up only opinion pieces making the claim. The second sentence is supportable.
- **Proposed fact:** "Alerts pull attention even when nothing is waiting. In a week with notifications on, people reported more inattention and restlessness than in a week with them off. Getting alerts in three batches a day left people less stressed."
- **Proposed cite:** Kushlev, Proulx & Dunn, CHI (2016); Fitz et al., *Computers in Human Behavior* (2019)
- **Evidence:**
  - Kushlev et al.: 221 students, two-week within-person experiment.
  - Fitz et al.: 200+ adults, randomized, two weeks. The three-daily-batch group was happier and less stressed and unlocked their phones less; hourly batches did little.
  - *Read: university and author summaries.* Kushlev is ten years old but is the experimental anchor; Fitz is the current replication direction.
- **Also:** the code comment in `clearBell()` repeats "anticipatory dopamine". It is not shown to players; reword it in the same edit so the claim does not migrate back.

### 5. 'Seen' receipts (lever `social`)
- **Now:** "Once someone knows you saw their message, not replying feels like something you're doing to them. Reciprocity does the rest."
- **Proposed fact:** "Once 'seen' shows, silence says something. In a survey of 700 Messenger users, senders felt worst when a message was read and not answered, and 68% of people who knew about receipts had avoided opening a message so it would not show as seen."
- **Proposed cite:** Hoyle et al., CHI (2017)
- **Evidence:** 316 recipients and 402 senders. Of 294 recipients who believed senders could see views, 201 (68.4%) had deliberately avoided opening a message; the top reason was "I wanted to pretend I never saw the message." *Read: full paper.* Limits: survey data from 2015, US MTurk sample.

## What stays
The five-lever structure, the FTC dark-patterns frame, and the game's mechanics. Only the fact cards, one task line, and one code comment change.

## Founder decision
Approve all five, approve some, or send wording back. On approval: edit the five cards, bump Flok to v36, run senses and routes (two Flok routes exist, including the full shift), push, and send the play link.

## Sources
- [Lindström et al. 2021, Nature Communications](https://doi.org/10.1038/s41467-020-19607-x)
- [Rixen et al. 2023, The Loop and Reasons to Break It](https://doi.org/10.1145/3604275)
- [Silverman & Barasch 2023, Journal of Consumer Research](https://academic.oup.com/jcr/article-abstract/49/6/1095/6623414)
- [Mrkva et al. 2020, Journal of Consumer Psychology](https://doi.org/10.1002/jcpy.1156)
- [Kushlev, Proulx & Dunn 2016, CHI (PDF)](https://www.interruptions.net/literature/Kushlev-CHI16.pdf)
- [Fitz et al. 2019, Computers in Human Behavior](https://doi.org/10.1016/j.chb.2019.07.016)
- [Hoyle et al. 2017, CHI (PDF)](https://www.cs.oberlin.edu/~rhoyle/papers/hoyle-chi17.pdf)
