from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)

    document_type = Column(String(10), nullable=False)   # CC, NIT, CE
    document_number = Column(String(50), nullable=False)

    name = Column(String(255), nullable=False)
    email = Column(String(255))

    address = Column(String(255))
    municipality_code = Column(String(10))  # Código DIAN

    created_at = Column(DateTime(timezone=True), server_default=func.now())
