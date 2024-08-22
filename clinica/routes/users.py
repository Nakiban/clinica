from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session

from clinica.config.database import get_db
from clinica.config.security import create_hash
from clinica.routes.version import VersionAbout
from clinica.src.models.user import User
from clinica.src.schemas.message_schema import MessageSchema
from clinica.src.schemas.users.user_dto import UserDTO
from clinica.src.schemas.users.user_list import UserList
from clinica.src.schemas.users.user_schema import UserSchema

router = APIRouter(prefix=f'/api/{VersionAbout().VERSION_API}', tags=['User'])
Session = Annotated[Session, Depends(get_db)]


@router.get('/users', response_model=UserList)
def all(session: Session, skip: int = 0, limit: int = 100) -> JSONResponse:
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@router.get('/user/{id}', response_model=UserDTO)
def show(id: int, session: Session) -> JSONResponse:
    user = session.scalar(select(User).where(User.id == id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Error ao pesquisar usuario'
        )
    return user


@router.post('/user', response_model=UserDTO, status_code=HTTPStatus.CREATED)
def create(user: UserSchema, session: Session) -> JSONResponse:
    db = session.scalar(
        select(User).where(
            (User.username == user.username) | (user.email == user.email)
        )
    )

    if db:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuario já registrado'
        )
        logger.debug(db)

    user_create = User(
        username=user.username, password=create_hash(user.password), email=user.email
    )

    session.add(user_create)
    session.commit()
    session.refresh(user_create)

    logger.debug(user_create)
    return user_create


@router.patch('/user/{id}')
def update(id: int, user: UserSchema, session: Session) -> JSONResponse:
    user = session.scalar(select(User).where(User.id == id))

    if not user:
        logger.debug(f'User {id} not exists.')
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Error ao pesquisar usuario'
        )

    user.username = user.username
    user.email = user.email
    user.password = create_hash(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    logger.debug(user)

    return user


@router.delete(
    '/user/{id}', status_code=HTTPStatus.ACCEPTED, response_model=MessageSchema
)
def delete(id: int, session: Session):
    user = session.scalar(select(User).where(User.id == id))
    if user:
        logger.debug(user)
        session.delete(user)
        session.commit()
        session.flush()

        return {'message': 'Deletado com sucesso.'}
    return {'message': 'Falha ao deletar.'}
