import datetime as dt
from typing import List
import math
import uuid
from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator, model_validator

from src.types.item import ItemNoID, ItemWithID


class ReceiptNoIDs(BaseModel):
    retailer: str
    purchase_date: dt.datetime = Field(..., alias="purchaseDate")
    purchase_time: str = Field(..., alias="purchaseTime")
    total: float
    items: List[ItemNoID]

    @field_validator("purchase_time")
    def check_purchase_time_format(cls, value: str) -> str:
        parts = value.split(":")
        if len(parts) != 2:
            raise ValueError("Purchase time must be in HH:MM format")

        if int(parts[0]) < 0 or int(parts[0]) > 23:
            raise ValueError("Hour must be between 0 and 23")

        if int(parts[1]) < 0 or int(parts[1]) > 59:
            raise ValueError("Minute must be between 0 and 59")

        return value

    @model_validator(mode="after")
    def check_amounts_equal(self) -> Self:
        if not math.isclose(self.total, sum(item.price for item in self.items)):
            raise ValueError("Total amount does not match sum of item prices")

        return self


class ReceiptWithIDs(ReceiptNoIDs):
    id: uuid.UUID
    items: List[ItemWithID]
