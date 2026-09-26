s=open('/tmp/tsp/sandbags.html').read()
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
AX=163
once("+mbtaBus(248,157)+","+mbtaBus(232,157)+")
once("+busstop(374,142)","+busstop(356,142)")
once("+payphone(80,196)+payphone(94,196)+payphone(108,196)","+payphone(194,196)+payphone(207,196)+payphone(220,196)")
once("+figure(126,198,38,{felt:'cyan'","+figure(150,198,38,{felt:'cyan'")
once("+figure(158,198,38,{felt:'magenta'","+figure(176,198,38,{felt:'magenta'")
once('<circle class="pulse" cx="364" cy="177" r="4"','<circle class="pulse" cx="347" cy="177" r="4"')
once('<ellipse cx="141" cy="192" rx="40" ry="14" fill="url(#kl3)"/>','<ellipse cx="%d" cy="192" rx="40" ry="14" fill="url(#kl3)"/>'%AX)
once('<ellipse cx="141" cy="195" rx="16" ry="3.4"','<ellipse cx="%d" cy="195" rx="16" ry="3.4"'%AX)
once('<ellipse cx="141" cy="195.6" rx="7"','<ellipse cx="%d" cy="195.6" rx="7"'%AX)
once("translate(141 195.2) scale(.34) translate(-141 -195.2)\">'+ant(141,194.6)","translate(%d 195.2) scale(.34) translate(-%d -195.2)\">'+ant(%d,194.6)"%(AX,AX,AX))
once("var o=gagGlow(141,193,30,8,'#ffb860');","var o=gagGlow(%d,193,30,8,'#ffb860');"%AX)
once('translate(141 194) scale(.5) translate(-188 -194)','translate(%d 194) scale(.5) translate(-188 -194)'%AX)
once("(q.x-141.3)/.5","(q.x-%.1f)/.5"%(AX+.3))
once("    if(pi===3 && vw<400) x0=-34;   // v43: a phone keeps Sparr's corner and the two of them in frame\n    sv.setAttribute('viewBox',x0.toFixed(1)+' '+(200-h).toFixed(1)+' '+vw.toFixed(1)+' '+h.toFixed(1));\n    sv.setAttribute('preserveAspectRatio','xMidYMax slice');\n",
"""    if(pi===3 && vw<400) x0=28;   // v46: a phone keeps Sparr's corner and the whole bus in frame
    sv.setAttribute('viewBox',x0.toFixed(1)+' '+(200-h).toFixed(1)+' '+vw.toFixed(1)+' '+h.toFixed(1));
    sv.setAttribute('preserveAspectRatio','xMidYMax slice');
    /* v46 (founder: "Swap the balloon and payphone position to conceal
       Longwood but show the whole bus"): on Dead Ants the balloon hangs in
       front of the mouth of Longwood Avenue, so the avenue is revealed as it
       climbs; everywhere else it keeps its own place. */
    var bl=$('balloon');
    if(bl) bl.style.left = pi===3 ? ((104-x0)/vw*r.width).toFixed(1)+'px' : '';
""")
note='''  v46 2026-09-26 (founder: "Swap the balloon and payphone position to conceal
  Longwood but show the whole bus"). On Dead Ants the balloon now hangs in
  front of the mouth of Longwood Avenue, placed in the set's own units so it
  lands there at any width; lifting off reveals the avenue. The payphones take
  the balloon's old spot beside the two of them, and the row is tightened so
  the whole 39 and its stop fit on a phone. Left to right: Sparr's, the
  balloon over Longwood, the two of them with the ant between, the payphones,
  the bus.
'''
i=s.index('  v45 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v45')==1 and s.count('&middot; v45</p>')==1
s=s.replace('<span class="ver">v45','<span class="ver">v46').replace('&middot; v45</p>','&middot; v46</p>')
open('/tmp/sb/v46.html','w').write(s); print('ok')
