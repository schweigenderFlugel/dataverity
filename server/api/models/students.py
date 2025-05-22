from typing import Optional, TYPE_CHECKING
from datetime import datetime, timezone
from typing import Optional
from decimal import Decimal
from enum import Enum as PyEnum
from sqlalchemy import Column, SmallInteger, Integer, Boolean, Enum, VARCHAR, Numeric, TIMESTAMP
from sqlmodel import SQLModel, Field, Relationship
from pydantic import create_model

if TYPE_CHECKING:
  from .users import Users

class Genero(str, PyEnum):
  M = 'M'
  F = 'F'

class Seccion(str, PyEnum):
  A = 'A'
  B = 'B'
  C = 'C'

class TipoNEAE(str, PyEnum):
  TDAH = 'TDAH'
  TEA = 'TEA'
  Dislexia = 'Dislexia'
  Normal = 'Normal'

class StudentsBase(SQLModel):
  legajo: str = Field(sa_column=Column(VARCHAR, unique=True))
  nombre: str = Field(sa_column=Column(VARCHAR(30)), description='Tiene que ser nombre completo')
  edad: int = Field(sa_column=Column(SmallInteger), description='Tiene que ser un número entero', gt=4, lt=14)
  genero: Genero = Field(sa_column=Column(Enum(Genero)))
  grado: int = Field(sa_column=Column(SmallInteger), gt=0, lt=7)
  seccion: Seccion = Field(sa_column=Column(Enum(Seccion)))
  asistencia_inicial: bool = Field(sa_column=Column(Boolean))
  asistencia: Decimal = Field(sa_column=Column(Numeric(5,2)))
  calificacion_matematica: Decimal = Field(sa_column=Column(Numeric(4,2)), gt=-1, lt=11)
  calificacion_lengua: Decimal = Field(sa_column=Column(Numeric(4,2)), gt=-1, lt=11)
  horas_clase_semanales: int = Field(sa_column=Column(SmallInteger))
  motivacion: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  habilidades_de_autoregulacion: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  habilidades_interpersonales: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  habilidades_intrapersonales: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  conducta_riesgo: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  libros_en_casa: bool = Field(sa_column=Column(Boolean))
  internet_en_casa: bool = Field(sa_column=Column(Boolean))
  distancia_escuela_km: Decimal = Field(sa_column=Column(Numeric(5,2)))
  clima_escolar: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  capacitacion_docente_anual_horas: int = Field(sa_column=Column(SmallInteger))
  tenencia_director_anos: int = Field(sa_column=Column(Integer))
  adecuaciones_curriculares: bool = Field(sa_column=Column(Boolean))
  tipo_neae: TipoNEAE = Field(sa_column=Column(Enum(TipoNEAE)))
  violencia_familiar: bool = Field(sa_column=Column(Boolean))
  enfermedad_grave_familiar: bool = Field(sa_column=Column(Boolean))
  catastrofe_familiar: bool = Field(sa_column=Column(Boolean))
  resilencia_familiar: int = Field(sa_column=Column(SmallInteger), gt=0, lt=6)
  conducta_riesgo_observada: bool = Field(sa_column=Column(Boolean))

class CreateUpdateDate(SQLModel):
  created_at: Optional[datetime] = Field(sa_column=Column(TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))
  updated_at: Optional[datetime] = Field(sa_column=Column(TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))

class StudentIdModel(SQLModel):
  id_estudiante: Optional[int] = Field(default=None, primary_key=True, lt=541)
  
class Students(CreateUpdateDate, StudentsBase, StudentIdModel, table=True):
  __tablename__ = 'students'
  user_id: str = Field(foreign_key="users.id")
  user: Optional["Users"] = Relationship(back_populates="students")

class StudentsResponse(StudentsBase, StudentIdModel):
  pass

class StudentCreate(StudentsBase):
  pass

optional_fields = {
  field: (Optional[typ], None)
  for field, typ in StudentsBase.__annotations__.items()
}

StudentUpdate = create_model(
    "StudentUpdate",
    __base__=StudentsBase,
    **optional_fields
)
