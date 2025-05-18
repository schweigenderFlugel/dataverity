from fastapi.testclient import TestClient
from fastapi import status

def test_creat_customer(client: TestClient):
    reponse = client.post(
        '/auth/register', 
        json={
            'message': 'User successfully registered' 
        }
    )
    assert reponse.status_code == status.HTTP_201_CREATED