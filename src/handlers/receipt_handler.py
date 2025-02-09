import uuid
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from src.apps.receipt_app import ReceiptApp
from src.exceptions import AppError
from src.handlers.handler import Handler
from src.domain.receipt import Receipt


class ReceiptResponse(BaseModel):
    id: uuid.UUID


class PointsResponse(BaseModel):
    points: int


class ReceiptHandler(Handler):
    def __init__(self, app: ReceiptApp) -> None:
        self._app = app
        self._router = APIRouter(prefix="/receipts", tags=["receipts"])

    def register(self, *, api: FastAPI) -> None:
        self._router.add_api_route(
            path="/process",
            endpoint=self.process_receipt,
            response_model=ReceiptResponse,
            methods=["POST"],
        )
        self._router.add_api_route(
            path="/{receipt_id}/points",
            endpoint=self.get_receipt_points,
            response_model=PointsResponse,
            methods=["GET"],
        )

        api.include_router(router=self._router)

    def process_receipt(self, receipt: Receipt) -> ReceiptResponse:
        try:
            receipt_with_ids = self._app.add_receipt(receipt=receipt)
        except AppError:
            raise HTTPException(status_code=400, detail="Failed to process receipt.")

        return ReceiptResponse(id=receipt_with_ids.id)

    def get_receipt_points(self, receipt_id: uuid.UUID) -> PointsResponse:
        try:
            points = self._app.calculate_receipt_points(receipt_id=receipt_id)
        except AppError:
            raise HTTPException(
                status_code=400,
                detail="Error retrieving receipt and calculating points.",
            )

        return PointsResponse(points=points)
