# Put the locked print pixels back into a Nano Banana collage frame (it may redraw faces).
# Keeps NB's light/shadows/curls on the table; each print's picture area comes from base_collage.png,
# tone-matched to NB's local mean/std, with a feathered edge. Usage: relock.py nb.png out.png
import sys, numpy as np
from PIL import Image, ImageFilter
exec(open("base_collage.py").read().split("# the sleeve paper")[0].replace("bg = ", "_bg = "))  # helpers only
W, H = 2752, 1536
masks = []
def mplace(w, h, border_px, cx, cy, rot, inset):
    m = Image.new("L", (w + 2 * border_px, h + 2 * border_px), 0)
    m.paste(255, (border_px + inset, border_px + inset, border_px + w - inset, border_px + h - inset))
    m = m.rotate(rot, Image.BICUBIC, expand=True); full = Image.new("L", (W, H), 0)
    full.paste(m, (int(cx - m.width / 2), int(cy - m.height / 2))); masks.append(full)
b = lambda w: round(w * 0.035)
mplace(640, 360, b(640), 2250, 470, -5, 14)     # K2 (16:9)
mplace(620, 346, b(620), 2230, 1130, 4, 14)     # K3
mplace(760, 428, 0, 520, 640, 5, 16)            # original
mplace(980, 547, b(980), 1330, 480, -2, 14)     # restored
base = np.asarray(Image.open("base_collage.png").convert("RGB"), np.float32)
nb = np.asarray(Image.open(sys.argv[1]).convert("RGB").resize((W, H), Image.LANCZOS), np.float32)
out = nb.copy()
for m in masks:
    a = np.asarray(m.filter(ImageFilter.GaussianBlur(6)), np.float32)[..., None] / 255
    sel = np.asarray(m) > 250
    src = (base - base[sel].mean(0)) / (base[sel].std(0) + 1e-6) * nb[sel].std(0) + nb[sel].mean(0)
    out = out * (1 - a) + src * a
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(sys.argv[2])
