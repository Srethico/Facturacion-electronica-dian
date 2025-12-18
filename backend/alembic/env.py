from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys



# --------------------------------------------------
# Alembic Config
# --------------------------------------------------

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --------------------------------------------------
# Add app to PYTHONPATH
# --------------------------------------------------

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --------------------------------------------------
# Import metadata
# --------------------------------------------------

from app.core.settings import settings
from app.db.base import Base
from app.db.models import *  # noqa
from app.modules.products.models import Product  # noqa


target_metadata = Base.metadata

# --------------------------------------------------
# Offline migrations
# --------------------------------------------------


def run_migrations_offline() -> None:
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# --------------------------------------------------
# Online migrations
# --------------------------------------------------


def run_migrations_online() -> None:
    connectable = engine_from_config(
        {
            "sqlalchemy.url": settings.DATABASE_URL
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,        # detecta cambios de tipo
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# --------------------------------------------------
# Run
# --------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
