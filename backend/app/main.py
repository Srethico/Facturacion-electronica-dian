from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.core.logging import configure_logging
from app.api.v1.api import api_router
from app.core.security_headers import security_headers


def create_application() -> FastAPI:
    configure_logging(settings.DEBUG)

    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
        docs_url=f"{settings.API_V1_PREFIX}/docs",
        redoc_url=None if settings.ENVIRONMENT == "production"
        else f"{settings.API_V1_PREFIX}/redoc",
    )

    app.middleware("http")(security_headers)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API v1
    app.include_router(
        api_router,
        prefix=settings.API_V1_PREFIX,
    )

    # ✅ HEALTH DENTRO DE API V1
    @app.get(f"{settings.API_V1_PREFIX}/health", tags=["health"])
    async def health_check():
        return {"status": "ok"}

    return app


app = create_application()
