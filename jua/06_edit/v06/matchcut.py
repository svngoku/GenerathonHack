# Match cuts (Marty, v15): every change of scene is a HARD cut, and each cut is aligned pixel by pixel.
# For each cut, compare the outgoing last frame (A) with the incoming first frame (B) on edge maps, and search
# a zoom box (1.0-2.0x) on A or on B that makes the two frames coincide (normalised cross-correlation, FFT).
# If the match is clearly better than the plain cut:
#   - zoom box on A -> A pushes in over its last D seconds and lands exactly on B's composition at the cut;
#   - zoom box on B -> B opens on A's composition and eases back to its own framing over D seconds.
# Operates in place on the normalised segments g??.mp4 written by `STOP=segs KEEP=1 build_v06.py`,
# then `SKIP_G=1 build_v06.py` rebuilds the picture with hard cuts. Report -> matchcut_report.json
import json, os, subprocess, numpy as np, imageio_ffmpeg
from PIL import Image
FF = imageio_ffmpeg.get_ffmpeg_exe(); W, H, FPS, D = 1920, 1080, 24, 1.25
T = json.load(open(os.environ.get("TIMELINE", "timeline_v15.json"))); B = T["bounds"]; SEG = T["segments"]
L = json.load(open("seg_layout.json")); starts = L["starts"]
SKIP_CUTS = set(os.environ.get("NOMATCH", "").split(",")) - {""}   # segment names whose incoming cut stays plain
TW, TH = 192, 108; ease = lambda t: t * t * (3 - 2 * t)

def frame(f, t):
    raw = subprocess.run([FF, "-loglevel", "error", "-ss", f"{max(t,0):.3f}", "-i", f, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return Image.frombytes("RGB", (W, H), raw[:W * H * 3])
def feat(im, w, h):
    g = np.asarray(im.convert("L").resize((w, h), Image.BILINEAR), np.float32)
    gx = np.zeros_like(g); gy = np.zeros_like(g); gx[:, 1:-1] = g[:, 2:] - g[:, :-2]; gy[1:-1] = g[2:] - g[:-2]
    m = np.hypot(gx, gy); return 0.7 * m / (m.std() + 1e-6) + 0.3 * (g - g.mean()) / (g.std() + 1e-6)
def ncc_map(img, tpl):
    th, tw = tpl.shape; t = (tpl - tpl.mean()) / (tpl.std() * tpl.size + 1e-6)
    F = np.fft.rfft2(img); num = np.fft.irfft2(F * np.conj(np.fft.rfft2(t, img.shape)), img.shape)
    c = np.cumsum(np.cumsum(np.pad(img, ((1, 0), (1, 0))), 0), 1); c2 = np.cumsum(np.cumsum(np.pad(img ** 2, ((1, 0), (1, 0))), 0), 1)
    win = lambda cc: cc[th:, tw:] - cc[:-th, tw:] - cc[th:, :-tw] + cc[:-th, :-tw]
    n = th * tw; s = win(c); s2 = win(c2); sd = np.sqrt(np.maximum(s2 / n - (s / n) ** 2, 1e-6))
    return num[: img.shape[0] - th + 1, : img.shape[1] - tw + 1] / sd
def search(zoomed, fixed):
    tpl = feat(fixed, TW, TH); best = (-1, 1.0, 0.0, 0.0)
    for z in np.arange(1.0, 2.001, 0.05):
        w, h = int(round(TW * z)), int(round(TH * z)); m = ncc_map(feat(zoomed, w, h), tpl)
        y, x = np.unravel_index(np.argmax(m), m.shape)
        if m[y, x] > best[0]: best = (float(m[y, x]), float(z), x / w, y / h)
    return best   # (score, zoom, box x0, box y0) in normalised coords, box size 1/zoom
def crop(im, box):
    x0, y0, s = box; return im.resize((W, H), Image.LANCZOS, box=(x0 * W, y0 * H, (x0 + s) * W, (y0 + s) * H))
def rewrite(f, fn):
    n = int(round(float(subprocess.run([FF, "-i", f], capture_output=True, text=True).stderr.split("Duration: ")[1].split(",")[0].split(":")[2]) * FPS)) + 2
    p = subprocess.Popen([FF, "-loglevel", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    q = subprocess.Popen([FF, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-pix_fmt", "yuv420p", f + ".tmp.mp4"], stdin=subprocess.PIPE)
    i = 0
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        q.stdin.write(fn(i / FPS, Image.frombytes("RGB", (W, H), b)).tobytes()); i += 1
    q.stdin.close(); q.wait(); os.replace(f + ".tmp.mp4", f)

report = []
for k in range(1, len(SEG)):
    a, b = f"g{k-1:02d}.mp4", f"g{k:02d}.mp4"; tcut = B[k] - starts[k - 1] - 1 / 48
    A, Bf = frame(a, tcut - 1 / 24), frame(b, 0)
    ident = float(ncc_map(feat(A, TW, TH), feat(Bf, TW, TH)).max())
    sa, sb = search(A, Bf), search(Bf, A)
    side, (sc, z, x0, y0) = ("out", sa) if sa[0] >= sb[0] else ("in", sb)
    use = SEG[k]["name"] not in SKIP_CUTS and z > 1.04 and sc > 0.30 and sc - ident > 0.06
    report.append(dict(cut=f"{SEG[k-1]['name']}->{SEG[k]['name']}", at=B[k], plain=round(ident, 3), best=round(sc, 3), side=side, zoom=round(z, 2), box=[round(x0, 3), round(y0, 3)], applied=use))
    print(report[-1], flush=True)
    if not use: continue
    box = (x0, y0, 1 / z); full = (0.0, 0.0, 1.0)
    lerp = lambda u: tuple(f0 + (f1 - f0) * ease(u) for f0, f1 in zip(full, box))
    if side == "out":   # push in on A during its last D s, land on the matched box at the cut
        rewrite(a, lambda t, im: crop(im, lerp(min(1, max(0, (t - (tcut - D)) / D)))) if t > tcut - D else im)
    else:               # B opens on the matched box and eases back to its own framing
        rewrite(b, lambda t, im: crop(im, lerp(1 - min(1, t / D))) if t < D else im)
json.dump(report, open("matchcut_report.json", "w"), indent=1)
