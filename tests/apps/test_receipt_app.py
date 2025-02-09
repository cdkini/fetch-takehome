import uuid
import pytest

from unittest import mock
from src.apps.receipt_app import ReceiptApp
from src.providers.receipt_provider import ReceiptProvider
from src.domain.receipt import Receipt


@pytest.fixture
def mock_receipt_provider() -> mock.Mock:
    return mock.Mock(spec=ReceiptProvider)


@pytest.fixture
def receipt_app(mock_receipt_provider: mock.Mock) -> ReceiptApp:
    return ReceiptApp(receipt_provider=mock_receipt_provider)


@pytest.mark.parametrize(
    "receipt_fixture_name, expected_points",
    [
        pytest.param("target_receipt_w_ids", 28, id="target"),
        pytest.param("mnm_corner_market_receipt_w_ids", 109, id="m&m corner market"),
    ],
)
def test_calculate_points(
    receipt_app: ReceiptApp,
    mock_receipt_provider: mock.Mock,
    request,
    receipt_fixture_name: str,
    expected_points: int,
):
    receipt = request.getfixturevalue(receipt_fixture_name)

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
