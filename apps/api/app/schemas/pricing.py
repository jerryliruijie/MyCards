from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PriceSnapshotCreate(BaseModel):
    card_id: UUID
    price_source_id: UUID
    value: float = Field(ge=0)
    currency: str = "USD"
    captured_at: datetime
    confidence: Optional[float] = Field(default=None, ge=0, le=1)
    note: Optional[str] = None


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
