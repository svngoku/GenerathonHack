# Hybrid shot 05 (keeps the "no generated lettering" rule): Seedance take B mimes writing but left faint pencil
# gibberish. (1) erase it: inside the writing band, paper pixels are restored from frame 0 (static camera; the hand,
# darker, is never touched); (2) bake "Mama Nzeba" (Caveat, OFL), revealed left->right following the model's own
# stroke progress (rightmost changed column in the band), so the ink appears under the pen.
import sys, subprocess, numpy as np, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
FF = imageio_ffmpeg.get_ffmpeg_exe(); SW, SH = 1280, 720; W, H = 1920, 1080
BAND = (590, 330, 820, 390)              # x0,y0,x1,y1 at 720p, where B writes
raw = subprocess.run([FF, "-loglevel", "error", "-i", "name_B_mime.mp4", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, SH, SW, 3).astype(np.float32)
x0, y0, x1, y1 = BAND
from scipy_free import dilate
band = fr[:, y0:y1, x0:x1]
clean = band.max(0)                                        # clean paper plate: brightest value over time (ink and hand only darken)
last = band[-1]
ink_last = dilate(((clean.mean(2) - last.mean(2)) > 12) & ((clean.mean(2) - last.mean(2)) < 70), 2)
prog = []
for b in band:
    dk = clean.mean(2) - b.mean(2); d = (dk > 12) & (dk < 70) & ink_last
    prog.append(d.sum() / max(ink_last.sum(), 1))
prog = np.maximum.accumulate(np.clip((np.array(prog, np.float32) - 0.05) / 0.9, 0, 1))
# name mask at 720p, centred in the band
m = Image.new("L", (SW, SH), 0); dr = ImageDraw.Draw(m); font = ImageFont.truetype("../../06_edit/v05/Caveat.ttf", 44)
t = "Mama Nzeba"; tw = dr.textlength(t, font=font); tx = x0 + (x1 - x0 - tw) / 2; dr.text((tx, y0 + 2), t, font=font, fill=255)
mask = np.asarray(m, np.float32) / 255; xs = np.arange(SW)[None, :]; ink = np.array([34, 42, 78], np.float32)
out = subprocess.Popen([FF, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{SW}x{SH}", "-r", "24", "-i", "-",
                        "-i", "name_B_mime.mp4", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", "name_B_hybrid.mp4"], stdin=subprocess.PIPE)
for i, f in enumerate(fr):
    f = f.copy(); b = f[y0:y1, x0:x1]
    hand = dilate((clean.mean(2) - b.mean(2)) > 70, 10)
    er = (ink_last & ~hand)[..., None]; f[y0:y1, x0:x1] = np.where(er, clean, b)
    notHand = np.ones((SH, SW), bool); notHand[y0:y1, x0:x1] = ~hand
    edge = tx + tw * prog[i]; a = (mask * (xs < edge) * notHand * 0.92)[..., None]
    out.stdin.write(np.clip(f * (1 - a) + ink * a, 0, 255).astype(np.uint8).tobytes())
out.stdin.close(); out.wait(); print("prog at 3/6/9/12s:", [round(float(prog[min(int(s*24), len(prog)-1)]), 2) for s in (3, 6, 9, 12)])
