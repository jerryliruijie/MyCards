from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.models.common import TimestampMixin, UUIDMixin, UserOwnedMixin, utcnow


class StoragePosition(UUIDMixin, TimestampMixin, UserOwnedMixin, table=True):
    name: str = Field(index=True, max_length=200)
    parent_id: Optional[UUID] = Field(default=None, foreign_key="storageposition.id", index=True)
    position_type: Optional[str] = Field(default=None, max_length=80)
    notes: Optional[str] = None


class CardStorageAssignment(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    storage_position_id: UUID = Field(foreign_key="storageposition.id", index=True)
    quantity: int = Field(default=1, ge=1)
    assigned_at: datetime = Field(default_factory=utcnow)
