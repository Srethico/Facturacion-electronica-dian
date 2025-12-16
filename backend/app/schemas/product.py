# backend/app/schemas/product.py
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    sku: str
    name: str
    base_price: Decimal # Usar Decimal para precisión monetaria
    tax_code: str
    tax_rate: Decimal
    dian_product_code: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True