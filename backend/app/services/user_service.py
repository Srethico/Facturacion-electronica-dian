# backend/app/services/user_service.py

from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.models.user import User as DBUser
from app.schemas.user import UserCreate
from app.utils.security import get_password_hash # Importa la función de hashing

class UserService:
    """
    Clase de servicio que maneja las operaciones CRUD y autenticación para el modelo User.
    """
    def __init__(self, db: Session):
        self.db = db

    # ------------------ CREAR (CREATE) ------------------

    def create(self, user_in: UserCreate) -> DBUser:
        """Crea un nuevo usuario, hasheando la contraseña antes de guardar."""
        
        # 1. Hashing de la contraseña (¡CRUCIAL!)
        hashed_password = get_password_hash(user_in.password)
        
        # 2. Preparamos los datos para la DB
        db_user = DBUser(
            email=user_in.email,
            hashed_password=hashed_password,
            full_name=user_in.full_name,
            role=user_in.role,
            is_active=user_in.is_active
        )
        
        # 3. Guardar en la DB
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    # ------------------ LEER (READ) ------------------

    def get_by_email(self, email: str) -> Optional[DBUser]:
        """Obtiene un usuario por su correo electrónico (útil para login)."""
        return self.db.query(DBUser).filter(DBUser.email == email).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[DBUser]:
        """Obtiene una lista paginada de todos los usuarios."""
        return self.db.query(DBUser).offset(skip).limit(limit).all()

# (Otros métodos CRUD como get_by_id, update, delete se omiten por brevedad)