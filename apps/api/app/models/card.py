from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.models.common import TimestampMixin, UserOwnedMixin, UUIDMixin, utcnow


class Card(UUIDMixin, TimestampMixin, UserOwnedMixin, table=True):
    title: str = Field(index=True, max_length=255)
    description: Optional[str] = None

    sport_id: Optional[UUID] = Field(default=None, foreign_key="sport.id", index=True)
    team_id: Optional[UUID] = Field(default=None, foreign_key="team.id", index=True)
    player_id: Optional[UUID] = Field(default=None, foreign_key="player.id", index=True)

    brand_id: Optional[UUID] = Field(default=None, foreign_key="brand.id", index=True)
    set_id: Optional[UUID] = Field(default=None, foreign_key="cardset.id", index=True)
    card_type_id: Optional[UUID] = Field(default=None, foreign_key="cardtype.id", index=True)

    year: Optional[int] = Field(default=None, index=True)
    card_number: Optional[str] = Field(default=None, max_length=50, index=True)
    parallel: Optional[str] = Field(default=None, max_length=120)

    grading_company_id: Optional[UUID] = Field(
        default=None, foreign_key="gradingcompany.id", index=True
    )
    grade: Optional[str] = Field(default=None, max_length=32)
    serial_number: Optional[str] = Field(default=None, max_length=120)
    condition_notes: Optional[str] = None


class CardImage(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    storage_key: str = Field(max_length=500)
    content_type: Optional[str] = Field(default=None, max_length=120)
    is_primary: bool = Field(default=False)
    sort_order: int = Field(default=0)


class ManualValuation(UUIDMixin, TimestampMixin, table=True):
    card_id: UUID = Field(foreign_key="card.id", index=True)
    value: float = Field(nullable=False, ge=0)
    currency: str = Field(default="USD", max_length=8)
    valued_at: datetime = Field(index=True)
    note: Optional[str] = None


class CardTag(table=True):
    card_id: UUID = Field(foreign_key="card.id", primary_key=True)
    tag_id: UUID = Field(foreign_key="tag.id", primary_key=True)
    created_at: datetime = Field(default_factory=utcnow)
