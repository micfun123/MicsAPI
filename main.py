from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from minecraft import MCtext

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse("/docs")
    

@app.get("/api/mctext/", responses = {200: {"content": {"image/png": {}}}}, response_class=StreamingResponse)
async def mctext(Text : str):
       
    file = MCtext(Text) 

    return StreamingResponse(file, media_type="image/png")