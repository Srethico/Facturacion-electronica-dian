# backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base # Importamos tu base declarativa

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    
    # --- Campos Fiscales DIAN ---
    
    # NIT o Cédula (Campo obligatorio para facturación)
    identification_number = Column(String, index=True, unique=True, nullable=False) 
    
    # 1: Cédula de Ciudadanía, 31: NIT, 41: Registro civil, etc. (Usar códigos DIAN)
    type_identification = Column(String, nullable=False) 
    
    # Razón social (para empresas) o Nombre completo (para persona natural)
    business_name = Column(String, nullable=False) 
    
    # Código de Responsabilidad Fiscal (e.g., 'R-99-PN' - No aplica, 'O-13' - Gran Contribuyente)
    fiscal_responsibility_code = Column(String, default="R-99-PN")
    
    # Dirección (Requerido para la DIAN)
    address = Column(String, nullable=False)
    
    # Código del municipio (e.g., 05001 para Medellín, 11001 para Bogotá).
    # Se usa el código DANE.
    city_code = Column(String, nullable=False) 
    
    # Correo Electrónico (Donde se envía la factura)
    email = Column(String, index=True)
    
    # --- Campos Internos/Opcionales ---
    
    phone = Column(String)
    is_active = Column(Boolean, default=True)

    # Representación de cadena para depuración
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.business_name}')>"