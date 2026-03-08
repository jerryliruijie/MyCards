from sqlmodel import Session

from app.db.session import engine
from app.models.reference import PriceSource
from app.repositories.cards import CardRepository
from app.services.pricing import PricingService


def run_price_refresh_once() -> None:
    card_repo = CardRepository()
    pricing = PricingService()

    with Session(engine) as session:
        sources = pricing.list_sources(session)
        mock_sources = [s for s in sources if s.provider_key == "mock-pricing"]
        if not mock_sources:
            return

        source: PriceSource = mock_sources[0]
        for card_id in card_repo.list_card_ids(session):
            # TODO: Replace with scheduler-triggered provider fan-out in production mode.
            from app.integrations.pricing.registry import get_pricing_provider
            from app.schemas.pricing import PriceSnapshotCreate

            provider = get_pricing_provider(source.provider_key)
            fetched = provider.fetch_price(card_id)
            payload = PriceSnapshotCreate(
                card_id=card_id,
                price_source_id=source.id,
                value=fetched.value,
                currency=fetched.currency,
                captured_at=fetched.captured_at,
                confidence=fetched.confidence,
                note=fetched.note,
            )
            pricing.create_snapshot(session, payload)


if __name__ == "__main__":
    run_price_refresh_once()
    print("Price refresh complete")
