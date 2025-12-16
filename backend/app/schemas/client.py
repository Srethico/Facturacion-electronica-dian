# backend/app/schemas/client.py

from pydantic import BaseModel, EmailStr
from typing import Optional

# --- Schema Base para la Creación (Datos de Entrada) ---
class ClientCreate(BaseModel):
    # Campos obligatorios para crear un cliente
    identification_number: str
    type_identification: str  # Código DIAN (e.g., '31' para NIT)
    business_name: str
    fiscal_responsibility_code: str = "R-99-PN" # Valor por defecto común
    address: str
    city_code: str # Código DANE
    email: Optional[EmailStr] = None 
    phone: Optional[str] = None

    class Config:
        # Permite que Pydantic lea los campos por nombre aunque sean de SQLAlchemy
        from_attributes = True

# --- Schema para la Respuesta (Datos de Salida) ---
class Client(ClientCreate):
    id: int
    is_active: bool
    
    # Esto asegura que la clase Client se mantenga limpia para la API.
    # No es necesario agregar más si ya está en ClientCreate.