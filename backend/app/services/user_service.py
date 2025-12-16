# backend/app/services/user_service.py

from sqlalchemy.orm import Session
from app.db.models.user import User as DBUser, UserRole
from app.schemas.user import UserRegister, UserCreate
from app.utils.security import get_password_hash, verify_password 
from app.utils.jwt import create_access_token # Podría no ser necesario aquí, pero se usa en auth.py

from typing import Optional

class UserService:
    def __init__(self, db: Session):
        self.db = db

    # =================================================================
    # LECTURA
    # =================================================================
    
    def get_by_email(self, email: str) -> Optional[DBUser]:
        """Busca un usuario por su dirección de correo electrónico."""
        return self.db.query(DBUser).filter(DBUser.email == email).first()

    # =================================================================
    # CREACIÓN (La lógica crucial para el registro)
    # =================================================================

    def create(self, user_in: UserRegister) -> DBUser:
        """
        Crea un nuevo usuario en la base de datos a partir del esquema de registro.
        Asigna el hash de la contraseña y los valores por defecto.
        """
        # 1. Hashear la contraseña
        hashed_password = get_password_hash(user_in.password)
        
        # 2. Crear el objeto del modelo de base de datos
        db_user = DBUser(
            email=user_in.email,
            full_name=user_in.full_name,
            # Campos de control que asignamos por defecto:
            hashed_password=hashed_password,
            role=UserRole.VENDEDOR,     # Rol por defecto para un nuevo registro
            is_active=True,             # Activo por defecto
            is_superuser=False          # No es superusuario por defecto
        )

        # 3. Guardar en la DB
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        
        return db_user

    # =================================================================
    # AUTENTICACIÓN
    # =================================================================

    def authenticate(self, email: str, password: str) -> Optional[DBUser]:
        """
        Verifica las credenciales de un usuario.
        """
        user = self.get_by_email(email)
        
        if user and verify_password(password, user.hashed_password):
            return user
        
        return None

    # Nota: Tu endpoint /token usa este método, pero el endpoint /register usa create()

# Renombramiento de métodos para que coincida con tu auth.py (si es necesario)
    def get_user_by_email(self, email: str) -> Optional[DBUser]:
        return self.get_by_email(email)