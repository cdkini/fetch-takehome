import datetime as dt
from typing import List
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator


class Item(BaseModel):
    short_description: str = Field(..., alias="shortDescription")
    price: float


class Receipt(BaseModel):
    retailer: str
    purchase_date: dt.datetime = Field(..., alias="purchaseDate")
    purchase_time: str = Field(..., alias="purchaseTime")
    total: float
    items: List[Item]

    @model_validator(mode="after")
    def check_amounts_equal(self) -> Self:
        if self.total != sum(item.price for item in self.items):
            raise ValueError("Total amount does not match sum of item prices")
        return self
