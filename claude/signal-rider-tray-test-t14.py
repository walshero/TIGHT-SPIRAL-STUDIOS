import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t09.py').read().split('async def main')[0])
async def go():
    async with async_playwright() as p:
        b=await p.chromium.launch();errs=[]
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg)
        vis=lambda: pg.evaluate("()=>getComputedStyle(document.getElementById('rideRow')).display")
        print('overview ride row:',await vis())
        await pg.evaluate("()=>document.querySelector('#cards .cat').click()");await pg.wait_for_timeout(150)
        st=await pg.evaluate("()=>({h:document.querySelector('#cards .cath h3').textContent,prog:document.querySelector('#cards .prog').textContent,next:document.querySelector('.nextcat').textContent,focus:document.activeElement.tagName+':'+document.activeElement.textContent})")
        print('in Sleep:',st,'ride row:',await vis())
        await pg.screenshot(path='v14-cat.png')
        # walk with Next to the end
        names=[]
        for i in range(12):
            t=await pg.evaluate("()=>{var n=document.querySelector('.nextcat');if(!n)return null;var t=n.textContent;n.click();return t;}")
            await pg.wait_for_timeout(100)
            if t is None:break
            names.append(t)
            if t=='Review your week':break
        print('walk:',names)
        rv=await pg.evaluate("()=>({h:document.querySelector('#cards .cath h3').textContent,txt:document.querySelector('#cards .cath').textContent.slice(0,200),blocks:document.querySelectorAll('#cards .wk').length})")
        print('review:',rv,'ride row:',await vis())
        await pg.screenshot(path='v14-review.png',full_page=False)
        # remove one block on review, then skip-to-review path with unseen list
        await pg.evaluate("()=>document.querySelector('#cards .wk').click()");await pg.wait_for_timeout(120)
        print('after remove blocks:',await pg.evaluate("()=>document.querySelectorAll('#cards .wk').length"))
        await pg.click('#cards .back');await pg.wait_for_timeout(100)
        await pg.evaluate("()=>[...document.querySelectorAll('#cards .cat')].find(b=>b.textContent.includes('Money')).click()");await pg.wait_for_timeout(100)
        # fresh tray? seen persists within visit; test skip
        await pg.evaluate("()=>[...document.querySelectorAll('#cards .catnav .btn')].find(b=>b.textContent==='Skip to review').click()");await pg.wait_for_timeout(100)
        print('skip review:',await pg.evaluate("()=>document.querySelector('#cards .cath').textContent.slice(0,260)"))
        await pg.click('#bRide');await pg.wait_for_timeout(600)
        print('ride started:',await pg.evaluate("()=>!!window.__dtn.run&&getComputedStyle(document.getElementById('tray')).display"))
        # reopening tray resets walk
        await pg.evaluate("()=>{}")
        print('errors',errs);await b.close()
asyncio.run(go())
