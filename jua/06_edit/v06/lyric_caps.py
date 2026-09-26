# Lyric captions for v06: the scene is linked to the line of "Pitié" that is playing (lyrics as sung, EN translation ours).
# Drawn as PNG overlays (no generated lettering). Style differs from the testimony subtitles (bottom-centre, upright):
# lower-left, slanted serif, with a small note mark, so a viewer knows it is the song, not the witness.
import json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1920, 1080
F = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CAPS = json.load(open("lyric_caps.json"))

def slanted(text, size, fill):
    f = ImageFont.truetype(F, size)
    w = int(f.getlength(text)) + size; h = int(size * 1.5)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(im).text((size // 4, 0), text, font=f, fill=fill)
    k = 0.2  # fake italic: shear right
    return im.transform((w + int(k * h), h), Image.AFFINE, (1, k, -k * h, 0, 1, 0), Image.BICUBIC)

for i, c in enumerate(CAPS):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fr = slanted("♪  " + c["fr"], 38, (246, 236, 214, 255)); en = slanted(c["en"], 27, (214, 202, 180, 235))
    x, y = 96, H - 205
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.alpha_composite(fr, (x, y)); sh.alpha_composite(en, (x + 44, y + 56))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); shadow.putalpha(sh.getchannel("A").filter(ImageFilter.GaussianBlur(6)).point(lambda a: int(a * 0.8)))
    im.alpha_composite(shadow, (2, 3)); im.alpha_composite(sh)
    im.save(f"lyr_{i}.png")
    print(i, c["t0"], c["t1"], c["fr"])
