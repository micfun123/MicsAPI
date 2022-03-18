from fastapi import FastAPI, Request
from fastapi.responses import FileResponse , RedirectResponse , StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = FastAPI(
    title = "Mics TextAPI",
    description="Generate image text in a video game font \n This what made by Michael twitter = https://twitter.com/Michaelrbparker ",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)

font = ImageFont.truetype('fontm.ttf', 50)

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

@app.get("/")
def root():
    return RedirectResponse("/docs")
    

@app.get("/api/mctext/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def mctext(Text : str):
       
    file = MCtext(Text) 

    return StreamingResponse(file, media_type="image/png")