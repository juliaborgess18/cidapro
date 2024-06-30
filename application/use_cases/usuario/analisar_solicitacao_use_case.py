from application.mapper.solicitacao_mapper import SolicitacaoMapper
from application.mapper.usuario_mapper import UsuarioMapper
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo


class AnalisarSolicitanteUseCase:

    @classmethod
    async def execute(cls, id: int) -> dict:
        solicitacao_mapeada = None
        solicitante_mapeado = None

        if(id != 0):
            solicitacao = SolicitacaoRepo.selecionar_por_id(id) if id != 0 else None
            solicitante = UsuarioRepo.selecionar_por_id(solicitacao.id_usuario)

            solicitacao_mapeada = SolicitacaoMapper.visualizar_solicitacao(solicitacao)
            solicitante_mapeado = UsuarioMapper.visualizar_usuario(solicitante)
        return {"solicitante": solicitante_mapeado, "solicitacao": solicitacao_mapeada}