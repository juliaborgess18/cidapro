from pydantic import BaseModel


class CriarSolicitacaoDTO(BaseModel):
    status      : str          
    id_usuario  : str 
    id_pais     : str 
