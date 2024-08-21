from fastapi import FastAPI, Request

from clinica.config.log_config import logger
from clinica.routes import pacientes, users

app = FastAPI()


@app.middleware('http')
async def log_requests(request: Request, call_next):
    logger.info(f'Nova requisição: {request.method} {request.url}')
    response = await call_next(request)
    logger.info(f'Resposta: {response.status_code}')
    return response


app.include_router(users.router)
app.include_router(pacientes.router)
