from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src import ROOT_DIR
from src.config import Config
from src.web.services import load_html

app = FastAPI()
config = Config()


app.mount(
    "/static",
    StaticFiles(directory=(ROOT_DIR / config.STATIC_FILES)),
    name="static",
)


@app.get("/")
async def main_page():
    index_html = load_html("index.html", config)
    return HTMLResponse(content=index_html)
