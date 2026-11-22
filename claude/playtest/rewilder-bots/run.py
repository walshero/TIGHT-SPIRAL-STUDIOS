import asyncio, json, sys, time
from playwright.async_api import async_playwright
SRC="/home/claude/tsp/lab/rewilder.html"; BOT=open("/home/claude/pt/bot.js").read()
async def one(b,cfg):
    pg=await b.new_page(viewport={"width":844,"height":390}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
    await pg.goto("file://"+SRC); await pg.wait_for_timeout(400)
    await pg.evaluate("()=>{window.requestAnimationFrame=()=>0}"); await pg.add_script_tag(content=BOT)
    r=await pg.evaluate("c=>__runBot(c)",cfg); r["pageerrors"]=errs; await pg.close(); return r
async def main():
    plan=json.loads(sys.argv[1]); out=sys.argv[2]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--mute-audio"])
        res=[]; t=time.time()
        sem=asyncio.Semaphore(4)
        async def w(c):
            async with sem: return await one(b,c)
        res=await asyncio.gather(*[w(c) for c in plan])
        json.dump(res,open(out,"w")); print("runs",len(res),"wall",round(time.time()-t,1))
        await b.close()
asyncio.run(main())
