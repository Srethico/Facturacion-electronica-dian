from sqlalchemy.orm import Session

from app.db.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self) -> None:
        self.repository = UserRepository()

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        # Verificar si el email ya existe
        existing_user = self.repository.get_by_email(db, user_in.email)
        if existing_user:
            raise ValueError("Email already registered")

        # Hash seguro del password
        hashed_password = hash_password(user_in.password)

        user = User(
            email=user_in.email,
            hashed_password=hashed_password,
            is_active=True,
            is_superuser=False,
        )

        return self.repository.create(db, user)
