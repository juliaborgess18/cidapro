import datetime
from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from application.mapper.solicitacao_mapper import SolicitacaoMapper
from application.mapper.usuario_mapper import UsuarioMapper
from application.use_cases.usuario.consultar_resultado_solicitante_use_case import ConsultarResultadoSolicitanteUseCase
from application.use_cases.usuario.visualizar_historico_solicitante import VisualizarHistoricoSolicitacoesUseCase
from application.use_cases.usuario.visualizar_solicitante_use_case import VisualizarSolicitanteUseCase
from infrastructure.repositories.motivo_repo import MotivoRepo
from domain.errors.NotFoundException import NotFoundException
from infrastructure.repositories.pais_repo import PaisRepo
from infrastructure.repositories.solicitacao_repo import SolicitacaoRepo
from infrastructure.repositories.usuario_repo import UsuarioRepo
from presentation.util.templates import obter_jinja_templates

router = APIRouter(tags=["Usuário"])

templates = obter_jinja_templates("presentation/templates/usuario/pages")

@router.get("/usuario/solicitante/pagina_inicial", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request):
    return templates.TemplateResponse("solicitante/pagina_inicial_solicitante.html", {"request": request})

@router.get("/usuario/solicitante/nova_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request):
    paises  = PaisRepo.obter_paises()
    motivos = MotivoRepo.obter_motivos()
    return templates.TemplateResponse("solicitante/nova_solicitacao.html", {"request": request, "paises":paises, "motivos":motivos})

@router.get("/usuario/solicitante/consultar_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request, id_solicitacao: str="", id_usuario: str = ""):
    solicitacao = await ConsultarResultadoSolicitanteUseCase.execute(id_solicitacao, id_usuario)
    return templates.TemplateResponse("solicitante/consultar_resultado.html", {"request": request, "solicitacao": solicitacao})

<<<<<<< HEAD
@router.get("/usuario/solicitante/histórico_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request):
    solicitacoes = await VisualizarHistoricoSolicitacoesUseCase.execute()
=======
@router.get("/usuario/solicitante/historico_solicitacao/{id_usuario}", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request, id_usuario: str):
    solicitacoes = SolicitacaoRepo.selecionar_todos_por_usuario_logado(id_usuario)
>>>>>>> julia
    return templates.TemplateResponse("solicitante/historico_de_solicitacoes.html", {"request": request, "solicitacoes": solicitacoes})

@router.get("/usuario/examinador/pagina_inicial", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request):
    return templates.TemplateResponse("examinador/pagina_inicial_examinador.html", {"request": request})

@router.get("/usuario/examinador/visualizar_solicitante", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request, id_solicitante: int = 0):

    resposta = await VisualizarSolicitanteUseCase.execute(id_solicitante)

    return templates.TemplateResponse("examinador/visualizar_solicitante.html", 
    {
        "request": request,
        "solicitante": resposta['solicitante'],
        "solicitacoes": resposta['solicitacoes']
    })

@router.get("/usuario/examinador/analisar_solicitacao", response_class=HTMLResponse)
async def get_pagina_inicial_solicitante(request: Request):
    return templates.TemplateResponse("examinador/analisar_solicitacao.html", {"request": request})
