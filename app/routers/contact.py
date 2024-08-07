from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactRead, ContactUpdate

router = APIRouter()

@router.post("/", response_model=ContactRead)
async def create_contact(contact: ContactCreate, db: AsyncSession = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

@router.get('/count')
async def get_contacts_count(db: AsyncSession = Depends(get_db)):
    result = await db.execute(func.count(Contact.email))
    count = result.scalar()
    return count

@router.get("/", response_model=List[ContactRead])
async def get_contacts(
    email: str,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Contact).where(Contact.email == email))
    db_contact = result.scalars().first()
    if db_contact is None:
        return "We are sorry currently we don't cover your area"
    return db_contact

@router.put("/{email}", response_model=ContactRead)
async def update_contact(email: str, courier: ContactUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Contact).filter(Contact.email == email))
    db_contact = result.scalars().first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="couriers not found")
    for var, value in vars(courier).items():
        setattr(db_contact, var, value) if value else None
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

@router.delete("/{email}", response_model=ContactRead)
async def delete_contact(email: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Contact).filter(Contact.email == email))
    contact = result.scalars().first()
    if contact is None:
        raise HTTPException(status_code=404, detail="contacts not found")
    await db.delete(contact)
    await db.commit()
    return contact
