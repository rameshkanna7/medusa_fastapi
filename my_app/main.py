from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import SessionLocal

app = FastAPI()
templates = Jinja2Templates(directory=Path("my_app") / "templates")
app.mount("/static", StaticFiles(directory=Path("my_app") / "static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


data = [
    {"name": "Pandas", "import": "pd"},
    {"name": "Numpy", "import": "np"},
    {"name": "Matplotlib", "import": "pyplot"},
    {"name": "tensorflow", "import": "tf"},
]


@app.get("/index", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("cards.html", context={"request": request})


@app.get("/calendar", response_class=HTMLResponse)
async def calendar_page(request: Request):
    list_data = range(30)
    return templates.TemplateResponse(
        "ocr.html", context={"request": request, "data": list_data}
    )


@app.get("/tailwind", response_class=HTMLResponse)
async def tailwind(request: Request, hx_request: Optional[str] = Header(None)):
    if hx_request:
        return templates.TemplateResponse(
            "table.html", context={"request": request, "lib": data}
        )
    return templates.TemplateResponse(
        "learn.html", context={"request": request, "lib": data}
    )


@app.get("/")
async def database_check(db: Session = Depends(get_db)):
    # Use the 'db' session for database operations
    result = db.execute("SELECT top(1) * FROM HUB_TEST")
    rows = result.fetchall()
    return {
        "message": "Database connection established and data retrieved.",
        "data": rows,
    }
