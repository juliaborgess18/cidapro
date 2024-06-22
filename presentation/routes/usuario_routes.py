from fastapi import APIRouter, Request
from application.dto.usuario_dto import AlterarUsuarioDTO, CriarUsuarioDTO
from application.mapper.usuario_mapper import UsuarioMapper
from infrastructure.repositories.usuario_repo import UsuarioRepo

router = APIRouter(tags=["Usuário"])

@router.post("/usuario")
async def post_usuario(usuario: CriarUsuarioDTO):
    novo_usuario = UsuarioMapper.cadastrar_usuario(usuario)
    novo_usuario_repo = UsuarioRepo.inserir(novo_usuario)
    return {"Usuário criado": novo_usuario_repo.nome}

@router.get("/usuario")
async def get_usuarios():
    usuarios = UsuarioRepo.selecionar_todos()
    return {"Usuários": usuarios }

@router.get("/usuario/{id_usuario}")
async def get_usuario(id_usuario:str):
    usuario = UsuarioRepo.selecionar_por_id(id_usuario)
    return {"Usuário": usuario}
    
@router.put("/usuario")
async def put_usuario(usuario: AlterarUsuarioDTO):
    usuario_alterado = UsuarioMapper.alterar_usuario(usuario)
    usuario_alterado_repo = UsuarioRepo.alterar(usuario_alterado)
    return {"Usuário alterado": usuario_alterado_repo.nome}

@router.delete("/usuario")
async def delete_usuario(id_usuario: str):
    UsuarioRepo.deletar(id_usuario)
    return {"Usuário excluido"}