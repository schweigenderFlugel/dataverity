import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session
from api.main import app
from dotenv import load_dotenv
import os

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}, # check_same_thread: FastAPI corre en un entono multihilo, y false es para evitar que se ejecute un codigo en un hilo y un codigo en otro 
    poolclass=StaticPool, # StaticPool: para crear un base de datos temporal en la memoria
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