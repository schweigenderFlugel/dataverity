from datetime import datetime
from typing import Optional
from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column, Integer, String
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

class StudentBase(SQLModel):
  id_estudiante: int = Field(sa_column=Column(pg.INTEGER, unique=True))
  legajo: str = Field(sa_column=Column(pg.VARCHAR, unique=True), max_length=10)
  nombre: str = Field(sa_column=Column(pg.VARCHAR), max_length=30, description='Tiene que ser nombre completo')
  edad: int = Field(sa_column=Column(pg.SMALLINT), max_length=10)
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
  adecuaciones_curriculare: int = Field(Integer, nullable=False)
  tipo_nea: TipoNEAE = Field(sa_column=Column(pg.ENUM(TipoNEAE)))
  violencia_familia: int = Field(sa_column=Column(pg.INTEGER))
  enfermedad_grave_familia: int = Field(sa_column=Column(pg.INTEGER))
  catastrofe_familia: int = Field(sa_column=Column(pg.INTEGER))
  resilencia_familia: int = Field(sa_column=Column(pg.INTEGER))
  conducta_riesgo_observada: int = Field(sa_column=Column(pg.INTEGER))
    
class Student(StudentBase, table=True):
  id: Optional[UUID] = Field(sa_column=Column(pg.UUID, nullable=True, primary_key=True), default=uuid4())
  createdAt: Optional[int] = Field(sa_column=Column(pg.DATE, nullable=True), default=datetime.timestamp(datetime.now()))
  updatedAt: Optional[int] = Field(sa_column=Column(pg.DATE, nullable=True), default=datetime.timestamp(datetime.now()))

class StudentCreate(StudentBase):
  pass

class StudentUpdate(Optional[StudentBase]):
  pass