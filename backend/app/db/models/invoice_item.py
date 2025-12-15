from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
from app.db.base import Base

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    product_code = Column(String(50))
    description = Column(String(255))

    quantity = Column(Numeric(10, 2))
    unit_price = Column(Numeric(12, 2))
    tax_rate = Column(Numeric(5, 2))
