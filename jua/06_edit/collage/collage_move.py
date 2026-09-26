# Local 12 s pull-back over the locked collage keyframe: starts on the named sleeve, ends on the whole family arrangement.
import sys, numpy as np
from PIL import Image
W, H, FPS, D = 1920, 1080, 24, float(sys.argv[1]) if len(sys.argv) > 1 else 12
src = Image.open("kf_collage_b_locked.png").convert("RGB"); w0, h0 = src.size
ease = lambda t: t * t * (3 - 2 * t)
n = int(D * FPS)
for i in range(n):
    t = ease(i / (n - 1)); z = 2.1 + (1.0 - 2.1) * t
    cw, ch = w0 / z, h0 / z
    cx = w0 * (0.472 + (0.5 - 0.472) * t); cy = h0 * (0.725 + (0.5 - 0.725) * t)
    cx = min(max(cx, cw / 2), w0 - cw / 2); cy = min(max(cy, ch / 2), h0 - ch / 2)
    sys.stdout.buffer.write(src.resize((W, H), Image.LANCZOS, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)).tobytes())
