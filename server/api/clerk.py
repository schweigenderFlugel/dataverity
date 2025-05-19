from typing import Annotated
from fastapi import Request, HTTPException, Depends
from clerk_backend_api import Clerk
from dotenv import load_dotenv
import os

load_dotenv()
CLERK_SECRET_KEY = os.getenv('CLERK_SECRET_KEY')

clerk = Clerk(bearer_auth=CLERK_SECRET_KEY)

def protected_route(request: Request):
  auth_header = request.headers.get("Authorization")
  if not auth_header or not auth_header.startswith("Bearer "):
    raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    
  client_token = auth_header.split(" ")[1]
    
  try:
    client = clerk.clients.verify(client_token)
    if not client or not client.is_valid:
      raise HTTPException(status_code=401, detail="Invalid session")
  except Exception as e:
    raise HTTPException(status_code=401, detail=str(e))
    
  return {"message": f"Welcome, user {client.user_id}!"}

AuthDep = Annotated[str, Depends(protected_route)]