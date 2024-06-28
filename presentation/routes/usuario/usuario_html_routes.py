from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Usuário"])

templates = obter_jinja_templates("presentation/templates/usuario/pages")

@router.get("/usuario/solicitante/pagina_inicial", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("solicitante/pagina_inicial_solicitante.html", {"request": request})

@router.get("/usuario/solicitante/nova_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("solicitante/nova_solicitacao.html", {"request": request})

@router.get("/usuario/solicitante/consultar_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("solicitante/consultar_resultado.html", {"request": request})

@router.get("/usuario/solicitante/histórico_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("solicitante/historico_de_solicitacoes.html", {"request": request})

@router.get("/usuario/examinador/pagina_inicial", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("examinador/pagina_inicial_examinador.html", {"request": request})

@router.get("/usuario/examinador/visualizar_solicitante", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("examinador/visualizar_solicitante.html", {"request": request})

@router.get("/usuario/examinador/analisar_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("examinador/analisar_solicitacao.html", {"request": request})
