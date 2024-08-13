from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.modules.users.users import UserDTOScherma, UserScherma

router = APIRouter(prefix="/api")


@router.get('/users')
def index() -> JSONResponse:
    return {'message': 'user'}


@router.post('/user', response_model=UserDTOScherma)
def create(user: UserScherma) -> JSONResponse:
    return user


@router.patch('/user/{id}')
def update(id: int, request: Request) -> JSONResponse:
    return {}


@router.delete('/user/{id}')
def delete(id) -> JSONResponse:
    return id
