from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from src.config import Config
from src.services import load_html


app = FastAPI()
config = Config()


@app.get("/")
async def main_page():
    index_html = load_html("index.html")
    return HTMLResponse(content=index_html)
