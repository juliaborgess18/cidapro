from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.use_cases.main.cadastrar_usuario_use_case import CadastrarUsuarioUseCase
from application.use_cases.main.entrar_usuario_use_case import EntrarUsuarioUseCase

router = APIRouter(tags=["Main"])

@router.post("/entrar", response_class=JSONResponse)
async def post_entrar(entrar_dto: EntrarUsuarioDTO):
    response = await EntrarUsuarioUseCase.execute(entrar_dto)
    return response

@router.post("/cadastrar", response_class=JSONResponse)
async def post_usuario(usuario: CriarUsuarioDTO):
    _ = await CadastrarUsuarioUseCase.execute(usuario)
    return JSONResponse(content={"redirect": {"url": "/cadastro_confirmado"}})