import uuid
from pydantic import BaseModel, Field


class Item(BaseModel):
    short_description: str = Field(..., alias="shortDescription")
    price: float


class ItemWithID(Item):
    id: uuid.UUID
