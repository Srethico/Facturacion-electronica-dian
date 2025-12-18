# backend/app/services/invoice_service.py

from sqlalchemy.orm import Session
from app.db.models.invoice import Invoice as DBInvoice, InvoiceItem as DBInvoiceItem
from app.db.models.user import User as DBUser
from app.db.models.client import Client as DBClient
from app.schemas.invoice import InvoiceCreate, InvoiceItemCreate
from app.schemas.user import UserRole
from fastapi import HTTPException, status

class InvoiceService:
    def __init__(self, db: Session):
        self.db = db

    def _calculate_totals(self, invoice_in: InvoiceCreate):
        """Calcula el subtotal, impuestos (IVA 19%) y el total de la factura."""
        subtotal = 0.0
        
        # 1. Calcular Subtotal basado en Items
        for item in invoice_in.items:
            subtotal += item.quantity * item.unit_price
        
        # 2. Calcular IVA (asumiendo 19% para el ejemplo DIAN)
        tax_rate = 0.19 
        total_tax = round(subtotal * tax_rate, 2)
        
        # 3. Calcular Total
        total = round(subtotal + total_tax, 2)

        return subtotal, total_tax, total

    def create_invoice(self, invoice_in: InvoiceCreate, owner: DBUser) -> DBInvoice:
        """
        Crea una nueva factura y sus ítems, asociándola al cliente y al vendedor.
        """
        
        # 1. Verificar si el cliente existe y pertenece al dueño (owner)
        client = self.db.query(DBClient).filter(
            DBClient.id == invoice_in.client_id,
            DBClient.owner_id == owner.id
        ).first()

        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no encontrado o no pertenece a este usuario."
            )
            
        # 2. Calcular Totales
        subtotal, total_tax, total = self._calculate_totals(invoice_in)
        
        # 3. Crear la Factura
        db_invoice = DBInvoice(
            client_id=invoice_in.client_id,
            owner_id=owner.id,
            invoice_date=invoice_in.invoice_date,
            subtotal=subtotal,
            total_tax=total_tax,
            total=total,
            # Simulamos el consecutivo y el CUFE
            consecutive_number="FAC-{}".format(len(self.get_multi(owner)) + 1),
            cufe="CUFE-SIMULADO-{}".format(hash(total)),
        )

        self.db.add(db_invoice)
        self.db.flush() # Importante para obtener el ID de la factura (db_invoice.id)

        # 4. Crear los Items de la Factura
        for item_in in invoice_in.items:
            db_item = DBInvoiceItem(
                invoice_id=db_invoice.id,
                product_code=item_in.product_code,
                description=item_in.description,
                quantity=item_in.quantity,
                unit_price=item_in.unit_price,
                tax_rate=0.19, # Tasa fija
            )
            self.db.add(db_item)
            
        self.db.commit()
        self.db.refresh(db_invoice)
        return db_invoice

    def get_multi(self, owner: DBUser, skip: int = 0, limit: int = 100) -> list[DBInvoice]:
        """Obtiene todas las facturas de un dueño específico."""
        return self.db.query(DBInvoice).filter(DBInvoice.owner_id == owner.id).offset(skip).limit(limit).all()

    def get_by_id(self, invoice_id: int, owner: DBUser) -> DBInvoice:
        """Obtiene una factura por ID, asegurando que pertenece al dueño."""
        invoice = self.db.query(DBInvoice).filter(
            DBInvoice.id == invoice_id,
            DBInvoice.owner_id == owner.id
        ).first()
        
        if not invoice:
             raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Factura no encontrada."
            )
        return invoice