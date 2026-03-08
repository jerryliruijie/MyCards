from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.integrations.pricing.registry import get_pricing_provider
from app.models.reference import PriceSource
from app.schemas.pricing import PriceSnapshotCreate, PriceSnapshotRead, PriceSourceRead
from app.services.pricing import PricingService

router = APIRouter()
service = PricingService()


@router.get("/sources", response_model=list[PriceSourceRead])
def list_sources(session: Session = Depends(get_session)):
    return service.list_sources(session)


@router.post("/snapshots", response_model=PriceSnapshotRead, status_code=status.HTTP_201_CREATED)
def create_snapshot(payload: PriceSnapshotCreate, session: Session = Depends(get_session)):
    return service.create_snapshot(session, payload)


@router.get("/snapshots/card/{card_id}", response_model=list[PriceSnapshotRead])
def list_card_snapshots(card_id: UUID, session: Session = Depends(get_session)):
    return service.list_card_snapshots(session, card_id)


@router.post("/refresh/card/{card_id}", response_model=PriceSnapshotRead)
def refresh_card_price(card_id: UUID, source_id: UUID, session: Session = Depends(get_session)):
    source = session.get(PriceSource, source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Price source not found")

    provider = get_pricing_provider(source.provider_key)
    provider_price = provider.fetch_price(card_id)
    payload = PriceSnapshotCreate(
        card_id=card_id,
        price_source_id=source.id,
        value=provider_price.value,
        currency=provider_price.currency,
        captured_at=provider_price.captured_at,
        confidence=provider_price.confidence,
        note=provider_price.note,
    )
    return service.create_snapshot(session, payload)
