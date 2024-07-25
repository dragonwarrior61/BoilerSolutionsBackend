from sqlalchemy import Column, Integer, ARRAY, Text, Boolean, DateTime
from app.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=True)
    date = Column(DateTime, nullable=True)
    type = Column(Text, nullable=True)
    status = Column(Text, nullable=True)
    warehouse = Column(Text, nullable=True)
    note = Column(Text, nullable=True)
    agent_name = Column(Text, nullable=True)
    ean = Column(ARRAY(Text), nullable=True)
    quantity = Column(ARRAY(Integer), nullable=True)
    supplier_name = Column(ARRAY(Text), nullable=True)
    item = Column(ARRAY(Integer), nullable=True)
    pdf_sent = Column(ARRAY(Boolean), nullable=True)
    pay_url = Column(ARRAY(Text), nullable=True)
    tracking = Column(ARRAY(Text), nullable=True)
    arrive_agent = Column(ARRAY(Boolean), nullable=True)
    wechat_group = Column(ARRAY(Text), nullable=True)
    pp = Column(ARRAY(Text), nullable=True)
    each_status = Column(ARRAY(Text), nullable=True)
    shipment_name = Column(ARRAY(Text), nullable=True)
    box_number = Column(ARRAY(Integer), nullable=True)
    document = Column(ARRAY(Text), nullable=True)
    add_date = Column(ARRAY(DateTime), nullable=True)
    date_agent = Column(ARRAY(DateTime), nullable=True)
    SID = Column(ARRAY(Text), nullable=True)
    GID = Column(ARRAY(Text), nullable=True)
    date_port = Column(ARRAY(DateTime), nullable=True)
    newid = Column(ARRAY(Text), nullable=True)