from datetime import datetime

from pydantic import BaseModel

from .sexo_enum import SexoEnum


class PacienteSchema(BaseModel):
    id: int
    nome: str
    data_nascimento: str
    cpf: str
    sexo: SexoEnum
    created_at: datetime
