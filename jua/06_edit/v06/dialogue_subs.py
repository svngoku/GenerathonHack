# v13 dialogue subtitles (English), same look as the v05 testimony subtitles: cream serif with a soft dark shadow, bottom centre.
# Usage: python3 dialogue_subs.py  -> dsub_<i>.png (1920x1080 RGBA), one per line in LINES
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1920, 1080
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 40)
LINES = [
    "Mum, look! There's a box… what is it?",
    "There's nothing written…",
    "Oh… this! Your aunt gave it to us.",
    "You know, back home… we have so few photos.\nI only have one of me as a child.",
    "Wow! We can see her face!",
    "Mbote, Mama Nzeba! (Hello, Mama Nzeba!)",
]
for i, t in enumerate(LINES):
    rows = t.split("\n"); lh = 52; y0 = 1004 - lh * len(rows)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    for k, r in enumerate(rows):
        x = (W - d.textlength(r, font=F)) / 2; d.text((x + 2, y0 + k * lh + 2), r, font=F, fill=(0, 0, 0, 230))
    sh = sh.filter(ImageFilter.GaussianBlur(3)); d = ImageDraw.Draw(sh)
    for k, r in enumerate(rows):
        x = (W - d.textlength(r, font=F)) / 2; d.text((x, y0 + k * lh), r, font=F, fill=(244, 234, 213, 255))
    sh.save(f"dsub_{i}.png")
print(len(LINES), "subtitles")
