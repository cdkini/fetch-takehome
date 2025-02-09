import uuid
from sqlalchemy.orm import scoped_session

from src.types.item import ItemWithID
from src.types.receipt import Receipt as ReceiptNoIDs
from src.types.receipt import ReceiptWithIDs
from src.models.receipt import Receipt as DBReceipt
from src.models.item import Item as DBItem


class ReceiptProvider:
    def __init__(self, session: scoped_session) -> None:
        self._session = session

    def add_receipt(self, receipt: ReceiptNoIDs) -> ReceiptWithIDs:
        id_ = uuid.uuid4()
        db_item = DBReceipt(
            id=id_,
            retailer=receipt.retailer,
            purchase_date=receipt.purchase_date,
            purchase_time=receipt.purchase_time,
            total=receipt.total,
            items=[
                DBItem(
                    id=uuid.uuid4(),
                    receipt_id=id_,
                    short_description=item.short_description,
                    price=item.price,
                )
                for item in receipt.items
            ],
        )

        with self._session() as session:
            session.add(db_item)
            session.commit()

        return self.to_adm(db_item)

    def get_by_id(self, receipt_id: uuid.UUID) -> ReceiptWithIDs:
        db_receipt = (
            self._session.query(DBReceipt).filter(DBReceipt.id == receipt_id).one()
        )
        return self.to_adm(db_receipt)

    @staticmethod
    def to_adm(db_receipt: DBReceipt) -> ReceiptWithIDs:
        return ReceiptWithIDs(
            id=db_receipt.id,
            retailer=db_receipt.retailer,
            purchaseDate=db_receipt.purchase_date,
            purchaseTime=db_receipt.purchase_time,
            total=db_receipt.total,
            items=[
                ItemWithID(
                    id=item.id,
                    shortDescription=item.short_description,
                    price=item.price,
                )
                for item in db_receipt.items
            ],
        )
