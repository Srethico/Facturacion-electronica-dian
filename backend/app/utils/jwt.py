# backend/app/utils/jwt.py

from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from app.core.config import SECRET_KEY, ALGORITHM

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea un token JWT.
    data: Diccionario de claims a incluir (ej. {"sub": user.email}).
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Si no se especifica, usa el tiempo por defecto de ACCESS_TOKEN_EXPIRE_SECONDS
        expire = datetime.utcnow() + timedelta(minutes=30) 
        
    to_encode.update({"exp": expire})
    
    # Crea el token firmado
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Decodifica y verifica la validez del token JWT.
    Devuelve los claims del token si es válido, o None si falla.
    """
    try:
        # Intenta decodificar el token usando la clave secreta y el algoritmo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # El claim 'sub' (subject) debería contener el identificador del usuario
        username: str = payload.get("sub")
        if username is None:
            return None # Falla si no tiene el campo 'sub'
            
        return payload
        
    except JWTError:
        # Captura errores como token expirado, firma inválida, o problemas de formato
        return None