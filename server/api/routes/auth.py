from fastapi import APIRouter
from server.api.db import DatabaseDep
from server.api.clerk import AuthDep

router = APIRouter(
  tags=['Auth'],
  prefix='/auth',
)

@router.post('/')
async def login(
  auth: AuthDep,
  session: DatabaseDep
):
  print(auth)