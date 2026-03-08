from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.models.common import TimestampMixin, UUIDMixin


class User(UUIDMixin, TimestampMixin, table=True):
    email: Optional[str] = Field(default=None, unique=True, index=True)
    display_name: str = Field(default="Owner", max_length=120)
    is_active: bool = Field(default=True)


class Sport(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)


class Team(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, max_length=200)
    sport_id: Optional[UUID] = Field(default=None, foreign_key="sport.id", index=True)


class Player(UUIDMixin, TimestampMixin, table=True):
    full_name: str = Field(index=True, max_length=200)
    sport_id: Optional[UUID] = Field(default=None, foreign_key="sport.id", index=True)
    team_id: Optional[UUID] = Field(default=None, foreign_key="team.id", index=True)


class Brand(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)


class CardSet(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, max_length=200)
    brand_id: Optional[UUID] = Field(default=None, foreign_key="brand.id", index=True)
    release_year: Optional[int] = Field(default=None, index=True)


class CardType(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)


class GradingCompany(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)


class PriceSource(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)
    provider_key: str = Field(index=True, max_length=120)
    is_enabled: bool = Field(default=True)
    notes: Optional[str] = None


class Tag(UUIDMixin, TimestampMixin, table=True):
    name: str = Field(index=True, unique=True, max_length=120)
    color: Optional[str] = Field(default=None, max_length=16)
