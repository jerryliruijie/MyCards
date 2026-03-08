from typing import Optional
from uuid import UUID

from sqlmodel import Session, select

from app.models.storage import CardStorageAssignment, StoragePosition


class StorageRepository:
    def list_positions(self, session: Session, parent_id: Optional[UUID] = None) -> list[StoragePosition]:
        stmt = select(StoragePosition)
        if parent_id is None:
            stmt = stmt.where(StoragePosition.parent_id.is_(None))
        else:
            stmt = stmt.where(StoragePosition.parent_id == parent_id)
        stmt = stmt.order_by(StoragePosition.name.asc())
        return list(session.exec(stmt))

    def list_all_positions(self, session: Session) -> list[StoragePosition]:
        return list(session.exec(select(StoragePosition).order_by(StoragePosition.name.asc())))

    def create_position(self, session: Session, position: StoragePosition) -> StoragePosition:
        session.add(position)
        session.commit()
        session.refresh(position)
        return position

    def assign_card(self, session: Session, assignment: CardStorageAssignment) -> CardStorageAssignment:
        session.add(assignment)
        session.commit()
        session.refresh(assignment)
        return assignment

    def list_assignments_for_position(
        self, session: Session, position_id: UUID
    ) -> list[CardStorageAssignment]:
        stmt = select(CardStorageAssignment).where(CardStorageAssignment.storage_position_id == position_id)
        return list(session.exec(stmt))
