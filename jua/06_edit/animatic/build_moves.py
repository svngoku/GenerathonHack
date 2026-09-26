# Local camera moves over the locked composite (no generation): 01 pan, 03 push + light band.
import sys, numpy as np
from PIL import Image
src=Image.open("print_on_table.png").convert("RGB")   # 1920x1080: K1 on locked table
W,H,FPS=int(sys.argv[2]),int(sys.argv[3]),24
ease=lambda t:t*t*(3-2*t)
def frames(c0,w0,c1,w1,n,band=False):
    xs=np.arange(W)[None,:].astype(np.float32); ys=np.arange(H)[:,None].astype(np.float32)
    warm=np.array([217,163,95],np.float32)
    for i in range(n):
        t=ease(i/(n-1)); w=w0+(w1-w0)*t; h=w*9/16
        cx=c0[0]+(c1[0]-c0[0])*t; cy=c0[1]+(c1[1]-c0[1])*t
        x0=min(max(cx-w/2,0),1920-w); y0=min(max(cy-h/2,0),1080-h)
        fr=np.asarray(src.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+w,y0+h)),np.float32)
        if band:
            pos=-0.3*W+1.6*W*(i/(n-1)); d=(xs+0.35*ys-pos)/(0.22*W); b=np.exp(-d*d)*0.22
            fr=fr*(1-b[...,None])+(fr*0.6+warm*0.55)*b[...,None]
        sys.stdout.buffer.write(np.clip(fr,0,255).astype(np.uint8).tobytes())
if sys.argv[1]=="01": frames((1400,600),900,(950,330),700,10*FPS)
if sys.argv[1]=="03": frames((960,540),1920,(950,310),640,10*FPS,band=True)
