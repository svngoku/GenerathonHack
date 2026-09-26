# Bake the name "Mama Nzeba" (Caveat, OFL) onto shot 05, revealed left->right with the pen (3.5s->10.5s).
# Ink is applied only on paper-coloured pixels, so it never paints over the hand. Reads/writes raw RGB 1920x1080.
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1920,1080,24
font=ImageFont.truetype("Caveat.ttf",86); font.set_variation_by_name("Regular") if hasattr(font,"set_variation_by_name") else None
txt="Mama Nzeba"; m=Image.new("L",(W,H),0); d=ImageDraw.Draw(m)
tw=d.textlength(txt,font=font); x0=1140-tw; y0=500
d.text((x0,y0),txt,fill=255,font=font); mask=np.asarray(m,np.float32)/255
xs=np.arange(W)[None,:]; ink=np.array([38,30,26],np.float32)
n=0; fb=W*H*3
while True:
    buf=sys.stdin.buffer.read(fb)
    if len(buf)<fb: break
    f=np.frombuffer(buf,np.uint8).reshape(H,W,3).astype(np.float32); t=n/FPS
    p=min(1,max(0,(t-3.5)/7.0)); edge=x0+tw*p
    reveal=(xs<edge).astype(np.float32)
    paper=((f.mean(axis=2)>150)&(f[...,0]>f[...,2])).astype(np.float32)   # light, warm = sleeve paper
    a=(mask*reveal*paper*0.9)[...,None]
    sys.stdout.buffer.write(np.clip(f*(1-a)+ink*a,0,255).astype(np.uint8).tobytes()); n+=1
