def test_login_success(client):
    payload = {
        "email": "admin@facturacion.com",
        "password": "PasswordSeguro123",
    }

    response = client.post("/api/v1/auth/login", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    payload = {
        "email": "admin@facturacion.com",
        "password": "PasswordIncorrecto",
    }

    response = client.post("/api/v1/auth/login", json=payload)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_login_user_not_found(client):
    payload = {
        "email": "noexiste@facturacion.com",
        "password": "PasswordSeguro123",
    }

    response = client.post("/api/v1/auth/login", json=payload)

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
