from dataclasses import dataclass

from sqlmodel import Session, select

from app.models.card import Card, ManualValuation
from app.models.transactions import PurchaseLot
from app.repositories.pricing import PricingRepository


@dataclass
class PortfolioTotals:
    card_count: int
    total_cost_basis: float
    total_latest_value: float
    unrealized_pnl: float
    unrealized_pnl_pct: float


class PortfolioService:
    def __init__(self, pricing_repo: PricingRepository | None = None) -> None:
        self.pricing_repo = pricing_repo or PricingRepository()

    def _cost_basis_for_card(self, session: Session, card_id) -> float:
        lots = list(session.exec(select(PurchaseLot).where(PurchaseLot.card_id == card_id)))
        total = 0.0
        for lot in lots:
            total += (lot.quantity * lot.unit_price) + lot.fees + lot.tax + lot.shipping
        return total

    def _latest_value_for_card(self, session: Session, card_id) -> float:
        snapshot = self.pricing_repo.latest_snapshot_for_card(session, card_id)
        if snapshot:
            return snapshot.value

        manual_stmt = (
            select(ManualValuation)
            .where(ManualValuation.card_id == card_id)
            .order_by(ManualValuation.valued_at.desc())
            .limit(1)
        )
        manual = session.exec(manual_stmt).first()
        if manual:
            return manual.value
        return 0.0

    def summarize(self, session: Session) -> PortfolioTotals:
        card_ids = list(session.exec(select(Card.id)))
        cost_basis = 0.0
        latest_value = 0.0

        for card_id in card_ids:
            cost_basis += self._cost_basis_for_card(session, card_id)
            latest_value += self._latest_value_for_card(session, card_id)

        pnl = latest_value - cost_basis
        pnl_pct = (pnl / cost_basis) * 100 if cost_basis else 0.0
        return PortfolioTotals(
            card_count=len(card_ids),
            total_cost_basis=round(cost_basis, 2),
            total_latest_value=round(latest_value, 2),
            unrealized_pnl=round(pnl, 2),
            unrealized_pnl_pct=round(pnl_pct, 2),
        )
