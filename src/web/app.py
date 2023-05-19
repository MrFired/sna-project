from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.config import Config
from src.services import load_html


app = FastAPI()
config = Config()

# Serve static files
if config.STATIC_FILES:
    app.mount("/static", StaticFiles(directory=str(config.STATIC_FILES)), name="static")


@app.get("/")
async def main_page():
    index_html = load_html(config.STATIC_FILES / "index.html")
    return HTMLResponse(content=index_html)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)
