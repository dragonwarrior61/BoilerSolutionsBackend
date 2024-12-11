from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from typing import List
from app.database import get_db
from app.models.block import Block
from app.schemas.block import BlockCreate, BlockRead, BlockUpdate

router = APIRouter()

@router.post("/", response_model=BlockRead)
async def create_block(block: BlockCreate, db: AsyncSession = Depends(get_db)):
    db_block = Block(**block.dict())
    db.add(db_block)
    await db.commit()
    await db.refresh(db_block)
    return db_block

@router.get("/")
async def get_block(
    date: str = Query('', description="Text for date"),
    group_number: str = Query('', description="Text for group_number"),
    detail_area: str = Query('', description="Text for detail_area"),
    db: AsyncSession = Depends(get_db)
):
    query = select(Block)
    if date:
        query = query.where(Block.date == date)
    if group_number:
        query = query.where(Block.group_number == group_number)
        if detail_area:
            query = query.where(Block.detail_area == detail_area)
    result = await db.execute(query)
    db_block = result.scalars().all()
    if db_block is None:
        raise HTTPException(status_code=404, detail="block not found")
    return db_block

@router.get("/block_detail")
async def get_block(
    date: str = Query('', description="Text for date"),
    group_number: str = Query('', description="Text for group_number"),
    detail_area: str = Query('', description="Text for detail_area"),
    db: AsyncSession = Depends(get_db)
):
    query = select(Block)
    if date:
        query = query.where(Block.date == date)
    if group_number:
        query = query.where(Block.group_number == group_number)
        if detail_area:
            query = query.where(Block.detail_area == detail_area)
    result = await db.execute(query)
    db_block = result.scalars().all()
    if db_block:
        return True
    else:
        return False

@router.put("/{id}", response_model=BlockRead)
async def update_block(id: int, block: BlockUpdate, db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(Block).where(Block.id == id))
    db_block = result.scalars().first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="block not found")
    for var, value in vars(block).items():
        setattr(db_block, var, value) if value else None
    await db.commit()
    await db.refresh(db_block)
    return db_block

@router.delete("/{id}", response_model=BlockRead)
async def delete_block(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Block).filter(Block.id == id))
    db_block = result.scalars().first()
    if db_block is None:
        raise HTTPException(status_code=404, detail="block not found")
    await db.delete(db_block)
    await db.commit()
    return db_block
