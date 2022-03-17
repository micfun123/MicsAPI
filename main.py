from fastapi import FastAPI, Request
from fastapi.responses import FileResponse , RedirectResponse , StreamingResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title = "Mics TextAPI",
    description="Generate image text in a video game font \n This what made by Michael twitter = https://twitter.com/Michaelrbparker ",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)


@app.get("/")
def root():
    return RedirectResponse("/docs")
    

