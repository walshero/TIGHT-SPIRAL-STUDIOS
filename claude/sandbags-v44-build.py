s=open('/tmp/tsp/sandbags.html').read()
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
# the brick blocks behind Sparr's and Longwood go (scene x < 142); MassArt and the blocks east of it stay
for a in ["     box(-20,10,110,150,10,'var(--p-brick)','var(--p-brick-d)','var(--p-char-d)')+\n     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(-12,20,7,9,7,9,7,6)+'</g>'+\n",
          "     box(100,30,120,130,10,'var(--p-terra)','var(--p-terra-d)','var(--p-char-d)')+\n     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(108,40,8,8,7,9,7,6)+'</g>'+\n",
          "     box(-210,24,100,136,10,'var(--p-terra-d)','var(--p-char-d)','var(--p-char-d)')+\n     '<g class=\"noedge\" fill=\"var(--p-char-d)\">'+win(-202,34,6,10,7,9,7,5)+'</g>'+\n",
          "     box(-104,56,80,104,10,'var(--p-brick)','var(--p-brick-d)','var(--p-char-d)')+\n"]:
    once(a,"")
once("[[30,10],[150,30],[270,0],[520,20],[380,44]]","[[270,0],[520,20],[380,44]]")
once("[[-12,20,7,9,14,15],[108,40,8,8,14,15],[248,10,5,10,12.5,15]","[[248,10,5,10,12.5,15]")
# trees in their place
once("  var DA_FAR=","""  /* v44 (founder: "Keep the tall gray building but remove the buildings
     behind Sparrs and replace with trees"): the brick blocks behind Sparr's
     and up Longwood are gone; big street and campus trees stand there
     instead, dark at night, their undersides warmed by the lamps. */
  function daTrees(){
    var r=skR(107), o='', lit='';
    [[-120,62,30],[-84,50,34],[-50,58,30],[-18,46,36],[16,54,32],[48,44,34],[80,60,26],[104,68,22],[128,76,16]].forEach(function(t){
      var x=t[0], top=t[1], rr=t[2], cy=top+rr*.9;
      o+=rc(x-1.6,cy,3.2,150-cy,'#1c1714');
      for(var k=0;k<9;k++){ var a=Math.PI*(k/8), dx=Math.cos(a)*rr*.62, dy=-Math.sin(a)*rr*.5;
        o+='<circle cx="'+(x+dx+(r()-.5)*4).toFixed(1)+'" cy="'+(cy+dy+(r()-.5)*4).toFixed(1)+'" r="'+(rr*(.34+r()*.14)).toFixed(1)+'" fill="'+(k%3?'#1f2c26':'#253529')+'"/>'; }
      o+='<ellipse cx="'+x+'" cy="'+(cy+rr*.12).toFixed(1)+'" rx="'+(rr*.78).toFixed(1)+'" ry="'+(rr*.46).toFixed(1)+'" fill="#1d2924"/>';
      lit+='<ellipse cx="'+(x+(r()-.5)*6).toFixed(1)+'" cy="'+(cy+rr*.42).toFixed(1)+'" rx="'+(rr*.5).toFixed(1)+'" ry="'+(rr*.14).toFixed(1)+'" fill="#6a5a36" opacity=".55"/>';
    });
    return '<g class="ly1">'+o+'<g class="noedge">'+lit+'</g></g>';
  }
  var DA_FAR=""")
once("    o+=DA_FAR;","    o+=DA_FAR+daTrees();")
note='''  v44 2026-09-26 (founder: "Keep the tall gray building but remove the
  buildings behind Sparrs and replace with trees"). The brick blocks behind
  Sparr's and up Longwood Avenue are gone; a stand of big street and campus
  trees takes their place, dark at night with lamp-warmed undersides.
  MassArt's tower and the blocks east of it stay.
'''
i=s.index('  v43 2026-09-26'); s=s[:i]+note+'\n'+s[i:]
assert s.count('<span class="ver">v43')==1 and s.count('&middot; v43</p>')==1
s=s.replace('<span class="ver">v43','<span class="ver">v44').replace('&middot; v43</p>','&middot; v44</p>')
open('/tmp/sb/v44.html','w').write(s); print('ok')
