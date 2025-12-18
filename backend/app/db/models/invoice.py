# backend/app/db/models/invoice.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
# Importaciones de modelos y base
from app.db.base import Base 




# 1. MODELO DE LÍNEA DE DETALLE (INVOICE ITEM)
# =================================================================

class InvoiceItem(Base):
    """
    Representa una línea de detalle dentro de una Factura Electrónica.
    """
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)

    # Relación con la Cabecera de Factura
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    invoice = relationship("Invoice", back_populates="items") # <-- Conecta con la cabecera

    # Detalles del Item (Producto/Servicio)
    product_code = Column(String(50), index=True, nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    
    # Cálculos de Impuestos para este item
    base_amount = Column(Float, nullable=False) # Cantidad * Precio Unitario
    tax_rate = Column(Float, default=0.19, nullable=False) # Tasa de IVA (ej: 0.19 para 19%)
    tax_amount = Column(Float, nullable=False) # base_amount * tax_rate
    
    # Total de la línea (base_amount + tax_amount)
    line_total = Column(Float, nullable=False)


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