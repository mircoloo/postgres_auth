def test_create_user(client):
    response = client.post(
        "/v1/user",
        json={
            "email": "test@example.com",
            "password": "secret"
        }
    )
    assert response.status_code == 201

    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_get_user_not_found(client):
    response = client.get("/v1/users/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
