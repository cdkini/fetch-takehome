import uuid
from fastapi import APIRouter, FastAPI
from src.apps.receipt_app import ReceiptApp
from src.handlers.handler import Handler


class ReceiptHandler(Handler):
    def __init__(self, app: ReceiptApp) -> None:
        self._app = app
        self._router = APIRouter(prefix="/receipts", tags=["receipts"])

    def register(self, *, api: FastAPI) -> None:
        self._router.add_api_route(
            path="/process", endpoint=self.process_receipt, methods=["POST"]
        )
        self._router.add_api_route(
            path="/{receipt_id}", endpoint=self.get_receipt, methods=["GET"]
        )
        self._router.add_api_route(
            path="/{receipt_id}/points",
            endpoint=self.get_receipt_points,
            methods=["GET"],
        )

        api.include_router(router=self._router)

    def process_receipt(self, receipt: dict) -> dict:
        pass

    def get_receipt(self, receipt_id: uuid.UUID) -> dict:
        pass

    def get_receipt_points(self, receipt_id: uuid.UUID) -> dict:
        pass
