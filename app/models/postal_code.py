from sqlalchemy import Column, String, Integer
from app.database import Base


class Postal_code(Base):
    __tablename__ = 'postal_codes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_number = Column(String, nullable=True)
    detail_area = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)

