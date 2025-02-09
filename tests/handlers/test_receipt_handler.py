from unittest import mock
import uuid
from fastapi import FastAPI, HTTPException
import pytest

from src.apps.receipt_app import ReceiptApp
from src.domain.receipt import ReceiptWithIDs
from src.exceptions import AppError
from src.handlers.receipt_handler import ReceiptHandler
from src.models.receipt import Receipt


@pytest.fixture
def mock_receipt_app() -> mock.Mock:
    return mock.Mock(spec=ReceiptApp)


@pytest.fixture
def receipt_handler(mock_receipt_app: ReceiptApp, app: FastAPI) -> ReceiptHandler:
    handler = ReceiptHandler(app=mock_receipt_app)
    handler.register(api=app)
    return handler


def test_process_receipt_success(
    receipt_handler: ReceiptHandler,
    mock_receipt_app: mock.Mock,
    target_receipt: Receipt,
    target_receipt_w_ids: ReceiptWithIDs,
):
    # Arrange
    mock_receipt_app.add_receipt.return_value = target_receipt_w_ids

    # Act
    result = receipt_handler.process_receipt(receipt=target_receipt)

    # Assert
    assert result.model_dump() == {"id": target_receipt_w_ids.id}
    mock_receipt_app.add_receipt.assert_called_once_with(receipt=target_receipt)


def test_process_receipt_failure(
    receipt_handler: ReceiptHandler,
    mock_receipt_app: mock.Mock,
    target_receipt: Receipt,
):
    # Arrange
    mock_receipt_app.add_receipt.side_effect = AppError(err="generic")

    # Act & Assert
    with pytest.raises(HTTPException) as e:
        receipt_handler.process_receipt(receipt=target_receipt)

    # Assert
    assert e.value.status_code == 400
    mock_receipt_app.add_receipt.assert_called_once_with(receipt=target_receipt)


def test_get_receipt_points_success(
    receipt_handler: ReceiptHandler,
    mock_receipt_app: mock.Mock,
):
    # Arrange
    receipt_id = uuid.uuid4()
    mock_receipt_app.calculate_receipt_points.return_value = 28

    # Act
    result = receipt_handler.get_receipt_points(receipt_id=receipt_id)

    # Assert
    assert result.model_dump() == {"points": 28}
    mock_receipt_app.calculate_receipt_points.assert_called_once_with(
        receipt_id=receipt_id
    )


@pytest.mark.parametrize(
    "err, status_code",
    [
        pytest.param("not_found", 404, id="not_found"),
        pytest.param("generic", 400, id="generic"),
    ],
)
def test_get_receipt_points_failure(
    receipt_handler: ReceiptHandler,
    mock_receipt_app: mock.Mock,
    err: str,
    status_code: int,
):
    # Arrange
    receipt_id = uuid.uuid4()
    mock_receipt_app.calculate_receipt_points.side_effect = AppError(err=err)

    # Act & Assert
    with pytest.raises(HTTPException) as e:
        receipt_handler.get_receipt_points(receipt_id=receipt_id)

    # Assert
    assert e.value.status_code == status_code
    mock_receipt_app.calculate_receipt_points.assert_called_once_with(
        receipt_id=receipt_id
    )
