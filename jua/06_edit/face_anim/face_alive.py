# 1:52.75-2:12.25 face beat (Marty: "make her smile and eyes blinking" — rule exception, disclosed on the end card).
# Part 1 (9.5 s): locked pixels of the restored face (kf_face.png = crop of locked/restored.png), gentle push 1.00 -> 1.03.
# Part 2 (10 s): the Kling 3.0 Pro take (true start frame = this locked frame; Seedance 2.5 re-drew her face) that starts on that same frame (blink, then a small closed-lip smile), held at 1.03,
# so the join is invisible and she comes alive under "Cette photo… pour qu'on se souvienne de son visage".
# Usage: python3 face_alive.py take.mp4 | ffmpeg -f rawvideo -pix_fmt rgb24 -s 1920x1080 -r 24 -i - ...
import sys, subprocess, numpy as np, imageio_ffmpeg
from PIL import Image
W, H, FPS = 1920, 1080, 24; Z = 1.03; P1 = 9.5
ease = lambda t: t * t * (3 - 2 * t)
def zoom(im, z):
    w, h = im.size; cw, ch = w / z, h / z
    return im.resize((W, H), Image.LANCZOS, box=((w - cw) / 2, (h - ch) / 2, (w + cw) / 2, (h + ch) / 2))
kf = Image.open("kf_face.png").convert("RGB")
n1 = int(P1 * FPS)
for i in range(n1):
    sys.stdout.buffer.write(zoom(kf, 1 + (Z - 1) * ease(i / (n1 - 1))).tobytes())
p = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-i", sys.argv[1], "-vf", "fps=24", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
SW, SH = 1920, 1080
while True:
    b = p.stdout.read(SW * SH * 3)
    if len(b) < SW * SH * 3: break
    sys.stdout.buffer.write(zoom(Image.frombytes("RGB", (SW, SH), b), Z).tobytes())
