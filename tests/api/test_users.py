import pytest 
from src.config.settings import BASE_URL_API
from faker import Faker 


fake = Faker()

# CREATE USER
def test_create_user(api_client):
    payload = {
        "name": fake.name(),
        "job": "QA Engineer"
    }

    response = api_client.post(f"/users", json = payload)

    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]
    assert "id" in response.json()

# GET USER
def test_get_user(api_client):
    user_id = 2
    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    # assert response.json()["data"]["id"] == user_id


# Update user
def test_update_user(api_client):
    user_id = 2
    payload = {
        "name": fake.first_name(),
        "job": " Senior QA Engineer"
    }

    response = api_client.put(f"/users/{user_id}",json = payload)
    assert response.status_code == 200
    assert response.json()["job"] == payload["job"]

# 4️⃣ DELETE USER
def test_delete_user(api_client):
    user_id = 2

    response = api_client.delete(f"/users/{user_id}")

    assert response.status_code == 200  # reqres returns 204 for delete


# 5️⃣ LIST USERS
def test_list_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0