#!/usr/bin/env python3
"""PLAYER-CLEAR GATE — no text may cover the player character while it moves.

Founder rule, studio-wide (2026-11-10): "Messages that block the character in movement are
a no-no across games." See CLAUDE.md, "MESSAGES NEVER COVER THE MOVING CHARACTER".

How it measures (arithmetic, not judgment):
  * The game exposes window.__tspPlayer() -> {x, y, w, h} in CSS px (the character's on-screen
    box), or null when the character is off screen. Optional: window.__tspToast(text) fires
    the game's own message so the gate can stress it.
  * Optional: window.__tspScenes = ['name', ...] and window.__tspScene(name), so a game can
    put its character into the stretches that matter (a chute at full speed, a pipe, a ride).
    Speed is where a leading camera pushes the character into the message band, so a game
    with fast stretches should list them.
  * The gate plays the page at phone size (390 x 844) with random arrow-key steering, ~10 s
    from the start and ~4 s in each listed scene, firing a test message every 0.7 s, and
    samples every 80 ms.
  * At each sample where the character moved more than 2 px since the last one, every
    visible element that carries its own text (effective opacity > 0.05) is tested against
    the character's box. Any overlap is a violation.

Exit 0 PASS. Exit 1 HALT (overlap found). Exit 0 with NOT ARMED when the page has no
__tspPlayer hook: the gate cannot see that game's character yet, and says so by name rather
than reading as clean. Exit 2 refused (no browser, bad input).
"""
import asyncio, json, pathlib, random, sys

PROBE = r"""() => {
  const p = window.__tspPlayer && window.__tspPlayer();
  if (!p) return {p: null, hits: []};
  const hits = [];
  const op = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= parseFloat(cs.opacity); } return o; };
  for (const el of document.body.querySelectorAll('*')) {
    if (el.tagName === 'SCRIPT' || el.tagName === 'STYLE' || el.tagName === 'CANVAS') continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    if (r.right < p.x || r.left > p.x + p.w || r.bottom < p.y || r.top > p.y + p.h) continue;
    if (op(el) <= 0.05) continue;
    hits.push({tag: el.tagName, id: el.id || '', cls: el.className || '', text: el.textContent.trim().slice(0, 40),
               box: [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]});
  }
  return {p, hits};
}"""

async def run(path):
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        await pg.goto(pathlib.Path(path).resolve().as_uri()); await pg.wait_for_timeout(900)
        if not await pg.evaluate("() => typeof window.__tspPlayer === 'function'"):
            print(f"PLAYER-CLEAR: NOT ARMED  {path}  (no window.__tspPlayer hook; the gate cannot see this game's character)")
            await b.close(); return 0
        has_toast = await pg.evaluate("() => typeof window.__tspToast === 'function'")
        scenes = await pg.evaluate("() => Array.isArray(window.__tspScenes) ? window.__tspScenes : []")
        rnd = random.Random(11); keys = ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown']
        held = []; last = None; moving = 0; viol = []; t = 0.0; next_key = 0.0; next_toast = 0.3
        await pg.mouse.click(195, 600)  # first input dismisses any entry invitation
        plan = [(None, 10.0)] + [(sc, 4.0) for sc in scenes]; seg_end = 0.0
        for scene, dur in plan:
          if scene is not None:
            await pg.evaluate("(n) => window.__tspScene(n)", scene); last = None
          seg_end += dur
          while t < seg_end:
              if t >= next_key:
                  for k in held: await pg.keyboard.up(k)
                  held = [rnd.choice(keys)] + ([rnd.choice(keys)] if rnd.random() < .4 else [])
                  for k in held: await pg.keyboard.down(k)
                  next_key = t + 0.4 + rnd.random() * 0.8
              if has_toast and t >= next_toast:
                  await pg.evaluate("() => window.__tspToast('Player-clear gate test message')"); next_toast = t + 0.7
              res = await pg.evaluate(PROBE)
              p = res['p']
              if p and last and abs(p['x'] - last['x']) + abs(p['y'] - last['y']) > 2:
                  moving += 1
                  for h in res['hits']:
                      viol.append((round(t, 2), h, [round(p['x']), round(p['y']), round(p['w']), round(p['h'])]))
              last = p
              await pg.wait_for_timeout(80); t += 0.08
        for k in held: await pg.keyboard.up(k)
        await b.close()
    if moving == 0:
        print(f"PLAYER-CLEAR: HALT  {path}  the character never moved under steering; nothing was measured")
        return 1
    if viol:
        print(f"PLAYER-CLEAR: HALT  {path}  {len(viol)} overlap(s) across {moving} moving samples")
        seen = set()
        for t_, h, p in viol:
            key = (h['tag'], h['id'], h['text'])
            if key in seen: continue
            seen.add(key)
            print(f"   t={t_}s  <{h['tag'].lower()} id='{h['id']}'> \"{h['text']}\" box {h['box']} covers character {p}")
        return 1
    print(f"PLAYER-CLEAR: PASS  {path}  {moving} moving samples ({len(scenes)} scene(s)), no text over the character"
          + ("" if has_toast else "  (no __tspToast hook: messages not stressed)"))
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2: print('usage: player-clear.py <file.html>'); sys.exit(2)
    try:
        sys.exit(asyncio.run(run(sys.argv[1])))
    except ImportError:
        print('PLAYER-CLEAR: REFUSED  no playwright, cannot open a browser'); sys.exit(2)
