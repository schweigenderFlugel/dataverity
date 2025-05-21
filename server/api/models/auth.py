from datetime import datetime, timezone
from typing import Optional
from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

class Role(Enum):
  ADMIN = 'ADMIN'
  NORMAL = 'NORMAL'

class UserBase(SQLModel):
  email: str = Field(sa_column=Column(pg.VARCHAR, unique=True), description='Tiene que ser un email único')

class User(UserBase, table=True):
  __tablename__ = 'users'

  id: Optional[UUID] = Field(sa_column=Column(pg.UUID, primary_key=True), default_factory=lambda: uuid4())
  role: Optional[Role] = Field(sa_column=Column(pg.ENUM(Role)), default=Role.NORMAL)
  created_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))
  updated_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))

class Login(UserBase):
  pass