from sqlmodel import Session

from app.models.pricing import PriceSnapshot
from app.repositories.pricing import PricingRepository
from app.schemas.pricing import PriceSnapshotCreate


class PricingService:
    def __init__(self, repo: PricingRepository | None = None) -> None:
        self.repo = repo or PricingRepository()

    def create_snapshot(self, session: Session, payload: PriceSnapshotCreate) -> PriceSnapshot:
        snapshot = PriceSnapshot(**payload.model_dump())
        return self.repo.create_snapshot(session, snapshot)

    def list_card_snapshots(self, session: Session, card_id):
        return self.repo.list_card_snapshots(session, card_id)

    def list_sources(self, session: Session):
        return self.repo.list_sources(session)
