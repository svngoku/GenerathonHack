# Shot 02 (18s): original 3s -> stage1 -> stage2 -> stage3 (4s each, 1s crossfades) -> wipe back to original 3s.
# Corner caption "stage N · step · model" (serif, 60% opacity). Raw RGB 1920x1080 @24 to stdout.
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1920,1080,24
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",30)
def load(p): return Image.open(p).convert("RGB").resize((W,H),Image.LANCZOS)
def cap(im,t):
    im=im.copy(); d=ImageDraw.Draw(im,"RGBA"); tw=d.textlength(t,font=f); x,y=W-tw-48,H-78
    d.rectangle((x-12,y-8,x+tw+12,y+44),fill=(0,0,0,110)); d.text((x,y),t,fill=(244,234,213,153),font=f); return np.asarray(im,np.float32)
seq=[("locked/original.png","original · 1972 · fictional"),("03_restore/stage_1_dust.png","stage 1 · dust · Nano Banana 2"),
     ("03_restore/stage_2_cracks.png","stage 2 · crack repair · Nano Banana 2"),("03_restore/stage_3_clarity.png","stage 3 · clarity · Nano Banana 2")]
fr=[cap(load(p),t) for p,t in seq]; orig=fr[0]
out=lambda a: sys.stdout.buffer.write(np.clip(a,0,255).astype(np.uint8).tobytes())
for _ in range(3*FPS): out(fr[0])
for i in range(1,4):
    for k in range(FPS): a=k/FPS; out(fr[i-1]*(1-a)+fr[i]*a)
    for _ in range(3*FPS): out(fr[i])
xs=np.arange(W)[None,:,None]
for k in range(2*FPS):          # wipe back to the original, left to right
    edge=W*(k/(2*FPS-1)); m=(xs<edge).astype(np.float32); out(orig*m+fr[3]*(1-m))
for _ in range(FPS): out(orig)
