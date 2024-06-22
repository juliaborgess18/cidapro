from dataclasses import dataclass
from typing import Optional


@dataclass
class Solicitacao():
    id              : Optional[str] = None
    dh_solicitacao  : Optional[str] = None
    status          : Optional[str] = None
    id_usuario      : Optional[str] = None
    id_pais         : Optional[str] = None
    