from fastapi import APIRouter, Body, HTTPException
from pathlib import Path
from sqlalchemy.exc import IntegrityError
from sqlmodel import select
from fastapi.responses import StreamingResponse, JSONResponse
from uuid import UUID

import io
import csv
import json

from models.students import Students, StudentCreate, StudentUpdate, StudentsResponse
from models.users import Users
from models.response import Response
from db import DatabaseDep, CacheDep
from clerk import AuthDep
from data.generate_recommendations import generate_all_recommendations

router = APIRouter(
  tags=['Consultancy'],
  prefix='/consultancy',
)

@router.post(
  '',
  status_code=201,
  tags=['Consultancy'], 
  summary='Create a new consult',
  responses={
    201: Response(
      description='Student successfully created',
      content_type='application/json',
      message='Student successfully created!',
    ).custom_response(),
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="Not authenticated"
    ).custom_response(),
    409: Response(
      description='The Student already exists', 
      content_type='application/json',
      message="The student already exists"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Unexpected internal server error"
    ).custom_response(),
  },
)
async def create_student(
  auth: AuthDep,
  session: DatabaseDep,
  cache: CacheDep,
  body: StudentCreate = Body(),
):
  try:
    user_id = auth.payload['sub']
    user_found = session.exec(select(Users).where(Users.user_id == user_id)).first()
    cached_list = cache.get(f"list_{user_found.id}")
    if cached_list:
      cache.delete(f"list_{user_found.id}")
    data = body.model_dump()
    data['user_id'] = user_found.id 
    consult = Students.model_validate(data)
    session.add(consult)
    session.commit()
    session.refresh(consult)
    return { "message": 'Estudiante creado exitosamente!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=409, detail="El estuadiante ya existe")
    
@router.put(
  '/{consult_id}',
  status_code=201,
  tags=['Consultancy'], 
  summary='Create a new consult',
  responses={
    201: Response(
      description='Student successfully udpated',
      content_type='application/json',
      message='',
    ).custom_response(),
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="No autenticado"
    ).custom_response(),
    404: Response(
      description="The consult doesn't exist", 
      content_type='application/json',
      message="Estudiante no encontrado"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Error inesperado!"
    ).custom_response(),
  },
  )
async def update_student(
  auth: AuthDep,
  session: DatabaseDep,
  consult_id: UUID,
  body: StudentUpdate, # type: ignore
):
  try:
    consult = session.get(Students, consult_id)
    if consult is None:
      raise HTTPException(status_code=404, detail="Consult not found")
    consult_data_dict = body.model_dump(exclude_unset=True)
    consult.sqlmodel_update(consult_data_dict)
    session.add(consult)
    session.commit()
    session.refresh(consult)
    return { "message": 'Estudiante actualizado existosamente!' }
  except HTTPException as http_err:
    raise http_err
  except Exception as e:
    raise HTTPException(status_code=500, detail=e)
  
@router.get(
  '/list', 
  status_code=200, 
  tags=['Consultancy'], 
  summary='Consultancy',
  response_class=StreamingResponse,
  responses={
    200: Response(
      description='Get a list of students',
      content_type='application/json',
      message='Consult successfully created!',
    ).custom_response(),
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="Not authenticated"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Unexpected internal server error"
    ).custom_response(),
  },
)
async def get_students_list(
  auth: AuthDep,
  session: DatabaseDep,
  cache: CacheDep
):
  try:
    user_id = auth.payload['sub']
    user_found = session.exec(select(Users).where(Users.user_id == user_id)).first()
    consults = session.exec(select(Students).where(Students.user_id == user_found.id)).all()
    cached_list = cache.get(f"list_{user_found.id}")
    
    if cached_list:
      return JSONResponse(content=json.loads(cached_list))
    
    data = [student.model_dump(mode='json') for student in consults]
    cache.set(f"list_{user_found.id}", json.dumps(data), ex=120)
    return JSONResponse(content=data)
  except Exception:
    raise HTTPException(status_code=500, detail='Error inesperado!')

    
@router.get(
  '/list-to-csv', 
  status_code=200, 
  tags=['Consultancy'], 
  summary='Consultancy',
  response_class=StreamingResponse,
  responses={
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="Not authenticated"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Error inesperado!"
    ).custom_response(),
  },
)
async def students_list_to_csv(
  auth: AuthDep,
  session: DatabaseDep,
):
  try:
    buffer = io.StringIO()
    user_id = auth.payload['sub']
    user_found = session.exec(select(Users).where(Users.user_id == user_id)).first()
    consults = session.exec(select(Students).where(Students.user_id == user_found.id)).all()
    keys = list(StudentsResponse.model_fields.keys())
    writer = csv.DictWriter(buffer, fieldnames=keys)
    writer.writeheader()
    for c in consults:
      ignored = {"created_at", "updated_at", 'user_id', 'user'}
      writer.writerow(c.model_dump(exclude=ignored))
    buffer.seek(0)
    return StreamingResponse(
      buffer,
      media_type="text/csv",
      headers={"Content-Disposition": "attachment; filename=studiantes.csv"}
    )
  except Exception:
    raise HTTPException(status_code=500, detail='Error inesperado!')

@router.get('/recommendations')
async def get_recommendations(
  auth: AuthDep,
  session: DatabaseDep,
):
  buffer = io.StringIO()
  user_id = auth.payload['sub']
  user_found = session.exec(select(Users).where(Users.user_id == user_id)).first()
  consults = session.exec(select(Students).where(Students.user_id == user_found.id)).all()
  keys = list(StudentsResponse.model_fields.keys())
  writer = csv.DictWriter(buffer, fieldnames=keys)
  writer.writeheader()
  for c in consults:
    ignored = {"created_at", "updated_at", 'user_id', 'user'}
    writer.writerow(c.model_dump(exclude=ignored))
  buffer.seek(0)
  base_url = Path(__file__).resolve(strict=True).parent
  path = (base_url / ".." / "data" / "simulacion_estudiantes.csv").resolve()  
  output_dir = (base_url / ".." / "outputs").resolve()
  return generate_all_recommendations(buffer, output_dir)