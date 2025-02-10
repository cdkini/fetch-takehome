from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel
from src.services.receipt_service import ReceiptService
import uvicorn

from src.db import init_db


class APIConfig(BaseModel):
    connection_string: str = "sqlite:///data.db"
    engine_kwargs: dict = {"echo": True}
    app_host: str = "0.0.0.0"
    app_port: int = 8000


class API:
    def __init__(self, config: APIConfig):
        self._app = self.init_app()
        self._session = init_db(
            connection_string=config.connection_string,
            engine_kwargs=config.engine_kwargs,
        )

    @property
    def app(self):
        return self._app

    def init_app(self):
        app = FastAPI()

        @app.get("/")
        def root():
            return {"message": "Hello, Fetch!"}

        return app

    def init_services(self):
        receipt_service = ReceiptService(session=self._session)
        receipt_service.register(api=self._app)


def get_app(config: APIConfig = APIConfig()) -> FastAPI:
    api = API(config=config)
    api.init_services()
    return api.app


if __name__ == "__main__":
    uvicorn.run(
        app="src.api:get_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
