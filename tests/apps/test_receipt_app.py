import uuid
import pytest

from unittest import mock
from src.apps.receipt_app import ReceiptApp
from src.providers.receipt_provider import ReceiptProvider
from src.types.item import ItemWithID
from src.types.receipt import Receipt, ReceiptWithIDs


@pytest.fixture
def mock_receipt_provider() -> mock.Mock:
    return mock.Mock(spec=ReceiptProvider)


@pytest.fixture
def receipt_app(mock_receipt_provider: mock.Mock) -> ReceiptApp:
    return ReceiptApp(receipt_provider=mock_receipt_provider)


@pytest.mark.parametrize(
    "receipt, expected_points",
    [
        pytest.param(
            ReceiptWithIDs(
                id=uuid.uuid4(),
                retailer="Target",
                purchaseDate="2022-01-01",
                purchaseTime="13:01",
                items=[
                    ItemWithID(
                        id=uuid.uuid4(),
                        shortDescription="Mountain Dew 12PK",
                        price="6.49",
                    ),
                    ItemWithID(
                        id=uuid.uuid4(),
                        shortDescription="Emils Cheese Pizza",
                        price="12.25",
                    ),
                    ItemWithID(
                        id=uuid.uuid4(),
                        shortDescription="Knorr Creamy Chicken",
                        price="1.26",
                    ),
                    ItemWithID(
                        id=uuid.uuid4(),
                        shortDescription="Doritos Nacho Cheese",
                        price="3.35",
                    ),
                    ItemWithID(
                        id=uuid.uuid4(),
                        shortDescription="   Klarbrunn 12-PK 12 FL OZ  ",
                        price="12.00",
                    ),
                ],
                total="35.35",
            ),
            28,
            id="target",
        ),
        pytest.param(
            ReceiptWithIDs(
                id=uuid.uuid4(),
                retailer="M&M Corner Market",
                purchaseDate="2022-03-20",
                purchaseTime="14:33",
                items=[
                    ItemWithID(
                        id=uuid.uuid4(), shortDescription="Gatorade", price="2.25"
                    ),
                    ItemWithID(
                        id=uuid.uuid4(), shortDescription="Gatorade", price="2.25"
                    ),
                    ItemWithID(
                        id=uuid.uuid4(), shortDescription="Gatorade", price="2.25"
                    ),
                    ItemWithID(
                        id=uuid.uuid4(), shortDescription="Gatorade", price="2.25"
                    ),
                ],
                total="9.00",
            ),
            109,
            id="m&m corner market",
        ),
    ],
)
def test_calculate_points(
    receipt_app: ReceiptApp,
    mock_receipt_provider: mock.Mock,
    receipt: ReceiptWithIDs,
    expected_points: int,
):
    # Arrange
    receipt_id = receipt.id
    mock_receipt_provider.get_by_id.return_value = receipt

    # Act
    points = receipt_app.calculate_receipt_points(receipt_id=receipt_id)

    # Assert
    assert points == expected_points


def test_add_receipt(receipt_app: ReceiptApp, mock_receipt_provider: mock.Mock):
    # Arrange
    receipt = Receipt(
        retailer="Dunder Mifflin",
        purchaseDate="2022-01-01",
        purchaseTime="13:01",
        total=0,
        items=[],
    )

    # Act
    receipt_app.add_receipt(receipt=receipt)

    # Assert
    mock_receipt_provider.add_receipt.assert_called_once_with(receipt=receipt)


def test_get_receipt(receipt_app: ReceiptApp, mock_receipt_provider: mock.Mock):
    # Arrange
    receipt_id = uuid.uuid4()

    # Act
    receipt_app.get_receipt(receipt_id=receipt_id)

    # Assert
    mock_receipt_provider.get_by_id.assert_called_once_with(receipt_id=receipt_id)
