from __future__ import annotations
from typing import Literal


class BaseError(Exception):
    pass  # Base class for all exceptions in this module


class ProviderError(BaseError):
    pass


class AppError(BaseError):
    def __init__(self, err: Literal["generic"] | Literal["not_found"]) -> None:
        self.err = err
