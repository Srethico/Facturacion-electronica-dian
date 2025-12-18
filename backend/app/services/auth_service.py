from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.core.security import verify_password


class AuthService:
    """
    Servicio de autenticación.
    Contiene la lógica REAL de login.
    """

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def authenticate(self, db: Session, email: str, password: str) -> bool:
        """
        Verifica credenciales de usuario.
        Devuelve True si son válidas, False si no.
        """
        user = self.user_repository.get_by_email(db, email)

        if not user:
            return False

        if not user.is_active:
            return False

        return verify_password(password, user.hashed_password)
