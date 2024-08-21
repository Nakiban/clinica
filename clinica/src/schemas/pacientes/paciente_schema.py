from datetime import datetime

from pydantic import BaseModel


class PacienteSchema(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: int
    etnia: int
    created_at: datetime
