#!/usr/bin/env python3
"""Signal Rider v0.15: the opening screen holds together at the founder's page zoom.
Founder 2026-11-09 18:52, phone screenshot at about 150% page zoom: top bar buttons overlapped
and ran off the edge, the steer hint was cut off on both sides, the speed readout ran off
the right. Measured: at 390px the bar already overflowed (buttons shrank below their words);
at 260px (x1.5) and 195px (x2.0) the hint, Library, Settings and the speed panel left the screen.
Fix: one Menu button holds Restart, Library and Settings; the hint wraps; the HUD trims to
hits, balance and speed on narrow screens; messages track the real bar and HUD heights.
Also: the visible word "Comfort" is barred by the 2026-10-13 ruling (now "Settings"), and the
button that said Back was read aloud as "Restart the ride" (now "Restart and load a week").
Base: canon v0.14 (ae3fe244)."""
import hashlib
P = 'lab/down-the-nerve.html'
s = open(P).read()
assert hashlib.sha256(s.encode()).hexdigest().startswith('ae3fe244'), 'base is not canon v0.14'
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70]); s = s.replace(a, b)

rep('<title>Signal Rider v0.14</title>', '<title>Signal Rider v0.15</title>')
rep('<span class="chip">v0.14</span>', '<span class="chip">v0.15</span>')

# ---- top bar: Studio, version, LAB, Menu. One row at 390px.
OLD_BAR = ('  <button class="btn" id="bRestart" type="button" aria-label="Restart the ride">Back</button>\n'
           '  <button class="btn" id="bLib" type="button">Library</button>\n'
           '  <button class="btn" id="bComfort" type="button">Comfort</button>\n</header>')
NEW_BAR = '  <button class="btn" id="bMenu" type="button" aria-haspopup="dialog">Menu</button>\n</header>'
rep(OLD_BAR, NEW_BAR)

MENU = ('<div class="sheet" id="sMenu" role="dialog" aria-modal="true" aria-labelledby="hM"><div class="card">\n'
        '  <h2 id="hM">Menu</h2>\n'
        '  <div class="menucol">\n'
        '    <button class="btn" id="bRestart" type="button" aria-label="Restart the ride and load a week">Restart and load a week</button>\n'
        '    <button class="btn" id="bLib" type="button">Library</button>\n'
        '    <button class="btn" id="bComfort" type="button">Settings</button>\n'
        '  </div>\n'
        '  <div class="row"><button class="btn primary" data-close>Back to the ride</button></div>\n'
        '</div></div>\n')
rep('<div class="sheet" id="sComfort" role="dialog"', MENU + '<div class="sheet" id="sComfort" role="dialog"')
rep('<h2 id="hC">Comfort</h2>', '<h2 id="hC">Settings</h2>')

rep("document.getElementById('bLib').onclick=function(){openSheet('sLib');};",
    "document.getElementById('bMenu').onclick=function(){openSheet('sMenu');};\n"
    "document.getElementById('sMenu').addEventListener('click',function(e){if(e.target.closest('.menucol button')){var m=document.getElementById('sMenu');m.style.display='none';m.classList.remove('open');}},true);\n"
    "document.getElementById('bLib').onclick=function(){openSheet('sLib');};")

rep("#bar .title{font-weight:700;font-size:20px;margin-right:auto}",
    "#bar .title{font-weight:700;font-size:20px;margin-right:auto}\n"
    "#bar{flex-wrap:wrap;row-gap:6px}#bar>.btn,#bar .chip{flex-shrink:0;white-space:nowrap}#bar .title{display:flex;gap:6px;flex-wrap:wrap}\n"
    ".menucol{display:flex;flex-direction:column;gap:10px;margin:12px 0}.menucol .btn{width:100%;justify-content:flex-start;padding:0 16px}")

# ---- steer hint wraps inside the screen
rep("#steerHint{pointer-events:auto}",
    "#steerHint{pointer-events:auto;white-space:normal;max-width:calc(100vw - 24px);text-align:center;line-height:1.25;padding:8px 18px;width:max-content}")

# ---- HUD: speed scales with width; on narrow screens leg name and trip go to screen readers only
rep('<div class="unit">meters per second</div>',
    '<div class="unit"><span class="ul">meters per second</span><span class="us" aria-hidden="true">m/s</span></div>')
rep("#speed{text-align:right}",
    "#speed{text-align:right;flex-shrink:0}#speed .num{font-size:clamp(26px,11vw,44px)!important}#trip{min-width:0}#trip>div{max-width:100%;white-space:normal}.us{display:none}\n"
    "@media (max-width:340px){#legname,#tripv,.unit .ul{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;padding:0!important;margin:0!important}"
    ".unit .us{display:inline}#bal{width:72px}#hud{gap:6px;flex-wrap:wrap!important}#trip{order:-1!important;flex:1 1 100%!important;display:flex!important;justify-content:center!important}}\n"
    "#hits{flex-shrink:0;max-width:none!important}#hits svg{flex-shrink:0;min-width:26px}")

# ---- messages sit under the real bar and above the real HUD
rep("#msgs.low{top:auto;bottom:calc(112px + env(safe-area-inset-bottom))}",
    "#msgs.low{top:auto;bottom:calc(var(--hudh,112px) + 6px)}")
rep("top:calc(58px + env(safe-area-inset-top));display:flex;flex-direction:column;align-items:center;gap:8px;pointer-events:none;padding:0 8px}",
    "top:calc(var(--barb,58px) + 6px);display:flex;flex-direction:column;align-items:center;gap:8px;pointer-events:none;padding:0 8px}")
rep("function placeMsgs(pp){",
    "function syncChrome(){var b=document.getElementById('bar'),h=document.getElementById('hud'),r=document.documentElement.style;\n"
    "  if(b)r.setProperty('--barb',Math.round(b.getBoundingClientRect().bottom)+'px');\n"
    "  if(h&&h.style.display!=='none'){var q=h.getBoundingClientRect();if(q.height)r.setProperty('--hudh',Math.round(innerHeight-q.top)+'px');}}\n"
    "addEventListener('resize',syncChrome);addEventListener('load',syncChrome);setTimeout(syncChrome,0);\n"
    "function placeMsgs(pp){if(!syncChrome.t||performance.now()-syncChrome.t>1000){syncChrome.t=performance.now();syncChrome();}")

assert '>Comfort<' not in s
open(P, 'w').write(s)
print('ok', len(s.encode()), hashlib.sha256(s.encode()).hexdigest())
