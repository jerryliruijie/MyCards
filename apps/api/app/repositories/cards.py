from datetime import datetime, timezone
from typing import Iterable, Optional
from uuid import UUID

from sqlmodel import Session, desc, select

from app.models.card import Card, CardImage, CardTag
from app.models.pricing import PriceSnapshot
from app.models.transactions import PurchaseLot


class CardRepository:
    def list_cards(
        self,
        session: Session,
        q: Optional[str] = None,
        sport_id: Optional[UUID] = None,
        player_id: Optional[UUID] = None,
        tag_id: Optional[UUID] = None,
    ) -> list[Card]:
        stmt = select(Card)
        if q:
            stmt = stmt.where(Card.title.ilike(f"%{q}%"))
        if sport_id:
            stmt = stmt.where(Card.sport_id == sport_id)
        if player_id:
            stmt = stmt.where(Card.player_id == player_id)
        if tag_id:
            stmt = stmt.join(CardTag, CardTag.card_id == Card.id).where(CardTag.tag_id == tag_id)
        stmt = stmt.order_by(desc(Card.updated_at))
        return list(session.exec(stmt))

    def get_card(self, session: Session, card_id: UUID) -> Optional[Card]:
        return session.get(Card, card_id)

    def create_card(self, session: Session, card: Card) -> Card:
        session.add(card)
        session.commit()
        session.refresh(card)
        return card

    def update_card(self, session: Session, card: Card, data: dict) -> Card:
        for key, value in data.items():
            setattr(card, key, value)
        card.updated_at = datetime.now(timezone.utc)
        session.add(card)
        session.commit()
        session.refresh(card)
        return card

    def delete_card(self, session: Session, card: Card) -> None:
        session.delete(card)
        session.commit()

    def list_images(self, session: Session, card_id: UUID) -> list[CardImage]:
        stmt = (
            select(CardImage)
            .where(CardImage.card_id == card_id)
            .order_by(CardImage.is_primary.desc(), CardImage.sort_order.asc())
        )
        return list(session.exec(stmt))

    def get_primary_image(self, session: Session, card_id: UUID) -> CardImage | None:
        stmt = (
            select(CardImage)
            .where(CardImage.card_id == card_id)
            .order_by(CardImage.is_primary.desc(), CardImage.sort_order.asc())
            .limit(1)
        )
        return session.exec(stmt).first()

    def add_image(self, session: Session, image: CardImage) -> CardImage:
        if image.is_primary:
            self.clear_primary_images(session, image.card_id)
        session.add(image)
        session.commit()
        session.refresh(image)
        return image

    def clear_primary_images(self, session: Session, card_id: UUID) -> None:
        for image in self.list_images(session, card_id):
            if image.is_primary:
                image.is_primary = False
                session.add(image)

    def delete_image(self, session: Session, image_id: UUID) -> bool:
        image = session.get(CardImage, image_id)
        if not image:
            return False
        session.delete(image)
        session.commit()
        return True

    def assign_tag(self, session: Session, card_id: UUID, tag_id: UUID) -> CardTag:
        existing = session.get(CardTag, (card_id, tag_id))
        if existing:
            return existing
        rel = CardTag(card_id=card_id, tag_id=tag_id)
        session.add(rel)
        session.commit()
        return rel

    def remove_tag(self, session: Session, card_id: UUID, tag_id: UUID) -> bool:
        rel = session.get(CardTag, (card_id, tag_id))
        if not rel:
            return False
        session.delete(rel)
        session.commit()
        return True

    def list_card_ids(self, session: Session) -> Iterable[UUID]:
        stmt = select(Card.id)
        return list(session.exec(stmt))

    def latest_purchase_lot(self, session: Session, card_id: UUID) -> PurchaseLot | None:
        stmt = (
            select(PurchaseLot)
            .where(PurchaseLot.card_id == card_id)
            .order_by(desc(PurchaseLot.purchased_at))
            .limit(1)
        )
        return session.exec(stmt).first()

    def latest_price_snapshot(self, session: Session, card_id: UUID) -> PriceSnapshot | None:
        stmt = (
            select(PriceSnapshot)
            .where(PriceSnapshot.card_id == card_id)
            .order_by(desc(PriceSnapshot.captured_at))
            .limit(1)
        )
        return session.exec(stmt).first()
