import uuid
from sqlalchemy.orm import scoped_session
from sqlalchemy.exc import NoResultFound
from unittest import mock
import pytest

from src.exceptions import ProviderError
from src.models.receipt import Receipt
from src.providers.receipt_provider import ReceiptProvider


@pytest.fixture
def mock_session() -> mock.Mock:
    return mock.Mock(spec=scoped_session)


@pytest.fixture
def receipt_provider(mock_session: mock.Mock) -> ReceiptProvider:
    return ReceiptProvider(session=mock_session)


def test_get_by_id_failure(receipt_provider: ReceiptProvider, mock_session: mock.Mock):
    # Arrange
    mock_session.query.side_effect = NoResultFound

    # Act & Assert
    with pytest.raises(ProviderError):
        receipt_provider.get_by_id(uuid.uuid4())


def test_add_receipt_failure(
    receipt_provider: ReceiptProvider, mock_session: mock.Mock, target_receipt: Receipt
):
    # Arrange
    mock_session.commit.side_effect = Exception

    # Act & Assert
    with pytest.raises(ProviderError):
        receipt_provider.add_receipt(target_receipt)

    mock_session.rollback.assert_called_once()
