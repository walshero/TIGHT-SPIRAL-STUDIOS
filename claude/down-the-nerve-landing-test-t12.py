import asyncio, sys
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t09.py').read().split('async def main')[0])
# Aimers. delay = reaction time in ms before the aimer sees the new target; rate = the game's steer speed (2.7 rad/s).
AIMER = """(cfg)=>{var r=window.__dtn.run;clearInterval(window.__aim);var hist=[];
 window.__aim=setInterval(function(){if(!r.lm){hist=[];return;}var now=performance.now();hist.push([now,r.lm.tgt]);
  var seen=null;for(var i=hist.length-1;i>=0;i--){if(now-hist[i][0]>=cfg.delay){seen=hist[i][1];break;}}
  if(seen===null||cfg.delay<0)return;var d=Math.atan2(Math.sin(seen-r.theta),Math.cos(seen-r.theta));
  var step=2.7*0.016;r.theta+=Math.abs(d)<step?d:Math.sign(d)*step;},16);}"""
async def trial(pg, leg):
    await pg.wait_for_timeout(900); await pg.keyboard.press('Escape'); await pg.wait_for_timeout(60)
    await pg.evaluate("(L)=>{var r=window.__dtn.run,sy=window.__dtn.syns();sy.forEach(function(x,i){if(i>=L){x.done=false;x.fill=0;x.afill=0;}});r.over=false;r.faded=false;r.hits=0;r.leg=L;r.lm=null;r.s=sy[L].s-2;}", leg)
    for i in range(40):
        await pg.wait_for_timeout(250)
        st = await pg.evaluate("(L)=>({leg:window.__dtn.run.leg,hits:window.__dtn.run.hits,over:window.__dtn.run.over,h:document.getElementById('hE').textContent})", leg)
        if st['leg'] != leg or st['over']: return 'fire' if 'alarm' not in st['h'] else 'alarm'
        if st['hits'] > 0: return 'miss'
    return 'timeout'
async def tries(pg, leg):
    """Player experience: what landed carries over between tries. Returns how many tries it took, or 'fade'/'alarm'."""
    await pg.wait_for_timeout(900); await pg.keyboard.press('Escape'); await pg.wait_for_timeout(60)
    await pg.evaluate("(L)=>{var r=window.__dtn.run,sy=window.__dtn.syns();sy.forEach(function(x,i){if(i>=L){x.done=false;x.fill=0;x.afill=0;}});r.over=false;r.faded=false;r.hits=0;r.leg=L;r.lm=null;r.s=sy[L].s-2;}", leg)
    for i in range(160):
        await pg.wait_for_timeout(250)
        st = await pg.evaluate("()=>({over:window.__dtn.run.over,faded:window.__dtn.run.faded,hits:window.__dtn.run.hits,h:document.getElementById('hE').textContent})")
        if st['faded']: return 'fade'
        if st['over']: return 'alarm' if 'alarm' in st['h'] else str(st['hits']+1)
    return 'timeout'
async def go():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    WEEKS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['default','hard']
    async with async_playwright() as p:
        b = await p.chromium.launch(); errs = []
        for week in WEEKS:
            pg = await b.new_page(viewport={'width': 390, 'height': 844}); pg.on('pageerror', lambda e: errs.append(str(e)))
            await to_tray(pg)
            if week == 'hard':
                for cat, labs in [('Money', ['meals', 'Rent']), ('Feeling alone', ['alone'])]:
                    await pg.evaluate("(c)=>[...document.querySelectorAll('#cards .cat')].find(b=>b.querySelector('*')?b.textContent.trim().startsWith(c):b.textContent.includes(c)).click()", cat); await pg.wait_for_timeout(120)
                    for l in labs:
                        await pg.evaluate("(l)=>[...document.querySelectorAll('#cards .wk')].find(b=>b.textContent.includes(l)).click()", l); await pg.wait_for_timeout(80)
                    await pg.click('#cards .back'); await pg.wait_for_timeout(120)
            await pg.click('#bRide'); await pg.wait_for_timeout(500)
            st = await pg.evaluate("()=>({stressed:window.__dtn.syns()[3].stressed,pads:window.__dtn.syns()[3].pads.length,w:window.__dtn.syns()[3].w,need:window.__dtn.syns()[3].need})")
            print(week, st)
            for name, delay in [('perfect', 0), ('human 250ms', 250), ('slow 450ms', 450), ('no steering', -1)]:
                await pg.evaluate(AIMER, {'delay': delay})
                row = []
                for leg in ([1, 3] if week == 'default' else [3]):
                    res = [await (tries(pg, leg) if 'tries' in sys.argv else trial(pg, leg)) for _ in range(N)]
                    row.append(f"leg{leg}: " + ' '.join(res))
                print(f"  {name:12s}", ' | '.join(row))
            await pg.close()
        # three misses in a row end the run on the fade card, which names the gap
        pg = await b.new_page(viewport={'width': 390, 'height': 844}); pg.on('pageerror', lambda e: errs.append(str(e)))
        await to_tray(pg); await pg.click('#bRide'); await pg.wait_for_timeout(400)
        await pg.evaluate("()=>{var r=window.__dtn.run,sy=window.__dtn.syns();r.s=sy[0].s-2;}")
        for i in range(80):
            await pg.wait_for_timeout(250)
            if await pg.evaluate("()=>window.__dtn.run.faded"): break
        await pg.wait_for_timeout(1200)
        fade = await pg.evaluate("()=>({hits:window.__dtn.run.hits,open:document.getElementById('sFade').classList.contains('open'),why:document.getElementById('fadeWhy').textContent.slice(0,70),leg:window.__dtn.run.leg})")
        if 'nofade' in sys.argv: await b.close(); return
        print('three misses:', fade, 'secs', i * 0.25)
        await pg.screenshot(path='v12-fade.png')
        print('errors', errs); await b.close()
asyncio.run(go())
