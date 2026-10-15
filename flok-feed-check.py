#!/usr/bin/env python3
"""flok-feed-check.py — the feed must look posted, not stocked. Arithmetic, not taste.

Founder, 2026-10-11: "The photos on Flok often make no sense; are repurposed, and don't
seem like a user's typical posts." v24/v25 reused one Rockies postcard three times for
one user, paired an aerial city shot with "anyone up?", and gave a catering tray of
eighteen cups to "is 6 coffees a personality". Each of these is countable, so count it.

HALTs:
  H1 reuse      a photo appears on more than one post, unless declared in R1_REPOST
  H2 stranger   a photo appears on two different posters (cohort and north_trail)
  H3 orphan     an embedded photo that no post shows (dead weight + a credit for nothing)
  H4 ledger     CREDITS keys != photos actually shown; ALT missing for a shown photo
  H5 tie        a photo whose caption shares no word with TIES[photo]: the caption has
                to be ABOUT the picture, or the picture is a stock insert
  H7 face     one handle, one avatar: a poster's hue must match in feed, Level 1 and DMs
  H6 texture    text-only share outside its range: cohort 15-45% (all-photo feeds read as
                ads); Tess's own feed 30-70% (she stops posting photos after two)
  H8 cast       a handle shown anywhere in the feed, the DMs or the strangers has no declared
                tie to Tess in CAST (founder: "these need to look like actual relationships")
  H9 cause      lever 1 (founder 2026-10-14: "Her mom comments and then she posts 'anyone up'
                makes no sense"). Tess's post after a payout must answer the person who paid
                (name or @handle); a post after nothing must name no payer; the first Boost
                must pay (Horvath: a contingency is learned from early reward, then thinned);
                no reaction line may repeat.

Usage: python3 flok-feed-check.py [the-console.html]   exit 1 on any HALT
"""
import json, re, sys

# Caption words a poster would use for their own picture. Add a tie when you add a photo.
TIES = {
    "basil": ["basil", "repotted"], "oldphone": ["phone", "2009"], "coffee": ["third", "one"],
    "loaf": ["loaf", "sourdough"], "creek": ["mountains", "lake"], "bed": ["bed", "streak"],
    "sunset": ["sunset"], "boxes": ["mugs", "cat"], "night": ["city", "new"],
    "window": ["window", "rain"], "lake": ["lake", "golden", "reposting"], "mushroom": ["found", "loop"],
    "lamp": ["bed", "before"], "mugs": ["year", "ago", "night"],
    "SHOT": ["checked", "times"],
}
# v31: Tess's own feed is mostly text after two photos (founder, 2026-10-13: "after they post
# a couple of pictures ... they're not posting pictures"). Her range is wider than the cohort's.
TEXT_RANGE = {"cohort": (0.15, 0.45), "north_trail": (0.30, 0.70)}
# H9: who each payout is, in words Tess would use to answer them
PAYER = {"mom": ["sunroom.mornings", "mom"], "quinn": ["q.ramos", "quinn"], "hank": ["hank"],
         "stranger": ["stranger"]}

def arr(s, name):
    m = re.search(r"const " + name + r"=\[(.*?)\];", s, re.S)
    if not m:
        raise SystemExit(f"HALT: {name} not found")
    return [None if t.strip() == "null" else t.strip().strip("'\"")
            for t in re.findall(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"|null", m.group(1))]

def main(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"data:image/jpeg;base64,[A-Za-z0-9+/=]+", "B64", s)
    halts = []
    bodies, bimg = arr(s, "BODIES"), arr(s, "BODY_IMG")
    r1, r1img = arr(s, "R1_POSTS"), arr(s, "R1_IMG")
    rep = {int(a): int(b) for a, b in re.findall(r"(\d+)\s*:\s*(\d+)",
           (re.search(r"const R1_REPOST=\{(.*?)\};", s) or [None, ""])[1] if re.search(r"const R1_REPOST=\{(.*?)\};", s) else "")}
    embedded = re.findall(r"\n  (\w+):\"B64\"", re.search(r"const IMG=\{.*?\n\};", s, re.S).group(0))
    alt = json.loads(re.search(r"const ALT=(\{.*?\});", s).group(1))
    credits = [c[0] for c in json.loads(re.search(r"const CREDITS=(\[.*?\]\]);", s, re.S).group(1))]
    if len(bodies) != len(bimg): halts.append(f"BODY_IMG has {len(bimg)} entries for {len(bodies)} bodies")
    if len(r1) != len(r1img): halts.append(f"R1_IMG has {len(r1img)} entries for {len(r1)} posts")

    uses = {}
    for i, (b, k) in enumerate(zip(bodies, bimg)):
        if k: uses.setdefault(k, []).append(("cohort", i, b))
    for i, (b, k) in enumerate(zip(r1, r1img)):
        if k and i not in rep: uses.setdefault(k, []).append(("north_trail", i, b))
        if i in rep and r1img[rep[i]] != k:
            halts.append(f"H1 repost {i} declares post {rep[i]} but shows a different photo")
    # v34 lever-1 reactions: photos count like any of Tess's posts; the lake repost is
    # declared by its own first word ("reposting"), the way a person declares one
    rm = re.search(r"const REACT=(\{.*?\]\]\});", s, re.S)
    react = json.loads(re.sub(r"(\w+):\[\[", r'"\1":[[', rm.group(1))) if rm else {}
    for k, rows in react.items():
        for j, row in enumerate(rows):
            if len(row) > 1 and not (row[0].startswith("reposting") and row[1] == (r1img[0] if r1img else None)):
                uses.setdefault(row[1], []).append(("north_trail", 200 + j, row[0]))
            elif len(row) > 1 and not set(re.findall(r"[a-z0-9]+", row[0].lower())) & set(TIES.get(row[1], [])):
                halts.append(f"H5 tie: '{row[1]}' on \"{row[0]}\"")
    ex = re.search(r"const R1_EXTRA=(\[.*?\]\]);", s)
    for j, (b, k) in enumerate(json.loads(ex.group(1)) if ex else []):
        if k: uses.setdefault(k, []).append(("north_trail", 100 + j, b))
    for k, u in uses.items():
        if len(u) > 1: halts.append(f"H1 reuse: '{k}' on {len(u)} posts: " + "; ".join(x[2] for x in u))
        if len({x[0] for x in u}) > 1: halts.append(f"H2 stranger: '{k}' shown by two different posters")
    shown = {k for k in uses if k != "SHOT"}
    for k in embedded:
        if k not in shown: halts.append(f"H3 orphan: '{k}' embedded but never shown")
    if set(credits) != set(embedded): halts.append(f"H4 ledger: credits {sorted(set(credits) ^ set(embedded))} out of step")
    for k in shown:
        if k not in alt: halts.append(f"H4 ledger: no ALT for '{k}'")
    for k, u in uses.items():
        for poster, i, b in u:
            words = set(re.findall(r"[a-z0-9]+", b.lower()))
            if not words & set(TIES.get(k, [])):
                halts.append(f"H5 tie: '{k}' on \"{b}\" (no caption word in {TIES.get(k, 'no TIES entry')})")
    # Tess's texture is what a player SEES on lever 1: her first post plus twelve Boosts
    sched = arr(s, "SCHEDULE") if "const SCHEDULE=" in s else []
    seen_imgs = list(r1img[:1])
    if react and sched:
        occ = {}
        for t in range(12):
            k = sched[t % len(sched)] or "none"; i = occ.get(k, 0); occ[k] = i + 1
            row = react[k][min(i, len(react[k]) - 1)]
            seen_imgs.append(row[1] if len(row) > 1 else None)
    else:
        seen_imgs = r1img
    for name, imgs in (("cohort", bimg), ("north_trail", seen_imgs)):
        share = sum(1 for k in imgs if not k) / max(1, len(imgs))
        lo, hi = TEXT_RANGE[name]
        if not lo <= share <= hi: halts.append(f"H6 texture: {name} text-only share {share:.0%} (want {lo:.0%}-{hi:.0%})")
    cast = re.search(r"const CAST=(\{.*?\});", s, re.S)
    cast = json.loads(cast.group(1)) if cast else {}
    shown_handles = set(re.findall(r'"([^"]+)"', re.search(r"const NAMES=\[(.*?)\]", s).group(1)))
    # accounts are the objects that carry an avatar hue; lever names do not
    shown_handles |= set(re.findall(r'name:"([^"]+)",hue:', s)) | set(re.findall(r'who:"([^"]+)",hue:', s))
    for h in sorted(shown_handles):
        if h not in cast: halts.append(f"H8 cast: '{h}' appears with no declared tie to Tess")

    hues = {}
    hl = [int(x) for x in re.search(r"const HUES=\[(.*?)\]", s).group(1).split(",")]
    for n, h in zip(re.findall(r'"([^"]+)"', re.search(r"const NAMES=\[(.*?)\]", s).group(1)), hl):
        hues.setdefault(n, set()).add(h)
    for n, h in re.findall(r'name:"([^"]+)",hue:(\d+)', s):
        hues.setdefault(n, set()).add(int(h))
    for n, hs in hues.items():
        if len(hs) > 1: halts.append(f"H7 face: '{n}' wears {len(hs)} avatar hues {sorted(hs)}")

    # H9 cause and effect
    if not react:
        halts.append("H9 cause: lever 1 is a fixed list of posts (no REACT): what Tess posts cannot answer what the Boost paid")
    else:
        if not sched or sched[0] is None: halts.append("H9 cause: the first Boost pays nothing")
        for k in {x for x in sched if x}:
            if k not in react: halts.append(f"H9 cause: payout '{k}' has no reaction lines")
        names = [w for ws in PAYER.values() for w in ws]
        seen_lines = {}
        for k, rows in react.items():
            for row in rows:
                low = row[0].lower()
                if k in PAYER and not any(w in low for w in PAYER[k]):
                    halts.append(f"H9 cause: after '{k}' Tess posts \"{row[0]}\", answering nobody who paid")
                if k == "none" and (any(re.search(r"\b" + re.escape(w) + r"\b", low) for w in names) or "@" in low):
                    halts.append(f"H9 cause: after nothing Tess answers someone: \"{row[0]}\"")
                if row[0] in seen_lines: halts.append(f"H9 cause: \"{row[0]}\" reacts to both '{seen_lines[row[0]]}' and '{k}'")
                seen_lines[row[0]] = k
    total = sum(len(u) for u in uses.values())
    print(f"flok-feed-check: {len(bodies)} cohort + {len(r1)} north_trail posts, {total} with pictures, "
          f"{len(embedded)} photos embedded, {len(rep)} declared repost(s)")
    for h in halts: print("HALT", h)
    print("PASS" if not halts else f"{len(halts)} HALT(s)")
    return 1 if halts else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "the-console.html"))
