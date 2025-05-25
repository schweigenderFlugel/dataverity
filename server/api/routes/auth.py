from fastapi import APIRouter, HTTPException
from db import DatabaseDep
from clerk import AuthDep
from sqlmodel import select

from models.users import Users

router = APIRouter(
  tags=['Auth'],
  prefix='/auth',
)

@router.get('/')
async def login(
  auth: AuthDep,
  session: DatabaseDep,
):
  try:
    user_id = auth.payload['sub']
    registered = session.exec(select(Users).where(Users.user_id == user_id)).first()
    if registered: return { "message": "Ingesaste exitosamente!" }
    else:
      user = Users(user_id=user_id)
      session.add(user)
      session.commit()
      session.refresh(user)
      return { "message": "Exitosamente registrado!" }
  except Exception as e:
    raise HTTPException(status_code=500, detail='Error inesperado!')