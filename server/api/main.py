from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.middlewares.logger import RequestLoggerMiddleware
from api.routes import auth

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.add_middleware(RequestLoggerMiddleware)
app.include_router(auth.router)

@app.get('/')
async def home():
  return { "message": "Hallo Welt" }