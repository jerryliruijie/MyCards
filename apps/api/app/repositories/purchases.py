from uuid import UUID

from sqlmodel import Session, desc, select

from app.models.transactions import PurchaseLot


class PurchaseRepository:
    def list_for_card(self, session: Session, card_id: UUID) -> list[PurchaseLot]:
        stmt = select(PurchaseLot).where(PurchaseLot.card_id == card_id).order_by(desc(PurchaseLot.purchased_at))
        return list(session.exec(stmt))

    def create(self, session: Session, lot: PurchaseLot) -> PurchaseLot:
        session.add(lot)
        session.commit()
        session.refresh(lot)
        return lot
