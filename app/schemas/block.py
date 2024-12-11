from pydantic import BaseModel
from typing import List, Optional

class BlockBase(BaseModel):
    date: Optional[str] = None
    group_number: Optional[str] = None
    detail_area: Optional[str] = None


class BlockCreate(BlockBase):
    pass

class BlockUpdate(BlockBase):
    pass

class BlockRead(BlockBase):
    id: int
    class Config:
        orm_mode = True
