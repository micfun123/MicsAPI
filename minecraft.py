from PIL import Image, ImageDraw, ImageFont
from cv2 import line

text = "Minecraft OG"
font = ImageFont.truetype('font\Minecraft Evenings.ttf', 25)

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


x,y = get_text_dimensions(text, font)
print(x)
print(y)
print(x+5)
print(y+5)




im = Image.new('RGBA', (x+5, y+5), (255, 255, 255, 0))
draw = ImageDraw.Draw(im)

draw.text((5,5), text, fill=(128 , 128 , 128),font=font)

im.save('test.png')

