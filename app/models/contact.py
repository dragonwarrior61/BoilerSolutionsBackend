from sqlalchemy import Column, String, Integer
from app.database import Base


class Contact(Base):
    __tablename__ = 'contacts'
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, primary_key=True)
    contact_number = Column(String, nullable=True)
    house_number = Column(String, nullable=True)
    street_name = Column(String, nullable=True)
    town = Column(String, nullable=True)
    postcode = Column(String, nullable=True)

