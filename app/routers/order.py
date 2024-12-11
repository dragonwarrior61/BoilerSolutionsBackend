from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate

router = APIRouter()

@router.post("/", response_model=OrderRead)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

@router.get("/count")
async def get_orders_count(
    email: str = Query('', description="email address"),
    db: AsyncSession = Depends(get_db)
):
    query = select(Order)
    if email:
        query = query.where(Order.email == email)
    result = await db.execute(query)
    db_orders = result.scalars().all()

    return len(db_orders)

@router.get("/")
async def get_orders(
    page: int = Query(1, ge=1, description="Page number"),
    items_per_page: int = Query(50, ge=1, le=100, description="Number of items per page"),
    email: str = Query('', description='eamil address'),
    db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * items_per_page
    query = select(Order)
    if email:
        query = query.where(Order.email == email)
    query = query.offset(offset).limit(items_per_page)
    result = await db.execute(query)
    db_orders = result.scalars().all()
    return db_orders

@router.get("/{id}", response_model=List[OrderRead])
async def get_order(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Order).where(Order.id == id))
    db_order = result.scalars().first()
    if db_order is None:
        return "We are sorry currently we don't cover your area"
    return db_order

@router.put("/{id}", response_model=OrderRead)
async def update_order(id: int, courier: OrderUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).filter(Order.id == id))
    db_order = result.scalars().first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="couriers not found")
    for var, value in vars(courier).items():
        setattr(db_order, var, value) if value else None
    await db.commit()
    await db.refresh(db_order)
    return db_order

@router.delete("/{id}", response_model=OrderRead)
async def delete_order(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).filter(Order.id == id))
    order = result.scalars().first()
    if order is None:
        raise HTTPException(status_code=404, detail="orders not found")
    await db.delete(order)
    await db.commit()
    return order
