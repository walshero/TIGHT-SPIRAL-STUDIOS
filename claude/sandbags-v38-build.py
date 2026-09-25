import sys
src=sys.argv[1]; dst=sys.argv[2]
s=open(src).read()
def R(old,new,n=1):
    global s
    c=s.count(old); assert c==n,(c,old[:70]); s=s.replace(old,new)

# ================= LENS PASS: light edits (from the value mock-ups) =================
# Echigo: one warm light at the noodle shop
R("village(-116,516,134,8,5,.3)+","'<g class=\"mass\">'+village(-116,516,134,8,5,0)+'</g>'+")
for a in ["takayuka(-106,134,30,8,'var(--p-tinred)','var(--p-tinred-d)',1,",
          "takayuka(174,132,28,8,'var(--p-tinblue)','var(--p-tinblue-d)',2,",
          "takayuka(214,128,32,8,'var(--p-tinred)','var(--p-tinred-d)',1,",
          "takayuka(418,130,30,8,'var(--p-tingreen)','var(--p-tingreen-d)',2,",
          "takayuka(466,134,28,8,'var(--p-tinblue)','var(--p-tinblue-d)',1,"]:
    R(a,a[:a.rfind(',',0,-1)+1]+'0,')
for a in ["fw(130,145,12,9,1)","fw(178,145,12,9,1)","fw(250,145,12,9,1)",
          "fw(292,131,11,10,1)","fw(356,139,9,9,1)","fw(414,143,12,8,1)","fw(486,134,10,9,1)"]:
    R(a,a[:-2]+'0)')
R("cedar(-110,122,56,44)+koshi(-100,130,36,12,1)","cedar(-110,122,56,44)+koshi(-100,130,36,12,0)")
R("koshi(-104,171,40,16,1)","koshi(-104,171,40,16,0)")
R("koshi(412,171,34,15,1)","koshi(412,171,34,15,0)")
R('<rect x="-104" y="192" width="40" height="8" fill="var(--lit)"/><rect x="412" y="192" width="34" height="8" fill="var(--lit)"/>','')
R("figure(104,199,34,","'<g class=\"noedge\"><ellipse cx=\"60\" cy=\"196\" rx=\"62\" ry=\"7\" fill=\"var(--lit)\" opacity=\".30\"/><ellipse cx=\"52\" cy=\"196\" rx=\"30\" ry=\"4\" fill=\"#ffe2a0\" opacity=\".35\"/></g>'+figure(104,199,34,")
# Crosswalk: the child reads against the stripes
R("figure(118,183,23,{felt:'orange',dir:-1,coat:'var(--p-verm)',coatD:'var(--p-verm-d)'","figure(118,183,23,{felt:'orange',dir:-1,coat:'#f4dc6a',coatD:'#d8b83c'")
# Peach: the neighbours' door is open and lit; other windows off; his house a step darker
R("'<g class=\"lit glow\">'+win(-106,146,3,1,10,11,16,0)+win(-80,166,1,1,10,11,0,0)+'</g>'","'<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(-106,146,3,1,10,11,16,0)+win(-80,166,1,1,10,11,0,0)+'</g>'")
R("'<g class=\"lit glow\">'+win(454,164,1,1,11,12,0,0)+'</g>'","'<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(454,164,1,1,11,12,0,0)+'</g>'")
R("cape(14,152,102,16,","'<g class=\"stepdark\">'+cape(14,152,102,16,")
R("shutter(28,160,12,13,'var(--p-char-d)')+shutter(88,160,12,13,'var(--p-char-d)')+","shutter(28,160,12,13,'var(--p-char-d)')+shutter(88,160,12,13,'var(--p-char-d)')+'</g>'+")
R("rc(311,160,12,18,'var(--p-moss-d)',' rx=\".8\"')+","'<g class=\"lit glow door\">'+lr(311,160,12,18)+'</g>'+'<g class=\"noedge\">'+rc(309.6,158.6,14.8,1.6,'var(--p-timber-d)')+rc(309.6,158.6,1.6,19.4,'var(--p-timber-d)')+rc(321.6,158.6,1.6,19.4,'var(--p-timber-d)')+'</g>'+")
R("P('M306 178 l22 0 l8 22 l-38 0 z','var(--p-bone-d)')+","P('M306 178 l22 0 l8 22 l-38 0 z','var(--p-bone-d)')+'<g class=\"noedge\">'+P('M310 178 l14 0 l7 22 l-27 0 z','#ffcf7a')+'</g>'+")
# Dead Ants: most far windows off, a sodium pool where the ant crosses, Sparr's counter down a little
R("'<g class=\"lit glow\" opacity=\".9\">'+win(2,56,1,1,7,9,0,0)+win(122,76,1,1,7,9,0,0)+win(150,112,1,1,7,9,0,0)+win(262,46,1,1,6,9,0,0)+win(380,90,1,1,7,9,0,0)+win(506,66,1,1,7,9,0,0)+win(492,120,1,1,7,9,0,0)+win(610,90,1,1,7,9,0,0)+'</g>'",
  "'<g class=\"lit glow\" opacity=\".7\">'+win(380,90,1,1,7,9,0,0)+win(610,90,1,1,7,9,0,0)+'</g>'")
for a in ["shop(0,116,64,2,8,'var(--p-brick)','var(--p-brick-d)','var(--p-bone-d)',1)",
          "shop(132,98,82,3,8,'var(--p-brick-d)','var(--p-char-d)','var(--p-bone-d)',2)",
          "shop(220,134,60,1,8,'var(--p-brick)','var(--p-brick-d)','var(--p-cream-d)',1)",
          "shop(446,112,78,2,8,'var(--p-terra-d)','var(--p-char-d)','var(--p-bone-d)',1)"]:
    R(a,a[:-2]+'0)')
R("'<ellipse cx=\"290\" cy=\"160\" rx=\"60\" ry=\"6\" fill=\"var(--lit)\" opacity=\".13\"/></g>'","'</g>'")
R("'<ellipse cx=\"176\" cy=\"195.4\" rx=\"11\" ry=\"2.4\" fill=\"#ffd98a\" opacity=\".16\"/>'",
  "'<ellipse cx=\"176\" cy=\"193\" rx=\"44\" ry=\"9\" fill=\"#ffb054\" opacity=\".30\"/><ellipse cx=\"176\" cy=\"194.4\" rx=\"22\" ry=\"4.4\" fill=\"#ffd28a\" opacity=\".55\"/>'")
R("'<g class=\"lit glow\">'+lr(-120,136,34,20)+lr(-80,136,32,20)+'</g>'","'<g class=\"lit glow\" opacity=\".6\">'+lr(-120,136,34,20)+lr(-80,136,32,20)+'</g>'")

# ================= LENS PASS: the camera (key light added, never darkness) =================
def key(i,cx,cy,rx,ry,col,op):
    return ("'<g class=\"noedge keylight\"><defs><radialGradient id=\"kl%d\"><stop offset=\"0\" stop-color=\"%s\" stop-opacity=\"%s\"/>"
            "<stop offset=\".55\" stop-color=\"%s\" stop-opacity=\"%s\"/><stop offset=\"1\" stop-color=\"%s\" stop-opacity=\"0\"/></radialGradient></defs>"
            "<ellipse cx=\"%s\" cy=\"%s\" rx=\"%s\" ry=\"%s\" fill=\"url(#kl%d)\"/></g>'+") % (i,col,op,col,round(op*.35,3),col,cx,cy,rx,ry,i)
R("'</g>'+'</g>'+ echigoPlatform()", key(0,56,160,70,48,'#ffd58a',.55)+"'</g>'+'</g>'+ echigoPlatform()")
R("'<g class=\"fx noedge\">'+\n     '<g class=\"blink\">", key(1,96,180,70,26,'#fff3cf',.5)+"'<g class=\"fx noedge\">'+\n     '<g class=\"blink hand\">")
R("'<g class=\"fx noedge\"><g class=\"bounce\">'", key(2,318,170,46,34,'#ffd48a',.55)+"'<g class=\"fx noedge\"><g class=\"bounce\">'")
R("'<g class=\"fx noedge\">'+\n     '<ellipse cx=\"176\"", key(3,176,188,60,22,'#ffb860',.5)+"'<g class=\"fx noedge\">'+\n     '<ellipse cx=\"176\"")
# lights that live on the soft mid layer go soft with it
R('<rect class="blink" x="234" y="136"','<rect class="blink mid" x="234" y="136"')
R('<rect class="blink2" x="241" y="136"','<rect class="blink2 mid" x="241" y="136"')
R('<circle class="blink" cx="237" cy="137.8"','<circle class="blink mid" cx="237" cy="137.8"')
R('<circle class="pulse" cx="328" cy="162" r="5"','<circle class="pulse mid" cx="328" cy="162" r="5"')
R('<rect class="pulse" x="-40" y="124" width="96"','<rect class="pulse mid" x="-40" y="124" width="96"')
R("'<g class=\"crawl\">'+ant(176,194)+'</g>'","'<g class=\"crawl antnow\">'+ant(176,194)+'</g>'")
# depth-of-field filters and the gag stage live in the scenery svg
R('<g id="sceneLayers"></g>','<defs><filter id="dofFar" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="1.5"/></filter><filter id="dofMid" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation=".55"/></filter></defs><g id="sceneLayers"></g><g id="gag" aria-hidden="true"></g>')

CSS=r"""
/* v38 THE LENS. Keep the light, move the focus (founder 09-25: "each scene looks
   like a power outage. This isn't how photographers or filmmakers find focus").
   A macro lens on a paper model: far layers and sky go soft, the street stays
   sharp, a warm key light is added on the story. Nothing is darkened. */
#scenery .ly1{ filter:url(#card1) url(#dofFar) saturate(.85); }
#scenery .ly2{ filter:url(#card2) url(#dofMid); }
#scenery .fx .mid{ filter:url(#dofMid); }
#scenery .keylight{ mix-blend-mode:screen; transition:opacity .6s ease 1s; }
.skybox .skyart{ filter:blur(1.2px); }
.skybox[data-piece="1"] .skyart{ filter:blur(1.6px); }
.skybox::after{ content:''; position:absolute; inset:0; pointer-events:none; z-index:3;
  background:radial-gradient(ellipse 80% 75% at 50% 55%, rgba(0,0,0,0) 62%, rgba(20,16,12,.16) 100%); }
.skybox[data-piece="3"]{ --sky-light:radial-gradient(circle at 74% 18%, rgba(232,238,255,.34), rgba(210,222,255,.05) 4%, rgba(210,222,255,0) 12%); }
#scenery .mass *{ fill:var(--p-sage-d) !important; }
#scenery .stepdark{ filter:brightness(.78); }
#scenery .door{ fill:#ffc25a; }

/* v38 FUNNY FAILURE (founder 09-25: "when the sandbags crashes... something
   happens in the village"). Timing floor: the balloon falls .6s, holds .4s,
   the gag plays 1.5 to 2.5s, then the frame is still. No red, no stamp. The
   key light leaves the story and follows the gag, the way a film cut would.
   Every gag element's resting style IS its last frame, so reduced motion
   shows the punchline without the movement. */
.skybox.gagging #sceneLayers{ animation:thud .32s .55s ease-out both; }
@keyframes thud{ 0%{ transform:none; } 35%{ transform:translateY(1.6px); } 70%{ transform:translateY(-.5px); } 100%{ transform:none; } }
.skybox.gagging #scenery .keylight{ opacity:.35; }
#gag .gglow{ mix-blend-mode:screen; animation:gglow .6s 1s ease-out both; }
@keyframes gglow{ from{ opacity:0; } to{ opacity:1; } }
#gag *{ transform-box:fill-box; }
/* Echigo: the thud knocks a can out of the machine; a villager gives it his umbrella */
#gag .can{ transform-origin:center; animation:canfall .32s 1s cubic-bezier(.5,0,1,.6) both, canroll .7s 1.32s ease-out both, appear .01s 1s both; }
@keyframes appear{ from{ opacity:0; } to{ opacity:1; } }
@keyframes canfall{ from{ translate:0 -13px; opacity:1; } to{ translate:0 0; } }
@keyframes canroll{ from{ transform:translateX(-22px) rotate(-400deg); } to{ transform:none; } }
#gag .walker{ animation:walkin 1s 1.5s ease-in-out both, appear .01s 1.5s both; }
@keyframes walkin{ from{ transform:translateX(44px); } to{ transform:none; } }
#gag .walker .step{ transform-origin:50% 0; animation:step .25s 1.5s 4 alternate both; }
@keyframes step{ from{ transform:rotate(-8deg); } to{ transform:rotate(8deg); } }
#gag .gift{ transform-origin:50% 100%; animation:gift .6s 2.6s ease-in-out both, appear .01s 2.6s both; }
@keyframes gift{ from{ transform:translate(10px,-17px) rotate(0deg); } 60%{ transform:translate(4px,-10px) rotate(-30deg); } to{ transform:none; } }
/* Crosswalk: the pigeons scatter, the signal turns to WALK, they come back single file */
.skybox.gagging #scenery .fx .pw{ opacity:0; animation:pfly .8s 1s ease-in both; }
@keyframes pfly{ from{ opacity:1; transform:none; } 80%{ opacity:1; } to{ opacity:0; transform:translate(-30px,-90px) scale(.7); } }
.skybox.gagging #scenery .fx .hand{ opacity:0; animation:handoff .3s 1.6s both; }
@keyframes handoff{ from{ opacity:1; } to{ opacity:0; } }
#gag .walksig{ animation:gglow .3s 1.6s both; }
#gag .file{ animation:file 1.5s 2s linear both, appear .01s 2s both; }
@keyframes file{ from{ transform:translateX(118px); } to{ transform:none; } }
/* Peach Cobbler: the thud sends the trampoline kid up and over */
.skybox.gagging #scenery .fx .bounce{ transform-origin:50% 50%; animation:flip 1.9s 1s cubic-bezier(.3,0,.6,1) both; }
@keyframes flip{ 0%{ transform:none; } 12%{ transform:translateY(3px); } 45%{ transform:translateY(-58px) rotate(-180deg); } 70%{ transform:translateY(-6px) rotate(-360deg); } 78%{ transform:translateY(0) rotate(-360deg); }
  86%{ transform:translateY(-7px) rotate(-360deg); } 93%{ transform:translateY(0) rotate(-360deg); } 97%{ transform:translateY(-2px) rotate(-360deg); } 100%{ transform:none; } }
/* Dead Ants: a sandbag rolls off the basket and an ant carries it away. The ant lives. */
.skybox.gagging #scenery .fx .antnow{ opacity:0; }
#gag .bag{ transform-origin:center; animation:bagroll .8s 1s ease-out both; }
@keyframes bagroll{ from{ transform:translateX(var(--fromx,30px)) rotate(300deg); } to{ transform:none; } }
#gag .ant2{ animation:antin .4s 1.8s ease-in-out both; }
@keyframes antin{ from{ transform:translateX(-10px); } to{ transform:none; } }
#gag .carry{ animation:carry 1.6s 2.3s ease-in-out both; }
@keyframes carry{ from{ transform:none; } to{ transform:translateX(-64px); } }
#gag .lift{ animation:lift .25s 2.1s ease-out both; }
@keyframes lift{ from{ transform:none; } to{ transform:translate(-.5px,-3px); } }
#gag .carry .bag{ animation:bagroll .8s 1s ease-out both; }
@media (prefers-reduced-motion: reduce){
  .skybox.gagging #sceneLayers, #gag *, .skybox.gagging #scenery .fx *{ animation:none !important; }
}
html.se-reduce .skybox.gagging #sceneLayers, html.se-reduce #gag *, html.se-reduce .skybox.gagging #scenery .fx *{ animation:none !important; }
"""
R("</head>","<style>"+CSS+"</style>\n</head>")

# ================= the gags themselves =================
JS=r"""
  /* v38 FUNNY FAILURE: one small village gag per piece, in the sharp foreground
     plane, lit by a key light that follows it. Built on crash, cleared on load. */
  function gagGlow(cx,cy,rx,ry,col){
    return '<g class="gglow"><defs><radialGradient id="gg"><stop offset="0" stop-color="'+col+'" stop-opacity=".55"/><stop offset="1" stop-color="'+col+'" stop-opacity="0"/></radialGradient></defs>'
      +'<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="url(#gg)"/></g>';
  }
  function gagEchigo(){
    var x=258, y=159, s=22, sh=y-s*.76, o='';
    o+=gagGlow(250,153,34,12,'#ffd58a');
    // the villager, bare-headed now; his umbrella is the gift
    o+='<g class="walker"><g class="noedge">'
      +'<ellipse cx="'+x+'" cy="'+y+'" rx="'+(s*.34)+'" ry="1.8" fill="rgba(18,14,10,.32)"/>'
      +'<path d="M'+(x-s*.14)+' '+sh+' L'+(x+s*.14)+' '+sh+' L'+(x+s*.22)+' '+y+' L'+(x-s*.22)+' '+y+' z" fill="var(--p-indigo)"/>'
      +'<g class="step">'+rc(x-s*.31,sh+s*.06,s*.16,s*.30,'var(--p-indigo)',' rx=".7"')+'</g>'
      +rc(x+s*.15,sh+s*.06,s*.16,s*.30,'var(--p-indigo)',' rx=".7"')
      +rc(x-s*.155,sh+s*.32,s*.31,s*.09,'var(--p-gold)')
      +'<circle cx="'+x+'" cy="'+(sh-s*.1)+'" r="'+(s*.09)+'" fill="#e8b98f"/>'
      +P('M'+(x-s*.09)+' '+(sh-s*.1)+' a'+(s*.09)+' '+(s*.09)+' 0 0 1 '+(s*.18)+' 0 q-'+(s*.09)+' -'+(s*.03)+' -'+(s*.18)+' 0 z','var(--p-char-d)')
      +'</g></g>';
    // the can, fallen from the red machine's slot and rolled to a stop
    o+='<g class="can"><g class="noedge">'+rc(239.4,152,3.4,5,'var(--p-verm)',' rx=".6"')+rc(239.4,153.6,3.4,1.3,'var(--p-cream)')+'</g></g>';
    // his umbrella, set down over the can like a roof
    var ux=241.1, uy=153.4, r=8;
    o+='<g class="gift"><g class="noedge">'+rc(ux-.5,uy-r*.42,1,6,'var(--p-timber)')
      +'<path d="M'+(ux-r)+' '+(uy-r*.42+1.6)+' a'+r+' '+(r*.5)+' 0 0 1 '+(2*r)+' 0 z" fill="var(--p-verm)"/>'
      +ln('M'+ux+' '+(uy-r*.42-1.5)+' L'+(ux-r*.7)+' '+(uy-r*.42+1.4)+' M'+ux+' '+(uy-r*.42-1.5)+' L'+(ux+r*.7)+' '+(uy-r*.42+1.4),'var(--p-cream)',.6,.7)
      +'</g></g>';
    return o;
  }
  function gagCrosswalk(){
    var o=gagGlow(96,182,64,16,'#fff3cf');
    // WALK: a pale walking figure lights in the signal box
    o+='<g class="walksig"><g class="noedge"><circle cx="154.6" cy="138.6" r="1.1" fill="#f2f0ea"/>'
      +ln('M154.4 140 l-.6 3.6 M153.8 143.6 l-1.6 3 M153.8 143.6 l1.4 3 M154.3 141 l-1.8 1.6 M154.3 141 l1.9 1.2','#f2f0ea',.9)+'</g></g>';
    // the pigeons, back on foot, in single file along the stripes
    var p='';
    [0,10,20,30].forEach(function(dx,i){ p+=pigeon(62+dx,187.6,[1.2+i*.1,-i*.3,2,-1]).replace('class="pw"','class="pw2"'); });
    o+='<g class="file">'+p+'</g>';
    return o;
  }
  function gagPeach(){ return gagGlow(352,176,40,24,'#ffd48a'); }
  function gagDeadAnts(fromx){
    var o=gagGlow(150,193,48,10,'#ffb860');
    var bag='<g class="noedge">'+rc(-2.8,-2.2,5.6,4.2,'var(--p-kraft)',' rx="1.4"')+rc(-.9,-3,1.8,1.2,'var(--p-kraft-d)',' rx=".4"')+'</g>';
    o+='<g class="carry"><g class="ant2">'+ant(124+64,194)+'</g>'
      +'<g transform="translate('+(188.6)+' 193)"><g class="lift"><g class="bag" style="--fromx:'+fromx.toFixed(1)+'px">'+bag+'</g></g></g></g>';
    return o;
  }
  function startGag(){
    var sb=$('skybox'), g=$('gag'); if(!g) return;
    var html='';
    if(pi===0) html=gagEchigo();
    else if(pi===1) html=gagCrosswalk();
    else if(pi===2) html=gagPeach();
    else {
      // where the basket came down, in the set's own units, so the bag rolls from it
      var fromx=30;
      try{
        var sv=$('scenery'), br=$('balloon').getBoundingClientRect(), pt=sv.createSVGPoint();
        pt.x=br.left+br.width/2; pt.y=br.bottom;
        var q=pt.matrixTransform(sv.getScreenCTM().inverse());
        fromx=Math.max(-120,Math.min(160,q.x-188.6));
      }catch(e){}
      html=gagDeadAnts(fromx);
    }
    g.innerHTML=html;
    sb.classList.remove('gagging'); void sb.offsetWidth; sb.classList.add('gagging');
  }
  function clearGag(){ var g=$('gag'); if(g) g.innerHTML=''; $('skybox').classList.remove('gagging'); }
"""
R("  function crash(w){\n    crashed=true; lifted=false;", JS+"\n  function crash(w){\n    crashed=true; lifted=false;\n    startGag();")
R("    $('sceneLayers').innerHTML=SCENERY[pi];","    clearGag();\n    $('sceneLayers').innerHTML=SCENERY[pi];")

# ================= version =================
R('<p class="updated"><span id="seUpdated"></span> &middot; v37</p>','<p class="updated"><span id="seUpdated"></span> &middot; v38</p>')
R("<title>Sandbags: a flash fiction climb</title>","<title>Sandbags v38: a flash fiction climb</title>")
R('<h1 class="gametitle">Sandbags<span class="sub">a flash fiction climb</span></h1>','<h1 class="gametitle">Sandbags <span class="ver">v38</span><span class="sub">a flash fiction climb</span></h1>')
R("<style>"+CSS,"<style>\n.gametitle .ver{ font-size:20px; font-weight:700; color:var(--rust); white-space:nowrap; letter-spacing:0; }"+CSS)
BANNER="""
  v38 2026-09-25, THE LENS AND THE VILLAGE LAUGHS. Two founder rulings the same
  afternoon. (1) Focus: "each scene looks like a power outage. This isn't how
  photographers or filmmakers find focus." So nothing is darkened; the far layers
  and the sky go soft like a macro lens on a paper model, the street stays sharp,
  and a warm key light is added on each story spot (the noodle shop, the
  crosswalk, the neighbours' open door, the ant's sodium pool). Lit windows
  elsewhere cut by about half; Crosswalk's child in a pale yellow coat so he reads
  against the stripes. (2) Funny failure is a requirement: every crash now plays
  a village gag after the fall, and the key light follows it. Echigo, the thud
  knocks a can out of the machine and a villager gives it his umbrella. Crosswalk,
  the pigeons scatter, the signal turns to WALK, they come back single file on
  the stripes. Peach Cobbler, the trampoline kid goes up and over. Dead Ants, a
  sandbag rolls off the basket and an ant carries it away. Reduced motion shows
  each punchline as a still. Mock-ups and measurements:
  claude/SANDBAGS-VALUE-MOCKUPS-2026-09-25.md.
"""
R("  EN195 Creative Writing. v2 GAME REBUILD 2026-07-06 (founder GATE-1 verdict: \"no game\").\n",
  "  EN195 Creative Writing. v2 GAME REBUILD 2026-07-06 (founder GATE-1 verdict: \"no game\").\n"+BANNER)
open(dst,'w').write(s); print('built',len(s))
