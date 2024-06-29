from typing import Optional
from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.utils.auth import conferir_senha
from domain.entities.usuario import Usuario
from domain.models.funcao_usuario import EXAMINADOR
from infrastructure.repositories.usuario_repo import UsuarioRepo
from sqlite3 import DatabaseError
from fastapi import status
from fastapi.responses import JSONResponse

from application.dto.entrar_usuario_dto import EntrarUsuarioDTO
from application.utils.cookies import adicionar_cookie_auth
from application.utils.pydantic import create_validation_errors
from infrastructure.repositories.usuario_repo import UsuarioRepo
from application.utils.auth import (
    conferir_senha,
    gerar_token,
)


class EntrarUsuarioUseCase():
    async def execute(dto: EntrarUsuarioDTO) -> Optional[JSONResponse]:
        usuario_entrou = UsuarioRepo.selecionar_por_email(dto.email)
        if (
            (not usuario_entrou)
            or (not usuario_entrou.senha)
            or (not conferir_senha(dto.senha, usuario_entrou.senha))
        ):
            return JSONResponse(
                content=create_validation_errors(
                    dto,
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
        
        response = EntrarUsuarioUseCase.VerificarFuncao(usuario_entrou)

        adicionar_cookie_auth(response, token)
        return response
    
    @staticmethod
    def VerificarFuncao(usuario: Usuario):
        if usuario.funcao == str(EXAMINADOR):
            return JSONResponse(content={"redirect": {"url": "/usuario/examinador/pagina_inicial"}})
        
        return JSONResponse(content={"redirect": {"url": "/usuario/solicitante/pagina_inicial"}})