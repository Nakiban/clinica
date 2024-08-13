from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api")


@router.get('/alunos')
def index() -> JSONResponse:
    return {}


@router.post('/alunos')
def store(request: Request) -> JSONResponse:
    return request.items


@router.patch('/alunos/{id}')
def update(id: int, request: Request) -> JSONResponse:
    return {}
