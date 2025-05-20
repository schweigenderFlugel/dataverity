from fastapi import APIRouter, Depends, Body, HTTPException
from server.api.models.consultancy import Student, StudentCreate
from db import DatabaseDep
from clerk import AuthDep

router = APIRouter(
  tags=['Auth'],
  prefix='/auth',
)

@router.post('/')
async def login(
  auth: AuthDep,
  session: DatabaseDep
):
  print(auth.credentials)