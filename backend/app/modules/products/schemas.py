# app/modules/products/schemas.py
from pydantic import BaseModel
from decimal import Decimal

class ProductBase(BaseModel):
    code: str
    name: str
    price: Decimal
    iva: Decimal = 0

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    active: bool

    class Config:
        from_attributes = True
