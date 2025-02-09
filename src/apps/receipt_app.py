import math
import uuid
from src.exceptions import AppError, ProviderError
from src.providers.receipt_provider import ReceiptProvider
from src.domain.receipt import Receipt, ReceiptWithIDs


class ReceiptApp:
    def __init__(self, receipt_provider: ReceiptProvider) -> None:
        self._receipt_provider = receipt_provider

    def add_receipt(self, receipt: Receipt) -> ReceiptWithIDs:
        try:
            return self._receipt_provider.add_receipt(receipt=receipt)
        except ProviderError as e:
            raise AppError("Failed to add receipt.") from e

    def get_receipt(self, receipt_id: uuid.UUID) -> ReceiptWithIDs:
        try:
            return self._receipt_provider.get_by_id(receipt_id=receipt_id)
        except ProviderError as e:
            raise AppError(f"Failed to retrieve receipt with id {receipt_id}.") from e

    def calculate_receipt_points(self, receipt_id: uuid.UUID) -> int:
        receipt = self.get_receipt(receipt_id=receipt_id)
        return self._calculate_receipt_points(receipt=receipt)

    def _calculate_receipt_points(self, receipt: ReceiptWithIDs) -> int:
        points = 0

        # One point for every alphanumeric character in the retailer name.
        points += sum(char.isalnum() for char in receipt.retailer)

        # 50 points if the total is a round dollar amount with no cents.
        if receipt.total == int(receipt.total):
            points += 50

        # 25 points if the total is a multiple of 0.25.
        if receipt.total % 0.25 == 0:
            points += 25

        # 5 points for every two items on the receipt.
        points += len(receipt.items) // 2 * 5

        # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer.
        # The result is the number of points earned.
        for item in receipt.items:
            if len(item.short_description.strip()) % 3 == 0:
                points += math.ceil(item.price * 0.2 + 0.5)

        # 6 points if the day in the purchase date is odd.
        if receipt.purchase_date.day % 2 == 1:
            points += 6

        # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        hour = int(receipt.purchase_time.split(":")[0])
        if 14 <= hour < 16:
            points += 10

        return points
