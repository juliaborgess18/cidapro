from typing import Optional
from pydantic import BaseModel

class CriarUsuarioDTO(BaseModel):
    nome            : str          
    cpf             : str 
    data_nascimento : str 
    email           : str 
    senha           : str 

class AlterarUsuarioDTO(BaseModel):
    id              : str           
    nome            : str   
    data_nascimento : str 
    email           : str 