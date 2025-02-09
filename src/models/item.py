from __future__ import annotations


import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import MappedColumn, Mapped, mapped_column, relationship

import src.db as db
from src.models.mixins import TimestampsMixin


class Item(db.Base, TimestampsMixin):
    __tablename__ = "items"

    id: MappedColumn[uuid.UUID] = mapped_column(primary_key=True)
    receipt_id: MappedColumn[uuid.UUID] = mapped_column(
        ForeignKey("receipts.id"), nullable=False
    )

    short_description: MappedColumn[str]
    price: MappedColumn[float]

    receipt: Mapped["Receipt"] = relationship(  # noqa: F821
        back_populates="items", foreign_keys="Item.receipt_id"
    )
