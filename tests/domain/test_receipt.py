from pydantic import ValidationError
import pytest
from src.domain.receipt import Receipt


def test_receipt_validators_raise_on_amount_mismatch():
    with pytest.raises(ValidationError):
        Receipt(
            retailer="myRetailer",
            purchaseDate="2022-01-01",
            purchaseTime="13:01",
            total=10,
            items=[
                {"shortDescription": "myItem", "price": 5},
                {"shortDescription": "myItem2", "price": 0},
            ],
        )


@pytest.mark.parametrize(
    "time",
    [
        pytest.param("25:01", id="incorrect_hour"),
        pytest.param("13:60", id="incorrect_minute"),
    ],
)
def test_receipt_validators_raise_on_invalid_time(time: str):
    with pytest.raises(ValidationError):
        Receipt(
            retailer="myRetailer",
            purchaseDate="2022-01-01",
            purchaseTime=time,
            total=0,
            items=[],
        )
