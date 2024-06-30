from infrastructure.repositories.motivo_repo import MotivoRepo
from infrastructure.repositories.pais_repo import PaisRepo
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo


def criar_bancos_e_inserir_dados():
    '''
    Remova o banco de dados presente em src/dados.db para que este método seja executado
    '''
    MotivoRepo.criar_tabela()
    PaisRepo.criar_tabela()
    UsuarioRepo.criar_tabela()
    SolicitacaoRepo.criar_tabela()

    MotivoRepo.inserir_dados()
    PaisRepo.inserir_dados()
    UsuarioRepo.inserir_dados()
    SolicitacaoRepo.inserir_dados()