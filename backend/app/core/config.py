# backend/app/core/config.py

import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv() 

# --- Configuración de JWT ---
# Deberías generar una clave más compleja y guardarla en tu .env
SECRET_KEY = os.environ.get("SECRET_KEY", "CLAVE_SECRETA") 
ALGORITHM = "HS256"
# Tiempo de vida del token (1 hora = 3600 segundos)
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60