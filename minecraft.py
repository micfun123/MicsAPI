from fastapi import APIRouter
from PIL import Image, ImageDraw, ImageFont
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO

font = ImageFont.truetype('font\Minecraft Evenings.ttf', 25)

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def MCtext(text):
    x,y = get_text_dimensions(text, font)
    im = Image.new('RGBA', (x+5, y+5), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    draw.text((5,5), text, fill=(128 , 128 , 128),font=font)

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

