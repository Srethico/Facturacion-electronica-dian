# backend/app/api/endpoints/client.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

# Importaciones de tu sistema
from app.api.endpoints.auth import get_current_user # Dependencia de autenticación
from app.db.session import get_db
from app.db.models.user import User as DBUser
from app.db.models.client import Client as DBClient
from app.services.client_service import ClientService
from app.schemas.client import Client, ClientCreate

router = APIRouter()

# =================================================================
# ENDPOINT 1: CREAR NUEVO CLIENTE (Ruta Protegida)
# =================================================================

@router.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def create_client(
    client_in: ClientCreate, 
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user) # 🔑 Protección de la ruta
):
    """
    Crea un nuevo cliente asociado al usuario (vendedor) autenticado.
    Verifica que no exista otro cliente del mismo vendedor con el mismo NIT/ID.
    """
    client_service = ClientService(db)
    
    # 1. Verificar si el cliente ya existe para este vendedor (Multi-tenancy check)
    existing_client = client_service.get_by_identification(
        identification_number=client_in.identification_number,
        owner=current_user
    )
    
    if existing_client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un cliente con esta identificación registrado por usted."
        )
        
    # 2. Crear y guardar el cliente
    db_client = client_service.create(client_in=client_in, owner=current_user)
    
    return db_client


# =================================================================
# ENDPOINT 2: OBTENER LISTA DE CLIENTES (Ruta Protegida)
# =================================================================

@router.get("/", response_model=List[Client])
def read_clients(
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user), # 🔑 Protección de la ruta
    skip: int = Query(0, description="Número de registros a saltar (paginación)"),
    limit: int = Query(100, description="Límite de registros a devolver"),
):
    """
    Obtiene la lista de clientes creados por el usuario (vendedor) autenticado.
    """
    client_service = ClientService(db)
    
    clients = client_service.get_multi(owner=current_user, skip=skip, limit=limit)
    
    # Nota: El servicio ya aplica el filtro de 'owner_id'
    return clients