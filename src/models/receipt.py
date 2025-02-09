from __future__ import annotations


import datetime as dt
from typing import List
import uuid
from sqlalchemy.orm import MappedColumn, Mapped, mapped_column, relationship

import src.db as db
from src.models.mixins import TimestampsMixin


class Receipt(db.Base, TimestampsMixin):
    __tablename__ = "receipts"

    id: MappedColumn[uuid.UUID] = mapped_column(primary_key=True)

    retailer: MappedColumn[str]
    purchase_date: MappedColumn[dt.datetime]
    purchase_time: MappedColumn[str]
    total: MappedColumn[float]

    items: Mapped[List["Item"]] = relationship(  # noqa: F821
        back_populates="receipt",
    )
