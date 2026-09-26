# Final collage base (locked pixels only): the family arrangement on the locked table.
# restored print (centre), worn original (left), K2 + K3 souvenirs (right), the named sleeve (front).
# The name is baked handwriting (Caveat, OFL), never generated.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = "../../"
bg = Image.open("table_warm.png")  # locked/table_close.png colour-matched to the shot-05 table.convert("RGB"); W, H = bg.size
def framed(im, w, border=0.035):
    h = round(w * im.height / im.width); im = im.convert("RGB").resize((w, h), Image.LANCZOS)
    b = round(w * border); out = Image.new("RGB", (w + 2 * b, h + 2 * b), (236, 229, 214)); out.paste(im, (b, b)); return out
def place(im, cx, cy, rot):
    im = im.convert("RGBA").rotate(rot, Image.BICUBIC, expand=True)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.getchannel("A").point(lambda a: int(a * 0.55)))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    bg.paste(sh, (x + 10, y + 16), sh); bg.paste(im, (x, y), im)
# the sleeve paper from locked/sleeve.png, with the name baked in Caveat
sl = Image.open(R + "locked/sleeve.png").convert("RGB").crop((695, 282, 2023, 1259))
d = ImageDraw.Draw(sl); f = ImageFont.truetype("../v05/Caveat.ttf", 190); t = "Mama Nzeba"
d.text(((sl.width - d.textlength(t, font=f)) / 2, sl.height * 0.36), t, font=f, fill=(34, 42, 78))
sl = sl.resize((round(sl.width * 0.62), round(sl.height * 0.62)), Image.LANCZOS)
place(framed(Image.open(R + "02_source/portrait_k72/K2_seedream.jpg"), 640), 2250, 470, -5)
place(framed(Image.open(R + "02_source/portrait_k72/K3_nano.png"), 620), 2230, 1130, 4)
place(Image.open(R + "locked/original.png").resize((760, 428), Image.LANCZOS), 520, 640, 5)
place(framed(Image.open(R + "locked/restored.png"), 980), 1330, 480, -2)
place(sl, 1300, 1120, 1.5)
bg.save("base_collage.png"); print(bg.size)
