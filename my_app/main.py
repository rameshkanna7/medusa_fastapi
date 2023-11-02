from pathlib import Path

from fastapi import FastAPI, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
app = FastAPI()
templates = Jinja2Templates(directory=Path("my_app") / "templates")
app.mount("/static", StaticFiles(directory=Path("my_app") / "static"), name="static")

data = [
    {"name": "Pandas", "import": "pd"},
    {"name": "Numpy", "import": "np"},
    {"name": "Matplotlib", "import": "pyplot"},
    {"name": "tensorflow", "import": "tf"},
]


@app.get("/index", response_class=HTMLResponse)
async def root_page(request: Request, hx_request: Optional[str] = Header(None)):
    if hx_request:
        return templates.TemplateResponse("table.html", context={"request": request, "lib": data})
    return templates.TemplateResponse(
        "index.html", context={"request": request, "lib": data}
    )