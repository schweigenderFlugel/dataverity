from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.exc import IntegrityError
from models.students import Student, StudentCreate
from db import DatabaseDep
from clerk import AuthDep
from utils.csv_utils import csv_file

router = APIRouter(
  tags=['Consultancy'],
  prefix='/consultancy',
)

@router.post('', status_code=201, tags=['Consultancy'], summary='Consultancy')
async def consultancy(
  auth: AuthDep,
  session: DatabaseDep,
  body: StudentCreate = Body(),
):
  try:
    consult = Student.model_validate(body.model_dump())
    session.add(consult)
    session.commit()
    session.refresh(consult)
    keys = [k for k in consult.model_dump().keys()]
    values = [v for v in consult.model_dump().values()]
    csv_file(keys, values)
    return { "message": 'Consult successfully created!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=400, detail="The consult already exists!")
    else:
      raise HTTPException(status_code=500, detail='Unexpected error!')
    
@router.post('', status_code=201, tags=['Consultancy'], summary='Consultancy')
async def consultancy(
  auth: AuthDep,
  session: DatabaseDep,
  body: StudentCreate = Body(),
):
  try:
    consult = Student.model_validate(body.model_dump())
    session.add(consult)
    session.commit()
    session.refresh(consult)
    keys = [k for k in consult.model_dump().keys()]
    values = [v for v in consult.model_dump().values()]
    csv_file(keys, values)
    return { "message": 'Consult successfully created!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=400, detail="The consult already exists!")
    else:
      raise HTTPException(status_code=500, detail='Unexpected error!')
    
