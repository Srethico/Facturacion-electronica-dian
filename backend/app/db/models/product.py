# backend/app/db/models/product.py

from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from app.db.base import Base # Importamos tu base declarativa

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    
    # Código interno del producto (SKU)
    sku = Column(String, unique=True, nullable=False)
    
    # Nombre del producto/servicio
    name = Column(String, nullable=False)
    
    # Precio base sin impuestos
    base_price = Column(Numeric(10, 2), nullable=False)
    
    # --- Campos Fiscales DIAN ---
    
    # Código del Impuesto (e.g., 01=IVA, 03=Impuesto al Consumo)
    tax_code = Column(String, default="01", nullable=False)
    
    # Porcentaje de impuesto (e.g., 19.0 para IVA)
    tax_rate = Column(Numeric(5, 2), default=19.00, nullable=False)
    
    # Código de Clasificación UNSPSC o Código Interno de la empresa (requerido por DIAN)
    dian_product_code = Column(String, nullable=True) 

    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Product(sku='{self.sku}', name='{self.name}')>"