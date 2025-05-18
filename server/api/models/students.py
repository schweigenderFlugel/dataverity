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
  legajo: int = Field(sa_column=Column(pg.INTEGER, unique=True))
  genero: Genero = Field(sa_column=Column(pg.ENUM(Genero))) 
  grado: int = Field(sa_column=Column(pg.INTEGER)) 
  asistencia_inicial: int = Field(sa_column=Column(pg.INTEGER))
  asistencia: int = Field(sa_column=Column(pg.INTEGER)) 
  calificacion_matematica: int = Field(sa_column=Column(pg.INTEGER)) 
  calificacion_lengua: int = Field(sa_column=Column(pg.INTEGER)) 
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

class StudentCreate(StudentBase):
  pass