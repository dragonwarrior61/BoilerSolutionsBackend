from pydantic import BaseModel
from typing import List, Optional

class CalendarBase(BaseModel):
    number: Optional[int] = None
    email: Optional[List[str]] = None
    st_time: Optional[List[str]] = None
    en_time: Optional[List[str]] = None


class CalendarCreate(CalendarBase):
    pass

class CalendarUpdate(CalendarBase):
    pass

class CalendarRead(CalendarBase):
    date: str
    class Config:
        orm_mode = True
