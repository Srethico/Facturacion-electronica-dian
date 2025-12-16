# backend/app/core/dian_config.py

import os
from dotenv import load_dotenv

load_dotenv()

class DianConfig:
    # --- Datos de la Empresa (Vendedor - Obligatorios para DIAN) ---
    COMPANY_NIT = os.environ.get("DIAN_COMPANY_NIT", "800200190") # Tu NIT de ejemplo
    COMPANY_BUSINESS_NAME = os.environ.get("DIAN_BUSINESS_NAME", "Tu Empresa S.A.S.")
    COMPANY_ADDRESS = os.environ.get("DIAN_COMPANY_ADDRESS", "Calle 10 # 40-10")
    COMPANY_CITY_CODE = os.environ.get("DIAN_COMPANY_CITY_CODE", "05001") # Medellín DANE

    # --- Configuración de la Resolución de Facturación ---
    # La DIAN asigna un rango de números con prefijo específico
    RESOLUTION_NUMBER = os.environ.get("DIAN_RESOLUTION_NUMBER", "18760000001")
    RESOLUTION_PREFIX = os.environ.get("DIAN_RESOLUTION_PREFIX", "FV")
    RESOLUTION_START_DATE = "2024-01-01"
    RESOLUTION_END_DATE = "2025-12-31"
    RESOLUTION_START_NUMBER = 1
    RESOLUTION_END_NUMBER = 10000

    # --- Rutas del Certificado Digital (PFX/P12) ---
    CERTIFICATE_PATH = os.environ.get("DIAN_CERT_PATH", "/ruta/a/tu/certificado.p12")
    CERTIFICATE_PASSWORD = os.environ.get("DIAN_CERT_PASSWORD", "tu_clave_secreta")

    # --- URLs del Web Service (cambian entre Pruebas y Producción) ---
    DIAN_WSDL_URL_TEST = "URL_DE_PRUEBAS_DIAN.wsdl" # URL para enviar documentos en modo de pruebas
    DIAN_WSDL_URL_PROD = "URL_DE_PRODUCCION_DIAN.wsdl"
    
    # Modo de Operación (PRUEBAS / PRODUCCION)
    MODE = os.environ.get("DIAN_MODE", "TEST")