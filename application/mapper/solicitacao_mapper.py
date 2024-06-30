from datetime import datetime
from application.dto.solicitacao_dto import CriarSolicitacaoDTO
from application.dto.visualizar_solicitacao_dto import VisualizarSolicitacaoDTO
from domain.entities.solicitacao import Solicitacao
from infrastructure.repositories.pais_repo import PaisRepo


class SolicitacaoMapper:
    
    @classmethod
    def cadastrar_solicitacao(cls, solicitacao: CriarSolicitacaoDTO) -> Solicitacao:
        nova_solicitacao_db = Solicitacao()
        nova_solicitacao_db.dh_solicitacao = datetime.now()
        nova_solicitacao_db.status = solicitacao.status
        nova_solicitacao_db.id_usuario = solicitacao.id_usuario
        nova_solicitacao_db.id_pais = solicitacao.id_pais
        return nova_solicitacao_db
    
    @classmethod
    def visualizar_solicitacao(cls, solicitacao: Solicitacao) -> VisualizarSolicitacaoDTO:
        pais = PaisRepo.selecionar_por_id(solicitacao.id_pais)
        return VisualizarSolicitacaoDTO(id=str(solicitacao.id), dh_solicitacao=solicitacao.dh_solicitacao, status=solicitacao.status, pais=pais.nome)