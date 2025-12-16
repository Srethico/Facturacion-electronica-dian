# backend/app/schemas/invoice.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ----------------------------------------
# 1. ÍTEM DE FACTURA (BASE)
# ----------------------------------------

class InvoiceItemBase(BaseModel):
    """
    Esquema base para la línea de detalle de la factura.
    """
    product_code: Optional[str] = Field(None, max_length=50)
    description: str = Field(..., max_length=255, description="Descripción del producto o servicio.")
    quantity: float = Field(..., gt=0, description="Cantidad vendida.")
    unit_price: float = Field(..., ge=0, description="Precio unitario antes de impuestos.")
    # La tasa de impuesto se puede enviar, pero el servicio puede usar un valor por defecto.
    tax_rate: float = Field(0.19, ge=0, description="Tasa de IVA aplicada (ej. 0.19 para 19%).")
    
# ----------------------------------------
# 2. ÍTEM DE FACTURA (RESPUESTA)
# ----------------------------------------

class InvoiceItem(InvoiceItemBase):
    """
    Esquema completo para la respuesta del ítem, incluyendo los totales calculados.
    """
    id: int
    invoice_id: int
    
    # Campos calculados por el servicio
    base_amount: float
    tax_amount: float
    total_amount: float

    class Config:
        from_attributes = True

# ----------------------------------------
# 3. CREACIÓN DE FACTURA (ENTRADA)
# ----------------------------------------

class InvoiceCreate(BaseModel):
    """
    Esquema de entrada para crear una nueva factura.
    """
    client_id: int = Field(..., description="ID del cliente receptor (debe existir en la DB).")
    due_date: Optional[datetime] = Field(None, description="Fecha de vencimiento de la factura.")
    
    # Lista de ítems de la factura
    items: List[InvoiceItemBase] = Field(..., min_length=1, description="Lista de líneas de detalle de la factura.")

# ----------------------------------------
# 4. FACTURA COMPLETA (RESPUESTA)
# ----------------------------------------

class Invoice(BaseModel):
    """
    Esquema de respuesta para la factura completa.
    """
    id: int
    invoice_number: str
    creation_date: datetime
    due_date: Optional[datetime]
    
    # Relaciones y Totales
    owner_id: int
    client_id: int
    subtotal: float
    total_tax: float
    total_invoice: float
    
    # Campos de la DIAN
    dian_status: str
    cufe: Optional[str]
    
    # La lista de ítems ya procesados y calculados
    items: List[InvoiceItem] = Field(..., description="Detalles de las líneas de la factura.")

    class Config:
        from_attributes = True