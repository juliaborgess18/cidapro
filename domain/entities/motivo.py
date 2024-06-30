from dataclasses import dataclass
from typing import Optional


@dataclass
class Motivo:
    id        : Optional[str]
    nome      : Optional[str]