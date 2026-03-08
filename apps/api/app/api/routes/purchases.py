from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.purchases import PurchaseLotCreate, PurchaseLotRead
from app.services.purchases import PurchaseService

router = APIRouter()
service = PurchaseService()


@router.post("", response_model=PurchaseLotRead, status_code=status.HTTP_201_CREATED)
def create_purchase_lot(payload: PurchaseLotCreate, session: Session = Depends(get_session)):
    return service.create(session, payload)


@router.get("/card/{card_id}", response_model=list[PurchaseLotRead])
def list_card_purchase_lots(card_id: UUID, session: Session = Depends(get_session)):
    return service.list_for_card(session, card_id)
