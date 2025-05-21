from fastapi import APIRouter, Body, HTTPException
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlmodel import select
from fastapi.responses import StreamingResponse
from uuid import UUID
import io
import csv

from models.consultancy import ConsultBase, Consult, ConsultCreate, ConsultUpdate
from models.response import Response
from db import DatabaseDep
from clerk import AuthDep

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
      description='Consult successfully created',
      content_type='application/json',
      message='Consult successfully created!',
    ).custom_response(),
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="Not authenticated"
    ).custom_response(),
    409: Response(
      description='The consult already exists', 
      content_type='application/json',
      message="The consult already exists"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Unexpected internal server error"
    ).custom_response(),
  },
  )
async def create_consult(
  # auth: AuthDep,
  session: DatabaseDep,
  body: ConsultCreate = Body(),
):
  try:
    consult = Consult.model_validate(body.model_dump())
    session.add(consult)
    session.commit()
    session.refresh(consult)
    return { "message": 'Consult successfully created!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=409, detail="The consult already exists")
    else:
      raise HTTPException(status_code=500, detail=e)
    
@router.put(
  '/{consult_id}',
  status_code=201,
  tags=['Consultancy'], 
  summary='Create a new consult',
  responses={
    201: Response(
      description='Consult successfully udpated',
      content_type='application/json',
      message='Consult successfully updated!',
    ).custom_response(),
    401: Response(
      description='The user is not authenticated', 
      content_type='application/json',
      message="Not authenticated"
    ).custom_response(),
    404: Response(
      description="The consult doesn't exist", 
      content_type='application/json',
      message="Not Found"
    ).custom_response(),
    500: Response(
      description='Unexpected error has ocurred', 
      content_type='application/json',
      message="Unexpected internal server error"
    ).custom_response(),
  },
  )
async def update_consult(
  # auth: AuthDep,
  session: DatabaseDep,
  consult_id: UUID,
  body: ConsultUpdate, # type: ignore
):
  try:
    consult = session.get(Consult, consult_id)
    consult_data_dict = body.model_dump(exclude_unset=True)
    consult.sqlmodel_update(consult_data_dict)
    session.add(consult)
    session.commit()
    session.refresh(consult)
    return { "message": 'Consult successfully updated!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=409, detail="The consult already exists")
    else:
      raise HTTPException(status_code=500, detail=e)
    
@router.get('', 
  status_code=200, 
  tags=['Consultancy'], 
  summary='Consultancy',
  response_class=StreamingResponse,
  responses={
    200: Response(
      description='Consult successfully created',
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
async def list_to_csv(
  # auth: AuthDep,
  session: DatabaseDep,
):
  buffer = io.StringIO()
  consults = session.exec(select(Consult)).all()
  keys = list(ConsultBase.model_fields.keys())
  writer = csv.DictWriter(buffer, fieldnames=keys)
  writer.writeheader()
  for c in consults:
    ignored = {"created_at", "updated_at", "id"}
    writer.writerow(c.model_dump(exclude=ignored))
  buffer.seek(0)
  return StreamingResponse(
    buffer,
    media_type="text/csv",
    headers={"Content-Disposition": "attachment; filename=studiantes.csv"}
  )
