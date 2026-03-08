from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.tags import TagCreate, TagRead
from app.services.tags import TagService

router = APIRouter()
service = TagService()


@router.get("", response_model=list[TagRead])
def list_tags(session: Session = Depends(get_session)):
    return service.list_tags(session)


@router.post("", response_model=TagRead, status_code=status.HTTP_201_CREATED)
def create_tag(payload: TagCreate, session: Session = Depends(get_session)):
    return service.create_tag(session, payload)
