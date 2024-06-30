from application.mapper.solicitacao_mapper import SolicitacaoMapper
from application.mapper.usuario_mapper import UsuarioMapper
from domain.errors.NotFoundException import NotFoundException
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo


class VisualizarSolicitanteUseCase:

    @classmethod
    async def execute(cls, id: int) -> dict:
        usuario_mapeado = None
        solicitacoes_mapeadas = []
        if id != 0:
            usuario_solicitante = UsuarioRepo.selecionar_por_id(id)   
            if usuario_solicitante == None:
                raise NotFoundException("Usuário não encontrado.")
            
            solicitacoes = SolicitacaoRepo.selecionar_por_id_usuario(id)
            usuario_mapeado = UsuarioMapper.visualizar_usuario(usuario_solicitante)
            solicitacoes_mapeadas = [SolicitacaoMapper.visualizar_solicitacao(solicitacao) for solicitacao in solicitacoes]
        return {"solicitante": usuario_mapeado, "solicitacoes": solicitacoes_mapeadas}