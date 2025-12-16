# backend/app/schemas/client.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# ----------------------------------------
# 1. Esquema Base (Campos Comunes)
# ----------------------------------------
class ClientBase(BaseModel):
    identification_type: str = Field(..., max_length=5, description="Tipo de identificación (ej. NIT, C.C.)")
    identification_number: str = Field(..., max_length=20, description="Número de identificación o NIT")
    name: str = Field(..., max_length=150, description="Razón social o nombre completo del cliente")
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    # Código fiscal (Responsabilidad ante la DIAN)
    fiscal_responsibility_code: Optional[str] = Field("R-99-PN", max_length=10, description="Código de responsabilidad fiscal (e.g., R-99-PN para Persona Natural)")
    city_code: Optional[str] = Field(None, max_length=10, description="Código DANE de la ciudad")

# ----------------------------------------
# 2. Esquema de Creación (Datos de Entrada)
# ----------------------------------------
class ClientCreate(ClientBase):
    pass
    # No agregamos campos aquí, ya que ClientBase define la entrada completa.

# ----------------------------------------
# 3. Esquema de Respuesta (Datos de Salida)
# ----------------------------------------
class Client(ClientBase):
    id: int
    # Relación con el usuario que lo creó (para auditoría y multi-tenancy)
    owner_id: int 

    class Config:
        from_attributes = True # Permite mapeo desde el modelo SQLAlchemy (DB)