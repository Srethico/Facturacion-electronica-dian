# SISTEMA EN PROCESO DE CONSTRUCCIÓN

# uvicorn app.main:app --reload

# alembic revision --autogenerate -m "create refresh tokens table"

# alembic upgrade head


PS C:\Facturacion-electronica-dian> 
 *  Historial restaurado 

PS C:\Facturacion-electronica-dian> tree 
Listado de rutas de carpetas
El número de serie del volumen es 28E3-08F3
C:.
├───backend
│   ├───alembic
│   │   ├───versions
│   │   │   └───__pycache__
│   │   └───__pycache__
│   ├───app
│   │   ├───api
│   │   │   ├───endpoints
│   │   │   │   └───__pycache__
│   │   │   ├───routers
│   │   │   └───v1
│   │   ├───core
│   │   │   └───__pycache__
│   │   ├───db
│   │   │   ├───models
│   │   │   │   └───__pycache__
│   │   │   └───__pycache__
│   │   ├───modules
│   │   │   ├───auth
│   │   │   ├───clients
│   │   │   ├───dian
│   │   │   ├───invoices
│   │   │   ├───products
│   │   │   └───reports
│   │   ├───repositories
│   │   │   └───__pycache__
│   │   ├───schemas
│   │   │   └───__pycache__
│   │   ├───services
│   │   │   ├───dian_ws
│   │   │   ├───signing
│   │   │   ├───xml
│   │   │   └───__pycache__
│   │   ├───utils
│   │   │   └───__pycache__
│   │   └───__pycache__
│   ├───tests
│   └───venv
│       ├───Include
│       │   └───site
│       │       └───python3.13
│       │           └───greenlet
│       ├───Lib
│       │   └───site-packages
│       │       ├───alembic
│       │       │   ├───autogenerate
│       │       │   │   └───__pycache__
│       │       │   ├───ddl
│       │       │   │   └───__pycache__
│       │       │   ├───operations
│       │       │   │   └───__pycache__
│       │       │   ├───runtime
│       │       │   │   └───__pycache__
│       │       │   ├───script
│       │       │   │   └───__pycache__
│       │       │   ├───templates
│       │       │   │   ├───async
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───generic
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───multidb
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───pyproject
│       │       │   │   │   └───__pycache__
│       │       │   │   └───pyproject_async
│       │       │   │       └───__pycache__
│       │       │   ├───testing
│       │       │   │   ├───plugin
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───suite
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───util
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───alembic-1.17.2.dist-info
│       │       │   └───licenses
│       │       ├───annotated_doc
│       │       │   └───__pycache__
│       │       ├───annotated_doc-0.0.4.dist-info
│       │       │   └───licenses
│       │       ├───annotated_types
│       │       │   └───__pycache__
│       │       ├───annotated_types-0.7.0.dist-info
│       │       │   └───licenses
│       │       ├───anyio
│       │       │   ├───abc
│       │       │   │   └───__pycache__
│       │       │   ├───streams
│       │       │   │   └───__pycache__
│       │       │   ├───_backends
│       │       │   │   └───__pycache__
│       │       │   ├───_core
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───anyio-4.12.0.dist-info
│       │       │   └───licenses
│       │       ├───bcrypt
│       │       │   └───__pycache__
│       │       ├───bcrypt-3.2.2.dist-info
│       │       ├───cffi
│       │       │   └───__pycache__
│       │       ├───cffi-2.0.0.dist-info
│       │       │   └───licenses
│       │       ├───click
│       │       │   └───__pycache__
│       │       ├───click-8.3.1.dist-info
│       │       │   └───licenses
│       │       ├───colorama
│       │       │   ├───tests
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───colorama-0.4.6.dist-info
│       │       │   └───licenses
│       │       ├───cryptography
│       │       │   ├───hazmat
│       │       │   │   ├───asn1
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───backends
│       │       │   │   │   ├───openssl
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───bindings
│       │       │   │   │   ├───openssl
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───_rust
│       │       │   │   │   │   └───openssl
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───decrepit
│       │       │   │   │   ├───ciphers
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───primitives
│       │       │   │   │   ├───asymmetric
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───ciphers
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───kdf
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───serialization
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───twofactor
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───x509
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───cryptography-46.0.3.dist-info
│       │       │   └───licenses
│       │       ├───dns
│       │       │   ├───dnssecalgs
│       │       │   │   └───__pycache__
│       │       │   ├───quic
│       │       │   │   └───__pycache__
│       │       │   ├───rdtypes
│       │       │   │   ├───ANY
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───CH
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───IN
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───dnspython-2.8.0.dist-info
│       │       │   └───licenses
│       │       ├───dotenv
│       │       │   └───__pycache__
│       │       ├───ecdsa
│       │       │   └───__pycache__
│       │       ├───ecdsa-0.19.1.dist-info
│       │       ├───email_validator
│       │       │   └───__pycache__
│       │       ├───email_validator-2.3.0.dist-info
│       │       │   └───licenses
│       │       ├───fastapi
│       │       │   ├───dependencies
│       │       │   │   └───__pycache__
│       │       │   ├───middleware
│       │       │   │   └───__pycache__
│       │       │   ├───openapi
│       │       │   │   └───__pycache__
│       │       │   ├───security
│       │       │   │   └───__pycache__
│       │       │   ├───_compat
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───fastapi-0.124.4.dist-info
│       │       │   └───licenses
│       │       ├───greenlet
│       │       │   ├───platform
│       │       │   │   └───__pycache__
│       │       │   ├───tests
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───greenlet-3.3.0.dist-info
│       │       │   └───licenses
│       │       ├───h11
│       │       │   └───__pycache__
│       │       ├───h11-0.16.0.dist-info
│       │       │   └───licenses
│       │       ├───idna
│       │       │   └───__pycache__
│       │       ├───idna-3.11.dist-info
│       │       │   └───licenses
│       │       ├───jose
│       │       │   ├───backends
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───lxml
│       │       │   ├───html
│       │       │   │   └───__pycache__
│       │       │   ├───includes
│       │       │   │   ├───extlibs
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───libexslt
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───libxml
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───libxslt
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───isoschematron
│       │       │   │   ├───resources
│       │       │   │   │   ├───rng
│       │       │   │   │   └───xsl
│       │       │   │   │       └───iso-schematron-xslt1
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───lxml-6.0.2.dist-info
│       │       │   └───licenses
│       │       ├───mako
│       │       │   ├───ext
│       │       │   │   └───__pycache__
│       │       │   ├───testing
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───mako-1.3.10.dist-info
│       │       │   └───licenses
│       │       ├───markupsafe
│       │       │   └───__pycache__
│       │       ├───markupsafe-3.0.3.dist-info
│       │       │   └───licenses
│       │       ├───multipart
│       │       │   └───__pycache__
│       │       ├───passlib
│       │       │   ├───crypto
│       │       │   │   ├───scrypt
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───_blowfish
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───ext
│       │       │   │   ├───django
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───handlers
│       │       │   │   └───__pycache__
│       │       │   ├───tests
│       │       │   │   └───__pycache__
│       │       │   ├───utils
│       │       │   │   ├───compat
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───_data
│       │       │   │   └───wordsets
│       │       │   └───__pycache__
│       │       ├───passlib-1.7.4.dist-info
│       │       ├───pip
│       │       │   ├───_internal
│       │       │   │   ├───cli
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───commands
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───distributions
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───index
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───locations
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───metadata
│       │       │   │   │   ├───importlib
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───models
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───network
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───operations
│       │       │   │   │   ├───build
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───install
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───req
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───resolution
│       │       │   │   │   ├───legacy
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───resolvelib
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───utils
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───vcs
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───_vendor
│       │       │   │   ├───cachecontrol
│       │       │   │   │   ├───caches
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───certifi
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───distlib
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───distro
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───idna
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───msgpack
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───packaging
│       │       │   │   │   ├───licenses
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───pkg_resources
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───platformdirs
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───pygments
│       │       │   │   │   ├───filters
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───formatters
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───lexers
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───styles
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───pyproject_hooks
│       │       │   │   │   ├───_in_process
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───requests
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───resolvelib
│       │       │   │   │   ├───compat
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───rich
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───tomli
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───truststore
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───urllib3
│       │       │   │   │   ├───contrib
│       │       │   │   │   │   ├───_securetransport
│       │       │   │   │   │   │   └───__pycache__
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───packages
│       │       │   │   │   │   ├───backports
│       │       │   │   │   │   │   └───__pycache__
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   ├───util
│       │       │   │   │   │   └───__pycache__
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───pip-25.0.1.dist-info
│       │       ├───psycopg2
│       │       │   └───__pycache__
│       │       ├───psycopg2_binary-2.9.11.dist-info
│       │       │   └───licenses
│       │       ├───psycopg2_binary.libs
│       │       ├───pyasn1
│       │       │   ├───codec
│       │       │   │   ├───ber
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───cer
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───der
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───native
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───compat
│       │       │   │   └───__pycache__
│       │       │   ├───type
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───pyasn1-0.6.1.dist-info
│       │       ├───pycparser
│       │       │   ├───ply
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───pycparser-2.23.dist-info
│       │       ├───pydantic
│       │       │   ├───deprecated
│       │       │   │   └───__pycache__
│       │       │   ├───experimental
│       │       │   │   └───__pycache__
│       │       │   ├───plugin
│       │       │   │   └───__pycache__
│       │       │   ├───v1
│       │       │   │   └───__pycache__
│       │       │   ├───_internal
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───pydantic-2.12.5.dist-info
│       │       │   └───licenses
│       │       ├───pydantic_core
│       │       │   └───__pycache__
│       │       ├───pydantic_core-2.41.5.dist-info
│       │       │   └───licenses
│       │       ├───pydantic_settings
│       │       │   ├───sources
│       │       │   │   ├───providers
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───pydantic_settings-2.12.0.dist-info
│       │       │   └───licenses
│       │       ├───python_dotenv-1.2.1.dist-info
│       │       │   └───licenses
│       │       ├───python_jose-3.5.0.dist-info
│       │       │   └───licenses
│       │       ├───python_multipart
│       │       │   └───__pycache__
│       │       ├───python_multipart-0.0.20.dist-info
│       │       │   └───licenses
│       │       ├───rsa
│       │       │   └───__pycache__
│       │       ├───rsa-4.9.1.dist-info
│       │       ├───six-1.17.0.dist-info
│       │       ├───sqlalchemy
│       │       │   ├───connectors
│       │       │   │   └───__pycache__
│       │       │   ├───cyextension
│       │       │   │   └───__pycache__
│       │       │   ├───dialects
│       │       │   │   ├───mssql
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───mysql
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───oracle
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───postgresql
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───sqlite
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───engine
│       │       │   │   └───__pycache__
│       │       │   ├───event
│       │       │   │   └───__pycache__
│       │       │   ├───ext
│       │       │   │   ├───asyncio
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───declarative
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───mypy
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───future
│       │       │   │   └───__pycache__
│       │       │   ├───orm
│       │       │   │   └───__pycache__
│       │       │   ├───pool
│       │       │   │   └───__pycache__
│       │       │   ├───sql
│       │       │   │   └───__pycache__
│       │       │   ├───testing
│       │       │   │   ├───fixtures
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───plugin
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───suite
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───util
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───sqlalchemy-2.0.45.dist-info
│       │       │   └───licenses
│       │       ├───starlette
│       │       │   ├───middleware
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───starlette-0.50.0.dist-info
│       │       │   └───licenses
│       │       ├───typing_extensions-4.15.0.dist-info
│       │       │   └───licenses
│       │       ├───typing_inspection
│       │       │   └───__pycache__
│       │       ├───typing_inspection-0.4.2.dist-info
│       │       │   └───licenses
│       │       ├───uvicorn
│       │       │   ├───lifespan
│       │       │   │   └───__pycache__
│       │       │   ├───loops
│       │       │   │   └───__pycache__
│       │       │   ├───middleware
│       │       │   │   └───__pycache__
│       │       │   ├───protocols
│       │       │   │   ├───http
│       │       │   │   │   └───__pycache__
│       │       │   │   ├───websockets
│       │       │   │   │   └───__pycache__
│       │       │   │   └───__pycache__
│       │       │   ├───supervisors
│       │       │   │   └───__pycache__
│       │       │   └───__pycache__
│       │       ├───uvicorn-0.38.0.dist-info
│       │       │   └───licenses
│       │       └───__pycache__
│       └───Scripts
├───docs
│   ├───api
│   ├───deployment
│   └───dian
└───frontend
    └───react-app
PS C:\Facturacion-electronica-dian> 