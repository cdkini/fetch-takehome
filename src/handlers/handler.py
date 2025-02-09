from abc import ABC, abstractmethod


from fastapi import FastAPI


class Handler(ABC):
    @abstractmethod
    def register(self, *, api: FastAPI) -> None: ...
