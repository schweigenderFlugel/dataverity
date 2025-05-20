from fastapi.testclient import TestClient
from fastapi import status

data_to_send = {
  'legajo': '12345',
  'nombre': 'John Doe',
  'edad': '10',
  'genero': 'M',
  'grado': '5',
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
  'libros_en_casa': 20,
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

def test_creat_customer(client: TestClient):
  reponse = client.get(
    '/consultancy',
    json={
      'message': 'User successfully registered' 
    }
  )
  assert reponse.status_code == status.HTTP_201_CREATED


def test_create_item(client: TestClient):
  response = client.post(
    "/items/",
    headers={"X-Token": "coneofsilence"},
    json=data_to_send,
  )
  assert response.status_code == 200
  assert response.json() == {
    "id": "foobar",
    "title": "Foo Bar",
    "description": "The Foo Barters",
  }


def test_create_item_bad_token(client: TestClient):
  response = client.post(
    "/items/",
    headers={"X-Token": "hailhydra"},
    json=data_to_send,
  )
  assert response.status_code == 400
  assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item(client: TestClient):
  response = client.post(
    "/items/",
    headers={"X-Token": "coneofsilence"},
    json=data_to_send,
  )
  assert response.status_code == 409
  assert response.json() == {"detail": "Item already exists"}