from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

# from middlewares.logger import RequestLoggerMiddleware
from routes import consultancy, auth
from db import create_db_and_tables
from gemini import get_gemini_response

load_dotenv()

BACKEND_URL = os.getenv('BACKEND_URL')
FRONTEND_URL = os.getenv('FRONTEND_URL')

app = FastAPI(lifespan=create_db_and_tables)

app.add_middleware(
  CORSMiddleware,
  allow_origins=[BACKEND_URL, FRONTEND_URL],
  allow_credentials=True,
  allow_methods=["HEAD", "GET", "POST", "PUT", "DELETE"],
  allow_headers=["*"],
)

# app.add_middleware(RequestLoggerMiddleware)
app.include_router(consultancy.router)
app.include_router(auth.router)

get_gemini_response()

if __name__ == "__main__":
  environment = os.getenv("ENVIRONMENT")
  uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=3000,
    reload=(environment == "development"),
    use_colors=True
  )