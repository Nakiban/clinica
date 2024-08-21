import sys

from loguru import logger

logger.remove()
logger.add(sys.stdout, format='{time} {level} {message}', level='DEBUG')
logger.add(
    'logs/app.log',
    format='{time} {level} {message}',
    level='DEBUG',
    rotation='10 MB',
)
