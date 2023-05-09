from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.config import Config

app = FastAPI()
config = Config()


@app.get("/")
async def main_page():
    html_content = """
    <html>
        <head>
            <title>HoYoClub</title>
        </head>
        <body>
            Just a text.
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
