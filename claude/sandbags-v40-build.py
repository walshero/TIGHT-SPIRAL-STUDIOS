src=open('/tmp/tsp/sandbags.html').read()
js=open('/tmp/sb/roofs.js').read()
s=src
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:70]); s=s.replace(a,b)
a=s.index("   '<g transform=\"translate(0 -40)\">'+forestWall(78)")
b=s.index("+ echigoPlatform(),",a)+len("+ echigoPlatform(),")
s=s[:a]+"   echigoTown(),"+s[b:]
i=s.index('  var SCENERY=[\n'); s=s[:i]+js+'\n'+s[i:]
once("return [{c:mt,v:0,far:1},{c:o,v:5,wide:1}","/* v40: the Echigo sheet paints its own sky */ return [];\n      return [{c:mt,v:0,far:1},{c:o,v:5,wide:1}")
once("  function fitScene(){\n    var sv=$('scenery'); if(!sv) return;",
     "  function fitScene(){\n    var sv=$('scenery'); if(!sv) return;\n    // v40: Echigo is one sheet that fills the sky box; a phone crops it to its middle\n    if(pi===0){ sv.setAttribute('viewBox','0 0 400 250'); sv.setAttribute('preserveAspectRatio','xMidYMax slice'); return; }")
once("    if(pi===0) html=gagEchigo();","    if(pi===0) html='<g transform=\"translate(0 63)\">'+gagEchigo()+'</g>';  // v40: the machines moved down the new street")
css='''<style>
/* v40: Echigo fills the sky box; Hiroshige's rain is long lines, not dashes */
.skybox[data-piece="0"] .scenery{ height:100% !important; }
#scenery .urain{ stroke-dasharray:46 20; animation:urain .8s linear infinite; }
@keyframes urain{ to{ stroke-dashoffset:-66; } }
@media (prefers-reduced-motion: reduce){ #scenery .urain{ animation:none; } }
html.se-reduce #scenery .urain{ animation:none; }
</style>
</head>'''
once('</head>',css)
note='''  v40 2026-09-26, EVERY ROOF DIFFERENT (founder: "Build echigo with all
  different roofs", with a photograph of Magome-juku on the Nakasendo). Echigo
  is rebuilt on print C of the ukiyo-e mock-ups (studio pick; founder had not
  chosen): the sheet fills the sky box, a low horizon, the mountain two thirds
  of the frame, the town in three rows stepping down the slope, and fourteen
  houses with fourteen roof types: hisashi machiya, kura, the noodle shop with
  udatsu firewalls, stone-weighted shingles, an irimoya inn, a tin lean-to,
  hipped tile, a split-ridge tin gable, a copper shrine roof, a lopsided snow
  roof, a brewer's ridge vent, a flat slab, hipped tin, a kayabuki farmhouse
  and a gassho A-frame. Grey kawara drawn in channels and courses, onigawara
  at the ridge ends, a stone lantern, pots. The Shinkansen now runs on a
  viaduct behind the middle row instead of the foreground platform (flag).
  The crash gag's villager and can moved down with the vending machines.
'''
i=s.index('  v39 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
s=s.replace('<span class="ver">v39','<span class="ver">v40').replace('&middot; v39</p>','&middot; v40</p>')
open('/tmp/sb/v40.html','w').write(s); print('ok')
