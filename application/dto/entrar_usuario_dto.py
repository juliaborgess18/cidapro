from pydantic import BaseModel, field_validator

from application.utils.validators import is_email, is_not_empty, is_password


class EntrarUsuarioDTO(BaseModel):
    email: str
    senha: str

    @field_validator("email")
    def validar_email(cls, v):
        msg = is_email(v, "E-mail")
        if msg:
            raise ValueError(msg)
        return v

    # @field_validator("senha")
    # def validar_senha(cls, v):
    #     msg = is_not_empty(v, "Senha")
    #     if not msg:
    #         msg = is_password(v, "Senha")
    #     if msg:
    #         raise ValueError(msg.strip())
    #     return v