# Local beats for v05 (no generation). Usage: locals.py <beat>  -> raw RGB 1920x1080 @24 to stdout
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1920,1080,24; R="../../"
serif=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",s)
out=lambda a: sys.stdout.buffer.write(np.clip(a,0,255).astype(np.uint8).tobytes())
ease=lambda t:t*t*(3-2*t)
b=sys.argv[1]; D=float(sys.argv[2]) if len(sys.argv)>2 else 16
if b=="face":   # 16s slow push on the RESTORED face (locked/restored.png), during the voice
    src=Image.open(R+"locked/restored.png").convert("RGB"); w0,h0=src.size
    n=int(D*FPS)
    for i in range(n):
        t=ease(i/(n-1)); cw=w0*(0.34-0.10*t); ch=cw*9/16; cx=w0*0.515; cy=h0*(0.26-0.02*t)
        out(np.asarray(src.resize((W,H),Image.LANCZOS,box=(cx-cw/2,cy-ch/2,cx+cw/2,cy+ch/2)),np.float32))
elif b=="side":  # 12s original | restored, slow settle
    o=Image.open(R+"locked/original.png").convert("RGB"); r=Image.open(R+"locked/restored.png").convert("RGB")
    bg=Image.new("RGB",(W,H),(24,20,17)); pw=900; ph=round(pw*o.height/o.width)
    bg.paste(o.resize((pw,ph),Image.LANCZOS),(40,(H-ph)//2-40)); bg.paste(r.resize((pw,ph),Image.LANCZOS),(W-pw-40,(H-ph)//2-40))
    d=ImageDraw.Draw(bg); f=serif(26); y=(H-ph)//2-40+ph+14
    d.text((40,y),"original",fill=(200,190,170),font=f); d.text((W-pw-40,y),"restored · Nano Banana 2",fill=(200,190,170),font=f)
    a=np.asarray(bg,np.float32)
    for i in range(12*FPS): out(a*min(1,i/FPS))
elif b=="end":   # 10s end card
    bg=Image.new("RGB",(W,H),(24,20,17)); d=ImageDraw.Draw(bg)
    lines=[("We can restore the image. We remember the person together.",serif(44),(244,234,213),420),
           ("Fictional proof of concept. No real person is depicted.",serif(26),(200,190,170),540),
           ("Voice: AI-generated (Arcads · ElevenLabs), fictional testimony.",serif(26),(200,190,170),585),
           ("Music: Tabu Ley Rochereau, “Pitié”",serif(26),(200,190,170),630),
           ("Made with Jua pipeline in Arcads — umojua.com",serif(22),(160,150,135),720)]
    for t,f,c,y in lines: d.text(((W-d.textlength(t,font=f))/2,y),t,fill=c,font=f)
    a=np.asarray(bg,np.float32)
    for i in range(10*FPS): out(a*min(1,i/FPS,(10*FPS-i)/FPS))
