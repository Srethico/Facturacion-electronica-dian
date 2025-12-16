# backend/app/services/invoice_service.py

import uuid
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

# Importaciones de los modelos, esquemas y repositorio (asumiendo su existencia)
from app.db.models import Invoice, InvoiceItem
from ..schemas.invoice import InvoiceCreate, Invoice as InvoiceSchema, InvoiceItemBase
from ..repositories.invoice_repository import InvoiceRepository

class InvoiceService:
    """
    Contiene la lógica de negocio para la gestión de Facturas.
    Se encarga de los cálculos, la generación de metadatos (CUFE, consecutivo)
    y la orquestación con el repositorio.
    """
    def __init__(self, db: Session):
        self.db = db
        # Inicializa el repositorio para interactuar con la base de datos
        self.repository = InvoiceRepository(db)

    # ----------------------------------------
    # Métodos Privados de Utilidad
    # ----------------------------------------

    def _calculate_item_totals(self, item_in: InvoiceItemBase) -> dict:
        """Calcula los montos base, impuestos y totales de un ítem."""
        
        # Base Imponible (Precio Unitario * Cantidad)
        base_amount = item_in.quantity * item_in.unit_price
        
        # Monto del Impuesto (Base Imponible * Tasa de Impuesto)
        tax_amount = base_amount * item_in.tax_rate
        
        # Total por Ítem (Base Imponible + Impuesto)
        total_amount = base_amount + tax_amount
        
        return {
            "base_amount": round(base_amount, 2),
            "tax_amount": round(tax_amount, 2),
            "total_amount": round(total_amount, 2)
        }

    def _generate_sequential_number(self) -> str:
        """Simula la generación de un número de factura consecutivo (e.g. FES-0000001)."""
        # Se obtiene el conteo de facturas existentes
        last_invoice_count = self.repository.count_invoices()
        next_number = last_invoice_count + 1
        
        # Formato de consecutivo simulado
        return f"FES-{str(next_number).zfill(7)}"

    def _simulate_cufe_generation(self, invoice_data: dict) -> str:
        """Simula la generación del CUFE (Código Único de Factura Electrónica)."""
        # Cadena base simplificada para el hash simulado
        base_string = (
            f"{invoice_data['invoice_number']}|"
            f"{invoice_data['subtotal']}|"
            f"{invoice_data['total_tax']}|"
            f"{invoice_data['client_id']}"
        )
        # Generación de un hash UUID simple como simulación de CUFE (32 caracteres)
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, base_string)).replace('-', '').upper()[:32]
        
    # ----------------------------------------
    # Métodos Públicos (Lógica de Negocio)
    # ----------------------------------------

    def create_invoice(self, invoice_in: InvoiceCreate, owner_id: int) -> InvoiceSchema:
        """
        Crea una nueva factura, realiza todos los cálculos y la persiste en la DB.
        """
        # 1. Inicializar totales y procesar ítems
        subtotal = 0.0
        total_tax = 0.0
        
        invoice_items_models: List[InvoiceItem] = []
        
        for item_in in invoice_in.items:
            item_totals = self._calculate_item_totals(item_in)
            
            subtotal += item_totals["base_amount"]
            total_tax += item_totals["tax_amount"]
            
            # Crear la instancia del modelo InvoiceItem para la DB
            item_data = item_in.model_dump()
            item_data.update(item_totals)
            
            invoice_item_model = InvoiceItem(**item_data)
            invoice_items_models.append(invoice_item_model)
            
        total_invoice = subtotal + total_tax
        
        # 2. Generar metadatos
        invoice_number = self._generate_sequential_number()
        
        invoice_data_for_cufe = {
            "invoice_number": invoice_number,
            "subtotal": subtotal,
            "total_tax": total_tax,
            "client_id": invoice_in.client_id
        }
        cufe = self._simulate_cufe_generation(invoice_data_for_cufe)

        # 3. Crear el modelo Invoice principal
        invoice_model = Invoice(
            invoice_number=invoice_number,
            creation_date=datetime.now(),
            # Usar fecha de vencimiento si se provee, sino la fecha actual (o la lógica de negocio que aplique)
            due_date=invoice_in.due_date if invoice_in.due_date else datetime.now().date(), 
            owner_id=owner_id,
            client_id=invoice_in.client_id,
            subtotal=round(subtotal, 2),
            total_tax=round(total_tax, 2),
            total_invoice=round(total_invoice, 2),
            dian_status="GENERADA", # Estado inicial simulado
            cufe=cufe,
            items=invoice_items_models # SQLAlchemy vinculará los ítems
        )

        # 4. Persistir la factura
        created_invoice = self.repository.create_invoice(invoice_model)
        
        # 5. Retornar el esquema de respuesta validado desde el modelo de DB
        return InvoiceSchema.model_validate(created_invoice)

    def get_invoice(self, invoice_id: int, owner_id: int) -> Optional[InvoiceSchema]:
        """
        Busca y retorna una factura específica por su ID, asegurando pertenencia.
        """
        invoice_model = self.repository.get_invoice_by_id(invoice_id, owner_id)
        
        if invoice_model is None:
            return None
            
        return InvoiceSchema.model_validate(invoice_model)