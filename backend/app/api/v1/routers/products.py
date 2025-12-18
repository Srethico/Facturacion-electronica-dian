from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.v1.routers.auth import get_current_user
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(get_current_user)],
)

@router.post("/", response_model=ProductOut)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
):
    service = ProductService(db)
    return service.create_product(data.dict())

@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.list_products()

@router.put("/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
):
    service = ProductService(db)
    product = service.update_product(
        product_id,
        data.dict(exclude_unset=True),
    )
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    service = ProductService(db)
    product = service.delete_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}
