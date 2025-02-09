from __future__ import annotations


import uuid
from sqlalchemy.orm import MappedColumn, Mapped, mapped_column, relationship

import src.db as db
from src.models.mixins import TimestampsMixin


class Item(db.Base, TimestampsMixin):
    __tablename__ = "items"

    id: MappedColumn[uuid.UUID] = mapped_column(primary_key=True)

    short_description: MappedColumn[str]
    price: MappedColumn[float]

    receipt: Mapped["Receipt"] = relationship(back_populates="items")
