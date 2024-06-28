from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from application.utils.auth import checar_permissao, middleware_autenticacao
from infrastructure.repositories.pais_repo import PaisRepo
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.middlewares.exception_handler import configurar_excecoes
from presentation.routes import usuario_routes, solicitacao_routes, main_routes

UsuarioRepo.criar_tabela()
PaisRepo.criar_tabela()
SolicitacaoRepo.criar_tabela()

UsuarioRepo.inserir_dados()
PaisRepo.inserir_dados()
SolicitacaoRepo.inserir_dados()

app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/presentation/static", app=StaticFiles(directory="presentation/static"), name="static")

app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(usuario_routes.router)
app.include_router(solicitacao_routes.router)

