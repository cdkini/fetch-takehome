import uuid
from fastapi.testclient import TestClient


def test_receipt_get_errors(client: TestClient):
    receipt_id = uuid.uuid4()  # Does not exist
    response = client.get(f"/receipts/{receipt_id}/points")

    assert response.status_code == 400


def test_receipt_post_errors(client: TestClient):
    response = client.post("/receipts/process", json={})

    assert response.status_code == 422
