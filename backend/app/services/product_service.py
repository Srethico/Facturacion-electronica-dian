from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository

class ProductService:

    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def create_product(self, data: dict):
        if self.repo.get_by_sku(data["sku"]):
            raise ValueError("SKU ya existe")

        return self.repo.create(data)

    def list_products(self):
        return self.repo.list()

    def update_product(self, product_id: int, data: dict):
        product = self.repo.get_by_id(product_id)
        if not product:
            return None
        return self.repo.update(product, data)

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            return None
        self.repo.soft_delete(product)
        return product
