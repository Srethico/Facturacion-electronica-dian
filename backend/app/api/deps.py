from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import decode_access_token
from app.db.deps import get_db
from app.repositories.user_repository import UserRepository
from app.db.models.user import User
from app.core.permissions import Permission
from app.core.role_permissions import ROLE_PERMISSIONS

security = HTTPBearer()


# =========================
# Auth: usuario actual
# =========================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials

    email = decode_access_token(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = UserRepository().get_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return user


# =========================
# Auth: usuario activo
# =========================

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Dependencia explícita para endpoints que
    requieren usuario activo (regla de negocio).
    """
    return current_user


# =========================
# Authorization: roles
# =========================

def require_role(required_role: str):
    def role_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return current_user

    return role_dependency


# =========================
# Authorization: admin
# =========================

def require_admin_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Admin real:
    - role == admin OR
    - is_superuser == True
    """
    if current_user.role != "admin" and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    return current_user

def require_permission(permission: Permission):
    def permission_dependency(
        current_user: User = Depends(get_current_user),
    ) -> User:
        role = current_user.role

        allowed_permissions = ROLE_PERMISSIONS.get(role, set())

        if permission not in allowed_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )

        return current_user

    return permission_dependency
