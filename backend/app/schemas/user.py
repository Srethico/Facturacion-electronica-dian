from pydantic import BaseModel, EmailStr, Field


# =========================
# Base
# =========================

class UserBase(BaseModel):
    email: EmailStr


# =========================
# Create
# =========================

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


# =========================
# Read (response)
# =========================

class UserRead(UserBase):
    id: int
    role: str
    is_active: bool

    class Config:
        from_attributes = True
