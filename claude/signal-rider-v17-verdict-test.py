import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t09.py').read().split('async def main')[0])
async def go():
    async with async_playwright() as p:
        b=await p.chromium.launch();errs=[]
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg);await pg.click('#bRide');await pg.wait_for_timeout(400)
        # jump to the cortex (leg 3), aim at the target until the first beat lands, then screenshot each verdict kind
        await pg.evaluate("()=>{var r=window.__dtn.run,sy=window.__dtn.syns();sy.forEach(x=>{x.done=true});sy[3].done=false;r.leg=3;r.s=sy[3].s-1.5;}")
        shots={}
        for mode in ['full','wrong','miss']:
            for i in range(60):
                await pg.wait_for_timeout(50)
                st=await pg.evaluate("""(m)=>{var r=window.__dtn.run;if(!r.lm)return null;var sy=window.__dtn.syns()[3];
                  if(m==='full')r.theta=r.lm.tgt;else if(m==='wrong'){var o=sy.pads.find(p=>p!==r.lm.tgt);r.theta=o;}else r.theta=r.lm.tgt+Math.PI*0.9;
                  return r.lm.fb?{kind:r.lm.fb.kind,age:r.lm.t-r.lm.fb.t0,hits:r.lm.hits}:null;}""",mode)
                if st and st['kind']==mode and st['age']<0.25:
                    await pg.screenshot(path=f'v17-{mode}.png');shots[mode]=st;break
        print(shots);print('errors',errs);await b.close()
asyncio.run(go())
