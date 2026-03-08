from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class StoragePositionCreate(BaseModel):
    name: str
    parent_id: Optional[UUID] = None
    position_type: Optional[str] = None
    notes: Optional[str] = None
    user_id: Optional[UUID] = None


class StoragePositionRead(StoragePositionCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CardStorageAssignmentCreate(BaseModel):
    card_id: UUID
    storage_position_id: UUID
    quantity: int = Field(default=1, ge=1)


class CardStorageAssignmentRead(BaseModel):
    id: UUID
    card_id: UUID
    storage_position_id: UUID
    quantity: int

    class Config:
        from_attributes = True
