# backend/app/services/client_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

# Importar los modelos (tablas) de SQLAlchemy y los esquemas de Pydantic
from app.db.models.client import Client as DBClient
from app.schemas.client import ClientCreate, Client as ClientSchema # Renombramos Client para evitar confusión

# Definición de la clase de servicio que encapsula la lógica de la BD
class ClientService:
    """
    Clase de servicio que maneja todas las operaciones CRUD para el modelo Client.
    """
    def __init__(self, db: Session):
        # La sesión de la BD es inyectada en la instancia de servicio
        self.db = db

    # ------------------ CREAR (CREATE) ------------------

    def create(self, client_in: ClientCreate) -> DBClient:
        """Crea y guarda un nuevo cliente en la base de datos."""
        
        # 1. Creamos una instancia del modelo de la DB a partir de los datos Pydantic
        db_client = DBClient(**client_in.model_dump())
        
        # 2. Agregamos, confirmamos y actualizamos la instancia para obtener el ID
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        
        return db_client

    # ------------------ LEER (READ) ------------------
    
    def get_by_id(self, client_id: int) -> Optional[DBClient]:
        """Obtiene un cliente por su ID."""
        return self.db.query(DBClient).filter(DBClient.id == client_id).first()
    
    def get_by_identification(self, identification_number: str) -> Optional[DBClient]:
        """Obtiene un cliente por su NIT o Cédula."""
        return self.db.query(DBClient).filter(
            DBClient.identification_number == identification_number
        ).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[DBClient]:
        """Obtiene una lista paginada de todos los clientes."""
        return self.db.query(DBClient).offset(skip).limit(limit).all()

    # ------------------ ACTUALIZAR (UPDATE) ------------------
    # (Opcional por ahora, pero esencial para CRUD completo)

    # ------------------ ELIMINAR (DELETE) ------------------
    # (Opcional por ahora, pero esencial para CRUD completo)