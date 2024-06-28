from typing import Optional
from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.mapper.usuario_mapper import UsuarioMapper
from domain.entities.usuario import Usuario
from infrastructure.repositories.usuario_repo import UsuarioRepo

from infrastructure.repositories.usuario_repo import UsuarioRepo

class CadastrarUsuarioUseCase():
    async def execute(dto: CriarUsuarioDTO) -> Optional[Usuario]:
        novo_usuario = UsuarioMapper.cadastrar_usuario(dto)
        usuario_inserido = UsuarioRepo.inserir(novo_usuario)
        return usuario_inserido