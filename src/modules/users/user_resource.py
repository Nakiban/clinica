from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.modules.users.users import UserDTOScherma, UserScherma

router = APIRouter(prefix="/api")


@router.get('/users')
def all() -> JSONResponse:
    return {'message': 'user'}


@router.get('/user/{id}')
def show(id: int) -> JSONResponse:
    user = UserScherma
    return user


@router.post('/user', response_model=UserDTOScherma)
def create(user: UserScherma) -> JSONResponse:
    return user


@router.patch('/user/{id}')
def update(id: int, user: UserScherma) -> JSONResponse:
    return user


@router.delete('/user/{id}')
def delete(id) -> JSONResponse:
    return id
