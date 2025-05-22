import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session
from clerk_backend_api.jwks_helpers import RequestState, Session
from dotenv import load_dotenv
import os

from api.main import app
from api.db import get_session
from api.clerk import protected_route

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL,
    # Only for SQLite database: connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)

def fake_protected_route(request):
  return RequestState(
    is_signed_in=True,
    session=Session(user_id="test-user-id", session_id="fake-session-id", status="active"),
    user=None
  )

# Sobrescribimos la dependencia real
app.dependency_overrides[protected_route] = fake_protected_route

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
  def override_get_current_user():
    return {"id": "test-user-id", "email": "test@example.com"}
  app.dependency_overrides[get_session] = get_session_override
  app.dependency_overrides[protected_route] = override_get_current_user

  client = TestClient(app)
  yield client
  app.dependency_overrides.clear()