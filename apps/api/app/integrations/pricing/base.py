from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass
class ProviderPrice:
    card_id: UUID
    value: float
    currency: str
    captured_at: datetime
    confidence: float | None = None
    note: str | None = None


class PricingProvider(Protocol):
    provider_key: str

    def fetch_price(self, card_id: UUID) -> ProviderPrice | None:
        ...
