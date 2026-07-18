#!/usr/bin/env python3
"""
staging-area.py  -  Tight Spiral Studios review lane
Three named lenses a game passes before it can reach a player.

    HITCHCOCK  suspense / pacing   - does each screen make you need the next?
    HORVATH    desirable difficulty - does the design teach the way brains learn?
    LE GUIN    consequence / world - do choices cost, does the world hold?

GATE, not essay. Each lens emits arithmetic where it exists and a forced
review question where judgment is unavoidable. PASS / WARN / HALT.
Any HALT = exit 1 = does not ship.

    python3 staging-area.py <file.html>
"""
import sys, re

def load(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()

def harvest(src):
    scenes = re.findall(r'\{eyebrow:', src)
    options = re.findall(r'\{label:', src)
    structural_branch = bool(re.search(r'opt\.(next|goto|to)\b', src) or re.search(r'\bnext:\s*["\']', src))
    scalar_branch = bool(re.search(r'\bd:\s*-?\d', src) or re.search(r'promise\s*\+=', src) or re.search(r'score\s*\+=', src))
    ending_bands = len(re.findall(r'\bmin:\s*\d', src))
    return dict(scenes=len(scenes), options=len(options), structural_branch=structural_branch,
                scalar_branch=scalar_branch, ending_bands=ending_bands)

def lens_hitchcock(src, h):
    print("\n  HITCHCOCK - suspense / pacing")
    verdict = "PASS"; notes = []
    hooks = len(re.findall(r'class=.narrator.', src)); scenes = h["scenes"]
    if scenes == 0:
        print("  HALT  no scenes."); return "HALT"
    print(f"  scenes: {scenes}   hook lines: {hooks}")
    if hooks < scenes - 1: notes.append(f"only {hooks} hooks across {scenes} scenes"); verdict="WARN"
    clock = len(re.findall(r'\b\d{1,2}:\d{2}\s*[ap]\.?m', src, re.I))
    if clock >= scenes - 1: print(f"  ticking clock: {clock} timestamps. GOOD.")
    else:
        notes.append("no ticking clock")
        if verdict=="PASS": verdict="WARN"
    print("  FOUNDER READ: play cold. Did you NEED the next scene?")
    for n in notes: print(f"  - {n}")
    print(f"  => {verdict}"); return verdict

def lens_horvath(src, h):
    print("\n  HORVATH - desirable difficulty / learning (Jared Cooney Horvath)")
    verdict = "PASS"; notes = []; lowered = src.lower()
    deltas = [int(m) for m in re.findall(r'\bd:\s*(-?\d+)', src)]
    if h["options"] == 0:
        print("  HALT  no choices."); return "HALT"
    if deltas:
        spread = max(deltas)-min(deltas); distinct=len(set(deltas))
        print(f"  choice weights: {len(deltas)} values, spread {spread}, {distinct} distinct.")
        if spread==0 or distinct==1: notes.append("identical weight - no difficulty."); verdict="HALT"
        elif spread==1: notes.append(f"spread {spread} - faint."); verdict="WARN"
        else: print(f"  choices diverge (spread {spread}). GOOD.")
    elif h["structural_branch"]: print("  choices branch structurally. GOOD.")
    else: notes.append("cosmetic choices."); verdict="HALT"
    comfort = [t for t in ["no wrong moves","no wrong answers","you can't lose","no failure","everyone wins"] if t in lowered]
    if comfort:
        print("  FLAG  comfort-design language: " + ", ".join(f'"{t}"' for t in comfort))
        print("        Horvath: friction is where encoding happens.")
        if verdict=="PASS": verdict="WARN"
        notes.append('"no wrong moves" advertised - difficulty must live in the decision')
    if bool(re.search(r'function\s+choose', src)) and "fb" in lowered:
        print("  retrieval: feedback fires after the player commits. GOOD.")
    else:
        notes.append("retrieval order unverified")
        if verdict=="PASS": verdict="WARN"
    print("  FOUNDER READ: what does the player carry out the door?")
    for n in notes: print(f"  - {n}")
    print(f"  => {verdict}"); return verdict

def lens_leguin(src, h):
    print("\n  LE GUIN - consequence / world")
    verdict = "PASS"; notes = []
    if h["options"] == 0:
        print("  HALT  no choices."); return "HALT"
    print(f"  choices: {h['options']}   ending bands: {h['ending_bands']}")
    if h["structural_branch"]: print("  STRUCTURAL branch: path changes. Strong consequence.")
    elif h["scalar_branch"] and h["ending_bands"]>=2:
        print(f"  SCALAR: meter forks {h['ending_bands']} endings; same scenes, same order.")
        notes.append("scalar, not structural"); verdict="WARN"
    elif h["scalar_branch"]: notes.append("one ending - cosmetic."); verdict="HALT"
    else: notes.append("decoration."); verdict="HALT"
    print("  FOUNDER READ: does the world REMEMBER an early reckless choice?")
    for n in notes: print(f"  - {n}")
    print(f"  => {verdict}"); return verdict

def floor_checks(src):
    print("  FLOORS")
    fails = []
    ext = set(re.findall(r'https?://([^/\s"\'<>]+)', src))
    assets = [h for h in ext if h!="walshero.github.io" and "mailto" not in h]
    if [h for h in assets if "font" in h or "gstatic" in h]:
        print(f"  HALT  external hosts: {', '.join(sorted(assets))}"); fails.append("external-host")
    else: print("  offline: no external hosts. GOOD.")
    if re.findall(r'[\U0001F300-\U0001FAFF]', src): print("  HALT  emoji."); fails.append("emoji")
    else: print("  no emoji. GOOD.")
    screens = len(re.findall(r'\{eyebrow:', src)) + 1
    has_home = bool(re.search(r'(id|class)="[^"]*(home|restart|start-?over)', src, re.I) or re.search(r'aria-label="[^"]*(home|start)', src, re.I))
    has_back = bool(re.search(r'(id|class)="[^"]*(back|nav)', src, re.I) or re.search(r'aria-label="[^"]*back', src, re.I))
    persistent = bool(re.search(r'position:\s*(fixed|sticky)', src) and re.search(r'(class|id)="[^"]*nav', src, re.I))
    if screens>=2 and not (has_back and has_home and persistent):
        m=[]
        if not has_back: m.append("BACK")
        if not has_home: m.append("HOME")
        if not persistent: m.append("PERSISTENCE")
        print(f"  HALT  nav floor: {screens}-screen missing {', '.join(m)}"); fails.append("nav-floor")
    else: print("  nav floor: back+home reachable. GOOD.")
    print("  => " + ("HALT" if fails else "PASS")); return fails

def main():
    if len(sys.argv)!=2:
        print("usage: python3 staging-area.py <file.html>"); sys.exit(2)
    src = load(sys.argv[1])
    print("="*66); print(f"  STAGING AREA - {sys.argv[1]}"); print("  Hitchcock - Horvath - Le Guin"); print("="*66)
    ff = floor_checks(src); h = harvest(src)
    v = {"HITCHCOCK": lens_hitchcock(src,h), "HORVATH": lens_horvath(src,h), "LE GUIN": lens_leguin(src,h)}
    print("\n"+"="*66)
    for k,val in v.items(): print(f"  {k:<10} {val}")
    print("  FLOORS     " + ("HALT  ("+"; ".join(ff)+")" if ff else "PASS"))
    halted = ff or any(x=="HALT" for x in v.values()); warned = any(x=="WARN" for x in v.values())
    print("="*66)
    if halted: print("  VERDICT: HALT - does not clear. (exit 1)"); sys.exit(1)
    elif warned: print("  VERDICT: PASS WITH WARNINGS. (exit 0)"); sys.exit(0)
    else: print("  VERDICT: CLEAR. (exit 0)"); sys.exit(0)

if __name__ == "__main__":
    main()
