from pydantic import BaseModel


class VisualizarUsuarioDTO(BaseModel):
    id              : str
    nome            : str       
    cpf             : str
    data_nascimento : str
    email           : str