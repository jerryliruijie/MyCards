from sqlmodel import Session

from app.models.transactions import PurchaseLot
from app.repositories.purchases import PurchaseRepository
from app.schemas.purchases import PurchaseLotCreate


class PurchaseService:
    def __init__(self, repo: PurchaseRepository | None = None) -> None:
        self.repo = repo or PurchaseRepository()

    def list_for_card(self, session: Session, card_id):
        return self.repo.list_for_card(session, card_id)

    def create(self, session: Session, payload: PurchaseLotCreate) -> PurchaseLot:
        lot = PurchaseLot(**payload.model_dump())
        return self.repo.create(session, lot)
