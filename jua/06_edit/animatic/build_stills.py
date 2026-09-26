# Local animatic beats 02 and 06 (no generation). Writes raw RGB frames to stdout.
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=854,480,24
serif=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",s)
tab=Image.open("06_edit/animatic/print_on_table.png").convert("RGB")
orig=Image.open("locked/original.png").convert("RGB")
def cap(img,text,size=16,pos="br",alpha=160):
    im=img.copy(); d=ImageDraw.Draw(im,"RGBA"); f=serif(size); tw=d.textlength(text,font=f)
    x,y=(W-tw-18,H-size-18) if pos=="br" else ((W-tw)/2,H-size-40)
    d.rectangle((x-6,y-4,x+tw+6,y+size+6),fill=(0,0,0,alpha)); d.text((x,y),text,fill=(244,234,213),font=f); return im
def emit(im,n):
    b=np.asarray(im.convert("RGB").resize((W,H))).tobytes()
    for _ in range(n): sys.stdout.buffer.write(b)
beat=sys.argv[1]
if beat=="02":   # 18s: original 3s, three placeholder stages 4s each, wipe back 3s
    base=orig.resize((W,H))
    emit(cap(base,"original · fictional, generated"),3*FPS)
    for s in ["stage 1 · dust · [model]","stage 2 · cracks · [model]","stage 3 · clarity · [model]"]:
        emit(cap(base,s+"  (placeholder — restoration not run yet)"),4*FPS)
    emit(cap(base,"original"),3*FPS)
elif beat=="06": # 5s: side by side + end line + disclosure
    im=Image.new("RGB",(W,H),(28,24,20)); w=400; h=round(orig.height*w/orig.width)
    im.paste(orig.resize((w,h)),(18,60)); im.paste(orig.resize((w,h)),(W-w-18,60))
    d=ImageDraw.Draw(im); f=serif(13); d.text((18,60+h+6),"original",fill=(200,190,170),font=f); d.text((W-w-18,60+h+6),"restored (placeholder)",fill=(200,190,170),font=f)
    f2=serif(20); t="We can restore the image. We remember the person together."; d.text(((W-d.textlength(t,font=f2))/2,370),t,fill=(244,234,213),font=f2)
    f3=serif(13); t2="Fictional proof of concept. No real person is depicted."; d.text(((W-d.textlength(t2,font=f3))/2,410),t2,fill=(200,190,170),font=f3)
    emit(im,5*FPS)
