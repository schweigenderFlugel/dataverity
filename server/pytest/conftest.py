import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session
from dotenv import load_dotenv
import os

from api.main import app
from api.db import get_session

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL,
    # Only for SQLite database: connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)

@pytest.fixture(name='session')
def session_fixture():
  SQLModel.metadata.create_all(engine)
  with Session(engine) as session:
    yield session
  SQLModel.metadata.drop_all(engine)

@pytest.fixture(name='client')
def client_fixture(session: Session):
  def get_session_override():
    return session
  app.dependency_overrides[get_session] = get_session_override
  client = TestClient(app)
  yield client
  app.dependency_overrides.clear()