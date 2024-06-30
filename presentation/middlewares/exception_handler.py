import logging

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from application.utils.cookies import adicionar_mensagem_erro
from domain.errors.NotFoundException import NotFoundException
from domain.models.funcao_usuario import EXAMINADOR, SOLICITANTE
from presentation.util.templates import obter_jinja_templates


templates = obter_jinja_templates("templates")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configurar_excecoes(app: FastAPI):
    
    @app.exception_handler(401)
    async def unauthorized_exception_handler(request: Request, _):
        response = RedirectResponse(
            f"/", status_code=status.HTTP_302_FOUND
        )
        adicionar_mensagem_erro(
            response,
            f"A página {request.url.path} é restrita a usuários logados. Identifique-se para poder prosseguir.",
        )
        return response

    @app.exception_handler(403)
    async def forbidden_exception_handler(request: Request, _):  
        if request.state.usuario.funcao == str(EXAMINADOR):
            response = RedirectResponse(
                f"/usuario/examinador/pagina_inicial", status_code=status.HTTP_302_FOUND
            )
        elif request.state.usuario.funcao == str(SOLICITANTE):
            response = RedirectResponse(
                f"/usuario/solicitante/pagina_inicial", status_code=status.HTTP_302_FOUND
            )
        adicionar_mensagem_erro(
            response,
            f"Você está logado como <b>{request.state.usuario.nome}</b> e seu perfil de usuário não tem autorização de acesso à página <b>{request.url.path}</b>. Entre com um usuário do perfil adequado para poder acessar a página em questão.",
        )
        return response
    
    @app.exception_handler(NotFoundException)
    async def resource_not_found_exception_handler(request: Request, _):  
        if request.state.usuario.funcao == str(EXAMINADOR):
            response = RedirectResponse(
                f"{request.url.path}", status_code=status.HTTP_302_FOUND
            )
        elif request.state.usuario.funcao == str(SOLICITANTE):
            response = RedirectResponse(
                f"{request.url.path}", status_code=status.HTTP_302_FOUND
            )
        adicionar_mensagem_erro(
            response,
            f"Usuário não encontrado.",
        )
        return response

    @app.exception_handler(404)
    async def page_not_found_exception_handler(request: Request, _ ):
        return templates.TemplateResponse(
            "pages/404.html", {"request": request, "usuario": request.state.usuario}
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, ex: HTTPException):
        logger.error("Ocorreu uma exceção não tratada: %s", ex)
        view_model = {
            "request": request,
            "usuario": request.state.usuario,
            "detail": "Erro na requisição HTTP.",
        }
        return templates.TemplateResponse(
            "pages/erro.html", view_model, status_code=ex.status_code
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, ex: Exception):
        logger.error("Ocorreu uma exceção não tratada: %s", ex)
        view_model = {
            "request": request,
            "usuario": request.state.usuario,
            "detail": "Erro interno do servidor.",
        }
        return templates.TemplateResponse("pages/erro.html", view_model, status_code=500)
