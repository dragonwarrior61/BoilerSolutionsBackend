from sqlalchemy import Column, String, Integer
from app.database import Base


class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    catalog_id = Column(String, nullable=True)
    area_id = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    discount = Column(Integer, nullable=True)

