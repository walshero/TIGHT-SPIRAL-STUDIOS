#!/usr/bin/env python3
"""E2E for ACT 3 SCENE 2 (Aug 1964) - keyboard-complete run, integrity
assertions, code battery, mobile+A++ pass. Exit 0 = all pass."""
import os, sys, time
from playwright.sync_api import sync_playwright

F = "file://" + os.path.abspath("choose-your-leader-full.html")
SHOTS = os.path.abspath("studio-eyes-shots/s2")
os.makedirs(SHOTS, exist_ok=True)
FAILS = []

def note(m): print("  " + m)

def press(pg, label, timeout=10000):
    """Keyboard activation: focus the named button, press Enter."""
    b = pg.get_by_role("button", name=label, exact=True).first
    b.wait_for(state="visible", timeout=timeout)
    b.focus()
    pg.keyboard.press("Enter")
    pg.wait_for_timeout(320)

def press_start(pg, prefix, timeout=10000):
    """For buttons whose accessible name has a suffix marker."""
    b = pg.locator(f'button:visible:has-text("{prefix}")').first
    b.wait_for(state="visible", timeout=timeout)
    b.focus()
    pg.keyboard.press("Enter")
    pg.wait_for_timeout(320)

def wait_btn(pg, label, timeout=15000):
    pg.get_by_role("button", name=label, exact=True).first.wait_for(state="visible", timeout=timeout)

def advance_address(pg, room_label="The room"):
    for _ in range(14):
        if pg.get_by_role("button", name=room_label, exact=True).first.is_visible():
            break
        press(pg, "Next line")
    wait_btn(pg, room_label, 4000)

def no_integrity_warning(pg, where):
    if "MEASUREMENT INTEGRITY" in (pg.inner_text("body") or ""):
        FAILS.append(f"integrity assertion FIRED at {where}")
    else:
        note(f"integrity silent at {where}")

def shot(pg, name):
    pg.screenshot(path=os.path.join(SHOTS, name))

def run_full(pg, prefix="", shots=True, aplus=False):
    """Fresh full keyboard run: Act1 -> Act2 -> Scene1 -> Scene2 landing."""
    pg.goto(F)
    pg.wait_for_timeout(400)
    if aplus:
        press(pg, "Studio Eyes - reading comfort, sound, and the content note")
        press(pg, "A++")
        pg.keyboard.press("Escape")
        pg.wait_for_timeout(200)
    press(pg, "Watch with captions only")
    press(pg, "Go on")                       # content note
    wait_btn(pg, "The picture is coming", 8000)
    press(pg, "The picture is coming")
    advance_address(pg)                       # Act 1 address, by keyboard
    press(pg, "The room")
    press(pg, "The hi-fi console")            # unlock the listing
    press(pg, "Turn the listing over")
    press(pg, "Turn the page over")
    press(pg, "Stay with the channel")
    press(pg, "The doorway is lit")
    press(pg, "Cut through the doorway")
    # Act 2 - the desk
    press(pg, "Sit down")
    press(pg, "Will Moscow read a blockade as an act of war?")
    press(pg, "Hold that question")
    press(pg, "Go on")                        # withheld 1 -> 2
    press(pg, "Go on")                        # -> breath
    press(pg, "Go on")                        # breath -> landed 1
    press(pg, "Go on")                        # -> landed 2
    press(pg, "By the door")
    press(pg, "The tag")
    press(pg, "The first evening")
    # Scene 1
    for _ in range(3): press(pg, "Next")
    press(pg, "The evening's listing")
    press(pg, "Seven o'clock")
    press(pg, "The room")
    press(pg, "Take the seat")
    press(pg, "Some")                         # blind
    press(pg, "Read the stamp")
    press(pg, "Go on")                        # 2a -> silence
    press(pg, "Go on")                        # silence -> 2b
    press(pg, "Go on")                        # 2b 1 -> 2
    press(pg, "Go on")                        # 2b 2 -> post ask
    no_integrity_warning(pg, prefix + "S1 post ask")
    press(pg, "A lot")                        # post
    press(pg, "Turn the set off")
    press(pg, "Go on")                        # dark -> breath
    press(pg, "Go on")                        # breath -> WL
    press_start(pg, "“the cost of freedom”")   # expand a WL chip
    pg.keyboard.press("Escape")               # collapse
    pg.wait_for_timeout(250)
    press(pg, "Go on")                        # WL -> third
    press(pg, "Go on")                        # third -> hearing
    press(pg, "Turn the set back on")
    press(pg, "They do")
    press(pg, "Who goes, if it comes to that?")
    press(pg, "Go on")
    press(pg, "Ring it with ships - the quarantine")
    press(pg, "The evening lands")
    # Listings: Scene 2 must be TONIGHT
    st2 = pg.inner_text("#stS2")
    if st2 != "TONIGHT": FAILS.append(f"{prefix}stS2 after S1 landing = {st2}, want TONIGHT")
    if shots: shot(pg, prefix + "listings-s2-tonight.png")
    # ============ SCENE 2 ============
    press(pg, "Go to the second evening")
    for _ in range(2): press(pg, "Next")
    press(pg, "The late listing")
    if shots: shot(pg, prefix + "s2-late-listing.png")
    press(pg, "Almost midnight")
    pg.wait_for_timeout(1500)                 # the one-second cut-in, then the slate
    if shots: shot(pg, prefix + "s2-cutin-slate.png")
    press(pg, "Stay with the channel")
    pg.wait_for_timeout(400)
    if shots: shot(pg, prefix + "s2-address-radio.png")
    advance_address(pg)
    press(pg, "The room")
    press(pg, "The folded paper")
    press_start(pg, "The folded paper - again")
    press(pg, "The armchair")
    press(pg, "The set")
    press_start(pg, "The set - again")
    if shots: shot(pg, prefix + "s2-room.png")
    press(pg, "Take the chair")
    if shots: shot(pg, prefix + "s2-blind-ask.png")
    press(pg, "Some")                         # S2 blind
    press(pg, "Read the stamp")
    press(pg, "The same hours, at sea")
    if shots: shot(pg, prefix + "s2-2a-cable.png")
    press(pg, "Go on")                        # cable -> oplan
    if shots: shot(pg, prefix + "s2-2a-oplan.png")
    press(pg, "Go on")                        # -> silence
    press(pg, "Go on")                        # -> 2b 1
    if shots: shot(pg, prefix + "s2-2b-resolution.png")
    press(pg, "Go on")                        # -> 2b 2 (EOA)
    if shots: shot(pg, prefix + "s2-2b-eoa.png")
    press(pg, "Go on")                        # -> post ask
    no_integrity_warning(pg, prefix + "S2 post ask")
    press(pg, "Fully")                        # S2 post
    press(pg, "Turn the set off")
    if shots: shot(pg, prefix + "s2-dark-props.png")
    press(pg, "Go on")                        # -> breath
    press(pg, "Go on")                        # -> WL 1964
    if shots: shot(pg, prefix + "s2-words-life.png")
    press_start(pg, "“no wider war”")
    if shots: shot(pg, prefix + "s2-wl-expanded.png")
    pg.keyboard.press("Escape")
    pg.wait_for_timeout(250)
    press(pg, "Go on")                        # WL -> same day
    if shots: shot(pg, prefix + "s2-same-day.png")
    press(pg, "Go on")                        # -> third
    press(pg, "Go on")                        # third -> hearing
    press(pg, "Turn the set back on")
    if shots: shot(pg, prefix + "s2-second-hearing.png")
    press(pg, "They don't")
    press(pg, "Our boy turns nineteen this winter.")
    press(pg, "Go on")
    if shots: shot(pg, prefix + "s2-call-courses.png")
    press(pg, "Hold the strike for the commander's full evaluation")
    if shots: shot(pg, prefix + "s2-call-held.png")
    press(pg, "The evening lands")
    st2 = pg.inner_text("#stS2")
    if st2 != "AIRED": FAILS.append(f"{prefix}stS2 after S2 landing = {st2}, want AIRED")
    code = pg.inner_text("#emitCode").strip()
    human = pg.input_value("#emitHuman")
    if "Second evening, blind" not in human: FAILS.append(prefix + "carry-out human record lacks Scene 2 lines")
    if shots: shot(pg, prefix + "s2-landing-carryout.png")
    note(f"{prefix}full run landed; code {code}")
    return code

def open_code_field(pg):
    pg.locator("summary", has_text="I have a code from last time").click()
    pg.wait_for_timeout(150)

def code_battery(pg, full_code):
    # 1) full-code resume + re-emit round trip
    pg.goto(F); pg.wait_for_timeout(400)
    open_code_field(pg)
    pg.fill("#codeIn0", full_code)
    press(pg, "Take me back")
    for row, want in [("#stAct1","AIRED"),("#stAct2","AIRED"),("#stS1","AIRED"),("#stS2","AIRED")]:
        got = pg.inner_text(row)
        if got != want: FAILS.append(f"resume(full): {row}={got}, want {want}")
    press(pg, "Carry my place out")
    re_code = pg.inner_text("#emitCode").strip()
    if re_code != full_code: FAILS.append(f"full code did not round-trip: {full_code} -> {re_code}")
    else: note("full S1+S2 code round-trips bit-identical")
    human = pg.input_value("#emitHuman")
    if "Second evening, blind" not in human or "First evening, blind" in human and "earlier record" in human:
        pass
    if "earlier record" in human: FAILS.append("clean full code mislabeled as earlier record")
    # locked replay law: blind ask shows the first-watch answer
    press(pg, "Return to the second evening")
    for _ in range(2): press(pg, "Next")
    press(pg, "The late listing")
    press(pg, "Almost midnight")
    pg.wait_for_timeout(1500)
    press(pg, "Stay with the channel")
    advance_address(pg)
    press(pg, "The room")
    press(pg, "Take the chair")
    body = pg.inner_text("body")
    if "You answered this on first watch" not in body:
        FAILS.append("S2 locked replay does not show the locked blind answer")
    else: note("S2 locked replay shows first-watch answer; blind cannot be blind twice")
    shot(pg, "s2-locked-replay-ask.png")

    # 2) crafted codes via the page's own pack/read
    pg.goto(F); pg.wait_for_timeout(400)
    r = pg.evaluate("""() => {
      const out = {};
      // Acts-1-2-only (this build + previous build identical)
      S.act1 = true; S.act2 = true; S.committed = true; S.fogSel = 1;
      S.deskSeen = {"d-map":2,"d-phone":1}; S.noticed = {"h-chair":1};
      out.acts12 = packCode();
      // Scene-1-only (bit-identical to the previous build's emission)
      S.s1.done = true; S.s1.blind = 2; S.s1.post = 3; S.s1.hear = 1;
      S.s1.reply = 2; S.s1.call = 3;
      out.s1only = packCode();
      out.s1onlyHash = readCode(out.s1only).hash;
      out.hashS1 = CODEBOOK_HASH; out.hashS12 = HASH_S12;
      // Scene 1+2
      S.s2.done = true; S.s2.blind = 1; S.s2.post = 4; S.s2.hear = 2;
      S.s2.reply = 3; S.s2.call = 2; S.s2.annot = {x:1};
      out.s12 = packCode();
      const d = readCode(out.s12);
      out.s12read = d;
      // legacy pre-R7 code: desk call bits set, old layout (38 trailing zeros)
      let v = 0n;
      const push = (val, bits) => { v = (v << BigInt(bits)) | BigInt(val & ((1 << bits) - 1)); };
      push(1,4); push(0,8); push(0,3); push(1,1); push(3,3); push(1,1);
      push(2,3); push(5,3); push(4,3);
      v = v << 38n;
      let pv = v << 5n;
      const bytes = [];
      for (let i = 8; i >= 0; i--) bytes.unshift(Number((pv >> BigInt(i*8)) & 0xFFn));
      push(crc8(bytes), 8);
      let s = "";
      for (let i = 14; i >= 0; i--) s += B32[Number((v >> BigInt(i*5)) & 31n)];
      out.legacy = "CYL1-" + s.slice(0,5) + "-" + s.slice(5,10) + "-" + s.slice(10,15);
      out.legacyRead = readCode(out.legacy);
      // old-record scene-1 code (hash 99)
      let w = 0n;
      const push2 = (val, bits) => { w = (w << BigInt(bits)) | BigInt(val & ((1 << bits) - 1)); };
      push2(1,4); push2(99,8); push2(1,3); push2(1,1); push2(0,3); push2(1,1);
      push2(0,3); push2(0,3); push2(0,3);
      push2(2,3); push2(3,3); push2(0,3); push2(0,2); push2(0,1); push2(1,2); push2(0,2); push2(1,3);
      w = w << 19n;
      let pw = w << 5n;
      const bts = [];
      for (let i = 8; i >= 0; i--) bts.unshift(Number((pw >> BigInt(i*8)) & 0xFFn));
      push2(crc8(bts), 8);
      let t = "";
      for (let i = 14; i >= 0; i--) t += B32[Number((w >> BigInt(i*5)) & 31n)];
      out.oldrec = "CYL1-" + t.slice(0,5) + "-" + t.slice(5,10) + "-" + t.slice(10,15);
      return out;
    }""")
    if r["s1onlyHash"] != r["hashS1"]:
        FAILS.append("Scene-1-only code hash is not CODEBOOK_HASH (regression: old codes would mislabel)")
    else: note("Scene-1-only code carries CODEBOOK_HASH - previous-build codes stay CURRENT")
    d = r["s12read"]
    exp = dict(scenes=3, s2blind=1, s2post=4, s2hear=2, s2reply=3, s2call=2, s1blind=2, s1post=3)
    for k, want in exp.items():
        if d[k] != want: FAILS.append(f"s12 read {k}={d[k]}, want {want}")
    if d["hash"] != r["hashS12"]: FAILS.append("S1+S2 code does not carry the combined hash")
    else: note("S1+S2 crafted code reads back raw fields + combined hash")
    lr = r["legacyRead"]
    if not lr or lr.get("callLegacy") != 5 or lr.get("desk") != 4 or lr.get("scenes") != 0:
        FAILS.append(f"legacy pre-R7 code misread: {lr}")
    else: note("legacy pre-R7 code (call bits set) reads: clamped, ignored, no crash")
    # acceptance of each crafted code through the UI - no crash, correct rows
    for label, code, wantS1, wantS2 in [
        ("acts12", r["acts12"], "TONIGHT", "LATER"),
        ("s1only", r["s1only"], "AIRED", "TONIGHT"),
        ("s12", r["s12"], "AIRED", "AIRED"),
        ("legacy", r["legacy"], "TONIGHT", "LATER"),
    ]:
        pg.goto(F); pg.wait_for_timeout(350)
        open_code_field(pg)
        pg.fill("#codeIn0", code)
        press(pg, "Take me back")
        got1, got2 = pg.inner_text("#stS1"), pg.inner_text("#stS2")
        if got1 != wantS1 or got2 != wantS2:
            FAILS.append(f"accept({label}): stS1={got1}/{wantS1} stS2={got2}/{wantS2}")
        else: note(f"accept({label}): listings correct ({got1}/{got2})")
        press(pg, "Carry my place out")
        re2 = pg.inner_text("#emitCode").strip()
        if label in ("s1only", "s12") and re2 != code:
            FAILS.append(f"{label} did not round-trip: {code} -> {re2}")
    # old-record label survives the round trip
    pg.goto(F); pg.wait_for_timeout(350)
    open_code_field(pg)
    pg.fill("#codeIn0", r["oldrec"])
    press(pg, "Take me back")
    press(pg, "Carry my place out")
    human = pg.input_value("#emitHuman")
    re3 = pg.inner_text("#emitCode").strip()
    h3 = pg.evaluate("c => readCode(c).hash", re3)
    if "earlier record" not in human: FAILS.append("old-record label missing from carry-out")
    elif h3 != 99: FAILS.append(f"old-record hash not carried forward (got {h3}, want 99)")
    else: note("old-record code: labeled, and hash 99 re-emitted (label survives round trips)")

def main():
    with sync_playwright() as pw:
        try: browser = pw.chromium.launch()
        except Exception: browser = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        errors = []
        def mkpage(w, h):
            ctx = browser.new_context(viewport={"width": w, "height": h})
            p = ctx.new_page()
            p.on("pageerror", lambda e: errors.append("pageerror: " + str(e)))
            p.on("console", lambda m: errors.append("console.error: " + m.text) if m.type == "error" else None)
            return p
        print("== desktop 1280x800, fresh keyboard run through Scene 2 landing ==")
        pg = mkpage(1280, 800)
        full_code = run_full(pg, prefix="")
        print("== code battery ==")
        code_battery(pg, full_code)
        pg.close()
        print("== mobile 390x844 + A++, fresh keyboard run ==")
        pm = mkpage(390, 844)
        run_full(pm, prefix="m-", shots=True, aplus=True)
        pm.close()
        browser.close()
        errs = [e for e in errors if "net::ERR" not in e]
        for e in errs[:10]: FAILS.append(e)
        print()
        if FAILS:
            print("FAILURES:")
            for f in FAILS: print("  - " + f)
            sys.exit(1)
        print("E2E PASS - zero pageerrors, both integrity assertions silent, battery green")
if __name__ == "__main__":
    main()
