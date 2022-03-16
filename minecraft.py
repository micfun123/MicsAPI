from PIL import Image, ImageDraw, ImageFont
import textwrap

astr = '''Test of my new API like it?'''
para = textwrap.wrap(astr, width=15)

MAX_W, MAX_H = 300, 300
im = Image.new('RGBA', (MAX_W, MAX_H), (255, 255, 255, 0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(
    'font\Minecraft Evenings.ttf', 25)

current_h, pad = 50, 10
for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((MAX_W - w) / 2, current_h), line, fill=(128 , 128 , 128),font=font)
    current_h += h + pad

im.save('test.png')
