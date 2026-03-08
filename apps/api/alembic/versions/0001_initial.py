"""initial schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-03-08 10:00:00.000000
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("display_name", sa.String(length=120), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
    )
    op.create_index("ix_user_email", "user", ["email"], unique=True)

    for table_name, cols in [
        ("sport", [sa.Column("name", sa.String(length=120), nullable=False)]),
        ("brand", [sa.Column("name", sa.String(length=120), nullable=False)]),
        ("cardtype", [sa.Column("name", sa.String(length=120), nullable=False)]),
        ("gradingcompany", [sa.Column("name", sa.String(length=120), nullable=False)]),
        ("tag", [sa.Column("name", sa.String(length=120), nullable=False), sa.Column("color", sa.String(length=16))]),
    ]:
        op.create_table(
            table_name,
            sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
            sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
            *cols,
        )
        op.create_index(f"ix_{table_name}_name", table_name, ["name"], unique=True)

    op.create_table(
        "pricesource",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("provider_key", sa.String(length=120), nullable=False),
        sa.Column("is_enabled", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
    )
    op.create_index("ix_pricesource_name", "pricesource", ["name"], unique=True)

    op.create_table(
        "team",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("sport_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("sport.id"), nullable=True),
    )
    op.create_table(
        "player",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("full_name", sa.String(length=200), nullable=False),
        sa.Column("sport_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("sport.id"), nullable=True),
        sa.Column("team_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("team.id"), nullable=True),
    )
    op.create_table(
        "cardset",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("brand_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brand.id"), nullable=True),
        sa.Column("release_year", sa.Integer(), nullable=True),
    )
    op.create_table(
        "card",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("sport_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("sport.id"), nullable=True),
        sa.Column("team_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("team.id"), nullable=True),
        sa.Column("player_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("player.id"), nullable=True),
        sa.Column("brand_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brand.id"), nullable=True),
        sa.Column("set_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cardset.id"), nullable=True),
        sa.Column("card_type_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cardtype.id"), nullable=True),
        sa.Column(
            "grading_company_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("gradingcompany.id"),
            nullable=True,
        ),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("card_number", sa.String(length=50), nullable=True),
        sa.Column("parallel", sa.String(length=120), nullable=True),
        sa.Column("grade", sa.String(length=32), nullable=True),
        sa.Column("serial_number", sa.String(length=120), nullable=True),
        sa.Column("condition_notes", sa.Text(), nullable=True),
    )
    op.create_index("ix_card_title", "card", ["title"])
    op.create_index("ix_card_filter", "card", ["user_id", "sport_id", "player_id", "set_id", "card_type_id"])

    op.create_table(
        "cardimage",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column("storage_key", sa.String(length=500), nullable=False),
        sa.Column("content_type", sa.String(length=120), nullable=True),
        sa.Column("is_primary", sa.Boolean(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
    )

    op.create_table(
        "storageposition",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=True),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column(
            "parent_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("storageposition.id"), nullable=True
        ),
        sa.Column("position_type", sa.String(length=80), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
    )

    op.create_table(
        "cardstorageassignment",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column(
            "storage_position_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("storageposition.id"),
            nullable=False,
        ),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("assigned_at", sa.DateTime(timezone=False), nullable=False),
    )

    op.create_table(
        "purchaselot",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column("purchased_at", sa.DateTime(timezone=False), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Float(), nullable=False),
        sa.Column("fees", sa.Float(), nullable=False),
        sa.Column("tax", sa.Float(), nullable=False),
        sa.Column("shipping", sa.Float(), nullable=False),
        sa.Column("seller", sa.String(length=200), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
    )
    op.create_index("ix_purchaselot_card_purchased", "purchaselot", ["card_id", "purchased_at"])

    op.create_table(
        "salelot",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column("sold_at", sa.DateTime(timezone=False), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Float(), nullable=False),
        sa.Column("fees", sa.Float(), nullable=False),
        sa.Column("buyer", sa.String(length=200), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
    )

    op.create_table(
        "pricesnapshot",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column("price_source_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("pricesource.id"), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("currency", sa.String(length=8), nullable=False),
        sa.Column("captured_at", sa.DateTime(timezone=False), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
    )
    op.create_index("ix_pricesnapshot_card_captured", "pricesnapshot", ["card_id", "captured_at"])

    op.create_table(
        "manualvaluation",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("currency", sa.String(length=8), nullable=False),
        sa.Column("valued_at", sa.DateTime(timezone=False), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
    )

    op.create_table(
        "cardtag",
        sa.Column("card_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("card.id"), primary_key=True),
        sa.Column("tag_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("tag.id"), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=False), nullable=False),
    )
    op.create_index("ix_cardtag_tag_card", "cardtag", ["tag_id", "card_id"])


def downgrade() -> None:
    for table in [
        "cardtag",
        "manualvaluation",
        "pricesnapshot",
        "salelot",
        "purchaselot",
        "cardstorageassignment",
        "storageposition",
        "cardimage",
        "card",
        "cardset",
        "player",
        "team",
        "pricesource",
        "tag",
        "gradingcompany",
        "cardtype",
        "brand",
        "sport",
        "user",
    ]:
        op.drop_table(table)
