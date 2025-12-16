# backend/app/utils/xml_ubl_generator.py

from lxml import etree
from app.db.models.invoice import Invoice as DBInvoice
from app.core.dian_config import DianConfig

# Definición de namespaces UBL (estándar requerido por DIAN)
NSMAP = {
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
    'sts': 'dian:gov:co:facturaelectronica:Structures-2.1',
    'ds': 'http://www.w3.org/2000/09/xmldsig#',
    'qdt': 'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2',
    'udt': 'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'fe': 'http://www.dian.gov.co/fenl/cfd/Schema/v1', # Namespace para DIAN
}

def generate_ubl_xml(db_invoice: DBInvoice) -> bytes:
    """
    Genera el XML de la factura electrónica UBL 2.1 a partir del objeto DBInvoice.
    """
    # Raíz del documento: <fe:Invoice>
    Invoice = etree.Element(
        f"{{{NSMAP['fe']}}}Invoice",
        nsmap=NSMAP,
        attrib={
            f"{{{NSMAP['xsi']}}}schemaLocation": "http://www.dian.gov.co/fenl/cfd/Schema/v1 DIAN_UBL_Invoice.xsd"
        }
    )
    
    # 1. Extensiones (Requeridas para la firma digital y CUFE)
    UBLExtensions = etree.SubElement(Invoice, f"{{{NSMAP['ext']}}}UBLExtensions")
    # ... Aquí iría la estructura compleja para la firma y el CUFE ...
    
    # 2. Información Básica de la Factura
    
    # Tipo de factura (380: Factura de Venta)
    etree.SubElement(Invoice, f"{{{NSMAP['cbc']}}}CustomizationID").text = "10" 
    
    # Consecutivo (e.g., FV001)
    etree.SubElement(Invoice, f"{{{NSMAP['cbc']}}}ID").text = f"{db_invoice.prefix}{db_invoice.consecutive}" 
    
    # Fecha y Hora de Emisión
    etree.SubElement(Invoice, f"{{{NSMAP['cbc']}}}IssueDate").text = db_invoice.issue_date.strftime("%Y-%m-%d")
    etree.SubElement(Invoice, f"{{{NSMAP['cbc']}}}IssueTime").text = db_invoice.issue_date.strftime("%H:%M:%S")

    # Tipo de Moneda (COP)
    etree.SubElement(Invoice, f"{{{NSMAP['cbc']}}}DocumentCurrencyCode").text = "COP" 
    
    # 3. SellerParty (Tu Empresa) - Se usaría la DianConfig
    # ... (Estructura compleja del Vendedor) ...
    
    # 4. BuyerParty (El Cliente) - Usaría db_invoice.client
    # ... (Estructura compleja del Cliente) ...

    # 5. TaxTotals
    # ... (Resumen de Impuestos) ...
    
    # 6. LegalMonetaryTotal (Totales)
    # ... (Total a pagar) ...
    
    # 7. InvoiceLines (Los ítems de la factura)
    # ... (Bucle para agregar los db_invoice.items) ...
    
    # Finalizar y dar formato
    xml_str = etree.tostring(Invoice, pretty_print=True, encoding='utf-8', xml_declaration=True)
    return xml_str

# Ejemplo de una función que podrías usar para enviar la factura
def send_to_dian(xml_document: bytes):
    """Aquí se implementaría la llamada al Web Service SOAP de la DIAN."""
    # Requiere librerías SOAP como 'zeep' o 'suds'
    pass