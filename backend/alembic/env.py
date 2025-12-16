import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# --- INICIO DEL CÓDIGO AÑADIDO PARA LA RUTA DE IMPORTACIÓN ---
# Esto añade la carpeta 'backend' al PYTHONPATH para que la importación 'from app...' funcione.
# Obtenemos la ruta del directorio donde se encuentra este script (alembic/env.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Subimos un nivel para obtener la ruta de la carpeta 'backend'
backend_dir = os.path.join(current_dir, "..")
# Añadimos 'backend' a la ruta de búsqueda de módulos de Python
sys.path.append(backend_dir)
# --- FIN DEL CÓDIGO AÑADIDO ---


from app.db.base import Base  # Esta línea ahora debería funcionar
# tu Base declarativa

# esto carga el archivo alembic.ini
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()