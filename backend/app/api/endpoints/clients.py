# backend/app/api/endpoints/clients.py (Código Refactorizado)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importar la función de dependencia de la DB
from app.db.session import get_db

# Importar los esquemas Pydantic y el nuevo servicio
from app.schemas.client import Client, ClientCreate
from app.services.client_service import ClientService

router = APIRouter()

# --- Endpoint para CREAR un Cliente ---
@router.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def create_new_client(client_in: ClientCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo cliente usando la capa de servicio.
    """
    # 1. Crear la instancia del servicio de cliente
    client_service = ClientService(db)

    # 2. Lógica de negocio/validación: Verificar si ya existe
    existing_client = client_service.get_by_identification(client_in.identification_number)
    
    if existing_client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un cliente con este número de identificación.",
        )
    
    # 3. Llamar al método del servicio para crear en la DB
    db_client = client_service.create(client_in)
    
    return db_client


# --- Endpoint para OBTENER todos los Clientes ---
@router.get("/", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista de clientes usando la capa de servicio.
    """
    client_service = ClientService(db)
    clients = client_service.get_all(skip=skip, limit=limit)
    return clients