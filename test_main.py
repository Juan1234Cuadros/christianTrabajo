from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_status_code():
    """
    Simula una petición GET a la ruta principal (/) directamente
    sobre la app (antes del despliegue) y valida que el código
    de estado sea estrictamente 200 OK.
    """
    response = client.get("/")
    assert response.status_code == 200
