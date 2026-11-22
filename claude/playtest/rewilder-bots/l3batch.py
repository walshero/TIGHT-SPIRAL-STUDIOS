import asyncio, json, sys, time
from playwright.async_api import async_playwright
import os
HERE=os.path.dirname(os.path.abspath(__file__))
# the build under test: the repo's lab copy, never a stale clone (2026-11-22: a hard-coded /home/claude/tsp path silently tested v0.85)
SRC=os.environ.get("REWILDER_SRC",os.path.join(HERE,"..","..","..","lab","rewilder.html")); BOT=open(os.path.join(HERE,"l3bot.js")).read()
async def one(b,cfg):
    pg=await b.new_page(viewport={"width":844,"height":390}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
    await pg.goto("file://"+SRC); await pg.wait_for_timeout(400)
    await pg.evaluate("()=>{window.requestAnimationFrame=()=>0}"); await pg.add_script_tag(content=BOT)
    try: r=await pg.evaluate("c=>__runL3(c)",cfg)
    except Exception as e: r={"seed":cfg["seed"],"style":cfg["style"],"crash":str(e)[:300]}
    r["pageerrors"]=errs; await pg.close()
    open(os.environ.get("RUNS_LOG","/tmp/rewilder-l3-runs.jsonl"),"a").write(json.dumps(r)+"\n"); return r
async def main():
    plan=json.loads(open(sys.argv[1]).read()); out=sys.argv[2]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--mute-audio"])
        sem=asyncio.Semaphore(2); t=time.time()
        async def w(c):
            async with sem: return await one(b,c)
        res=await asyncio.gather(*[w(c) for c in plan])
        json.dump(res,open(out,"w")); print("runs",len(res),"wall",round(time.time()-t))
        await b.close()
asyncio.run(main())
