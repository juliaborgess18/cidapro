from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.mapper.usuario_mapper import UsuarioMapper
from application.utils.cookies import adicionar_mensagem_sucesso, excluir_cookie_auth
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Usuário"])

templates = obter_jinja_templates("presentation/templates/usuario/pages")

@router.get("/usuario/sair", response_class=RedirectResponse)
async def get_sair():
    pass
