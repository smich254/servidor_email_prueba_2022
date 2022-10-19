from pydantic import BaseModel


class Email(BaseModel):
    de: str
    contras: str
    para: str
    asunto: str
    cuerpo: str