from typing import List
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from application.dto.solicitacao_dto import CriarSolicitacaoDTO
from application.mapper.solicitacao_mapper import SolicitacaoMapper
from domain.errors.NotFoundException import NotFoundException
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.pais_repo import PaisRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo


router = APIRouter(tags=["Solicitação"])

@router.get("/solicitacoes")
async def get_solicitacoes():
    solicitacoes = SolicitacaoRepo.selecionar_todos()
    return {"Solicitações": solicitacoes }

@router.get("/solicitacao/{id_solicitacao}")
async def get_solicitacao(id_solicitacao: str):
    solicitacao = SolicitacaoRepo.selecionar_por_id(id_solicitacao)
    return {"Solicitação": solicitacao }

@router.get("/solicitacao/{id_solicitacao}/{id_usuario}")
async def get_solicitacao(id_solicitacao: str, id_usuario: str):
    solicitacao = SolicitacaoRepo.selecionar_por_id_e_usuario_logado(id_solicitacao, id_usuario)
    return {"Solicitação": solicitacao }

@router.post("/solicitacao")
async def post_solicitacao(solicitacao: CriarSolicitacaoDTO):

    errors: List[str] = []

    if(not(UsuarioRepo.se_existe(solicitacao.id_usuario))):
        errors.append("Usuário não encontrado.")

    if(not(PaisRepo.se_existe(solicitacao.id_pais))):
        errors.append("Pais não encontrado.")

    if len(errors) != 0:
        raise NotFoundException(errors)

    nova_solicitacao = SolicitacaoMapper.cadastrar_solicitacao(solicitacao)
    nova_solicitacao_repo = SolicitacaoRepo.inserir(nova_solicitacao)
    
    return {"Solicitação criada": nova_solicitacao_repo.id }

@router.patch("/solicitacao", response_class=JSONResponse)
async def patch_solicitacao(id_solicitacao: str, status_solicitcao: str):
        
        if not(SolicitacaoRepo.se_existe(id_solicitacao)):
            raise NotFoundException(f"Solicitação com o id {id_solicitacao} não pode ser encontrada.")
        
        SolicitacaoRepo.alterar_status(id_solicitacao, status_solicitcao)
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)