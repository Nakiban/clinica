from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from clinica.config.database import get_db
from clinica.src.models.paciente import Paciente
from clinica.src.schemas.pacientes.paciente_schema import PacienteSchema

router = APIRouter(prefix='/api', tags=['Pacientes'])
Session = Annotated[Session, Depends(get_db)]


@router.get('/paciente', response_model=PacienteSchema)
def all(session: Session, skip: int = 0, limit: int = 100) -> JSONResponse:
    users = session.scalars(select(Paciente).offset(skip).limit(limit)).all()
    return {'users': users}
