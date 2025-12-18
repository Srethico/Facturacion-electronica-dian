import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import SessionLocal
from app.db.models.user import User
from app.core.security import hash_password


def create_admin():
    db = SessionLocal()

    email = "admin@facturacion.com"

    existing = db.query(User).filter(User.email == email).first()
    if existing:
        print("✅ Admin ya existe")
        return

    admin = User(
        email=email,
        hashed_password=hash_password("Admin123*"),
        is_active=True,
        is_superuser=True,
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)

    print("🚀 Admin creado correctamente")
    print("📧 Email:", email)
    print("🔑 Password: Admin123*")


if __name__ == "__main__":
    create_admin()
