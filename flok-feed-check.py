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
  H6 texture    text-only share outside 15-45% in either feed (all-photo feeds read as ads)

Usage: python3 flok-feed-check.py [the-console.html]   exit 1 on any HALT
"""
import json, re, sys

# Caption words a poster would use for their own picture. Add a tie when you add a photo.
TIES = {
    "basil": ["basil", "repotted"], "oldphone": ["phone", "2009"], "coffee": ["third", "one"],
    "loaf": ["loaf", "crumb"], "trail": ["trail"], "bed": ["log", "off"],
    "sunset": ["sunset"], "boxes": ["mugs", "cat"], "pizza": ["opinion"],
    "fog": ["fog"], "lake": ["lake", "golden", "reposting"], "mushroom": ["like", "this"],
    "window": ["day", "still", "here"], "lamp": ["bed", "before"],
    "SHOT": ["checked", "times"],
}

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
    for name, imgs in (("cohort", bimg), ("north_trail", r1img)):
        share = sum(1 for k in imgs if not k) / max(1, len(imgs))
        if not 0.15 <= share <= 0.45: halts.append(f"H6 texture: {name} text-only share {share:.0%} (want 15-45%)")

    hues = {}
    hl = [int(x) for x in re.search(r"const HUES=\[(.*?)\]", s).group(1).split(",")]
    for n, h in zip(re.findall(r'"([^"]+)"', re.search(r"const NAMES=\[(.*?)\]", s).group(1)), hl):
        hues.setdefault(n, set()).add(h)
    for n, h in re.findall(r'name:"([^"]+)",hue:(\d+)', s):
        hues.setdefault(n, set()).add(int(h))
    for n, hs in hues.items():
        if len(hs) > 1: halts.append(f"H7 face: '{n}' wears {len(hs)} avatar hues {sorted(hs)}")

    total = sum(len(u) for u in uses.values())
    print(f"flok-feed-check: {len(bodies)} cohort + {len(r1)} north_trail posts, {total} with pictures, "
          f"{len(embedded)} photos embedded, {len(rep)} declared repost(s)")
    for h in halts: print("HALT", h)
    print("PASS" if not halts else f"{len(halts)} HALT(s)")
    return 1 if halts else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "the-console.html"))
