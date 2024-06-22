import logging

from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse

from domain.errors.NotFoundException import NotFoundException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configurar_excecoes(app: FastAPI):
        
    @app.exception_handler(NotFoundException)
    async def recurso_nao_encontrado(request: Request, ex: NotFoundException):
        logger.error(ex.message)
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "Error(s)": ex.message })
    
    @app.exception_handler(Exception)
    async def excecao_ganerica(request: Request, ex: Exception):
        logger.error(ex)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={ "Error(s)": "Falha no servidor da aplicação. Por favor contate o suporte." })