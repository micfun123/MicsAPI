from fastapi import FastAPI, Request
from fastapi.responses import FileResponse , RedirectResponse , StreamingResponse,JSONResponse
from PIL import Image, ImageDraw, ImageFont , ImageEnhance , ImageSequence
from fastapi.staticfiles import StaticFiles
from io import BytesIO
import urllib.request 
import io
import os
import qrcode
import random
import textwrap


app = FastAPI(
    title = "Mics TextAPI",
    description="Generate image text in a video game font \n This what made by Michael twitter = https://twitter.com/Michaelrbparker \n The github repo = https://github.com/micfun123/MicsAPI",
    version="2.1.1",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)


app.mount("/static", StaticFiles(directory="app/static"), name="static")



def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]

fontm = ImageFont.truetype('app/fontm.ttf', 50)
fontp = ImageFont.truetype('app/PokemonSolid.ttf', 50)
fonta = ImageFont.truetype('app/AvengeroRegular.ttf', 50)

def qrcodemaker(text):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def MCtext(text):
    x,y = get_text_dimensions(text, fontm)
    im = Image.new('RGBA', (x+5, y+5), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    draw.text((5,5), text, fill=(128 , 128 , 128),font=fontm)

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

def pokemontextmaker(text):
    x,y = get_text_dimensions(text, fontp)
    im = Image.new('RGBA', (x+5, y+5), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    draw.text((5,5), text, fill=(255 , 253 , 48),stroke_width=3, stroke_fill=(56,106,187) ,font=fontp)

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

def theavengersmaker(text):
    x,y = get_text_dimensions(text, fonta)
    im = Image.new('RGBA', (x+5, y+5), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    draw.text((5,5), text, fill=(234 , 1 , 26),stroke_width=3, stroke_fill=(154,152,159) ,font=fonta)

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

def generate_image_Wanted(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    
    im1 = Image.open("app/images/wanted.jpg")
    im2 = Image.open(f)
    im2 = im2.resize((300, 285))
    im2 = im2.alpha_composite(im2)

    img = im1.copy()
    img.paste(im2, (85, 230))
    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

def generate_image_Trash(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    
    im1 = Image.open("app/images/trasher.jpg")
    im2 = Image.open(f)
    im2 = im2.resize((75, 75))

    img = im1.copy()
    img.paste(im2, (90, 380))
    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d


def slap(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    
    im1 = Image.open("app/images/slap1.gif")
    im2 = Image.open(f)
    im2 = im2.resize((100, 100))
    im2 = im2.convert("RGBA")
    
   
    frames = []
    for frame in ImageSequence.Iterator(im1):
        frame = frame.copy()
        frame = frame.convert("RGBA")
        frame.paste(im2, (500, 90))
        frames.append(frame)
        

    d = BytesIO()
    d.seek(0)
    frames[0].save(d,'output.gif', save_all=True, append_images=frames[1:-1]) 
    d.seek(0)
    return d

def ghost(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    
    im1 = Image.open("app/images/ghost.jpg")
    im2 = Image.open(f)
    im2 = im2.resize((90, 90))

    img = im1.copy()
    img.paste(im2, (120, 700))
    d = BytesIO()
    d.seek(0)
    img.save(d, "PNG")
    d.seek(0)
    return d

def generate_image_I_wish(text):
    im = Image.open("app/images/Iwish.jpg")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("app/Roboto-Black.ttf", 16)
    margin = 60
    offset = 290
    for line in textwrap.wrap(text, width=30):
            draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
            offset += font.getsize(line)[1]


    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

def generate_image_ifread(text):
    im = Image.open("app/images/iftheycouldread.jpg")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("app/Roboto-Black.ttf", 16)

    margin = 265
    offset = 85
    for line in textwrap.wrap(text, width=20):
            draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
            offset += font.getsize(line)[1]

    

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d

def generate_image_um_dad(text):
    im = Image.open("app/images/Umdad.jpg")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("app/Roboto-Black.ttf", 16)

    margin = 80
    offset = 420
    for line in textwrap.wrap(text, width=25):
            draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
            offset += font.getsize(line)[1]

    

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d


def image_Enhance_contrast(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    img = Image.open(f)
    contrast = ImageEnhance.Contrast(img)
    d = BytesIO()
    d.seek(0)
    contrast.enhance(1.5).save(d, "PNG")
    d.seek(0)
    return d

def image_Enhance_colour(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    img = Image.open(f)
    Color = ImageEnhance.Color(img)
    d = BytesIO()
    d.seek(0)
    Color.enhance(1.5).save(d, "PNG")
    d.seek(0)
    return d

def image_black_white(imageUrl):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    req = urllib.request.Request(imageUrl, headers=hdr)
    response = urllib.request.urlopen(req) 
    f = io.BytesIO(response.read())
    img = Image.open(f)
    Color = ImageEnhance.Color(img)
    d = BytesIO()
    d.seek(0)
    Color.enhance(0.0).save(d, "PNG")
    d.seek(0)
    return d

def headachegen(text):
    im = Image.open("app/images/headache.png")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("app/Roboto-Black.ttf", 16)

    margin = 160
    offset = 200
    for line in textwrap.wrap(text, width=15):
            draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
            offset += font.getsize(line)[1]

    

    d = BytesIO()
    d.seek(0)
    im.save(d, "PNG")
    d.seek(0)
    return d


@app.get("/")
def root():
    return RedirectResponse("/docs")
    

@app.get("/api/text/Minecraft", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def mctext(Text : str):
       
    file = MCtext(Text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/api/text/pokemon", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def pokemontext(Text : str):
       
    file = pokemontextmaker(Text) 

    return StreamingResponse(file, media_type="image/png")



@app.get("/api/text/theavengers", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def theavengerstext(Text : str):
       
    file = theavengersmaker(Text) 

    return StreamingResponse(file, media_type="image/png")


@app.get("/filters/wanted", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def wanted(image_url : str):
       
    file = generate_image_Wanted(image_url) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/api/other/QRCode", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def QRcodemaker(Text : str):
       
    file = qrcodemaker(Text) 
    return StreamingResponse(file, media_type="image/png")


@app.get("/filters/trash", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def trash(image_url : str):
       
    file = generate_image_Trash(image_url) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/filters/I_wish", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def I_wish(text):
       
    file = generate_image_I_wish(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Memes/if_the_could_read", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def if_the_could_read(text):
       
    file = generate_image_ifread(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Memes/um_dad", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def um_dad(text):
       
    file = generate_image_um_dad(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Memes/headache", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def headache(text):
       
    file = headachegen(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Image/contrast_enhance", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def um_dad(text):
       
    file = image_Enhance_contrast(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Image/colour_enhance", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def um_dad(text):
       
    file = image_Enhance_colour(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/Image/back_and_white", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def um_dad(text):
       
    file = image_black_white(text) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/filters/ghost", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def ghoster(url):
       
    file = ghost(url) 

    return StreamingResponse(file, media_type="image/png")

@app.get("/tea")
def tea():
    x = "static/teacuppics/{}".format(getRandomFile("static/teacuppics"))
    return FileResponse(x)


@app.get('/json/tea')
async def teajson(request: Request) -> JSONResponse:
    img = "teacuppics/{}".format(getRandomFile("static/teacuppics"))
    img_url = request.url_for('static', path=img)
    return {'img_url': img_url}

@app.get("/json/coffee")
def coffeejson(request: Request) -> JSONResponse:
    img = "coffeecups/{}".format(getRandomFile("static/coffeecups"))
    img_url = request.url_for('static', path=img)
    return {'img_url': img_url}


