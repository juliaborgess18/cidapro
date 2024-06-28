from pydantic import BaseModel

class AlterarUsuarioDTO(BaseModel):
    id              : str           
    nome            : str   
    data_nascimento : str 
    email           : str 