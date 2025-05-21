from fastapi.testclient import TestClient
from fastapi import status

data_to_send = {
  'legajo': '12345',
  'nombre': 'John Doe',
  'edad': '10',
  'genero': 'M',
  'grado': '5',
  'seccion': 'A',
  'asistencia_inicial': True,
  'asistencia': 20, 
  'calificacion_matematica': 7.5,
  'calificacion_lengua': 9.0,
  'horas_clase_semanales': 20,
  'motivacion': 2,
  'habilidades_de_autoregulacion': 3,
  'habilidades_interpersonales': 2,
  'habilidades_intrapersonales': 3,
  'conducta_riesgo': 4,
  'libros_en_casa': False,
  'internet_en_casa': True,
  'distancia_escuela_km': 50.6,
  'clima_escolar': 3,
  'capacitacion_docente_anual_horas': 20,
  'tenencia_director_anos': 10,
  'adecuaciones_curriculares': True,
  'tipo_nea': 'TEA',
  'violencia_familia': False,
  'enfermedad_grave_familia': False,
  'catastrofe_familia': True,
  'resilencia_familia': 4,
  'conducta_riesgo_observada': True, 
}

def test_get_consults(client: TestClient):
  response = client.get('/consultancy')
  assert response.status_code == status.HTTP_200_OK
  assert response.headers["content-type"] == "text/csv; charset=utf-8"
  assert response.headers["content-disposition"] == 'attachment; filename=studiantes.csv'

def test_create_consult_invalid(client: TestClient):
  response = client.post(
    "/consultancy",
    json={'legajo': '12345', 'nombre': 'John Doe', 'edad': '10'},
  )
  assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_consult(client: TestClient):
  response = client.post(
    "/consultancy",
    json=data_to_send,
  )
  assert response.status_code == status.HTTP_201_CREATED
  assert response.json() == {
    'message': 'Consult successfully created!' 
  }