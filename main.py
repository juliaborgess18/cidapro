from fastapi import FastAPI
import uvicorn
from infrastructure.repositories.pais_repo import PaisRepo
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.middlewares.exception_handler import configurar_excecoes
from presentation.routes import usuario_routes, solicitacao_routes

app = FastAPI()

app.include_router(usuario_routes.router)
app.include_router(solicitacao_routes.router)
configurar_excecoes(app)
# UsuarioRepo.criar_tabela()
# PaisRepo.criar_tabela()
# SolicitacaoRepo.criar_tabela()

# UsuarioRepo.inserir_dados()
# PaisRepo.inserir_dados()
# SolicitacaoRepo.inserir_dados()

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)




    



