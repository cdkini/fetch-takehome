import uuid


class ReceiptProvider:
    def __init__(self, session):
        pass

    def add_receipt(self, receipt: dict) -> dict:
        pass

    def get_receipt(self, receipt_id: uuid.UUID) -> dict:
        pass
