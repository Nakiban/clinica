from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SexoEnum(Enum):
    MASCULINO = 'masculino'
    FEMININO = 'feminino'
    OUTRO = 'outro'
    NAO_DECLARADO = 'não declarado'


class PacienteSchema(BaseModel):
    id: int
    nome: str
    data_nascimento: str
    cpf: str
    sexo: SexoEnum
    created_at: datetime
