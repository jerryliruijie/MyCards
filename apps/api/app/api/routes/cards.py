from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, File, Query, Response, UploadFile, status
from sqlmodel import Session

from app.db.session import get_session
from app.integrations.storage.registry import get_storage_backend
from app.schemas.cards import (
    CardCoreRead,
    CardCreate,
    CardImageCreate,
    CardImageRead,
    CardImageReorder,
    CardImageSetPrimary,
    CardRead,
    CardUpdate,
)
from app.schemas.tags import CardTagAssign
from app.services.cards import CardService

router = APIRouter()
service = CardService()


@router.get("", response_model=list[CardRead])
def list_cards(
    q: Optional[str] = None,
    sport_id: Optional[UUID] = None,
    player_id: Optional[UUID] = None,
    tag_id: Optional[UUID] = None,
    session: Session = Depends(get_session),
):
    return service.list_cards(session, q=q, sport_id=sport_id, player_id=player_id, tag_id=tag_id)


@router.get("/core/list", response_model=list[CardCoreRead])
def list_card_cores(session: Session = Depends(get_session)):
    return service.list_card_cores(session)


@router.post("", response_model=CardRead, status_code=status.HTTP_201_CREATED)
def create_card(payload: CardCreate, session: Session = Depends(get_session)):
    return service.create_card(session, payload)


@router.get("/{card_id}", response_model=CardRead)
def get_card(card_id: UUID, session: Session = Depends(get_session)):
    return service.get_card_or_404(session, card_id)


@router.get("/{card_id}/core", response_model=CardCoreRead)
def get_card_core(card_id: UUID, session: Session = Depends(get_session)):
    return service.get_card_core(session, card_id)


@router.patch("/{card_id}", response_model=CardRead)
def update_card(card_id: UUID, payload: CardUpdate, session: Session = Depends(get_session)):
    return service.update_card(session, card_id, payload)


@router.delete("/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(card_id: UUID, session: Session = Depends(get_session)):
    service.delete_card(session, card_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/{card_id}/images", response_model=list[CardImageRead])
def list_images(card_id: UUID, session: Session = Depends(get_session)):
    return service.list_images(session, card_id)


@router.post("/{card_id}/images", response_model=CardImageRead, status_code=status.HTTP_201_CREATED)
def add_image(card_id: UUID, payload: CardImageCreate, session: Session = Depends(get_session)):
    return service.add_image(session, card_id, payload)


@router.post("/{card_id}/images/upload", response_model=CardImageRead, status_code=status.HTTP_201_CREATED)
async def upload_image(
    card_id: UUID,
    file: UploadFile = File(...),
    is_primary: bool = Query(default=True),
    sort_order: int = Query(default=0),
    session: Session = Depends(get_session),
):
    storage = get_storage_backend()
    storage_key = await storage.save_card_image(card_id, file)
    payload = CardImageCreate(
        storage_key=storage_key,
        content_type=file.content_type,
        is_primary=is_primary,
        sort_order=sort_order,
    )
    return service.add_image(session, card_id, payload)


@router.patch("/images/set-primary", response_model=CardImageRead)
def set_primary_image(payload: CardImageSetPrimary, session: Session = Depends(get_session)):
    return service.set_primary_image(session, payload.image_id)


@router.patch("/{card_id}/images/reorder", status_code=status.HTTP_204_NO_CONTENT)
def reorder_images(card_id: UUID, payload: CardImageReorder, session: Session = Depends(get_session)):
    service.reorder_images(session, card_id, payload)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(image_id: UUID, session: Session = Depends(get_session)):
    service.delete_image(session, image_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{card_id}/tags", status_code=status.HTTP_204_NO_CONTENT)
def assign_tag(card_id: UUID, payload: CardTagAssign, session: Session = Depends(get_session)):
    service.assign_tag(session, card_id, payload.tag_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{card_id}/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_tag(card_id: UUID, tag_id: UUID, session: Session = Depends(get_session)):
    service.remove_tag(session, card_id, tag_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
