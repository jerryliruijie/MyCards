from datetime import datetime, timezone
from random import Random
from uuid import UUID

from app.integrations.pricing.base import PricingProvider, ProviderPrice


class MockPricingProvider(PricingProvider):
    provider_key = "mock-pricing"

    def __init__(self, seed: int = 42) -> None:
        self._rng = Random(seed)

    def fetch_price(self, card_id: UUID) -> ProviderPrice:
        base = self._rng.uniform(15, 650)
        confidence = self._rng.uniform(0.6, 0.95)
        return ProviderPrice(
            card_id=card_id,
            value=round(base, 2),
            currency="USD",
            captured_at=datetime.now(timezone.utc),
            confidence=round(confidence, 2),
            note="Mock provider value for development",
        )
