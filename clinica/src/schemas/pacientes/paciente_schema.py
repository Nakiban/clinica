from datetime import datetime

from pydantic import BaseModel


class PacienteSchema(BaseModel):
    id: int
    nome: str
    data_nascimento: str
    sexo: str
    created_at: datetime
