from fastapi import FastAPI

from typing_extensions import override

from sqlalchemy.orm import scoped_session
from src.apps.receipt_app import ReceiptApp
from src.handlers.receipt_handler import ReceiptHandler
from src.providers.receipt_provider import ReceiptProvider
from src.services.service import Service


class ReceiptService(Service):
    def __init__(self, session: scoped_session):
        receipt_provider = ReceiptProvider(session=session)
        self._app = ReceiptApp(receipt_provider=receipt_provider)
        self._handler = ReceiptHandler(app=self._app)

    @override
    def register(self, *, api: FastAPI) -> None:
        self._handler.register(api=api)
