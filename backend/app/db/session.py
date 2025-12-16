# backend/app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os # Necesario para leer variables de entorno

# --- Configuración (Basada en tu .env) ---

# IMPORTANTE: Asegúrate de tener instalada la librería 'python-dotenv'
# pip install python-dotenv
# Y de cargar las variables al inicio de tu app o usar la configuración de FastAPI
# Por simplicidad, asumiremos que DATABASE_URL ya está disponible.

# Lee la URL de conexión de tu variable de entorno
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # Esto es una comprobación de seguridad, ajusta según tu config de entorno
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")


# Crea el motor (engine) de SQLAlchemy
# `pool_pre_ping=True` ayuda a mantener las conexiones a la BD.
# `echo=False` (cambia a True para ver las consultas SQL en la consola)
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True, 
    echo=False
)

# Crea la clase SessionLocal. Esta será la clase que instanciarás para interactuar con la DB.
# autocommit=False: Control manual de transacciones
# autoflush=False: No vaciar automáticamente (útil para más control)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# --- Dependencia de FastAPI ---

# Esta función es un generador que provee una nueva sesión de DB para cada solicitud API.
# FastAPI la usará con Depends(get_db).
def get_db() -> Generator:
    """
    Función de dependencia que provee una sesión de SQLAlchemy a los endpoints.
    Asegura que la sesión se cierre después de cada solicitud.
    """
    db = SessionLocal()
    try:
        yield db # Retorna la sesión al endpoint
    finally:
        db.close() # Cierra la conexión después de que la solicitud ha sido procesada