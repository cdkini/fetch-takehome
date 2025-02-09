import uuid
from fastapi.testclient import TestClient


def test_receipt_get_errors(client: TestClient):
    receipt_id = uuid.uuid4()  # Does not exist
    response = client.get(f"/receipts/{receipt_id}/points")

    assert response.status_code == 400


def test_receipt_post_errors(client: TestClient):
    response = client.post("/receipts/process", json={})

    assert response.status_code == 422


def test_round_trip(client: TestClient):
    # Arrange
    payload = {
        "retailer": "myRetailer",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "total": 10,
        "items": [
            {"shortDescription": "myItem", "price": 5},
            {"shortDescription": "myItem2", "price": 5},
        ],
    }

    # Act
    response_a = client.post("/receipts/process", json=payload)
    receipt_id = response_a.json()["id"]
    response_b = client.get(f"/receipts/{receipt_id}/points")

    assert response_a.status_code == 200
    assert response_b.status_code == 200
    assert response_b.json() == {"points": 98}
