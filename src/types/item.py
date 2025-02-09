import uuid
from pydantic import BaseModel, Field


class ItemNoID(BaseModel):
    short_description: str = Field(..., alias="shortDescription")
    price: float


class ItemWithID(ItemNoID):
    id: uuid.UUID
