from datetime import datetime, timedelta, timezone
from typing import Any
import secrets
import hashlib

from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.settings import settings
from app.db.models.refresh_token import RefreshToken
from app.db.models.user import User


# =========================
# Password hashing (bcrypt)
# =========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Genera un hash seguro para un password en texto plano.
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifica un password contra su hash.
    """
    return pwd_context.verify(password, hashed_password)


# =========================
# JWT configuration
# =========================

ALGORITHM = "HS256"


def create_access_token(subject: str | int) -> str:
    """
    Crea un JWT firmado con expiración.
    El subject suele ser el email o el user_id.
    """
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload: dict[str, Any] = {
        "sub": str(subject),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> str | None:
    """
    Decodifica un JWT y devuelve el subject si es válido.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        return payload.get("sub")
    except JWTError:
        return None


# =========================
# Refresh Tokens (DB controlled)
# =========================

REFRESH_TOKEN_EXPIRE_DAYS = 7


def generate_refresh_token() -> str:
    """
    Genera un refresh token criptográficamente seguro.
    """
    return secrets.token_urlsafe(64)


def hash_refresh_token(token: str) -> str:
    """
    Hashea el refresh token con SHA-256.
    Nunca se guarda el token plano.
    """
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_refresh_token(
    db: Session,
    user: User,
) -> str:
    """
    Crea y persiste un refresh token para el usuario.
    Retorna el token PLANO (solo se devuelve una vez).
    """
    raw_token = generate_refresh_token()
    token_hash = hash_refresh_token(raw_token)

    expires_at = datetime.now(timezone.utc) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )

    refresh_token = RefreshToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=expires_at,
    )

    db.add(refresh_token)
    db.commit()
    db.refresh(refresh_token)

    return raw_token


def get_refresh_token(
    db: Session,
    raw_token: str,
) -> RefreshToken | None:
    """
    Obtiene un refresh token válido:
    - existe
    - no revocado
    - no expirado
    """
    token_hash = hash_refresh_token(raw_token)

    return (
        db.query(RefreshToken)
        .filter(
            RefreshToken.token_hash == token_hash,
            RefreshToken.revoked_at.is_(None),
            RefreshToken.expires_at > datetime.now(timezone.utc),
        )
        .first()
    )


def revoke_refresh_token(
    db: Session,
    token: RefreshToken,
) -> None:
    """
    Revoca un refresh token (logout o rotación).
    """
    token.revoked_at = datetime.now(timezone.utc)
    db.add(token)
    db.commit()
