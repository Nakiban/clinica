from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from clinica.config.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={'check_same_thread': False},  # Necessário apenas para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Registro de tabelas e modelos
table_registry = registry()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
