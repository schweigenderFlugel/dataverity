import time
import logging
from logging.handlers import RotatingFileHandler
import os
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class RequestLoggerMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    LOG_DIR = "logs"
    LOG_FILE = "app.log"

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    os.makedirs(LOG_DIR, exist_ok=True)

    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logger = logging.getLogger(__name__)
    logger.info(f'Request: {response.status_code} {request.method} {request.url} completed in: {process_time:.4f} secomds')
    logger.setLevel(logging.INFO)

    if not logger.handlers:
      console_handler = logging.StreamHandler()
      console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
      logger.addHandler(console_handler)

      file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, LOG_FILE), maxBytes=1000000, backupCount=3
      )
          
      file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
      logger.addHandler(file_handler)

    return response
    