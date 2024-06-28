from sqlite3 import DatabaseError
from fastapi import APIRouter, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.mapper.usuario_mapper import UsuarioMapper
from application.utils.cookies import adicionar_cookie_auth
from application.utils.pydantic import create_validation_errors
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates
from application.utils.auth import (
    conferir_senha,
    gerar_token,
)

router = APIRouter(tags=["Main"])

templates = obter_jinja_templates("presentation/templates/main/pages")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    """ Renderizando template inicial """
    return templates.TemplateResponse("entrar.html", {"request": request})

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

@router.get("/cadastrar", response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})

@router.post("/cadastrar", response_class=JSONResponse)
async def post_usuario(usuario: CriarUsuarioDTO):
    novo_usuario = UsuarioMapper.cadastrar_usuario(usuario)
    _ = UsuarioRepo.inserir(novo_usuario)
    return JSONResponse(content={"redirect": {"url": "/cadastro_confirmado"}})

@router.get("/cadastro_confirmado", response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("cadastro_confirmado.html", {"request": request})

@router.get("/sobre", response_class=HTMLResponse)
async def get_sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})