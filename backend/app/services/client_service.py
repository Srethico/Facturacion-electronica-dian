# backend/app/services/client_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models.client import Client as DBClient
from app.db.models.user import User as DBUser # Necesario para el tipado del owner
from app.schemas.client import ClientCreate # Necesario para la entrada de datos

class ClientService:
    """
    Servicio de lógica de negocio para la gestión de Clientes (Terceros).
    """
    def __init__(self, db: Session):
        self.db = db

    # =================================================================
    # CREACIÓN (CREATE)
    # =================================================================
    
    def create(self, client_in: ClientCreate, owner: DBUser) -> DBClient:
        """
        Crea un nuevo cliente asociado al usuario (vendedor) que lo está creando.
        """
        db_client = DBClient(
            # Mapeo de campos desde el esquema de entrada (Pydantic)
            identification_type=client_in.identification_type,
            identification_number=client_in.identification_number,
            name=client_in.name,
            email=client_in.email,
            address=client_in.address,
            phone=client_in.phone,
            fiscal_responsibility_code=client_in.fiscal_responsibility_code,
            city_code=client_in.city_code,
            
            # Asignación del propietario (Owner ID)
            owner_id=owner.id 
        )

        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    # =================================================================
    # LECTURA POR ID (READ)
    # =================================================================
    
    def get(self, client_id: int, owner: DBUser) -> Optional[DBClient]:
        """
        Obtiene un cliente por ID, verificando que pertenezca al usuario (owner).
        """
        return self.db.query(DBClient).filter(
            DBClient.id == client_id, 
            DBClient.owner_id == owner.id # Filtro de Multi-tenancy
        ).first()

    # =================================================================
    # LISTADO (LIST)
    # =================================================================
    
    def get_multi(self, owner: DBUser, skip: int = 0, limit: int = 100) -> List[DBClient]:
        """
        Obtiene una lista de clientes pertenecientes a un usuario específico.
        """
        return self.db.query(DBClient).filter(
            DBClient.owner_id == owner.id
        ).offset(skip).limit(limit).all()

    # =================================================================
    # VERIFICACIÓN DE EXISTENCIA
    # =================================================================
    
    def get_by_identification(self, identification_number: str, owner: DBUser) -> Optional[DBClient]:
        """
        Busca un cliente por número de identificación y Owner ID.
        """
        return self.db.query(DBClient).filter(
            DBClient.identification_number == identification_number,
            DBClient.owner_id == owner.id
        ).first()