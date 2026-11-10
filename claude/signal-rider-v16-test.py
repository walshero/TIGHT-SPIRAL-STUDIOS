import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t09.py').read().split('async def main')[0])
async def go():
    async with async_playwright() as p:
        b=await p.chromium.launch();errs=[]
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg)
        # add a third green so rotation is visible: Help -> pantry
        await pg.evaluate("()=>[...document.querySelectorAll('#cards .cat')].find(b=>b.textContent.includes('Help')).click()");await pg.wait_for_timeout(80)
        await pg.evaluate("()=>document.querySelector('#cards .wk').click()");await pg.click('#cards .back')
        await pg.click('#bRide');await pg.wait_for_timeout(500)
        seq=await pg.evaluate("()=>{var P=window.__dtn.pickups().slice().sort((a,b)=>a.s-b.s);return {g:P.filter(x=>x.good).map(x=>x.card.id),r:P.filter(x=>!x.good).map(x=>x.card.id)};}")
        def check(lst,name):
            k=len(set(lst));first=lst[:k];rep=any(lst[i]==lst[i+1] for i in range(len(lst)-1))
            print(name,'distinct',k,'| first',k,'all different:',len(set(first))==k,'| back-to-back repeat:',rep,'|',' '.join(lst[:10]))
        check(seq['g'],'greens');check(seq['r'],'pinks ')
        sp=await pg.evaluate("""()=>new Promise(res=>{var r=window.__dtn.run;var g=window.__dtn.pickups().filter(x=>x.good&&x.s>r.s+4&&!x.hit).sort((a,b)=>a.s-b.s)[0];var v0=null,t=0;var iv=setInterval(()=>{r.theta=g.a;if(v0===null&&g.s-r.s<2)v0=r.v;if(g.hit||t++>400){clearInterval(iv);setTimeout(()=>res({before:+(v0||0).toFixed(2),after:+r.v.toFixed(2),surgeLeft:+(r.surgeT||0).toFixed(2),hit:g.hit}),500);}},16);})""")
        print('green surge:',sp)
        await pg.evaluate("()=>{var r=window.__dtn.run,sy=window.__dtn.syns();r.s=sy[0].s-1.5;}");await pg.wait_for_timeout(1800)
        st=await pg.evaluate("()=>{var r=window.__dtn.run,sy=window.__dtn.syns()[0];return {inLanding:!!r.lm,key:r.lm&&r.lm.key,shapes:sy.rshape,tgtShape:r.lm&&sy.rshape[sy.pads.indexOf(r.lm.tgt)]};}")
        print('landing:',st);await pg.screenshot(path='v16-landing.png')
        print('alarm road text left:',await pg.evaluate("()=>document.documentElement.outerHTML.toLowerCase().includes('alarm road')"))
        print('errors',errs);await b.close()
asyncio.run(go())
