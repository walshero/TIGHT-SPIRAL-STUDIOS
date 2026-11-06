def scene_kisho(p):
    c=G['Core Craft']; s=f'url(#{p}sh)'; s2=f'url(#{p}sh2)'
    o=[defs(p), f'<rect x="-10" y="-60" width="428" height="440" fill="{c["dark"]}"/>']
    # moon with paper halo
    o.append(f'<circle cx="318" cy="78" r="58" fill="{c["mid"]}" opacity=".55"/>')
    o.append(f'<path d="{wob([(318+40*math.cos(a/12*6.283),78+40*math.sin(a/12*6.283)) for a in range(12)],1.2,3,3)}" fill="{CREAM}" filter="{s2}"/>')
    # far bank, near bank
    o.append(f'<path d="{band(wave(210,6,6,0.4),seed=5)}" fill="#2e3f74" filter="{s}"/>')
    # pond: layered ellipses (cut rings)
    for i,(rx,ry,col) in enumerate([(176,52,c['mid']),(150,42,'#5468a8'),(120,32,c['light']),(84,22,'#b7c4e8')]):
        pts=[(204+rx*math.cos(a/24*6.283),282+ry*math.sin(a/24*6.283)) for a in range(24)]
        o.append(f'<path d="{wob(pts,1.3,10+i,1)}" fill="{col}" filter="{s2}"/>')
    # ripple splash rings (cut cream threads)
    for r_,op in [(30,1),(48,.8),(66,.55)]:
        o.append(f'<ellipse cx="226" cy="282" rx="{r_}" ry="{r_*0.28:.1f}" fill="none" stroke="{CREAM}" stroke-width="3" opacity="{op}"/>')
    # near bank lower left with reeds (blade shapes, not trees)
    o.append(f'<path d="{band([(-10,330),(80,318),(170,336),(260,328),(418,342)],seed=7)}" fill="#18234a" filter="{s}"/>')
    r=random.Random(9)
    for i in range(9):
        x=14+i*11+r.uniform(-3,3); h=90+r.uniform(-25,30); lean=r.uniform(-14,10)
        o.append(f'<path d="M{x:.1f} 336 Q{x+lean*0.4:.1f} {336-h*0.6:.1f} {x+lean:.1f} {336-h:.1f} Q{x+lean*0.4+5:.1f} {336-h*0.55:.1f} {x+7:.1f} 336Z" fill="{["#3d5191","#4f63a3","#2e3f74"][i%3]}" filter="{s2}"/>')
    for i in range(6):
        x=330+i*12+r.uniform(-3,3); h=70+r.uniform(-20,25); lean=r.uniform(-12,12)
        o.append(f'<path d="M{x:.1f} 344 Q{x+lean*0.4:.1f} {344-h*0.6:.1f} {x+lean:.1f} {344-h:.1f} Q{x+lean*0.4+5:.1f} {344-h*0.55:.1f} {x+7:.1f} 344Z" fill="{["#4f63a3","#3d5191"][i%2]}" filter="{s2}"/>')
    # the frog mid-leap (cut paper, green-cream so it reads on indigo)
    fg='#c9dfa2'; fd='#7f9e55'
    o.append(f'<g transform="translate(196 178) rotate(-24)" filter="{s}">'
      f'<path d="M-6 6 L-58 28 L-86 20 L-60 14 L-30 -2Z" fill="{fd}"/>'          # back leg far
      f'<path d="M-4 12 L-62 40 L-96 36 L-66 26 L-28 6Z" fill="{fg}"/>'           # back leg near
      f'<path d="{wob([(46*math.cos(a/16*6.283),20*math.sin(a/16*6.283)) for a in range(16)],1,21,1)}" fill="{fg}"/>'  # body
      f'<path d="M30 -6 Q52 -16 62 -2 Q56 12 34 12Z" fill="{fg}"/>'               # head
      f'<circle cx="46" cy="-12" r="6.5" fill="{fg}"/><circle cx="47" cy="-12" r="2.6" fill="{INK}"/>'
      f'<path d="M24 12 L40 34 L52 38 L38 26 L30 8Z" fill="{fd}"/>'                # front leg
      f'<path d="M-30 4 Q0 14 34 6" fill="none" stroke="{fd}" stroke-width="2.4"/>'
      '</g>')
    # splash droplets
    for (x,y) in [(214,256),(240,250),(256,262),(200,262)]:
        o.append(f'<path d="M{x} {y} q3 -7 6 0 q-3 4 -6 0Z" fill="{CREAM}"/>')
    o.append(grain(p))
    return ''.join(o)

def scene_anchor(p):
    c=G['Workshop Diagnostic']; s=f'url(#{p}sh)'; s2=f'url(#{p}sh2)'
    o=[defs(p), f'<rect x="-10" y="-60" width="428" height="440" fill="#cfe3d6"/>']
    cols=['#a9cfb9',c['light'],'#5f9b83',c['mid'],'#245a4b']
    for i,col in enumerate(cols):
        o.append(f'<path d="{band(wave(40+i*48,7,8,i*0.9),seed=30+i)}" fill="{col}" filter="{s2}"/>')
    # sea floor street
    o.append(f'<path d="{band([(-10,298),(120,292),(260,300),(418,294)],seed=40)}" fill="#163a31" filter="{s}"/>')
    for x in range(10,408,46):
        o.append(f'<rect x="{x}" y="334" width="26" height="6" fill="{CREAM}" opacity=".85"/>')
    # bus stop sign
    o.append(f'<g filter="{s2}"><rect x="318" y="206" width="6" height="92" fill="{CREAM}"/>'
             f'<path d="{wob([(296,196),(346,196),(346,236),(296,236)],1,44,2)}" fill="{CREAM}"/>'
             f'<rect x="306" y="206" width="30" height="14" rx="3" fill="{c["dark"]}"/><circle cx="312" cy="224" r="3.2" fill="{c["dark"]}"/><circle cx="330" cy="224" r="3.2" fill="{c["dark"]}"/></g>')
    # bench
    o.append(f'<g filter="{s2}"><rect x="352" y="276" width="44" height="7" fill="{CREAM}"/><rect x="356" y="283" width="5" height="13" fill="{CREAM}"/><rect x="387" y="283" width="5" height="13" fill="{CREAM}"/></g>')
    # street lamp
    o.append(f'<g filter="{s2}"><rect x="62" y="186" width="6" height="110" fill="{CREAM}"/><path d="M50 190 L80 190 L74 176 L56 176Z" fill="{CREAM}"/><ellipse cx="65" cy="194" rx="12" ry="4" fill="#f6e3a0"/></g>')
    # rope from top
    o.append(f'<path d="M204 -4 Q198 60 206 118" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" opacity=".85"/>')
    # anchor (cut cream, hits the street)
    a=f'''<g filter="{s}" fill="{CREAM}">
<path fill-rule="evenodd" d="M206 104 a16 16 0 1 1 -0.1 0Z M206 113 a7 7 0 1 0 0.1 0Z"/>
<rect x="198" y="132" width="16" height="152" rx="3"/>
<path d="{wob([(170,150),(242,150),(242,164),(170,164)],0.8,50,2)}"/>
<path d="M150 252 Q160 300 206 302 Q252 300 262 252 L276 262 L262 226 L236 244 L250 252 Q244 284 206 286 Q168 284 162 252 L176 244 L150 226 L136 262Z"/>
</g>'''
    o.append(a)
    o.append(f'<path d="M150 302 q56 10 112 0" fill="none" stroke="{CREAM}" stroke-width="3" opacity=".6"/>')
    # bubbles
    for (x,y,r_) in [(232,90,5),(242,64,3.5),(228,40,4),(176,120,3)]:
        o.append(f'<circle cx="{x}" cy="{y}" r="{r_}" fill="none" stroke="{CREAM}" stroke-width="2"/>')
    o.append(grain(p))
    return ''.join(o)

def scene_camera(p):
    c=G['Drafty Air']; s=f'url(#{p}sh)'; s2=f'url(#{p}sh2)'
    o=[defs(p), f'<rect x="-10" y="-60" width="428" height="440" fill="#f3cdb2"/>']
    o.append(f'<path d="{band(wave(250,10,6,1.2),seed=60)}" fill="{c["light"]}" filter="{s2}"/>')
    o.append(f'<path d="{band(wave(292,12,5,2.4),seed=61)}" fill="{c["mid"]}" filter="{s}"/>')
    o.append(f'<path d="{band(wave(332,8,6,0.3),seed=62)}" fill="{c["dark"]}" filter="{s}"/>')
    def cloud(cx,cy,sc,seed):
        r=random.Random(seed); pts=[]
        for a in range(28):
            t=a/28*6.283; rad=1+0.18*math.sin(t*5+seed)+r.uniform(-.03,.03)
            pts.append((cx+sc*1.9*rad*math.cos(t), cy+sc*0.8*rad*math.sin(t)))
        flat=[(x,min(y,cy+sc*0.45)) for x,y in pts]
        return f'<path d="{wob(flat,1,seed,1)}" fill="{CREAM}" filter="{s2}"/>'
    o += [cloud(80,92,30,71), cloud(330,60,24,72), cloud(300,206,34,73), cloud(60,214,20,74)]
    # cut tether
    o.append(f'<path d="M232 196 C250 236 214 258 238 292" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="7 5"/>')
    o.append(f'<path d="M232 300 l12 -6 M234 288 l12 6" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    # camera, tilted, drifting
    o.append(f'''<g transform="translate(200 150) rotate(-17)" filter="{s}">
<path d="{wob([(-78,-40),(78,-40),(78,48),(-78,48)],1.2,80,3)}" fill="{CREAM}"/>
<path d="{wob([(-30,-40),(-16,-58),(22,-58),(34,-40)],1,81,2)}" fill="{CREAM}"/>
<rect x="-78" y="-14" width="156" height="12" fill="{c["mid"]}"/>
<circle cx="4" cy="6" r="34" fill="{c["dark"]}"/><circle cx="4" cy="6" r="25" fill="{c["light"]}"/><circle cx="4" cy="6" r="14" fill="{INK}"/>
<circle cx="-4" cy="-2" r="4.5" fill="{CREAM}"/>
<rect x="50" y="-34" width="18" height="10" rx="2" fill="{c["dark"]}"/>
</g>''')
    for i,(x,y) in enumerate([(92,140),(84,160),(96,180)]):
        o.append(f'<path d="M{x} {y} h{-30+i*6}" stroke="{c["dark"]}" stroke-width="4" stroke-linecap="round"/>')
    o.append(grain(p))
    return ''.join(o)

def scene_strange(p):
    c=G['Cliché Clinic']; s=f'url(#{p}sh)'; s2=f'url(#{p}sh2)'
    o=[defs(p), f'<rect x="-10" y="-60" width="428" height="440" fill="{c["dark"]}"/>']
    r=random.Random(90)
    for i in range(26):
        x=r.uniform(8,400); y=r.uniform(8,170); rr=r.uniform(1.2,2.6)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.1f}" fill="{CREAM}" opacity="{r.uniform(.5,.95):.2f}"/>')
    o.append(f'<path d="{band(wave(236,14,5,0.8),seed=91)}" fill="{c["mid"]}" filter="{s2}"/>')
    # the giant fork, monument-scale
    fork=f'''<g filter="{s}" fill="{CREAM}">
<path d="M164 40 L172 40 L174 150 L182 150 L184 40 L192 40 L194 150 L202 150 L204 40 L212 40 L214 150 L222 150 L224 40 L232 40 L234 168 Q232 196 208 204 L206 300 L190 300 L188 204 Q164 196 162 168Z"/>
</g>'''
    o.append(fork)
    o.append(f'<path d="M168 52 L170 146" stroke="{c["light"]}" stroke-width="2" opacity=".7"/>')
    o.append(f'<path d="{band(wave(286,8,6,2.1),seed=92)}" fill="#5d2c58" filter="{s}"/>')
    # winding path to the fork
    o.append(f'<path d="M150 380 C170 350 230 344 210 318 C200 306 196 300 198 292 L206 292 C210 304 238 330 214 352 C200 366 196 376 196 380Z" fill="{c["light"]}" opacity=".9" filter="{s2}"/>')
    # tiny traveler
    o.append(f'<g filter="{s2}" fill="{INK}"><circle cx="232" cy="318" r="5"/><path d="M228 324 L236 324 L238 344 L226 344Z"/><path d="M229 344 L227 354 M235 344 L238 354" stroke="{INK}" stroke-width="3" stroke-linecap="round"/></g>')
    o.append(f'<path d="{band([(-10,350),(120,340),(300,352),(418,344)],seed=93)}" fill="#3a1b37" filter="{s}"/>')
    o.append(grain(p,.08))
    return ''.join(o)
