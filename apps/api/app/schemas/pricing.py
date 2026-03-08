from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PriceSnapshotCreate(BaseModel):
    card_id: UUID
    price_source_id: UUID
    value: float = Field(ge=0)
    currency: str = "CNY"
    captured_at: datetime
    confidence: Optional[float] = Field(default=None, ge=0, le=1)
    note: Optional[str] = None


class ManualSnapshotCreate(BaseModel):
    card_id: UUID
    value: float = Field(ge=0)
    currency: str = "CNY"
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    note: Optional[str] = "手动录入市场价"


class PriceSnapshotRead(PriceSnapshotCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class PriceSourceRead(BaseModel):
    id: UUID
    name: str
    provider_key: str

    class Config:
        from_attributes = True

