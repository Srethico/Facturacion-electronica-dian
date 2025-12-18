from sqlalchemy import Column, Integer, String, Boolean, Numeric
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    sku = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)

    base_price = Column(Numeric(12, 2), nullable=False)

    tax_code = Column(String(10), nullable=False)
    tax_rate = Column(Numeric(5, 2), nullable=False)

    dian_product_code = Column(String(50), nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)
