from sqlmodel import Session

from app.models.pricing import PriceSnapshot
from app.repositories.pricing import PricingRepository
from app.schemas.pricing import ManualSnapshotCreate, PriceSnapshotCreate


class PricingService:
    def __init__(self, repo: PricingRepository | None = None) -> None:
        self.repo = repo or PricingRepository()

    def create_snapshot(self, session: Session, payload: PriceSnapshotCreate) -> PriceSnapshot:
        snapshot = PriceSnapshot(**payload.model_dump())
        return self.repo.create_snapshot(session, snapshot)

    def create_manual_snapshot(self, session: Session, payload: ManualSnapshotCreate) -> PriceSnapshot:
        source = self.repo.get_or_create_manual_source(session)
        snapshot = PriceSnapshot(
            card_id=payload.card_id,
            price_source_id=source.id,
            value=payload.value,
            currency=payload.currency,
            captured_at=payload.captured_at,
            note=payload.note,
        )
        return self.repo.create_snapshot(session, snapshot)

    def list_card_snapshots(self, session: Session, card_id):
        return self.repo.list_card_snapshots(session, card_id)

    def list_sources(self, session: Session):
        return self.repo.list_sources(session)
