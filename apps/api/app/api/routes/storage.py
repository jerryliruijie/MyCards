from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.storage import (
    CardStorageAssignmentCreate,
    CardStorageAssignmentRead,
    StoragePositionCreate,
    StoragePositionRead,
)
from app.services.storage import StorageService

router = APIRouter()
service = StorageService()


@router.get("/positions", response_model=list[StoragePositionRead])
def list_positions(
    parent_id: Optional[UUID] = None,
    all_positions: bool = False,
    session: Session = Depends(get_session),
):
    if all_positions:
        return service.list_positions(session, parent_id="all")
    return service.list_positions(session, parent_id=parent_id)


@router.post("/positions", response_model=StoragePositionRead, status_code=status.HTTP_201_CREATED)
def create_position(payload: StoragePositionCreate, session: Session = Depends(get_session)):
    return service.create_position(session, payload)


@router.post(
    "/assignments", response_model=CardStorageAssignmentRead, status_code=status.HTTP_201_CREATED
)
def assign_card(payload: CardStorageAssignmentCreate, session: Session = Depends(get_session)):
    return service.assign_card(session, payload)


@router.get("/positions/{position_id}/assignments", response_model=list[CardStorageAssignmentRead])
def list_position_assignments(position_id: UUID, session: Session = Depends(get_session)):
    return service.list_assignments_for_position(session, position_id)
