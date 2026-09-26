# v06 bridge for the 1:18–1:31 room beat (no generation).
# room_A (Seedance 2.5, 8.08 s) + 8.8 s held on its last frame, with ONE continuous slow push-in towards the table,
# so the dissolve into shot04 (hands on the table) arrives on a table, not on a wide room. "Le soir je vais revenir."
# Usage: python3 room_push.py | ffmpeg -f rawvideo -pix_fmt rgb24 -s 1920x1080 -r 24 -i - ...
import sys, subprocess, numpy as np
from PIL import Image
import imageio_ffmpeg
W, H, FPS = 1920, 1080, 24
SRC = "../../04_video/seedance25/room_A.mp4"; SW, SH = 1280, 720
HOLD = 8.8; Z1 = 1.30; CX1, CY1 = 0.36, 0.56      # end box centred on the table top
ease = lambda t: t * t * (3 - 2 * t)
p = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-i", SRC, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
frames = []
while True:
    b = p.stdout.read(SW * SH * 3)
    if len(b) < SW * SH * 3: break
    frames.append(b)
frames += [frames[-1]] * int(HOLD * FPS)
n = len(frames)
for i, b in enumerate(frames):
    t = ease(i / (n - 1)); z = 1 + (Z1 - 1) * t
    cw, ch = SW / z, SH / z
    cx = min(max(SW * (0.5 + (CX1 - 0.5) * t), cw / 2), SW - cw / 2)
    cy = min(max(SH * (0.5 + (CY1 - 0.5) * t), ch / 2), SH - ch / 2)
    im = Image.frombytes("RGB", (SW, SH), b).resize((W, H), Image.LANCZOS, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))
    sys.stdout.buffer.write(im.tobytes())
