from uuid import UUID

from sqlmodel import Session, desc, select

from app.models.pricing import PriceSnapshot
from app.models.reference import PriceSource


class PricingRepository:
    def create_snapshot(self, session: Session, snapshot: PriceSnapshot) -> PriceSnapshot:
        session.add(snapshot)
        session.commit()
        session.refresh(snapshot)
        return snapshot

    def list_card_snapshots(self, session: Session, card_id: UUID) -> list[PriceSnapshot]:
        stmt = (
            select(PriceSnapshot)
            .where(PriceSnapshot.card_id == card_id)
            .order_by(desc(PriceSnapshot.captured_at))
        )
        return list(session.exec(stmt))

    def latest_snapshot_for_card(self, session: Session, card_id: UUID) -> PriceSnapshot | None:
        stmt = (
            select(PriceSnapshot)
            .where(PriceSnapshot.card_id == card_id)
            .order_by(desc(PriceSnapshot.captured_at))
            .limit(1)
        )
        return session.exec(stmt).first()

    def list_sources(self, session: Session) -> list[PriceSource]:
        stmt = select(PriceSource).where(PriceSource.is_enabled.is_(True)).order_by(PriceSource.name.asc())
        return list(session.exec(stmt))

    def get_or_create_manual_source(self, session: Session) -> PriceSource:
        stmt = select(PriceSource).where(PriceSource.provider_key == "manual-input").limit(1)
        source = session.exec(stmt).first()
        if source:
            return source

        source = PriceSource(name="Manual Input", provider_key="manual-input", is_enabled=True)
        session.add(source)
        session.commit()
        session.refresh(source)
        return source
