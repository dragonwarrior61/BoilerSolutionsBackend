from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Postal_codeBase(BaseModel):
    group_number: Optional[str] = None
    detail_area: Optional[str] = None
    postal_code: Optional[str] = None

class Postal_codeCreate(Postal_codeBase):
    pass

class Postal_codeUpdate(Postal_codeBase):
    pass

class Postal_codeRead(Postal_codeBase):
    id: int
    class Config:
        orm_mode = True
