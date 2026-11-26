# Xenos avatars from Filament's 2012 concept sheet (Matt holds the rights). Outfit, hair and skin recoloured per character.
import numpy as np, cv2, json, base64, io
from PIL import Image
L={ # name: fig, top hue, bottom hue (None keeps), hair (h,s,v scale), skin value scale
 'You':(5,None,None,(20,.35,.45),1.0),
 'Geoffrey':(4,130,30,(25,.55,.7),.82),
 'christine':(18,355,42,(0,.1,.35),1.18),
 'dan':(2,0,None,(45,.55,1.25),1.25),
 'Rosa':(21,285,None,(18,.6,.75),1.0),
 'Coach Alex':(7,24,215,(0,.1,.4),1.08),
 'Nadeem':(3,170,None,(0,.05,.3),.9),
 'Mei':(25,48,215,(0,.08,.25),1.2)}
out={};tiles=[]
for name,(fi,top,bot,hair,skin) in L.items():
    im=np.array(Image.open(f'fig_{fi:02d}.png').convert('RGBA')).astype(np.float32);rgb=im[...,:3].astype(np.uint8)
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV_FULL).astype(np.float32);H,S,V=hsv[...,0]*360/255,hsv[...,1]/255,hsv[...,2]/255
    h_,w_=H.shape;yy=np.mgrid[0:h_,0:w_][0]/h_
    cloth=(H>185)&(H<232)&(S>.22)&(V>.40)
    hairm=(H>215)&(H<300)&(V<.62)&(yy<.30)
    skinm=(H>8)&(H<45)&(S>.25)
    def shift(mask,hue,sat=1.0):
        H[mask]=hue;S[mask]=np.clip(S[mask]*sat,0,1)
    if top is not None:shift(cloth&(yy<.56),top,1.0 if top not in (0,48,24) else 1.05)
    if bot is not None:shift(cloth&(yy>=.56),bot)
    if top==0:  # dan: white tank top
        m=cloth&(yy<.56);S[m]*=.12;V[m]=np.clip(V[m]*1.25+.1,0,1)
    if hair:
        hh,ss,vv=hair;H[hairm]=hh;S[hairm]=np.clip(ss+S[hairm]*.2,0,1);V[hairm]=np.clip(V[hairm]*vv+.04,0,1)
    V[skinm]=np.clip(V[skinm]*skin,0,1);S[skinm]=np.clip(S[skinm]*(1/skin)**.6,0,1)
    hsv2=np.dstack([H*255/360,S*255,V*255]).clip(0,255).astype(np.uint8)
    rgb2=cv2.cvtColor(hsv2,cv2.COLOR_HSV2RGB_FULL);a=im[...,3]
    # soft 1px alpha edge, defringe white halo from the jpeg
    a2=cv2.GaussianBlur(a,(0,0),.6);edge=(a>0)&(cv2.erode((a>0).astype(np.uint8),np.ones((3,3),np.uint8))==0)
    rgb2[edge]=(rgb2[edge]*.55).astype(np.uint8)
    tile=Image.fromarray(np.dstack([rgb2,a2.astype(np.uint8)]));tiles.append((name,tile))
# pack in a row
W=sum(t.width+4 for _,t in tiles);Hh=max(t.height for _,t in tiles);atl=Image.new('RGBA',(W,Hh));x=0;meta={}
for name,t in tiles:
    atl.paste(t,(x,0));a=np.array(t)[...,3];ys,xs=np.where(a>40)
    foot=int(ys.max());fx=int(np.median(xs[ys>foot-10]))  # feet anchor
    hip=int(foot*.56);cut=int(foot*.64)
    row=np.where(a[cut]>60)[0];runs=[];st=None
    for i,v in enumerate(row):
        if st is None:st=v
        if i==len(row)-1 or row[i+1]!=v+1:runs.append((st,v));st=None
    big=max(runs,key=lambda r:r[1]-r[0]) if runs else (fx,fx);hx=int((big[0]+big[1])/2)
    meta[name]=dict(x=x,y=0,w=t.width,h=t.height,ax=fx,ay=foot,hip=hip,cut=cut,hx=hx,amp={'christine':.35,'Mei':.55,'Rosa':.9}.get(name,1.0));x+=t.width+4
atl.save('avatar_atlas.png');b=io.BytesIO();atl.save(b,'WEBP',quality=92,method=6)
json.dump({'meta':meta,'png':'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()},open('avatars.json','w'))
c=Image.new('RGBA',atl.size,(120,190,90,255));c.alpha_composite(atl);c.convert('RGB').resize((atl.width*2,atl.height*2),Image.NEAREST).save('/tmp/avatars.jpg',quality=90)
print(atl.size,len(b.getvalue())//1024,'KB')
