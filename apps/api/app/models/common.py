from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TimestampMixin(SQLModel):
    created_at: datetime = Field(default_factory=utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=utcnow, nullable=False)


class UUIDMixin(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)


class UserOwnedMixin(SQLModel):
    user_id: Optional[UUID] = Field(default=None, foreign_key="user.id", index=True)
