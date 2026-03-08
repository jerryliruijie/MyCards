from sqlmodel import Session

from app.models.storage import CardStorageAssignment, StoragePosition
from app.repositories.storage import StorageRepository
from app.schemas.storage import CardStorageAssignmentCreate, StoragePositionCreate


class StorageService:
    def __init__(self, repo: StorageRepository | None = None) -> None:
        self.repo = repo or StorageRepository()

    def list_positions(self, session: Session, parent_id=None):
        if parent_id == "all":
            return self.repo.list_all_positions(session)
        return self.repo.list_positions(session, parent_id)

    def create_position(self, session: Session, payload: StoragePositionCreate) -> StoragePosition:
        position = StoragePosition(**payload.model_dump())
        return self.repo.create_position(session, position)

    def assign_card(
        self, session: Session, payload: CardStorageAssignmentCreate
    ) -> CardStorageAssignment:
        assignment = CardStorageAssignment(**payload.model_dump())
        return self.repo.assign_card(session, assignment)

    def list_assignments_for_position(self, session: Session, position_id):
        return self.repo.list_assignments_for_position(session, position_id)
