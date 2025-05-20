from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
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
  id_estudiante: int = Field(sa_column=Column(pg.INTEGER, unique=True))
  legajo: str = Field(sa_column=Column(pg.VARCHAR, unique=True))
  nombre: str = Field(sa_column=Column(pg.VARCHAR), description='Tiene que ser nombre completo')
  edad: int = Field(sa_column=Column(pg.SMALLINT))
  genero: Genero = Field(sa_column=Column(pg.ENUM(Genero)))
  grado: int = Field(sa_column=Column(pg.INTEGER))
  asistencia_inicial: bool = Field(sa_column=Column(pg.BOOLEAN))
  asistencia: int = Field(sa_column=Column(pg.INTEGER))
  calificacion_matematica: float = Field(sa_column=Column(pg.FLOAT))
  calificacion_lengua: float = Field(sa_column=Column(pg.FLOAT))
  horas_clase_semanales: int = Field(sa_column=Column(pg.INTEGER))
  motivacion: int = Field(sa_column=Column(pg.INTEGER))
  habilidades_de_autoregulacion: int = Field(sa_column=Column(pg.INTEGER))
  habilidades_interpersonales: int = Field(sa_column=Column(pg.INTEGER))
  habilidades_intrapersonales: int = Field(sa_column=Column(pg.INTEGER))
  conducta_riesgo: int = Field(sa_column=Column(pg.INTEGER))
  libros_en_casa: int = Field(sa_column=Column(pg.INTEGER))
  internet_en_casa: int = Field(sa_column=Column(pg.INTEGER))
  distancia_escuela_km: int = Field(sa_column=Column(pg.INTEGER))
  clima_escolar: int = Field(sa_column=Column(pg.INTEGER))
  capacitacion_docente_anual_horas: int = Field(sa_column=Column(pg.INTEGER))
  tenencia_director_anos: int = Field(sa_column=Column(pg.INTEGER))
  adecuaciones_curriculare: int = Field(sa_column=Column(pg.INTEGER))
  tipo_nea: TipoNEAE = Field(sa_column=Column(pg.ENUM(TipoNEAE)))
  violencia_familia: int = Field(sa_column=Column(pg.INTEGER))
  enfermedad_grave_familia: int = Field(sa_column=Column(pg.INTEGER))
  catastrofe_familia: int = Field(sa_column=Column(pg.INTEGER))
  resilencia_familia: int = Field(sa_column=Column(pg.INTEGER))
  conducta_riesgo_observada: int = Field(sa_column=Column(pg.INTEGER))
    
class Consult(ConsultBase, table=True):
  id: Optional[UUID] = Field(sa_column=Column(pg.UUID, primary_key=True), default_factory=lambda: uuid4())
  created_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))
  updated_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))

class ConsultCreate(ConsultBase):
  pass

class AbstractErrorResponse(BaseModel, ABC):
  description: str
  content_type: str
  message: str

  @abstractmethod
  def custom_response() -> dict:
    pass

class ErrorResponse(AbstractErrorResponse):
  def custom_response(self) -> dict:
    return {
      "description": self.description,
      "content": {
        self.content_type: {
          "example": {
            "description": self.description,
            "message": self.message
          }
        }
      }
    }
