from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)

    number = Column(String(50), unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    total = Column(Numeric(14, 2), nullable=False)
    tax_total = Column(Numeric(14, 2), nullable=False)

    status = Column(String(30), default="PENDING")  
    # PENDING | SENT | ACCEPTED | REJECTED

    created_at = Column(DateTime(timezone=True), server_default=func.now())
