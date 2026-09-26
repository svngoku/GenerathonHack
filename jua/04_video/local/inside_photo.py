# Shot "inside the photograph": four slow macro drifts over locked/original.png (K1 pixels only).
# Crop boxes are fractions of the print; each detail 4.5s with 0.5s dissolves. Output raw RGB 1920x1080 @24fps.
import sys, numpy as np
from PIL import Image
src=Image.open("locked/original.png").convert("RGB"); W0,H0=src.size
W,H,FPS=1920,1080,24
# (cx0,cy0,w0) -> (cx1,cy1,w1) as fractions of the print width/height; w = crop width fraction
details=[((0.515,0.21,0.20),(0.520,0.20,0.15)),   # headwrap + face
         ((0.455,0.74,0.20),(0.450,0.75,0.16)),   # folded hands
         ((0.420,0.90,0.26),(0.470,0.90,0.22)),   # liputa pattern
         ((0.930,0.76,0.14),(0.5,0.5,1.0))]   # torn edge, pulling back to the whole print
ease=lambda t:t*t*(3-2*t)
def frame(d,t):
    (a,b)=d; cx=a[0]+(b[0]-a[0])*t; cy=a[1]+(b[1]-a[1])*t; w=(a[2]+(b[2]-a[2])*t)*W0; h=w*9/16
    x0=min(max(cx*W0-w/2,0),W0-w); y0=min(max(cy*H0-h/2,0),H0-h)
    return np.asarray(src.resize((W,H),Image.LANCZOS,box=(x0,y0,x0+w,y0+h)),np.float32)
N=int(4.5*FPS); X=int(0.5*FPS); out=[]
for i,d in enumerate(details):
    for k in range(N):
        f=frame(d,ease(k/(N-1)))
        if i>0 and k<X:
            f=f*(k/X)+prev_last*(1-k/X)
        sys.stdout.buffer.write(np.clip(f,0,255).astype(np.uint8).tobytes())
    prev_last=frame(d,1.0)
