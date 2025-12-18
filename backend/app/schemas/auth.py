from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    """
    Request para autenticación.
    """
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
    )


class LoginResponse(BaseModel):
    """
    Response explícito para login.
    Compatible con Swagger y clientes externos.
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
