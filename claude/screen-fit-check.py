#!/usr/bin/env python3
"""screen-fit-check.py: does every fixed control fit the screen a game is played on?

Usage: python3 claude/screen-fit-check.py lab/rewilder.html [--shots DIR]
Loads the file at each screen in SCREENS, on the opening screen and again after Start.
A visible h1, button or link whose box leaves the viewport is a FAIL. Exit 1 on any FAIL
at a real device size. Zoomed rows (Safari page zoom) only warn.
The founder's test phone, an iPhone 16 Pro, is 402 x 874 points; Safari shows about 402 x 745.
"""
import asyncio,sys,os
from playwright.async_api import async_playwright
SCREENS=[('iPhone SE 1st gen',320,568,2,True,False),('iPhone 13 mini',375,812,3,True,False),('iPhone 16 Pro',402,874,3,True,False),
 ('iPhone 16 Pro in Safari',402,745,3,True,False),('iPhone 16 Pro Max',440,956,3,True,False),('iPhone 16 Pro sideways',874,402,3,True,False),
 ('Pixel 8',412,915,2.6,True,False),('iPad portrait',820,1180,2,True,False),('iPad landscape',1180,820,2,True,False),
 ('Laptop',1280,800,1,False,False),('Desktop',1920,1080,1,False,False),('iPhone 16 Pro at 150% zoom',268,583,3,True,True)]
JS="""()=>{const vw=innerWidth,vh=innerHeight,bad=[];document.querySelectorAll('h1,button,a').forEach(el=>{const cs=getComputedStyle(el);if(cs.display==='none'||cs.visibility!=='visible')return;
 let p=el;while(p&&p!==document.body){const c=getComputedStyle(p);if(c.display==='none'||c.visibility!=='visible')return;p=p.parentElement}
 const r=el.getBoundingClientRect();if(r.width<2||r.height<2)return;if(r.bottom<0||r.top>vh)return;
 if(r.left<-1||r.right>vw+1||r.top<-1||r.bottom>vh+1)bad.push((el.id||el.tagName)+' '+Math.round(r.left)+','+Math.round(r.top)+' to '+Math.round(r.right)+','+Math.round(r.bottom))});
 const hud=document.getElementById('hud');if(hud&&hud.scrollWidth>hud.clientWidth+1&&getComputedStyle(hud).display!=='none')bad.push('hud text overflows');return bad}"""
async def main():
    f=os.path.abspath(sys.argv[1]);shots=sys.argv[sys.argv.index('--shots')+1] if '--shots' in sys.argv else None;fail=0
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for name,w,h,d,touch,warn in SCREENS:
            ctx=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=min(d,2),has_touch=touch,is_mobile=touch);pg=await ctx.new_page()
            await pg.goto('file://'+f);await pg.wait_for_timeout(1200);bad=[('open',x) for x in await pg.evaluate(JS)]
            if shots:await pg.screenshot(path=f'{shots}/fit-{w}x{h}-open.png')
            if await pg.query_selector('#startBtn'):
                await pg.click('#startBtn');await pg.wait_for_timeout(900);await pg.evaluate("()=>{const t=document.getElementById('toast');if(t)t.click()}");bad+=[('play',x) for x in await pg.evaluate(JS)]
                if shots:await pg.screenshot(path=f'{shots}/fit-{w}x{h}-play.png')
            tag='pass' if not bad else ('warn' if warn else 'FAIL');fail+=tag=='FAIL'
            print(f'{tag}  {name} {w}x{h}'+''.join(f'\n      {a}: {x}' for a,x in bad));await ctx.close()
        await b.close()
    print('SCREEN FIT:', 'FAIL' if fail else 'pass');sys.exit(1 if fail else 0)
asyncio.run(main())
