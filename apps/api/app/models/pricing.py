from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.models.common import TimestampMixin, UUIDMixin


class PriceSnapshot(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    price_source_id: UUID = Field(foreign_key="pricesource.id", index=True)
    value: float = Field(ge=0)
    currency: str = Field(default="USD", max_length=8)
    captured_at: datetime = Field(index=True)
    confidence: Optional[float] = Field(default=None, ge=0, le=1)
    note: Optional[str] = None
