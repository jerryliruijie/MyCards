from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TagCreate(BaseModel):
    name: str
    color: Optional[str] = None


class TagRead(TagCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class CardTagAssign(BaseModel):
    tag_id: UUID
