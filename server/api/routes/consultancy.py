from fastapi import APIRouter, Depends, Body, HTTPException
# from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError
# from fastapi.encoders import jsonable_encoder
from models.students import Student, StudentCreate
from db import DatabaseDep
from clerk import AuthDep
import os

load_dotenv()

CLERK_SECRET_KEY = os.getenv('CLERK_SECRET_KEY')
CLERK_JWKS_URL = os.getenv('CLERK_JWKS_URL')

router = APIRouter(
  tags=['Consultancy'],
  prefix='/consultancy',
)

@router.post("", tags=['Consultancy'], summary='Consultancy')
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
    return { "message": 'Consult successfully created!' }
  except Exception as e:
    if isinstance(e, IntegrityError) and "duplicate key value violates unique constraint" in str(e.orig):  # PostgreSQL
      raise HTTPException(status_code=400, detail="The consult already exists!")
    else:
      raise HTTPException(status_code=500, detail='Unexpected error!')