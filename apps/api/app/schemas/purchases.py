from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PurchaseLotCreate(BaseModel):
    card_id: UUID
    purchased_at: datetime
    quantity: int = Field(default=1, ge=1)
    unit_price: float = Field(default=0, ge=0)
    fees: float = Field(default=0, ge=0)
    tax: float = Field(default=0, ge=0)
    shipping: float = Field(default=0, ge=0)
    seller: Optional[str] = None
    note: Optional[str] = None


class PurchaseLotRead(PurchaseLotCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
