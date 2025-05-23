from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os
import redis

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_USERNAME = os.getenv('REDIS_USERNAME')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

engine = create_engine(DATABASE_URL)

def create_db_and_tables(app: FastAPI):
  SQLModel.metadata.create_all(engine)
  yield

def get_session():
  with Session(engine) as session:
    try:
      yield session
    finally:
      session.close()

def get_data_cache():
  return redis.Redis(
    host=REDIS_HOST,
    port=int(REDIS_PORT),
    decode_responses=True,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
  )

DatabaseDep = Annotated[Session, Depends(get_session)]
CacheDep = Annotated[redis.Redis, Depends(get_data_cache)]