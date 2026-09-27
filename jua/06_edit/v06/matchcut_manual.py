# Object match cuts set by hand (v15): the print of Mama Nzeba stays at the same place and size across the cut.
#   touch -> album : album opens zoomed on the print being mounted (same place/size as the print on the table), eases out.
#   album -> wall  : album pushes in on her print in the album; hard cut to the framed portrait at the same place.
import json, sys
sys.argv = ["x"]; exec(open("matchcut.py").read().split("report = []")[0])   # reuse frame/crop/rewrite/ease
MAN = [("album", "in", (0.263, 0.382, 0.4545)), ("wall", "out", (0.235, 0.26, 0.417))]
names = [s["name"] for s in SEG]
for name, side, box in MAN:
    k = names.index(name); a, b = f"g{k-1:02d}.mp4", f"g{k:02d}.mp4"; tcut = B[k] - starts[k - 1] - 1 / 48
    full = (0.0, 0.0, 1.0); lerp = lambda u, box=box: tuple(f0 + (f1 - f0) * ease(u) for f0, f1 in zip(full, box))
    if side == "out": rewrite(a, lambda t, im: crop(im, lerp(min(1, max(0, (t - (tcut - D)) / D)))) if t > tcut - D else im)
    else: rewrite(b, lambda t, im: crop(im, lerp(1 - min(1, t / D))) if t < D else im)
    print("manual match", name, side, box)
