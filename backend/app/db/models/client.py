# backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Asumo que 'Base' es la clase declarativa de SQLAlchemy importada desde un archivo base
# (ej. app/db/base.py) y que 'User' está disponible.
from app.db.base import Base # Necesario para la herencia
from app.db.models.user import User # Necesario para la relación ForeignKey

class Client(Base):
    """
    Modelo de Base de Datos para los Clientes (Terceros)
    """
    __tablename__ = "clients"

    # Clave Primaria
    id = Column(Integer, primary_key=True, index=True)

    # Identificación del Cliente
    identification_type = Column(String(5), nullable=False) # ej. NIT, CC
    identification_number = Column(String(20), index=True, nullable=False)
    
    # Datos de Contacto y Nombre
    name = Column(String(150), index=True, nullable=False)
    email = Column(String(100), index=True, nullable=True)
    address = Column(String(200), nullable=True)
    phone = Column(String(20), nullable=True)

    # Campos de Facturación / DIAN
    fiscal_responsibility_code = Column(String(10), default="R-99-PN", nullable=False)
    city_code = Column(String(10), nullable=True) # Código DANE

    # Relación de Pertenencia (Multi-tenancy)
    # owner_id hace referencia al usuario (vendedor) que creó este cliente
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    
    # -----------------------------------------------------
    # Relaciones de SQLAlchemy
    # -----------------------------------------------------
    
    # Relación con el usuario propietario (el que emite la factura)
    # back_populates enlaza con el 'clients' definido en el modelo User
    owner = relationship("User", back_populates="clients")
    
    # Relación con las facturas emitidas a este cliente
    # lazy='dynamic' permite cargar las facturas solo cuando son solicitadas
    invoices = relationship("Invoice", back_populates="client", lazy="dynamic")
    invoices = relationship("Invoice", back_populates="client")
    
    # Método de representación para depuración
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', nit='{self.identification_number}')>"