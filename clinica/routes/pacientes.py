from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from clinica.config.database import get_db
from clinica.config.log_config import logger
from clinica.src.models.paciente import Paciente
from clinica.src.schemas.message_schema import MessageSchema
from clinica.src.schemas.pacientes import paciente_list, paciente_schema

router = APIRouter(prefix='/api', tags=['Pacientes'])
Session = Annotated[Session, Depends(get_db)]


@router.get('/paciente', response_model=paciente_list.PacienteList)
def all(session: Session, skip: int = 0, limit: int = 100) -> JSONResponse:
    pacientes = session.scalars(select(Paciente).offset(skip).limit(limit)).all()
    return {'users': pacientes}


@router.post('/paciente', response_model=paciente_schema.PacienteSchema)
def create(
    paciente: paciente_schema.PacienteSchema, session: Session
) -> JSONResponse:
    paciente = Paciente(
        nome=paciente.nome,
        data_nascimento=paciente.data_nascimento,
        sexo=paciente.sexo,
    )

    session.add(paciente)
    session.commit()
    session.refresh(paciente)
    logger.debug(paciente)

    return paciente


@router.get('/paciente/{paciente_id}', response_model=paciente_schema.PacienteSchema)
def show(paciente_id: int, session: Session) -> JSONResponse:
    paciente = session.scalar(select(Paciente).where(Paciente.id == paciente_id))
    if not paciente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Error ao pesquisar paciente'
        )
    return paciente


@router.patch('/paciente/{paciente_id}')
def update(
    paciente_id: int, paciente: paciente_schema.PacienteSchema, session: Session
) -> JSONResponse:
    paciente = session.scalar(select(Paciente).where(Paciente.id == paciente_id))

    if not paciente:
        logger.debug(f'Paciente {paciente_id} not exists.')
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Error ao pesquisar paciente'
        )

    paciente.nome = paciente.nome
    paciente.sexo = paciente.sexo
    session.add(paciente)
    session.commit()
    session.refresh(paciente)
    logger.debug(paciente)

    return paciente


@router.delete(
    '/paciente/{paciente_id}',
    status_code=HTTPStatus.ACCEPTED,
    response_model=MessageSchema,
)
def delete(paciente_id: int, session: Session):
    paciente = session.scalar(select(Paciente).where(Paciente.id == paciente_id))
    if paciente:
        logger.debug(paciente)
        session.delete(paciente)
        session.commit()
        session.flush()

        return {'message': 'Deletado com sucesso.'}
    return {'message': 'Falha ao deletar.'}
