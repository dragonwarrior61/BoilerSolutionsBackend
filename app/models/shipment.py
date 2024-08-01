from sqlalchemy import Column, Integer, ARRAY, Text, Boolean, DateTime, Numeric
from app.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=True)
    delivery_date = Column(DateTime, nullable=True)
    type = Column(Text, nullable=True)
    status = Column(Text, nullable=True)
    warehouse = Column(Text, nullable=True)
    note = Column(Text, nullable=True)
    agent = Column(Text, nullable=True)
    awb = Column(Text, nullable=True)
    vat = Column(Numeric(12, 4), nullable=True)
    custom_taxes = Column(Numeric(12, 4), nullable=True)
    shipment_cost = Column(Numeric(12, 4), nullable=True)
    ean = Column(ARRAY(Text), nullable=True)
    quantity = Column(ARRAY(Integer), nullable=True)
    item_per_box = Column(ARRAY(Integer), nullable=True)
    pdf_sent = Column(ARRAY(Boolean), nullable=True)
    pay_url = Column(ARRAY(Text), nullable=True)
    tracking = Column(ARRAY(Text), nullable=True)
    arrive_agent = Column(ARRAY(Boolean), nullable=True)
    wechat_group = Column(ARRAY(Text), nullable=True)
    pp = Column(ARRAY(Text), nullable=True)
    each_status = Column(ARRAY(Text), nullable=True)
    box_number = Column(ARRAY(Integer), nullable=True)
    document = Column(ARRAY(Text), nullable=True)
    date_added = Column(ARRAY(DateTime), nullable=True)
    date_agent = Column(ARRAY(DateTime), nullable=True)
    user = Column(ARRAY(Integer), nullable=True)