from fastapi import Request
from fastapi.responses import Response


async def security_headers(request: Request, call_next):
    response: Response = await call_next(request)

    path = request.url.path

    # ======================================================
    # CSP PERMISIVA SOLO PARA SWAGGER (DESARROLLO)
    # ======================================================
    if path.startswith("/api/v1/docs") or path.startswith("/api/v1/openapi"):
        response.headers["Content-Security-Policy"] = (
            "default-src 'self' https://cdn.jsdelivr.net https://unpkg.com; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://unpkg.com; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://unpkg.com; "
            "img-src 'self' data: https://cdn.jsdelivr.net https://unpkg.com; "
            "font-src 'self' https://cdn.jsdelivr.net https://unpkg.com; "
            "connect-src 'self';"
        )
        return response

    # ======================================================
    # CSP ESTRICTA PARA TODA LA APLICACIÓN
    # ======================================================
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self'; "
        "connect-src 'self';"
    )

    # Headers de seguridad adicionales
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    return response
