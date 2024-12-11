from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
 

class OrderBase(BaseModel):
    client: Optional[str] = None
    user_name: Optional[str] = None
    email: Optional[str] = None
    product: Optional[str] = None
    price: Optional[Decimal] = None
    phone: Optional[str] = None
    date: Optional[str] = None
    status: Optional[int] = None
    payment_status: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    class Config:
        orm_mode = True
