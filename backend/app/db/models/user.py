from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    CONTADOR = "CONTADOR"
    VENDEDOR = "VENDEDOR"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)

    role = Column(Enum(UserRole), default=UserRole.VENDEDOR, nullable=False)

    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Relaciones
    clients = relationship(
        "Client",
        back_populates="owner",
        lazy="dynamic"
    )

    invoices = relationship(
        "Invoice",
        back_populates="owner",
        lazy="dynamic"
    )

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role.name}')>"
