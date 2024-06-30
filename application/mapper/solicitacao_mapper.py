from datetime import datetime
from application.dto.solicitacao_dto import CriarSolicitacaoDTO
from domain.entities.solicitacao import Solicitacao


class SolicitacaoMapper:
    
    @classmethod
    def cadastrar_solicitacao(cls, solicitacao: CriarSolicitacaoDTO) -> Solicitacao:
        nova_solicitacao_db = Solicitacao()
        nova_solicitacao_db.dh_solicitacao = datetime.now()
        nova_solicitacao_db.status = solicitacao.status
        nova_solicitacao_db.id_usuario = solicitacao.id_usuario
        nova_solicitacao_db.id_pais = solicitacao.id_pais
        nova_solicitacao_db.id_motivo = solicitacao.id_motivo
        return nova_solicitacao_db   