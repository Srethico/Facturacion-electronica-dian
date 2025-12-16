# backend/app/main.py (Actualizado)
from fastapi import FastAPI
from dotenv import load_dotenv



load_dotenv()  # Carga las variables de entorno desde el .env


from app.api.endpoints import clients
from app.api.endpoints import auth # Importa el nuevo módulo de autenticación
# from app.api.endpoints import products # Nuevo
from app.api.endpoints import invoice # Nuevo

app = FastAPI(title="Facturación Electrónica DIAN API")



# Router de Facturas
app.include_router(
    invoice.router,
    prefix="/api/v1/invoices",
    tags=["Facturas Electrónicas"]
)

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

@app.get("/")
def read_root():
    return {"message": "API de Facturación Electrónica (Simulación) funcionando."}