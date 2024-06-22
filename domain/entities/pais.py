from dataclasses import dataclass
from typing import Optional


@dataclass
class Pais:
    id   : Optional[str] 
    nome : Optional[str] 