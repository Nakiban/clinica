from pydantic_settings import BaseSettings, SettingsConfigDict

from clinica.config.log_config import logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


settings = Settings()

if settings.DATABASE_URL:
    logger.debug(f'Database URL: {settings.DATABASE_URL}')
else:
    logger.error('DATABASE_URL não está definido no .env ou no ambiente.')
