import pytest
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.core.security import hash_password
from app.db.session import SessionLocal
from fastapi.testclient import TestClient

from app.main import app




@pytest.fixture(scope="session")
def db():
    db = SessionLocal()
    yield db
    db.close()


@pytest.fixture(scope="session", autouse=True)
def seed_users(db: Session):
    def upsert_user(email: str, **kwargs):
        user = db.query(User).filter(User.email == email).first()
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
        else:
            user = User(email=email, **kwargs)
            db.add(user)

    upsert_user(
        email="admin@facturacion.com",
        hashed_password=hash_password("PasswordSeguro123"),
        role="admin",
        is_superuser=True,
        is_active=True,
    )

    upsert_user(
        email="user@facturacion.com",
        hashed_password=hash_password("PasswordSeguro123"),
        role="user",
        is_active=True,
    )

    db.commit()


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
