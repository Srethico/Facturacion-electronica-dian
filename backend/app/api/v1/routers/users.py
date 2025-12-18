from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.api.deps import get_current_user, require_role
from app.db.models.user import User


router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()


# =========================
# Create user (ADMIN ONLY)
# =========================

@router.post(
    "",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin")),
):
    """
    Crear usuarios es una operación administrativa.
    """
    try:
        return user_service.create_user(db, user_in)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )


# =========================
# Current user
# =========================

@router.get(
    "/me",
    response_model=UserRead,
)
def read_current_user(
    current_user: User = Depends(get_current_user),
):
    """
    Retorna el usuario autenticado.
    """
    return current_user


# =========================
# Admin-only test endpoint
# =========================

@router.get("/admin-only")
def admin_only(
    current_user: User = Depends(require_role("admin")),
):
    """
    Endpoint de prueba para verificar permisos de admin.
    """
    return {
        "message": "Access granted",
        "email": current_user.email,
        "role": current_user.role,
    }
