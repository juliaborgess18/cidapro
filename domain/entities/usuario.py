from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    id              : Optional[str] = None
    nome            : Optional[str] = None         
    cpf             : Optional[str] = None
    data_nascimento : Optional[str] = None
    email           : Optional[str] = None
    senha           : Optional[str] = None
    funcao          : Optional[str] = None
    token           : Optional[str] = None