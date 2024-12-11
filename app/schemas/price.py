from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PriceBase(BaseModel):
    id: int
    catalog_id: Optional[str] = None
    area_id: Optional[int] = None
    price: Optional[int] = None
    discount: Optional[int] = None

class PriceCreate(PriceBase):
    pass

class PriceUpdate(PriceBase):
    pass

class PriceRead(PriceBase):
    id: int
    class Config:
        orm_mode = True
