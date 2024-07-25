from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, ARRAY, BigInteger
from app.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "internal_products"

    id = Column(BigInteger)
    part_number_key = Column(String, nullable=True)
    product_name = Column(Text, nullable=True)
    model_name = Column(Text, nullable=True)
    buy_button_rank = Column(Integer, nullable=True)
    ean = Column(Text, primary_key=True, unique=True)
    price = Column(Numeric(12, 4), nullable=True)
    sale_price = Column(Numeric(12, 4), nullable=True)
    image_link = Column(Text, nullable=True)
    barcode_title = Column(Text, nullable=True)
    masterbox_title = Column(Text, nullable=True)
    link_address_1688 = Column(Text, nullable=True)
    price_1688 = Column(Numeric(12, 4), nullable=True)
    variation_name_1688 = Column(Text, nullable=True)
    pcs_ctn = Column(Text, nullable=True)
    weight = Column(Numeric(12, 6), nullable=True)
    volumetric_weight = Column(Numeric(12, 6), nullable=True)
    dimensions = Column(Text, nullable=True)
    supplier_id = Column(Integer, nullable=True)
    english_name = Column(Text, nullable=True)
    romanian_name = Column(Text, nullable=True)
    material_name_en = Column(Text, nullable=True)
    material_name_ro = Column(Text, nullable=True)
    hs_code = Column(Text, nullable=True)
    battery = Column(Boolean, nullable=True)
    default_usage = Column(Text, nullable=True)
    production_time = Column(Numeric(12, 6), nullable=True)
    discontinued = Column(Boolean, nullable=True)
    stock = Column(Integer, nullable=True)
    warehouse = Column(Text, nullable=True)
    internal_shipping_price = Column(Numeric(12, 6), nullable=True)
    market_place = Column(ARRAY(Text), nullable=True)
    