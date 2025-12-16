# backend/app/db/models/user.py

from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db.base import Base # Importamos tu base declarativa
import enum

# Definimos los roles permitidos en la aplicación
class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    CONTADOR = "CONTADOR"
    VENDEDOR = "VENDEDOR"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # Usuario de acceso (e.g., correo electrónico)
    email = Column(String, unique=True, index=True, nullable=False)
    
    # Contraseña hasheada (¡NUNCA la contraseña en texto plano!)
    hashed_password = Column(String, nullable=False) 
    
    # Información personal
    full_name = Column(String)
    
    # Rol del usuario (importante para permisos de facturación)
    role = Column(Enum(UserRole), default=UserRole.VENDEDOR, nullable=False)
    
    # Estado de la cuenta
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role.name}')>"