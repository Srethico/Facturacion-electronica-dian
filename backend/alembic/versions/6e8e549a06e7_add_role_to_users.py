"""add role to users

Revision ID: 6e8e549a06e7
Revises: 5e432adaadd6
Create Date: 2025-12-17
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6e8e549a06e7"
down_revision = "5e432adaadd6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1️⃣ Agregar columna CON DEFAULT
    op.add_column(
        "users",
        sa.Column(
            "role",
            sa.String(length=20),
            nullable=False,
            server_default="user",
        ),
    )

    # 2️⃣ Crear índice
    op.create_index("ix_users_role", "users", ["role"], unique=False)

    # 3️⃣ Quitar el default (opcional pero profesional)
    op.alter_column("users", "role", server_default=None)


def downgrade() -> None:
    op.drop_index("ix_users_role", table_name="users")
    op.drop_column("users", "role")
