from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.use_cases.main.cadastrar_usuario_use_case import CadastrarUsuarioUseCase
from application.use_cases.main.entrar_usuario_use_case import EntrarUsuarioUseCase
from application.utils.cookies import adicionar_cookie_auth

router = APIRouter(tags=["Main"])

@router.post("/entrar", response_class=JSONResponse)
async def post_entrar(entrar_dto: EntrarUsuarioDTO):
    token = await EntrarUsuarioUseCase.execute(entrar_dto)
    response = JSONResponse(content={"redirect": {"url": "/usuario/solicitante/pagina_inicial"}})
    # response = JSONResponse(content={"redirect": {"url": "/usuario/examinador/pagina_inicial"}})
    adicionar_cookie_auth(response, token)
    return response

@router.post("/cadastrar", response_class=JSONResponse)
async def post_usuario(usuario: CriarUsuarioDTO):
    _ = await CadastrarUsuarioUseCase.execute(usuario)
    return JSONResponse(content={"redirect": {"url": "/cadastro_confirmado"}})