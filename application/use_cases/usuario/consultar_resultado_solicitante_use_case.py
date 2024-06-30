from typing import Optional

from domain.entities.solicitacao import Solicitacao
from domain.errors.NotFoundException import NotFoundException
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo


class ConsultarResultadoSolicitanteUseCase:
    
    @classmethod
    async def execute(cls, id_solicitacao:str, id_usuario: str) -> Optional[Solicitacao]:   
        solicitacao = None

        if id_solicitacao != "":
            solicitacao = SolicitacaoRepo.selecionar_por_id_e_usuario_logado(id_solicitacao, id_usuario)

            if solicitacao == None:
                raise NotFoundException("Solicitação não encontrada")

        return solicitacao 