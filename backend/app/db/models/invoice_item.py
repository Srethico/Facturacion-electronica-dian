# backend/app/db/models/invoice_item.py

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relación con la cabecera de la factura
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    invoice = relationship("Invoice", back_populates="items")

    # Relación con el maestro de productos (opcional, pero buena práctica)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True) 
    product = relationship("Product")
    
    # --- Datos de la línea (copia de los datos del producto al momento de facturar) ---
    
    description = Column(String, nullable=False)
    quantity = Column(Numeric(10, 2), nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    
    # --- Cálculos y Fiscales ---
    
    line_extension_amount = Column(Numeric(10, 2), nullable=False) # Cantidad * Precio Unitario
    
    # Impuestos aplicados a esta línea
    tax_rate = Column(Numeric(5, 2), nullable=False) 
    tax_amount = Column(Numeric(10, 2), nullable=False)
    
    # Total de la línea (Extension Amount + Tax Amount)
    total_line_amount = Column(Numeric(10, 2), nullable=False)