from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from application.utils.auth import checar_permissao, middleware_autenticacao
from infrastructure.util.data_seeder import criar_bancos_e_inserir_dados
from presentation.middlewares.exception_handler import configurar_excecoes
from presentation.routes.main import main_html_routes, main_api_routes
from presentation.routes.usuario import usuario_html_routes, usuario_api_routes
from presentation.routes.crud import solicitacao_crud_routes

criar_bancos_e_inserir_dados()

app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/presentation/static", app=StaticFiles(directory="presentation/static"), name="static")

app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)

app.include_router(main_html_routes.router)
app.include_router(usuario_html_routes.router)
app.include_router(main_api_routes.router)
app.include_router(usuario_api_routes.router)
app.include_router(solicitacao_crud_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)
