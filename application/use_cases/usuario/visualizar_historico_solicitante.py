from typing import List
from domain.entities.solicitacao import Solicitacao
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo


class VisualizarHistoricoSolicitacoesUseCase:
    
    @classmethod
    async def execute() -> List[Solicitacao]:
        solicitacoes = SolicitacaoRepo.selecionar_todos_por_usuario_logado()
        return solicitacoes