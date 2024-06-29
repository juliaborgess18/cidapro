
from typing import Optional

from domain.entities.solicitacao import Solicitacao
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo


class ConsultarResultadoSolicitanteUseCase:
    
    @classmethod
    async def execute(cls, id:str) -> Optional[Solicitacao]:   
        solicitacao = SolicitacaoRepo.selecionar_por_id(id)
        return solicitacao 