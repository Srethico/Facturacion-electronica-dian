from fastapi import APIRouter

from app.api.v1.routers import users, auth, products

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(products.router)  # 👈 ESTA ES LA CLAVE
