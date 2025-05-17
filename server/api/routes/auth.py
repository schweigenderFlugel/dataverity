from jose import jwt
from jose.exceptions import JWTError
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Request, status, Depends
import httpx

import os

load_dotenv()

CLERK_SECRET_KEY = os.getenv('CLERK_SECRET_KEY')
CLERK_JWKS_URL = os.getenv('CLERK_JWKS_URL')
CLERK_ISSUER = os.getenv('CLERK_ISSUER')


router = APIRouter(
    tags=['Auth'],
    prefix='/auth',
)

@router.get('/login')
async def login():
    jwks_cache = {}

async def get_jwks():
    global jwks_cache
    if not jwks_cache:
        async with httpx.AsyncClient() as client:
            response = await client.get(CLERK_JWKS_URL)
            jwks_cache = response.json()
    return jwks_cache

async def verify_token(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = auth_header.replace("Bearer ", "")

    jwks = await get_jwks()

    for key in jwks["keys"]:
        try:
            payload = jwt.decode(
                token,
                key=key,
                algorithms=["RS256"],
                audience=CLERK_AUDIENCE,
                issuer=CLERK_ISSUER,
            )
            return payload  # usuario autenticado
        except JWTError:
            continue

    raise HTTPException(status_code=401, detail="Invalid token")