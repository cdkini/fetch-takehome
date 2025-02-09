from typing import Generator
import uuid
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pathlib
import pytest

from src.domain.item import Item, ItemWithID
from src.domain.receipt import Receipt, ReceiptWithIDs


@pytest.fixture
def db_path() -> pathlib.Path:
    return pathlib.Path("test.db")


@pytest.fixture
def app(db_path: pathlib.Path) -> Generator[FastAPI, None, None]:
    from src.api import get_app, APIConfig

    config = APIConfig(connection_string=f"sqlite:///{db_path}")
    yield get_app(config=config)

    db_path.unlink(missing_ok=True)


@pytest.fixture
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    return TestClient(app)


@pytest.fixture
def target_receipt() -> Receipt:
    return Receipt(
        retailer="Target",
        purchaseDate="2022-01-01",
        purchaseTime="13:01",
        items=[
            Item(
                shortDescription="Mountain Dew 12PK",
                price="6.49",
            ),
            Item(
                shortDescription="Emils Cheese Pizza",
                price="12.25",
            ),
            Item(
                shortDescription="Knorr Creamy Chicken",
                price="1.26",
            ),
            Item(
                shortDescription="Doritos Nacho Cheese",
                price="3.35",
            ),
            Item(
                shortDescription="   Klarbrunn 12-PK 12 FL OZ  ",
                price="12.00",
            ),
        ],
        total="35.35",
    )


@pytest.fixture
def target_receipt_w_ids(target_receipt: Receipt) -> ReceiptWithIDs:
    return ReceiptWithIDs(
        id=uuid.uuid4(),
        retailer=target_receipt.retailer,
        purchaseDate=target_receipt.purchase_date,
        purchaseTime=target_receipt.purchase_time,
        items=[
            ItemWithID(
                id=uuid.uuid4(),
                shortDescription=item.short_description,
                price=item.price,
            )
            for item in target_receipt.items
        ],
        total=target_receipt.total,
    )


@pytest.fixture
def mnm_corner_market_receipt() -> Receipt:
    return Receipt(
        retailer="M&M Corner Market",
        purchaseDate="2022-03-20",
        purchaseTime="14:33",
        items=[
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25"),
        ],
        total="9.00",
    )


@pytest.fixture
def mnm_corner_market_receipt_w_ids(
    mnm_corner_market_receipt: Receipt,
) -> ReceiptWithIDs:
    return ReceiptWithIDs(
        id=uuid.uuid4(),
        retailer=mnm_corner_market_receipt.retailer,
        purchaseDate=mnm_corner_market_receipt.purchase_date,
        purchaseTime=mnm_corner_market_receipt.purchase_time,
        items=[
            ItemWithID(
                id=uuid.uuid4(),
                shortDescription=item.short_description,
                price=item.price,
            )
            for item in mnm_corner_market_receipt.items
        ],
        total=mnm_corner_market_receipt.total,
    )
