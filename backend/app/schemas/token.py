# backend/app/schemas/token.py

from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    """
    Esquema de respuesta para el login (el token de acceso).
    """
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """
    Esquema para la data contenida dentro del token (el payload decodificado).
    """
    # 'sub' (subject) es el estándar, aquí usamos el email del usuario.
    email: Optional[str] = None
    # 'role' también se incluye para validaciones rápidas en el backend.
    role: Optional[str] = None