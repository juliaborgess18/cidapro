from sqlite3 import DatabaseError
from fastapi import APIRouter, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.utils.cookies import adicionar_cookie_auth
from application.utils.pydantic import create_validation_errors
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates
from application.utils.auth import (
    conferir_senha,
    gerar_token,
)

router = APIRouter(tags=["Main"])

templates = obter_jinja_templates("presentation/templates/main")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request, return_url: str = Query("/")):
    """ Renderizando template inicial """
    return templates.TemplateResponse("entrar.html", {"request": request, "return_url": return_url})

@router.post("/entrar", response_class=JSONResponse)
async def post_entrar(entrar_dto: EntrarUsuarioDTO):
    usuario_entrou = UsuarioRepo.selecionar_por_email(entrar_dto.email)
    if (
        (not usuario_entrou)
        or (not usuario_entrou.senha)
        or (not conferir_senha(entrar_dto.senha, usuario_entrou.senha))
    ):
        return JSONResponse(
            content=create_validation_errors(
                entrar_dto,
                ["email", "senha"],
                ["Credenciais inválidas.", "Credenciais inválidas."],
            ),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    token = gerar_token()
    if not UsuarioRepo.alterar_token(usuario_entrou.id, token):
        raise DatabaseError(
            "Não foi possível alterar o token do cliente no banco de dados."
        )
    response = JSONResponse(content={"redirect": {"url": "/usuario/pagina_inicial_solicitante"}})
    adicionar_cookie_auth(response, token)
    return response

@router.get("/usuario/pagina_inicial_solicitante", response_class=HTMLResponse)
async def get_pagina_inicial_solitante(request: Request):
    return templates.TemplateResponse("pagina_inicial_solicitante.html", {"request": request})

@router.post("/usuario/sair", response_class=JSONResponse)
async def post_sair():
    pass