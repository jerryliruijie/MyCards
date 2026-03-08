from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.models.common import TimestampMixin, UUIDMixin


class PurchaseLot(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    purchased_at: datetime = Field(index=True)
    quantity: int = Field(default=1, ge=1)
    unit_price: float = Field(default=0, ge=0)
    fees: float = Field(default=0, ge=0)
    tax: float = Field(default=0, ge=0)
    shipping: float = Field(default=0, ge=0)
    seller: Optional[str] = Field(default=None, max_length=200)
    note: Optional[str] = None


class SaleLot(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    sold_at: Optional[datetime] = Field(default=None, index=True)
    quantity: int = Field(default=1, ge=1)
    unit_price: float = Field(default=0, ge=0)
    fees: float = Field(default=0, ge=0)
    buyer: Optional[str] = Field(default=None, max_length=200)
    note: Optional[str] = None
