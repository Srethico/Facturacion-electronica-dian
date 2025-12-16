# backend/create_tables.py (MODIFICADO)

import os
import sys
# ¡NUEVA LÍNEA CLAVE!
from dotenv import load_dotenv

# Asegura que la aplicación pueda encontrar las rutas internas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

# Carga las variables de entorno desde el .env. Debe estar antes de cualquier importación que las use.
# El archivo .env debe estar en la raíz de la carpeta 'backend'
load_dotenv() 

# Importar la Base y el Motor de tu configuración (ahora DATABASE_URL ya existe)
from app.db.base import Base 
from app.db.session import engine 

# Importar todos los modelos para que Base.metadata los conozca
import app.db.models 

def create_all_tables():
    """Crea todas las tablas definidas en los modelos."""
    print("Intentando crear todas las tablas...")
    
    # 1. Conexión y Creación
    Base.metadata.create_all(bind=engine)
    
    # 2. Comprobación
    print("Creación de tablas finalizada.")
    print("Verifica tu DB. Si las tablas ya existían, no se regeneraron.")


if __name__ == "__main__":
    create_all_tables()