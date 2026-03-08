from datetime import datetime, timedelta, timezone

from sqlmodel import Session, SQLModel, select

import app.models  # noqa: F401
from app.db.session import engine
from app.models.card import Card, CardImage, CardTag, ManualValuation
from app.models.pricing import PriceSnapshot
from app.models.reference import (
    Brand,
    CardSet,
    CardType,
    GradingCompany,
    Player,
    PriceSource,
    Sport,
    Tag,
    Team,
    User,
)
from app.models.storage import CardStorageAssignment, StoragePosition
from app.models.transactions import PurchaseLot


def get_or_create(session: Session, model, **kwargs):
    statement = select(model)
    for key, value in kwargs.items():
        statement = statement.where(getattr(model, key) == value)
    instance = session.exec(statement).first()
    if instance:
        return instance
    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def seed() -> None:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = get_or_create(session, User, email="owner@mycards.local", display_name="Owner")

        baseball = get_or_create(session, Sport, name="Baseball")
        basketball = get_or_create(session, Sport, name="Basketball")

        yankees = get_or_create(session, Team, name="New York Yankees", sport_id=baseball.id)
        lakers = get_or_create(session, Team, name="Los Angeles Lakers", sport_id=basketball.id)

        judge = get_or_create(
            session,
            Player,
            full_name="Aaron Judge",
            sport_id=baseball.id,
            team_id=yankees.id,
        )
        lebron = get_or_create(
            session,
            Player,
            full_name="LeBron James",
            sport_id=basketball.id,
            team_id=lakers.id,
        )

        topps = get_or_create(session, Brand, name="Topps")
        panini = get_or_create(session, Brand, name="Panini")

        topps_2023 = get_or_create(
            session,
            CardSet,
            name="Topps Series 1",
            brand_id=topps.id,
            release_year=2023,
        )
        prizm_2021 = get_or_create(
            session,
            CardSet,
            name="Prizm",
            brand_id=panini.id,
            release_year=2021,
        )

        base = get_or_create(session, CardType, name="Base")
        rookie = get_or_create(session, CardType, name="Rookie")

        psa = get_or_create(session, GradingCompany, name="PSA")

        manual_source = get_or_create(
            session,
            PriceSource,
            name="Manual Entry",
            provider_key="mock-pricing",
            notes="Used for manual and mock refresh workflows",
        )

        tag_pc = get_or_create(session, Tag, name="PC", color="#2563EB")
        get_or_create(session, Tag, name="Long-term", color="#16A34A")

        card1 = get_or_create(
            session,
            Card,
            title="Aaron Judge 2023 Topps Series 1 #99",
            user_id=user.id,
            sport_id=baseball.id,
            team_id=yankees.id,
            player_id=judge.id,
            brand_id=topps.id,
            set_id=topps_2023.id,
            card_type_id=base.id,
            year=2023,
            card_number="99",
            grading_company_id=psa.id,
            grade="PSA 10",
        )

        card2 = get_or_create(
            session,
            Card,
            title="LeBron James 2021 Prizm #1",
            user_id=user.id,
            sport_id=basketball.id,
            team_id=lakers.id,
            player_id=lebron.id,
            brand_id=panini.id,
            set_id=prizm_2021.id,
            card_type_id=rookie.id,
            year=2021,
            card_number="1",
        )

        get_or_create(
            session,
            CardImage,
            card_id=card1.id,
            storage_key="images/cards/aaron-judge-front.jpg",
            content_type="image/jpeg",
            is_primary=True,
            sort_order=0,
        )

        get_or_create(
            session,
            PurchaseLot,
            card_id=card1.id,
            purchased_at=datetime.now(timezone.utc) - timedelta(days=120),
            quantity=1,
            unit_price=95,
            fees=2,
            shipping=4,
            tax=3,
            seller="Card Show",
        )
        get_or_create(
            session,
            PurchaseLot,
            card_id=card2.id,
            purchased_at=datetime.now(timezone.utc) - timedelta(days=40),
            quantity=1,
            unit_price=180,
            fees=5,
            shipping=5,
            tax=6,
            seller="eBay",
        )

        shelf = get_or_create(session, StoragePosition, name="Office Shelf", user_id=user.id)
        box_a = get_or_create(
            session,
            StoragePosition,
            name="Box A",
            parent_id=shelf.id,
            user_id=user.id,
        )

        get_or_create(
            session,
            CardStorageAssignment,
            card_id=card1.id,
            storage_position_id=box_a.id,
            quantity=1,
        )

        get_or_create(
            session,
            ManualValuation,
            card_id=card1.id,
            value=140,
            currency="USD",
            valued_at=datetime.now(timezone.utc) - timedelta(days=5),
            note="Recent comp check",
        )

        get_or_create(
            session,
            PriceSnapshot,
            card_id=card1.id,
            price_source_id=manual_source.id,
            value=145,
            currency="USD",
            captured_at=datetime.now(timezone.utc) - timedelta(days=1),
            confidence=0.82,
            note="Mock reference",
        )

        get_or_create(session, CardTag, card_id=card1.id, tag_id=tag_pc.id)

        session.commit()


if __name__ == "__main__":
    seed()
    print("Seed complete")
