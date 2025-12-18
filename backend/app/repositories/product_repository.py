from sqlalchemy.orm import Session
from app.modules.products.models import Product

class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Product:
        product = Product(**data)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def list(self):
        return (
            self.db
            .query(Product)
            .filter(Product.is_active == True)
            .order_by(Product.id.desc())
            .all()
        )

    def get_by_id(self, product_id: int):
        return (
            self.db
            .query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def get_by_sku(self, sku: str):
        return (
            self.db
            .query(Product)
            .filter(Product.sku == sku)
            .first()
        )

    def update(self, product: Product, data: dict):
        for key, value in data.items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def soft_delete(self, product: Product):
        product.is_active = False
        self.db.commit()
