# backend/app/schemas/token.py

from pydantic import BaseModel
from typing import Optional

# --- 1. Datos que se GUARDAN DENTRO del Token (Payload) ---
class TokenData(BaseModel):
    # Esto es típicamente el email o el ID del usuario
    email: Optional[str] = None 

# --- 2. Respuesta de la API después de un Login exitoso ---
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer" # Estándar para tokens JWT