from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from fastapi import FastAPI


class Service(ABC):
    @abstractmethod
    def register(self, *, api: FastAPI) -> None: ...
