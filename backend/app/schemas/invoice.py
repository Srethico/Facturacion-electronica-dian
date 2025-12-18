# backend/app/schemas/invoice.py

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# ----------------------------------------------------------------------
# 1. ÍTEMS DE FACTURA
# ----------------------------------------------------------------------

# Schema base para la línea de detalle (lo que se comparte al crear y devolver)
class InvoiceItemBase(BaseModel):
    product_code: str
    description: str
    quantity: float
    unit_price: float

# Schema para la creación de un ítem (lo que el cliente envía)
class InvoiceItemCreate(InvoiceItemBase):
    pass # Hereda de base, no necesita campos adicionales al crear

# Schema para la respuesta (incluye los cálculos hechos por el servidor)
class InvoiceItem(InvoiceItemBase):
    id: int
    invoice_id: int
    base_amount: float
    tax_rate: float
    tax_amount: float
    line_total: float
    
    class Config:
        from_attributes = True

# ----------------------------------------------------------------------
# 2. CABECERA DE FACTURA
# ----------------------------------------------------------------------

# Schema base para la factura
class InvoiceBase(BaseModel):
    client_id: int
    invoice_date: datetime # Usado para la fecha de emisión (creation_date)
    due_date: Optional[datetime] = None

# Schema para la creación (requiere el ID del cliente y la lista de ítems)
class InvoiceCreate(InvoiceBase):
    items: List[InvoiceItemCreate]

# Schema para la respuesta completa (incluye todos los cálculos y detalles)
class Invoice(InvoiceBase):
    id: int
    owner_id: int
    invoice_number: str
    subtotal: float
    total_tax: float
    total_invoice: float
    dian_status: str
    cufe: Optional[str] = None
    xml_cude: Optional[str] = None
    
    # La lista de ítems ya calculados y almacenados
    items: List[InvoiceItem] = [] 

    class Config:
        from_attributes = True