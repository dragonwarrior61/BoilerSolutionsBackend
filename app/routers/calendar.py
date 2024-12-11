from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.models.calendar import Calendar
from app.schemas.calendar import CalendarCreate, CalendarRead, CalendarUpdate
from sqlalchemy import any_

router = APIRouter()

@router.post("/", response_model=CalendarRead)
async def create_calendar(date: str, email: str, st_time: str, en_time: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Calendar).where(Calendar.date == date))
    db_calendar = result.scalars().first()

    if db_calendar is None:
        db_calendar = Calendar(date = date, number = 1, email = [email], st_time = [st_time], en_time = [en_time])
        db.add(db_calendar)

    else:
        db_calendar.number += 1
        db_calendar.email = db_calendar.email + [email]
        db_calendar.st_time = db_calendar.st_time + [st_time]
        db_calendar.en_time = db_calendar.en_time + [en_time]

    await db.commit()
    await db.refresh(db_calendar)
    return db_calendar

@router.get("/admin", response_model=List[CalendarRead])
async def get_calendar(
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(Calendar))
    db_calendars = result.scalars().all()

    return db_calendars

@router.get("/{email}", response_model=List[CalendarRead])
async def get_user_calendar(
    email: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Calendar).where(email == any_(Calendar.email)))
    db_calendars = result.scalars().all()

    return db_calendars

@router.put("/", response_model=CalendarRead)
async def update_calendar(date: str, number: int, email: str, st_time: str, en_time: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Calendar).filter(Calendar.date == date))
    db_calendar = result.scalars().first()
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="couriers not found")
    db_calendar.email[number - 1] = email
    db_calendar.st_time[number - 1] = st_time
    db_calendar.en_time[number - 1] = en_time
    await db.commit()
    await db.refresh(db_calendar)
    return db_calendar

@router.delete("/", response_model=CalendarRead)
async def delete_calendar(date: str, number: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Calendar).filter(Calendar.date == date))
    db_calendar = result.scalars().first()
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="calendar not found")
    
    del db_calendar.email[number - 1]
    del db_calendar.st_time[number - 1]
    del db_calendar.en_time[number - 1]
    
    db_calendar.number -= 1
    await db.commit()
    
    return db_calendar
