"""
This script is used to test the rate limiting functionality of the container (currently none).
"""

import requests


BASE_CONTAINER_URL = "http://0.0.0.0:8000"


if __name__ == "__main__":
    while True:
        receipt_data = {
            "retailer": "myRetailer",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "total": 10,
            "items": [
                {"shortDescription": "myItem", "price": 5},
                {"shortDescription": "myItem2", "price": 5},
            ],
        }

        response = requests.post(
            f"{BASE_CONTAINER_URL}/receipts/process", json=receipt_data
        )
        response_data = response.json()

        print(response_data)

        id_ = response_data["id"]

        response = requests.get(f"{BASE_CONTAINER_URL}/receipts/{id_}/points")
        response_data = response.json()

        print(response_data)
