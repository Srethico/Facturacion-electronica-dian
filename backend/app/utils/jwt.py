# backend/app/utils/jwt.py

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_SECONDS

# --- CREAR TOKEN ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea un nuevo Access Token JWT.
    """
    # Copiamos los datos que irán en el token
    to_encode = data.copy()
    
    # Definimos la expiración del token (exp)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Usa el valor por defecto de la configuración si no se especifica
        expire = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
        
    to_encode.update({"exp": expire})
    
    # Codificamos el token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# --- VERIFICAR TOKEN ---
def verify_access_token(token: str) -> Optional[dict]:
    """
    Decodifica y verifica la validez del Access Token.
    """
    try:
        # Decodificamos el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extraemos el dato principal (email o sub)
        return payload
        
    except JWTError:
        # Si falla (expiró, firma incorrecta, etc.)
        return None