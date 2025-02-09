from __future__ import annotations

import datetime

import sqlalchemy as sa
from sqlalchemy.orm import MappedColumn, mapped_column, validates


class TimestampsMixin:
    created_at: MappedColumn[datetime.datetime] = mapped_column(
        server_default=sa.func.now()
    )
    updated_at: MappedColumn[datetime.datetime] = mapped_column(
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
    )

    @validates("created_at")
    def _write_once(self, key: str, value: str) -> str:
        existing = getattr(self, key, None)
        if existing is not None:
            raise ValueError(f"Field '{key}' is write-once")
        return value
