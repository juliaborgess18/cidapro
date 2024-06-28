from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Main"])

templates = obter_jinja_templates("presentation/templates/main/pages")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    """ Renderizando template inicial """
    return templates.TemplateResponse("entrar.html", {"request": request})

@router.get("/cadastrar", response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})

@router.get("/cadastro_confirmado", response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("cadastro_confirmado.html", {"request": request})

@router.get("/sobre", response_class=HTMLResponse)
async def get_sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})