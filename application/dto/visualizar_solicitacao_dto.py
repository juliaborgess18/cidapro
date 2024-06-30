from pydantic import BaseModel


class VisualizarSolicitacaoDTO(BaseModel):
    id              : str
    dh_solicitacao  : str
    status          : str
    motivo          : str
    pais            : str