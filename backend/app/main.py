# backend/app/main.py (Actualizado)

from fastapi import FastAPI
from app.api.endpoints import clients
from app.api.endpoints import auth # Importa el nuevo módulo de autenticación

app = FastAPI(title="Facturación Electrónica DIAN API")

# Router de Clientes
app.include_router(
    clients.router,
    prefix="/api/v1/clients",
    tags=["Clientes y Terceros"]
)

# Router de Autenticación (Login, Registro)
app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Autenticación"]
)

# ... (otras rutas)