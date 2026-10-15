# Flok post logic pass — 2026-10-14 (v34)

Founder: "Make the first boost of the game not 'nothing.' That's boring. Her mom comments and then
she posts 'anyone up' makes no sense. I need a logic director looking at these posts. What is the
deal with the crumb? Coherence please. I need George Saunders and Jared Horvath and Computer
Scientist Jen Golbeck looking at Flok posts and making sure this provides optimal gameplay."

Seated inline, one pass (cost discipline). Seats are lenses, not the real people.

## Findings
- **Horvath (learning).** A contingency is learned from early reward, then thinned: continuous, then
  variable (Skinner's own order). v33 opened on nothing. Worse, Tess's posts came off a fixed list,
  so her behaviour never answered the player's action: there was no cause and effect to learn.
- **Golbeck (social media / network science).** Real users reply to the person who engaged,
  family first. A story view from a drifting friend is the strongest pull (surveillance curiosity
  over a weak tie); a stranger's like is the weakest. Comparison ("how does tidepool get 2,000"),
  compulsive checking and the repost come after silence, not after a reply.
- **Saunders (fiction).** Every line is Tess, 26, a 7:30 patient, a sister in Denver, a friend
  drifting, reacting to one specific thing. "The crumb" is sourdough jargon; "posting through it"
  is generic. The stranger's like lands on her latest post, so she can't say it liked the lake.

## Built
- `REACT` in `the-console.html`: Tess's next post is chosen by what the Boost just paid
  (mom, stranger, quinn, hank, none), indexed by how many times that payout has come.
- `MOM_SAYS`: Mom's three comments escalate ("Where is this?", "You have work.", "Call me tomorrow.").
- `SCHEDULE` opens on Mom's comment, then a stranger, then the gaps grow.
- The receipt names the cause and her response: "Boost 1: Mom commented: 'Beautiful. Where is
  this?' She answered her in 90 seconds."
- Priya's bread now reads "sourdough attempt #41. it finally has the big holes."

## The check (arithmetic, not a rule)
`flok-feed-check.py` H9: lever 1 must be reactions (a fixed list HALTs); the first Boost must pay;
a post after a payout must name the payer; a post after nothing must name no payer; no line
reacts to two payouts. v33 HALTs it; a mutant with Mom -> "anyone up?" HALTs it; v34 passes.
Tess's photo texture is now measured over what a player sees on lever 1.
