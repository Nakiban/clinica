from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from clinica.config.database import table_registry


@table_registry.mapped_as_dataclass
class Paciente:
    __tablename__ = 'pacientes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column()
    data_nascimento: Mapped[datetime] = mapped_column()
    sexo: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
