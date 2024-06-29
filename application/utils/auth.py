import secrets
from typing import Optional
import bcrypt
from fastapi import HTTPException, Request, status

from application.utils.cookies import NOME_COOKIE_AUTH, adicionar_cookie_auth
from domain.entities.usuario import Usuario
from domain.models.funcao_usuario import *
from infrastructure.repositories.usuario_repo import UsuarioRepo



async def obter_usuario_logado(request: Request) -> Optional[Usuario]:
    try:
        token = request.cookies[NOME_COOKIE_AUTH]
        if token.strip() == "":
            return None
        usuario = UsuarioRepo.selecionar_por_token(token)
        return usuario
    except KeyError:
        return None


async def middleware_autenticacao(request: Request, call_next):
    usuario = await obter_usuario_logado(request)
    request.state.usuario = usuario
    response = await call_next(request)
    if response.status_code == status.HTTP_303_SEE_OTHER:
        return response
    if usuario:
        token = request.cookies[NOME_COOKIE_AUTH]
        adicionar_cookie_auth(response, token)
    return response


async def checar_permissao(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    area_do_solicitante = request.url.path.startswith("/usuario/solicitante")
    area_do_examinador = request.url.path.startswith("/usuario/examinador")
    if (area_do_solicitante or area_do_examinador) and not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if area_do_solicitante and usuario.funcao != str(SOLICITANTE):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_examinador and usuario.funcao != str(EXAMINADOR):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


def obter_hash_senha(senha: str) -> str:
    try:
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return hashed.decode()
    except ValueError:
        return ""


def conferir_senha(senha: str, hash_senha: str) -> bool:
    try:
        return bcrypt.checkpw(senha.encode(), hash_senha.encode())
    except ValueError:
        return False


def gerar_token(length: int = 32) -> str:
    try:
        return secrets.token_hex(length)
    except ValueError:
        return ""
