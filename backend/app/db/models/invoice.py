# backend/app/db/models/invoice.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
# Importaciones de modelos y base
from app.db.base import Base 



# =================================================================
# 2. MODELO DE CABECERA DE FACTURA (INVOICE)
# =================================================================

class Invoice(Base):
    """
    Representa la cabecera de una Factura Electrónica de Venta.
    """
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    
    # Datos de la Factura (Internos)
    invoice_number = Column(String(50), unique=True, index=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True) # Fecha de vencimiento

    # Relación con el Vendedor (Owner)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="invoices")

    # Relación con el Cliente
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", back_populates="invoices")

    # Datos Financieros (Totales)
    subtotal = Column(Float, nullable=False) # Suma de base_amount de los items
    total_tax = Column(Float, nullable=False) # Suma de tax_amount de los items
    total_invoice = Column(Float, nullable=False) # Subtotal + Total Impuestos

    # Campos de la DIAN (Simulados)
    dian_status = Column(String(20), default="PENDIENTE", nullable=False) # PENDIENTE, ACEPTADA, RECHAZADA
    cufe = Column(String(100), unique=True, index=True, nullable=True) # Código Único de Factura Electrónica
    xml_cude = Column(Text, nullable=True) # Para almacenar el XML de la respuesta de la DIAN (simulado)

    # Relaciones con las líneas de detalle
    # cascade="all, delete-orphan" asegura que si borras la factura, se borran sus items.
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan", lazy="dynamic")