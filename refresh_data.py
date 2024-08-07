import asyncio
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from sqlalchemy import select
from app.database import Base, engine
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.utils.postal_code import *
import ssl
import logging



# member
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
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
async def on_startup(db: AsyncSession = Depends(get_db)):
    await init_models()
    
    await refresh_postal_code(db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("refresh_data:app", host="0.0.0.0", port=3000, reload=False)
    