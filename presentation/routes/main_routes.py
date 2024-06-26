from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from presentation.util.templates import obter_jinja_templates

router = APIRouter()

# template = Jinja2Templates(directory="presentation/templates/main/")

templates = obter_jinja_templates("presentation/templates/main")

@router.get("/", response_class=HTMLResponse)
async def get_template(request: Request):
    """ Renderizando template inicial """
    return templates.TemplateResponse("entrar.html", {"request": request})
