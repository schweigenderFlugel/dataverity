from fastapi import APIRouter, Depends, Body, HTTPException
from api.models.auth import UserBase
from api.db import DatabaseDep
from api.clerk import AuthDep

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