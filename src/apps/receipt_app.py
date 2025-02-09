from src.providers.receipt_provider import ReceiptProvider


class ReceiptApp:
    def __init__(self, receipt_provider: ReceiptProvider) -> None:
        self._receipt_provider = receipt_provider
