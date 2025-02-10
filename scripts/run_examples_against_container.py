"""
This script is used to run the examples against the container.
"""

import json
import requests


BASE_CONTAINER_URL = "http://0.0.0.0:8000"


if __name__ == "__main__":
    files = ["examples/morning-receipt.json", "examples/simple-receipt.json"]

    for file in files:
        with open(file) as f:
            receipt_data = json.load(f)

        response = requests.post(
            f"{BASE_CONTAINER_URL}/receipts/process", json=receipt_data
        )
        response_data = response.json()

        print(response_data)

        id_ = response_data["id"]

        response = requests.get(f"{BASE_CONTAINER_URL}/receipts/{id_}/points")
        response_data = response.json()

        print(response_data)
