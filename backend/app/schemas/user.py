# backend/app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from app.db.models.user import UserRole # Importamos el Enum que definiste

# --- 1. Esquema de Creación (Datos de Entrada) ---
class UserCreate(BaseModel):
    # La contraseña solo se necesita al crear o cambiar. Nunca se devuelve.
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.VENDEDOR # Permitir asignar un rol al crear
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True

# --- 2. Esquema de Respuesta (Datos de Salida) ---
class User(BaseModel):
    # Nunca devolvemos la contraseña (hashed_password)
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True