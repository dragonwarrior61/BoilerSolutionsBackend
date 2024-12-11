from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.models.price import Price
from app.schemas.price import PriceCreate, PriceRead, PriceUpdate

router = APIRouter()

@router.post("/", response_model=PriceRead)
async def create_price(price: PriceCreate, db: AsyncSession = Depends(get_db)):
    db_price = Price(**price.dict())
    db.add(db_price)
    await db.commit()
    await db.refresh(db_price)
    return db_price

@router.get('/count')
async def get_prices_count(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Price))
    db_prices = result.scalars().all()
    return len(db_prices)

@router.get("/all", response_model=List[PriceRead])
async def get_prices(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Price))
    db_prices = result.scalars().all()
    return db_prices

@router.get("/", response_model=PriceRead)
async def get_price(
    catalog_id: str,
    area_id: int,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Price).where(Price.catalog_id == catalog_id, Price.area_id == area_id))
    db_price = result.scalars().first()
    return db_price

@router.put("/{id}", response_model=PriceRead)
async def update_price(id: int, price: PriceUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Price).where(Price.id == id))
    db_price = result.scalars().first()
    if db_price is None:
        raise HTTPException(status_code=404, detail="couriers not found")
    for var, value in vars(price).items():
        setattr(db_price, var, value) if value else None
    await db.commit()
    await db.refresh(db_price)
    return db_price

@router.delete("/{id}", response_model=PriceRead)
async def delete_price(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Price).filter(Price.id == id))
    price = result.scalars().first()
    if price is None:
        raise HTTPException(status_code=404, detail="prices not found")
    await db.delete(price)
    await db.commit()
    return price
