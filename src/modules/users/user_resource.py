from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter(prefix='/api')


@router.get('/users')
def get_all() -> JSONResponse:
    return {'message': 'user'}
