from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """
    Esquema estándar de respuesta de autenticación.
    Incluye access token y refresh token.
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    Payload decodificado del JWT (uso interno).
    NO se expone directamente al cliente.
    """
    email: Optional[str] = None
