# v14: 3 s on the locked restored portrait (black-and-white, untouched pixels), slow push 1.00 -> 1.05 toward her face,
# then a hard cut into her colour memory. Usage: python3 portrait_in.py | ffmpeg -f rawvideo -pix_fmt rgb24 -s 1920x1080 -r 24 -i - ...
import sys
from PIL import Image
W, H, FPS, D = 1920, 1080, 24, 3.0
src = Image.open("../../locked/restored.png").convert("RGB"); w0, h0 = src.size
ease = lambda t: t * t * (3 - 2 * t); n = int(D * FPS)
for i in range(n):
    z = 1 + 0.05 * ease(i / (n - 1)); ch = h0 / z; cw = ch * 16 / 9
    cx, cy = w0 * (0.5 + 0.02 * ease(i / (n - 1))), h0 / 2
    sys.stdout.buffer.write(src.resize((W, H), Image.LANCZOS, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)).tobytes())
