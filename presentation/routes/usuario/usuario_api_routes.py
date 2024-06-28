from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.mapper.usuario_mapper import UsuarioMapper
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Usuário"])

templates = obter_jinja_templates("presentation/templates/usuario/pages")

@router.post("/usuario/sair", response_class=JSONResponse)
async def post_sair():
    pass
