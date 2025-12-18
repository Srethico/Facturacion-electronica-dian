# backend/app/api/endpoints/invoice.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

# Importaciones de tu sistema
from app.api.endpoints.auth import get_current_user
from app.db.session import get_db
from app.db.models.user import User as DBUser
from app.services.invoice_service import InvoiceService
from app.schemas.invoice import Invoice, InvoiceCreate, InvoiceItem
from app.schemas.user import UserRole # Para validación de roles, si es necesario

router = APIRouter()

# =================================================================
# ENDPOINT 1: CREAR NUEVA FACTURA (Ruta Protegida)
# =================================================================

@router.post("/", response_model=Invoice, status_code=status.HTTP_201_CREATED)
def create_invoice(
    invoice_in: InvoiceCreate, 
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user) # 🔑 Protección de la ruta
):
    """Crea una nueva Factura Electrónica y sus ítems, realizando los cálculos (IVA, totales) y la simulación del CUFE."""
    
    # OPCIONAL: Restringir a ciertos roles si es necesario (ej: solo ADMIN/VENDEDOR)
    # if current_user.role not in [UserRole.ADMIN, UserRole.VENDEDOR]:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permisos insuficientes.")
        
    invoice_service = InvoiceService(db)
    
    try:
        db_invoice = invoice_service.create_invoice(invoice_in=invoice_in, owner=current_user)
        return db_invoice
    except HTTPException as e:
        raise e # Relanzar excepciones 404/400 del servicio
    except Exception as e:
        # Manejo de errores genéricos de base de datos
        print(f"Error al crear factura: {e}") 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear factura.")


# =================================================================
# ENDPOINT 2: OBTENER FACTURA POR ID (Ruta Protegida)
# =================================================================

@router.get("/{invoice_id}", response_model=Invoice)
def read_invoice(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user),
):
    """Obtiene una factura específica por ID (solo si pertenece al usuario)."""
    invoice_service = InvoiceService(db)
    return invoice_service.get_by_id(invoice_id, owner=current_user)


# =================================================================
# ENDPOINT 3: OBTENER LISTA DE FACTURAS (Ruta Protegida)
# =================================================================

@router.get("/", response_model=List[Invoice])
def read_invoices(
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_user),
    skip: int = Query(0),
    limit: int = Query(100),
):
    """Obtiene la lista de facturas creadas por el usuario autenticado."""
    invoice_service = InvoiceService(db)
    return invoice_service.get_multi(owner=current_user, skip=skip, limit=limit)