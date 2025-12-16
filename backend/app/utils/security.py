# backend/app/utils/security.py

from passlib.context import CryptContext
from app.core.config import PASSWORD_HASH_SCHEME

# Configuración del contexto de passlib para hashing
pwd_context = CryptContext(schemes=[PASSWORD_HASH_SCHEME], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con el hash almacenado.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Genera un hash seguro para la contraseña.
    """
    return pwd_context.hash(password)