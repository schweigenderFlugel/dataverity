from datetime import datetime, timezone
from typing import Optional
from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

class Genero(str, Enum):
  M = 'M'
  F = 'F'
  Otro = 'Otro'

class TipoNEAE(str, Enum):
  TDAH = 'TDAH'
  TEA = 'TEA'
  Dislexia = 'Dislexia'
  Normal = 'Normal'

class ConsultBase(SQLModel):
  legajo: str = Field(sa_column=Column(pg.VARCHAR), unique=True)
  nombre: str = Field(sa_column=Column(pg.VARCHAR), description='Tiene que ser nombre completo')
  edad: int = Field(sa_column=Column(pg.SMALLINT), description='Tiene que ser un número entero', gt=4, lt=14)
  genero: Genero = Field(sa_column=Column(pg.ENUM(Genero)))
  grado: int = Field(sa_column=Column(pg.INTEGER), gt=0, lt=7)
  asistencia_inicial: bool = Field(sa_column=Column(pg.BOOLEAN))
  asistencia: int = Field(sa_column=Column(pg.INTEGER))
  calificacion_matematica: float = Field(sa_column=Column(pg.FLOAT))
  calificacion_lengua: float = Field(sa_column=Column(pg.FLOAT))
  horas_clase_semanales: int = Field(sa_column=Column(pg.INTEGER))
  motivacion: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  habilidades_de_autoregulacion: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  habilidades_interpersonales: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  habilidades_intrapersonales: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  conducta_riesgo: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  libros_en_casa: int = Field(sa_column=Column(pg.SMALLINT))
  internet_en_casa: bool = Field(sa_column=Column(pg.BOOLEAN))
  distancia_escuela_km: float = Field(sa_column=Column(pg.FLOAT))
  clima_escolar: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  capacitacion_docente_anual_horas: int = Field(sa_column=Column(pg.SMALLINT))
  tenencia_director_anos: int = Field(sa_column=Column(pg.INTEGER))
  adecuaciones_curriculares: bool = Field(sa_column=Column(pg.BOOLEAN))
  tipo_nea: TipoNEAE = Field(sa_column=Column(pg.ENUM(TipoNEAE)))
  violencia_familia: bool = Field(sa_column=Column(pg.BOOLEAN))
  enfermedad_grave_familia: bool = Field(sa_column=Column(pg.BOOLEAN))
  catastrofe_familia: bool = Field(sa_column=Column(pg.BOOLEAN))
  resilencia_familia: int = Field(sa_column=Column(pg.SMALLINT), gt=0, lt=6)
  conducta_riesgo_observada: bool = Field(sa_column=Column(pg.BOOLEAN))
    
class Consult(ConsultBase, table=True):
  id: Optional[UUID] = Field(sa_column=Column(pg.UUID, primary_key=True), default_factory=lambda: uuid4())
  created_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))
  updated_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))

class ConsultCreate(ConsultBase):
  pass

