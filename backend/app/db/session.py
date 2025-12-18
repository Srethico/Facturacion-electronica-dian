from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,      # evita conexiones muertas
    pool_size=10,
    max_overflow=20,
    future=True,             # SQLAlchemy 2.x
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
