import pytest
from fastapi.testclient import TestClient

from app.main import app
import uuid

client = TestClient(app)


# =========================
# Helpers
# =========================

def login(email: str, password: str) -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


# =========================
# /users/me
# =========================

def test_read_current_user_success():
    token = login("admin@facturacion.com", "PasswordSeguro123")

    response = client.get(
        "/api/v1/users/me",
        headers=auth_headers(token),
    )

    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert data["email"] == "admin@facturacion.com"


def test_read_current_user_unauthorized():
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401


# =========================
# POST /users (RBAC)
# =========================

def test_create_user_forbidden_for_normal_user():
    token = login("user@facturacion.com", "PasswordSeguro123")

    response = client.post(
        "/api/v1/users",
        headers=auth_headers(token),
        json={
            "email": "blocked@facturacion.com",
            "password": "PasswordSeguro123",
        },
    )

    assert response.status_code == 403


def test_create_user_allowed_for_admin():
    token = login("admin@facturacion.com", "PasswordSeguro123")

    email = f"user_{uuid.uuid4()}@facturacion.com"

    response = client.post(
        "/api/v1/users",
        headers=auth_headers(token),
        json={
            "email": email,
            "password": "PasswordSeguro123",
        },
    )

    assert response.status_code == 201
    assert response.json()["email"] == email
