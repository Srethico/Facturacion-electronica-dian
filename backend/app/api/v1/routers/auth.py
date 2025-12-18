from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.auth import LoginRequest
from app.schemas.token import Token
from app.repositories.user_repository import UserRepository
from app.db.models.user import User
from app.core.security import (
    create_access_token,
    create_refresh_token,
    get_refresh_token,
    revoke_refresh_token,
    verify_password,
)
from app.api.deps import get_current_user


router = APIRouter(prefix="/auth", tags=["auth"])
user_repo = UserRepository()


# =========================
# Login (extendido con refresh token)
# =========================

@router.post("/login", response_model=Token)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):
    user: User | None = user_repo.get_by_email(db, data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(subject=user.email)
    refresh_token = create_refresh_token(db=db, user=user)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


# =========================
# Refresh token (rotation)
# =========================

@router.post("/refresh", response_model=Token)
def refresh(
    refresh_token: str,
    db: Session = Depends(get_db),
):
    token = get_refresh_token(db=db, raw_token=refresh_token)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    user = token.user

    # 🔁 ROTATION: revocamos el token viejo
    revoke_refresh_token(db=db, token=token)

    # Emitimos nuevos tokens
    access_token = create_access_token(subject=user.email)
    new_refresh_token = create_refresh_token(db=db, user=user)

    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }


# =========================
# Logout (revoke refresh token)
# =========================

@router.post("/logout")
def logout(
    refresh_token: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    token = get_refresh_token(db=db, raw_token=refresh_token)
    if not token:
        # Logout idempotente (no filtramos info)
        return {"message": "Logged out"}

    if token.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid refresh token",
        )

    revoke_refresh_token(db=db, token=token)
    return {"message": "Logged out"}
