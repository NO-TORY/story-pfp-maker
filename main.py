from __future__ import division
from PIL import Image, ImageDraw, ImageFont
from contextlib import closing
from os.path import isfile

assert isfile("LuckiestGuy.ttf")

ment = None
fontsize = 1
font = ImageFont.truetype("LuckiestGuy.ttf", fontsize)

while ment == None:
    ment = input("중간에 들어갈 영어 단어를 입력해주세요>>> ")

with closing(Image.new("RGB", size=(2500, 2500))) as base:
    base.save("base.jpg")
    size = base.size

while (font.getsize(ment)[0] < 2000) and (font.getsize(ment)[1] < 2000):
    fontsize += 1
    font = ImageFont.truetype("LuckiestGuy.ttf", fontsize)

fontsize -= 15
font = ImageFont.truetype("LuckiestGuy.ttf", fontsize)

with closing(Image.open("base.jpg")) as base:
    draw = ImageDraw.Draw(base, "RGB")
    draw.text(
        (300, 1000 - len(ment)),
        ment,
        font=font,
    )
    base.save("%s.jpg"%ment)
    base.show()
