# backend/app/utils/dian_security.py

import hashlib
import uuid
from typing import TYPE_CHECKING
from decimal import Decimal

# Importaciones condicionales para evitar errores de referencia circular
if TYPE_CHECKING:
    from app.db.models.invoice import Invoice as DBInvoice

# Esta es una CLAVE TÉCNICA que la DIAN te asigna al autorizar tu software de facturación.
# Es esencial para el CUFE.
SOFTWARE_TECHNICAL_KEY = "0D394C-3C1A8A-454E5F-B7C95B-F648D4" 
# La reemplazaremos en la configuración real, pero la usaremos como constante aquí.


def generate_cufe(invoice: 'DBInvoice', technical_key: str = SOFTWARE_TECHNICAL_KEY) -> str:
    """
    Calcula el Código Único de Factura Electrónica (CUFE) usando la fórmula DIAN.
    
    La fórmula combina varios campos de la factura en una cadena y calcula un hash SHA384.
    """
    
    # NOTA: En una implementación completa, se deben incluir más de 20 campos 
    # (NIT del emisor, fecha, totales, tipo de moneda, etc.)
    
    # 1. Preparar los datos clave (Ejemplo simplificado de la fórmula DIAN)
    
    # Formateo de totales a 2 decimales y sin separador de miles
    total_due_str = invoice.total_due.quantize(Decimal('.01')).to_eng_string()
    total_taxes_str = invoice.total_taxes.quantize(Decimal('.01')).to_eng_string()
    
    # 2. Concatenar los campos requeridos por la fórmula DIAN
    data_string = (
        f"{DianConfig.COMPANY_NIT}"              # NIT del emisor
        f"{invoice.prefix}{invoice.consecutive}" # Prefijo y consecutivo
        f"{invoice.issue_date.strftime('%Y%m%d')}"# Fecha de emisión (YYYYMMDD)
        f"{invoice.issue_date.strftime('%H%M%S')}"# Hora de emisión (HHMMSS)
        f"{total_due_str}"                       # Valor total de la factura
        f"{total_taxes_str}"                      # Valor total de impuestos
        f"{'COP'}"                               # Código de moneda
        f"{technical_key}"                       # Clave técnica del software (CRUCIAL)
        f"01"                                    # Código de ambiente (Pruebas/Producción)
    )
    
    # 3. Aplicar el algoritmo de hash SHA384
    cufe_hash = hashlib.sha384(data_string.encode('utf-8')).hexdigest()
    
    # 4. Devolver el hash en mayúsculas (formato CUFE)
    return cufe_hash.upper()


# ----------------------------------------------------------------------
# Lógica de Firma Digital (XML-DSig)
# ----------------------------------------------------------------------

# La firma XML-DSig requiere librerías especializadas (como xmlsec o pyOpenSSL + lxml) 
# y es la parte más compleja de la integración. Por ahora, definiremos la función placeholder.

def sign_xml_document(xml_data: bytes, cert_path: str, cert_password: str) -> bytes:
    """
    Firma el documento XML UBL 2.1 usando el certificado P12/PFX de la empresa
    para crear la estructura XML-DSig requerida por la DIAN.
    """
    # En una implementación real, aquí se usaría la librería xmlsec.
    # Esta función transforma el XML antes de enviarlo.
    print(f"DEBUG: Firmando el documento XML con certificado de {cert_path}")
    
    # Retorna el XML firmado. Por ahora, solo retorna el original para simulación.
    return xml_data