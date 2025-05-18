from uuid import UUID
from enum import Enum
from sqlmodel import SQLModel, Field

class Genero(str, Enum):
  M = 'M'
  F = 'F'
  OTRO = 'Otro'

class TipoNEAE(str, Enum):
  TDAH = 'TDAH'
  TEA = 'TEA'
  Dislexia = 'Dislexia'
  Normal = 'Normal'

class Students(SQLModel):
  id_estudiante: int = Field(nullable=False)
  genero: Genero = Field(nullable=False) 
  grado: int = Field(nullable=False) 
  asistencia_inicial: bool = Field(nullable=False)
  asistencia: int = Field(nullable=False) 
  calificacion_matematica: int = Field(nullable=False) 
  calificacion_lengua: int = Field(nullable=False) 
  horas_clase_semanales: int = Field(nullable=False) 
  motivacion: int = Field(nullable=False) 
  habilidades_de_autoregulacion: int = Field(nullable=False) 
  habilidades_interpersonales: int = Field(nullable=False) 
  habilidades_intrapersonales: int = Field(nullable=False) 
  conducta_riesgo: int = Field(nullable=False) 
  libros_en_casa: int = Field(nullable=False) 
  internet_en_casa: int = Field(nullable=False) 
  distancia_escuela_km: int = Field(nullable=False) 
  clima_escolar: int = Field(nullable=False) 
  capacitacion_docente_anual_horas: int = Field(nullable=False) 
  tenencia_director_anos: int = Field(nullable=False) 
  adecuaciones_curriculare: int = Field(nullable=False)
  tipo_nea: TipoNEAE = Field(nullable=False)
  violencia_familia: int = Field(nullable=False)
  enfermedad_grave_familia: bool = Field(nullable=False)
  catastrofe_familia: int = Field(nullable=False)
  resilencia_familia: int = Field(nullable=False)
  conducta_riesgo_observad: bool = Field(nullable=False)

class StudentsTable(Students, table=True):
  id: int = Field(primary_key=True, default_factory=UUID)
    