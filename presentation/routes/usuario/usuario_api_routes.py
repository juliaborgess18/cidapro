from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from application.utils.cookies import adicionar_mensagem_sucesso, excluir_cookie_auth
from domain.models.status_solicitacao import *
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Usuário"])

templates = obter_jinja_templates("presentation/templates/usuario/pages")

@router.get("/usuario/sair", response_class=RedirectResponse)
async def get_sair(request: Request):
    if request.state.usuario:
        UsuarioRepo.alterar_token(request.state.usuario.email, "")
    response = RedirectResponse("/", status.HTTP_303_SEE_OTHER)
    excluir_cookie_auth(response)
    adicionar_mensagem_sucesso(response, "Saída realizada com sucesso!")
    return response

@router.patch("/usuario/aceitar_solicitacao", response_class=JSONResponse)
async def patch_status_aceitar_solicitacao(request: Request, id_solicitacao: str):
    SolicitacaoRepo.alterar_status(id_solicitacao, SOLICITACAO_ACEITA)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "sucesso", "mensagem": "Solicitação aceita com sucesso"})

@router.patch("/usuario/negar_solicitacao", response_class=JSONResponse)
async def patch_status_negar_solicitacao(request: Request, id_solicitacao: int):
    SolicitacaoRepo.alterar_status(id_solicitacao, SOLICITACAO_NEGADA)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "sucesso", "mensagem": "Solicitação negada com sucesso"})

@router.patch("/usuario/cancelar_solicitacao", response_class=JSONResponse)
async def patch_status_cancelar_solicitacao(request: Request, id_solicitacao: int):
    SolicitacaoRepo.alterar_status(id_solicitacao, SOLICITACAO_CANCELADA)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "sucesso", "mensagem": "Solicitação cancelada com sucesso"})