# backend/app/core/config.py

import os
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv() 

# =================================================================
# CONFIGURACIÓN DE SEGURIDAD JWT
# =================================================================

# Clave secreta para firmar los tokens JWT. 
# Se recomienda usar una clave compleja de al menos 32 bytes (256 bits).
# Idealmente, obtenida de un generador seguro o del entorno (os.environ).
SECRET_KEY = os.environ.get("SECRET_KEY", "tu-clave-secreta-de-32-bytes-aqui-cambiala-en-produccion!")

# Algoritmo de hashing para JWT (ej. HS256, HS512)
ALGORITHM = "HS256"

# Tiempo de expiración del token de acceso (en segundos). 30 minutos por defecto.
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 30  

# =================================================================
# CONFIGURACIÓN DE HASHING (Contraseñas)
# =================================================================

# Esquema de hashing preferido para las contraseñas
PASSWORD_HASH_SCHEME = "bcrypt"