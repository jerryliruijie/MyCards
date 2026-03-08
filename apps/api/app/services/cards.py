from uuid import UUID

from fastapi import HTTPException
from sqlmodel import Session

from app.models.card import Card, CardImage
from app.repositories.cards import CardRepository
from app.schemas.cards import CardCoreRead, CardCreate, CardImageCreate, CardUpdate


class CardService:
    def __init__(self, repo: CardRepository | None = None) -> None:
        self.repo = repo or CardRepository()

    def list_cards(self, session: Session, **filters):
        return self.repo.list_cards(session, **filters)

    def get_card_or_404(self, session: Session, card_id: UUID) -> Card:
        card = self.repo.get_card(session, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def create_card(self, session: Session, payload: CardCreate) -> Card:
        card = Card(**payload.model_dump())
        return self.repo.create_card(session, card)

    def update_card(self, session: Session, card_id: UUID, payload: CardUpdate) -> Card:
        card = self.get_card_or_404(session, card_id)
        updates = payload.model_dump(exclude_unset=True)
        return self.repo.update_card(session, card, updates)

    def delete_card(self, session: Session, card_id: UUID) -> None:
        card = self.get_card_or_404(session, card_id)
        self.repo.delete_card(session, card)

    def list_images(self, session: Session, card_id: UUID):
        self.get_card_or_404(session, card_id)
        return self.repo.list_images(session, card_id)

    def add_image(self, session: Session, card_id: UUID, payload: CardImageCreate):
        self.get_card_or_404(session, card_id)
        image = CardImage(card_id=card_id, **payload.model_dump())
        return self.repo.add_image(session, image)

    def delete_image(self, session: Session, image_id: UUID) -> None:
        if not self.repo.delete_image(session, image_id):
            raise HTTPException(status_code=404, detail="Card image not found")

    def assign_tag(self, session: Session, card_id: UUID, tag_id: UUID) -> None:
        self.get_card_or_404(session, card_id)
        self.repo.assign_tag(session, card_id, tag_id)

    def remove_tag(self, session: Session, card_id: UUID, tag_id: UUID) -> None:
        self.get_card_or_404(session, card_id)
        if not self.repo.remove_tag(session, card_id, tag_id):
            raise HTTPException(status_code=404, detail="Card tag assignment not found")

    def get_card_core(self, session: Session, card_id: UUID) -> CardCoreRead:
        card = self.get_card_or_404(session, card_id)
        image = self.repo.get_primary_image(session, card_id)
        lot = self.repo.latest_purchase_lot(session, card_id)
        snap = self.repo.latest_price_snapshot(session, card_id)

        return CardCoreRead(
            card_id=card.id,
            title=card.title,
            primary_image_key=image.storage_key if image else None,
            buy_price=lot.unit_price if lot else None,
            market_price=snap.value if snap else None,
            currency=snap.currency if snap else "CNY",
        )

    def list_card_cores(self, session: Session) -> list[CardCoreRead]:
        cards = self.repo.list_cards(session)
        return [self.get_card_core(session, card.id) for card in cards]

