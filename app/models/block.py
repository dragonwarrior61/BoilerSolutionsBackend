from sqlalchemy import Column, String, Integer
from app.database import Base


class Block(Base):
    __tablename__ = 'blockes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, nullable=True)
    group_number = Column(String, nullable=True)
    detail_area = Column(String, nullable=True)