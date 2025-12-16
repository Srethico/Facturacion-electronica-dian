# backend/app/api/endpoints/invoice.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importaciones de tu sistema (asumiendo que estas rutas existen)
from app.api.endpoints.auth import get_current_user # Dependencia de autenticación
from app.db.session import get_db
from app.db.models.user import User as DBUser
from app.services.invoice_service import InvoiceService
from app.services.client_service import ClientService
from app.schemas.invoice import Invoice, InvoiceCreate, Invoice as InvoiceResponseSchema

router = APIRouter()

# =================================================================
# ENDPOINT 1: CREAR Y GENERAR FACTURA (Ruta Protegida)
# =================================================================

@router.post("/", response_model=InvoiceResponseSchema, status_code=status.HTTP_201_CREATED)
def create_invoice(
    invoice_in: InvoiceCreate, 
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user) # 🔑 Protección de la ruta
):
    """
    Crea una nueva Factura Electrónica. 
    Realiza cálculos (IVA, totales) y genera el número consecutivo y el CUFE simulado.
    """
    invoice_service = InvoiceService(db)
    client_service = ClientService(db)
    
    # 1. Validación: Verificar si el cliente existe y pertenece al usuario
    client = client_service.get(client_id=invoice_in.client_id, owner=current_user)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado o no pertenece al usuario actual."
        )
        
    # 2. Creación y cálculo de la factura
    try:
        new_invoice = invoice_service.create_invoice(
            invoice_in=invoice_in, 
            owner_id=current_user.id
        )
        return new_invoice
    except Exception as e:
        # Esto captura errores de base de datos o lógica interna (ej. si falta un producto)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al procesar la factura: {str(e)}"
        )


# =================================================================
# ENDPOINT 2: OBTENER FACTURA POR ID (Ruta Protegida)
# =================================================================

@router.get("/{invoice_id}", response_model=InvoiceResponseSchema)
def read_invoice(
    invoice_id: int, 
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user) # 🔑 Protección de la ruta
):
    """
    Obtiene una factura específica por ID, asegurando que pertenezca al usuario.
    """
    invoice_service = InvoiceService(db)
    
    invoice = invoice_service.get_invoice(invoice_id=invoice_id, owner_id=current_user.id)
    
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada o no pertenece al usuario actual."
        )
        
    return invoice