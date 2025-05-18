from fastapi import APIRouter, Depends, Body
from fastapi.responses import  JSONResponse
from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from models.students import Student, StudentBase, StudentCreate
from db import DatabaseDep
import os

load_dotenv()

CLERK_SECRET_KEY = os.getenv('CLERK_SECRET_KEY')
CLERK_JWKS_URL = os.getenv('CLERK_JWKS_URL')

router = APIRouter(
    tags=['Consultancy'],
    prefix='/consultancy',
)

clerk_config = ClerkConfig(jwks_url=CLERK_JWKS_URL)
clerk_auth_guard = ClerkHTTPBearer(config=clerk_config)

@router.post("", tags=['Consultancy'], summary='Consultancy')
async def consultancy(
  session: DatabaseDep,
  body: StudentCreate = Body(),
  # credentials: HTTPAuthorizationCredentials | None = Depends(clerk_auth_guard)
):
  consult = Student.model_validate(body.model_dump())
  session.add(consult)
  session.commit()
  session.refresh(consult)
  return { "message": 'Consult successfully created!' }
  # return JSONResponse(content=jsonable_encoder(credentials))