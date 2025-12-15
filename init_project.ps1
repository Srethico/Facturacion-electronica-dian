$ProjectName = "facturacion-electronica-dian"

Write-Host "Creando estructura del proyecto $ProjectName..."

# Root
New-Item -ItemType Directory -Force -Path $ProjectName
Set-Location $ProjectName

# Backend
New-Item -ItemType Directory -Force -Path backend/app
New-Item -ItemType Directory -Force -Path backend/alembic
New-Item -ItemType Directory -Force -Path backend/tests

New-Item -ItemType Directory -Force -Path backend/app/core
New-Item -ItemType Directory -Force -Path backend/app/db/models
New-Item -ItemType Directory -Force -Path backend/app/utils

New-Item -ItemType Directory -Force -Path backend/app/modules/auth
New-Item -ItemType Directory -Force -Path backend/app/modules/clients
New-Item -ItemType Directory -Force -Path backend/app/modules/products
New-Item -ItemType Directory -Force -Path backend/app/modules/invoices
New-Item -ItemType Directory -Force -Path backend/app/modules/dian
New-Item -ItemType Directory -Force -Path backend/app/modules/reports

New-Item -ItemType Directory -Force -Path backend/app/services/xml
New-Item -ItemType Directory -Force -Path backend/app/services/signing
New-Item -ItemType Directory -Force -Path backend/app/services/dian_ws

New-Item -ItemType File -Force -Path backend/app/main.py
New-Item -ItemType File -Force -Path backend/requirements.txt

# Frontend
New-Item -ItemType Directory -Force -Path frontend/react-app

# Docs
New-Item -ItemType Directory -Force -Path docs/api
New-Item -ItemType Directory -Force -Path docs/dian
New-Item -ItemType Directory -Force -Path docs/deployment

# Root files
New-Item -ItemType File -Force -Path .env.example
New-Item -ItemType File -Force -Path .gitignore
New-Item -ItemType File -Force -Path README.md

Write-Host "Estructura creada correctamente."
Write-Host "Abre la carpeta en VS Code y continuamos."
