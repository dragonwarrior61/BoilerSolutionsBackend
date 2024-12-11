from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from typing import List
from app.database import get_db
from app.models.postal_code import Postal_code
from app.schemas.postal_code import Postal_codeCreate, Postal_codeRead, Postal_codeUpdate

router = APIRouter()

@router.post("/", response_model=Postal_codeRead)
async def create_postal_codes_(postal_codes: Postal_codeCreate, db: AsyncSession = Depends(get_db)):
    db_postal_code = Postal_code(**postal_codes.dict())
    db.add(db_postal_code)
    await db.commit()
    await db.refresh(db_postal_code)
    return db_postal_code

@router.get("/", response_model=List[Postal_codeRead])
async def get_postal_code(
    code: str,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Postal_code).where(str(Postal_code.postal_code).lower() == code.lower()))
    db_postal_code = result.scalars().first()
    if db_postal_code is None:
        return "We are sorry currently we don't cover your area"
    return db_postal_code

@router.delete("/{postal_codes}", response_model=Postal_codeRead)
async def delete_postal_code(code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Postal_code).filter(str(Postal_code.postal_code).lower() == code.lower()))
    postal_code = result.scalars().first()
    if postal_code is None:
        raise HTTPException(status_code=404, detail="postal_codes not found")
    await db.delete(postal_code)
    await db.commit()
    return postal_code
