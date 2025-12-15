from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=False)

    price = Column(Numeric(12, 2), nullable=False)
    tax_rate = Column(Numeric(5, 2), nullable=False)  # 0, 5, 19

    created_at = Column(DateTime(timezone=True), server_default=func.now())
