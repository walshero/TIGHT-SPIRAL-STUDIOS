s=open('/tmp/tsp/sandbags.html').read()
js=open('/tmp/sb/deadants.js').read()
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
a=s.index("   /* 3, DEAD ANTS. v33")
far0=s.index("   '<g class=\"ly1\"><g transform=\"translate(0 40) scale(.62)\">'+",a)
far1=s.index("'</g></g>'+ haze(.36) +",far0)
farexpr=s[far0:far1+len("'</g></g>'")].strip()
end=s.index("\n  ];\n",a)
s=s[:a]+"   /* 3, DEAD ANTS: see v43 THE CORNER, REBUILT above */\n   deadAntsCorner()"+s[end:]
i=s.index('  var SCENERY=[\n')
s=s[:i]+js+'  var DA_FAR='+farexpr+';\n'+s[i:]
once("    if(pi===3 && vw<400) x0-=(400-vw)/2;","    if(pi===3 && vw<400) x0=-34;   // v43: a phone keeps Sparr's corner and the two of them in frame")
once("    var o=gagGlow(150,193,48,10,'#ffb860');","    var o=gagGlow(141,193,30,8,'#ffb860');")
once("    o+='<g class=\"carry\"><g class=\"ant2\">'+ant(124+64,194)+'</g>'\n      +'<g transform=\"translate('+(188.6)+' 193)\"><g class=\"lift\"><g class=\"bag\" style=\"--fromx:'+fromx.toFixed(1)+'px\">'+bag+'</g></g></g></g>';",
     "    // v43: the ant is a real ant's size now, so the gag is drawn at that scale about its spot\n    o+='<g transform=\"translate(141 194) scale(.5) translate(-188 -194)\"><g class=\"carry\"><g class=\"ant2\">'+ant(124+64,194)+'</g>'\n      +'<g transform=\"translate('+(188.6)+' 193)\"><g class=\"lift\"><g class=\"bag\" style=\"--fromx:'+fromx.toFixed(1)+'px\">'+bag+'</g></g></g></g></g>';")
once("        fromx=Math.max(-120,Math.min(160,q.x-188.6));","        fromx=Math.max(-240,Math.min(320,(q.x-141.3)/.5));")
note='''  v43 2026-09-26 (founder: "Sparrs in dead ants looks whacked. Perspective:
  Sparrs on the left. Break street for Longwood Ave and then the pay phones
  then the bus. Put characters between bus and corner and make ant much
  smaller. Use real Boston photos to get background right"). Dead Ants is
  rebuilt on the real corner: Sparr's, 635 Huntington / 158 Longwood, the 1909
  brick block on the west corner of Longwood Avenue; MassArt's Tower Building,
  621 Huntington, on the east corner; Longwood Avenue running away in
  one-point perspective to the medical area, street trees and lamps getting
  smaller; the E branch rails and catenary in Huntington's median. Sparr's
  front faces us square; its side wall runs up Longwood toward the vanishing
  point with the painted sign set letter by letter at depth. Left to right:
  Sparr's, Longwood Avenue, the payphones, the two of them with the ant
  between, the 39 at the curb. The ant is about a third of its old size.
'''
i=s.index('  v42 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v42')==1 and s.count('&middot; v42</p>')==1
s=s.replace('<span class="ver">v42','<span class="ver">v43').replace('&middot; v42</p>','&middot; v42</p>'.replace('v42','v43'))
open('/tmp/sb/v43.html','w').write(s); print('ok', len(farexpr))
