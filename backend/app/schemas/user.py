# backend/app/schemas/user.py (CORREGIDO Y AMPLIADO)

from pydantic import BaseModel, EmailStr
from typing import Optional
from app.db.models.user import UserRole # Importamos el Enum que definiste

# --- 1. Esquema de Registro (PARA EL ENDPOINT /auth/register) ---
# Este es el esquema MINIMAL que solo el usuario proporciona.
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    
    # NOTA: Omitimos 'role' y 'is_active' para evitar el 422 en el registro público.

# --- 2. Esquema de Creación Interna (USADO POR ADMIN O SERVICIO) ---
# Este esquema permite a un administrador crear o modificar todos los campos.
class UserCreate(UserRegister): # Heredamos los campos básicos
    role: UserRole = UserRole.VENDEDOR 
    is_active: Optional[bool] = True
    
    class Config:
        # Esto solo es necesario para la clase base si se usa directamente
        from_attributes = True


# --- 3. Esquema de Respuesta (Datos de Salida) ---
class User(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True

# --- 4. Esquema para Actualización ---
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None