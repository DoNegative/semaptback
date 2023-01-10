from fastapi.testclient import TestClient
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .main import app

client = TestClient(app)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

def test_create_user():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "FIO": "test",
            "email": "test",
            "number_phone": "test",
            "position_id": 2
            },
    )
    assert response.status_code == 200
    assert response.json() == {
         "FIO": "test",
            "email": "test",
            "number_phone": "test",
            "position_id": 2
    }