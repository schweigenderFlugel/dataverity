from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.logger import RequestLoggerMiddleware
from routes import consultancy
import uvicorn

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.add_middleware(RequestLoggerMiddleware)
app.include_router(consultancy.router)

@app.get('/')
async def home():
  return { "message": "Hallo Welto" }

if __name__ == "__main__":
  uvicorn.run(
    "main:app",
    host="localhost",
    port=3000,
    reload=True,
    use_colors=True
  )