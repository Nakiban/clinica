import sys

from fastapi import FastAPI
from loguru import logger

from src.modules.users import user_resource

logger.remove()
logger.add(
    sys.stdout, format='{time} {level} {message}', level='DEBUG'
)
logger.add(
    'logs/app.log',
    format='{time} {level} {message}',
    level='INFO',
    rotation='10 MB',
)

app = FastAPI()

app.include_router(user_resource.router)
