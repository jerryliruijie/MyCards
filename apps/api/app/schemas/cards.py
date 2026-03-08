from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CardBase(BaseModel):
    title: str
    description: Optional[str] = None
    sport_id: Optional[UUID] = None
    team_id: Optional[UUID] = None
    player_id: Optional[UUID] = None
    brand_id: Optional[UUID] = None
    set_id: Optional[UUID] = None
    card_type_id: Optional[UUID] = None
    year: Optional[int] = None
    card_number: Optional[str] = None
    parallel: Optional[str] = None
    grading_company_id: Optional[UUID] = None
    grade: Optional[str] = None
    serial_number: Optional[str] = None
    condition_notes: Optional[str] = None


class CardCreate(CardBase):
    user_id: Optional[UUID] = None


class CardUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    sport_id: Optional[UUID] = None
    team_id: Optional[UUID] = None
    player_id: Optional[UUID] = None
    brand_id: Optional[UUID] = None
    set_id: Optional[UUID] = None
    card_type_id: Optional[UUID] = None
    year: Optional[int] = None
    card_number: Optional[str] = None
    parallel: Optional[str] = None
    grading_company_id: Optional[UUID] = None
    grade: Optional[str] = None
    serial_number: Optional[str] = None
    condition_notes: Optional[str] = None


class CardRead(CardBase):
    id: UUID
    user_id: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CardImageCreate(BaseModel):
    storage_key: str
    content_type: Optional[str] = None
    is_primary: bool = False
    sort_order: int = 0


class CardImageRead(BaseModel):
    id: UUID
    card_id: UUID
    storage_key: str
    content_type: Optional[str]
    is_primary: bool
    sort_order: int

    class Config:
        from_attributes = True
