import sys
src=open('/tmp/tsp/sandbags.html').read()
js=open('/tmp/sb/ukiyo.js').read()
def mk(which,par):
    s=src
    a=s.index("   '<g transform=\"translate(0 -40)\">'+forestWall(78)")
    b=s.index("+ echigoPlatform(),",a)+len("+ echigoPlatform(),")
    s=s[:a]+"   uk"+which+"(),"+s[b:]
    i=s.index('  var SCENERY=[\n'); s=s[:i]+js+'\n'+s[i:]
    # sky: the print paints its own sky
    s=s.replace("return [{c:mt,v:0,far:1},{c:o,v:5,wide:1}","return [];return [{c:mt,v:0,far:1},{c:o,v:5,wide:1}",1)
    s=s.replace("  function fitScene(){\n    var sv=$('scenery'); if(!sv) return;",
      "  function fitScene(){\n    var sv=$('scenery'); if(!sv) return;\n    if(pi===0){ sv.setAttribute('viewBox','0 0 400 250'); sv.setAttribute('preserveAspectRatio','"+par+"'); return; }",1)
    css='''<style>
.skybox[data-piece="0"] .scenery{ height:100% !important; }
#scenery .urain{ stroke-dasharray:46 20; animation:urain .8s linear infinite; }
@keyframes urain{ to{ stroke-dashoffset:-66; } }
@media (prefers-reduced-motion: reduce){ #scenery .urain{ animation:none; } }
</style>
</head>'''
    s=s.replace('</head>',css,1)
    open('/tmp/sb/uk'+which+'.html','w').write(s)
for w in 'ABC': mk(w,'xMidYMax slice')
print('ok')
