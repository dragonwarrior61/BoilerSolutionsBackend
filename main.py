import asyncio
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from sqlalchemy import select
from app.routers import auth, users, profile, utils, postal_code
from app.database import Base, engine
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from create_database import *
from app.utils.postal_code import *
import ssl

# member
from fastapi import FastAPI
from pydantic import BaseModel
# from module import Member, get_member, check_access

app = FastAPI()

class MemberResponse(BaseModel):
    username: str
    role_name: str
    access_level: str

app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('ssl/cert.pem', keyfile='ssl/key.pem')

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_models()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])
app.include_router(utils.router, prefix="/api/utils", tags=["utils"])
app.include_router(postal_code.router, prefix="/postal_code", tags=["postal_code"])

if __name__ == "__main__":
    # Check if SSL arguments are provided
    import uvicorn

    ssl_keyfile = "ssl/key.pem"
    ssl_certfile = "ssl/cert.pem"
    # if ssl_keyfile and ssl_certfile:

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        # reload=True  # Optional: Enables auto-reload for code changes
    )
