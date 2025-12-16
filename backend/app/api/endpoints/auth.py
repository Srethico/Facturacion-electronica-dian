# backend/app/api/endpoints/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
# Importamos User, UserRegister (para registro) y UserCreate (para uso interno/admin)
from app.schemas.user import User, UserRegister, UserCreate 

from app.db.session import get_db
from app.db.models.user import User as DBUser
from app.schemas.token import Token, TokenData # Asumo que este esquema existe
from app.services.user_service import UserService # Asumo que este servicio existe
from app.utils.security import verify_password
from app.utils.jwt import create_access_token, verify_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_SECONDS
from datetime import timedelta

router = APIRouter()

# Define el esquema de seguridad: dónde espera la API encontrar el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


# =================================================================
# ENDPOINT 1: LOGIN (Generación del Token)
# =================================================================

@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    """
    Genera un token de acceso para el usuario que se loguea.
    FastAPI se encarga de recibir 'username' (email) y 'password' como datos de formulario.
    """
    user_service = UserService(db)
    
    # 1. Buscar usuario por email
    user = user_service.get_by_email(form_data.username)
    
    # 2. Verificar existencia y contraseña
    if not user or not verify_password(form_data.password, user.hashed_password):
        # Usamos 401 Unauthorized para fallo de credenciales
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Crear el token
    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role.name}, # 'sub' es estándar para el identificador
        expires_delta=access_token_expires
    )
    
    # 4. Devolver el token
    return {"access_token": access_token, "token_type": "bearer"}


# =================================================================
# ENDPOINT 2: CREACIÓN de Usuario (REGISTRO PÚBLICO)
# =================================================================

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_new_user(user_in: UserRegister, db: Session = Depends(get_db)): # 🔑 CORREGIDO: Ahora usa UserRegister
    """
    Crea un nuevo usuario en el sistema con el esquema de registro mínimo.
    """
    user_service = UserService(db)
    
    # 1. Verificar si el email ya está registrado
    if user_service.get_by_email(user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado."
        )
        
    # 2. Crear y guardar el usuario
    # El servicio (UserService.create) debe encargarse de asignar el rol ('VENDEDOR') 
    # y el estado ('is_active=True') por defecto, ya que no vienen en user_in.
    db_user = user_service.create(user_in) 
    
    return db_user


# =================================================================
# DEPENDENCIA: Obtener Usuario Actual (para proteger otras rutas)
# =================================================================

def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
) -> DBUser:
    """
    Dependencia que extrae y verifica el token JWT, y devuelve el objeto User de la BD.
    """
    # 1. Decodificar el token
    payload = verify_access_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no válido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Buscar usuario por el identificador (sub/email)
    user_email = payload.get("sub")
    if user_email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token con formato incorrecto",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user_service = UserService(db)
    user = user_service.get_by_email(user_email)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
        
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario está inactivo",
        )
        
    return user
    
# Ruta de prueba (para verificar que la autenticación funciona)
@router.get("/me", response_model=User)
def read_users_me(current_user: DBUser = Depends(get_current_user)):
    """
    Obtiene la información del usuario actualmente autenticado. (Ruta Protegida)
    """
    return current_user