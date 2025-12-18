from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


# =========================
# BASE
# =========================
class ProductBase(BaseModel):
    sku: str
    name: str
    base_price: Decimal = Field(..., gt=0, decimal_places=2)
    tax_code: str
    tax_rate: Decimal = Field(..., ge=0, le=100, decimal_places=2)
    dian_product_code: Optional[str] = None


# =========================
# CREATE
# =========================
class ProductCreate(ProductBase):
    pass


# =========================
# UPDATE
# =========================
class ProductUpdate(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    base_price: Optional[Decimal] = None
    tax_code: Optional[str] = None
    tax_rate: Optional[Decimal] = None
    dian_product_code: Optional[str] = None
    is_active: Optional[bool] = None


# =========================
# OUTPUT
# =========================
class ProductOut(ProductBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
