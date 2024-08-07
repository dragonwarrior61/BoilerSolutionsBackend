from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ContactBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    contact_number: Optional[str] = None
    house_number: Optional[str] = None
    street_name: Optional[str] = None
    town: Optional[str] = None
    postcode: Optional[str] = None


class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactRead(ContactBase):
    email: str
    class Config:
        orm_mode = True
