from sqlalchemy import Column, Text, ARRAY, Integer
from app.database import Base

class Calendar(Base):
    __tablename__ = 'calender'
    date = Column(Text, primary_key=True)
    number = Column(Integer, nullable=True)
    email = Column(ARRAY(Text), nullable=True)
    st_time = Column(ARRAY(Text), nullable=True)
    en_time = Column(ARRAY(Text), nullable=True)

