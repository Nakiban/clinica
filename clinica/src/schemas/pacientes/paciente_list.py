from typing import List

from pydantic import BaseModel

from clinica.src.schemas.pacientes.paciente_schema import PacienteSchema


class PacienteList(BaseModel):
    pacientes: List[PacienteSchema]
