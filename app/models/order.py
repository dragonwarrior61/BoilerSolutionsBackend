from sqlalchemy import Column, String, Integer, DECIMAL
from app.database import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client = Column(String, nullable=True)
    user_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    product = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=True)
    phone = Column(String, nullable=True)
    date = Column(String, nullable=True)
    status = Column(Integer, nullable=True)
    payment_status = Column(Integer, nullable=True)
