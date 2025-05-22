from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING
from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import TIMESTAMP
import sqlalchemy.dialects.postgresql as pg

class Role(Enum):
  ADMIN = 'ADMIN'
  NORMAL = 'NORMAL'

if TYPE_CHECKING:
  from .students import Students

class CreateUpdateDate(SQLModel):
  created_at: Optional[datetime] = Field(sa_column=Column(TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))
  updated_at: Optional[datetime] = Field(sa_column=Column(TIMESTAMP), default_factory=lambda: datetime.now(timezone.utc))

class UsersBase(SQLModel):
  user_id: str = Field(sa_column=Column(pg.VARCHAR, unique=True))

class UsersIdRole(SQLModel):
  id: Optional[UUID] = Field(sa_column=Column(pg.UUID, primary_key=True), default_factory=lambda: uuid4())
  role: Optional[Role] = Field(sa_column=Column(pg.ENUM(Role)), default=Role.NORMAL)

class Users(CreateUpdateDate, UsersBase, UsersIdRole, table=True):
  __tablename__ = 'users'
  students: List["Students"] = Relationship(back_populates="user")

class Login(UsersBase):
  pass