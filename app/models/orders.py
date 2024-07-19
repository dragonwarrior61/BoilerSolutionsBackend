from sqlalchemy import Column, String, Integer, Float, DateTime, PrimaryKeyConstraint, ARRAY, BigInteger
from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(BigInteger)
    vendor_name = Column(String, nullable=True, primary_key=True)
    type = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=True)
    payment_mode = Column(String, nullable=True)
    detailed_payment_method = Column(String, nullable=True)
    delivery_mode = Column(String, nullable=True)
    status = Column(Integer, nullable=True)
    payment_status = Column(Integer, nullable=True)
    customer_id = Column(BigInteger, nullable=True)
    product_id = Column(ARRAY(BigInteger), nullable=True)
    quantity = Column(ARRAY(Integer), nullable=True)
    shipping_tax = Column(Float, nullable=True)
    shipping_tax_voucher_split = Column(String, nullable=True)
    vouchers = Column(String, nullable=True)
    proforms = Column(String, nullable=True)
    attachments = Column(String, nullable=True)
    cashed_co = Column(Float, nullable=True)
    cashed_cod = Column(Float, nullable=True)
    refunded_amount = Column(Float, nullable=True)
    is_complete = Column(Integer, nullable=True)
    cancellation_reason = Column(String, nullable=True)
    refund_status = Column(String, nullable=True)
    maximum_date_for_shipment = Column(DateTime, nullable=True)
    late_shipment = Column(Integer, nullable=True)
    flags = Column(String, nullable=True)
    emag_club = Column(Integer, nullable=True)
    finalization_date = Column(DateTime, nullable=True)
    details = Column(String, nullable=True)
    payment_mode_id = Column(Integer, nullable=True)
    order_market_place = Column(String, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'order_market_place', name='pk_id_order_market_place'),
    )

