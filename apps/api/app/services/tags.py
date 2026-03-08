from sqlmodel import Session

from app.models.reference import Tag
from app.repositories.tags import TagRepository
from app.schemas.tags import TagCreate


class TagService:
    def __init__(self, repo: TagRepository | None = None) -> None:
        self.repo = repo or TagRepository()

    def list_tags(self, session: Session):
        return self.repo.list_tags(session)

    def create_tag(self, session: Session, payload: TagCreate) -> Tag:
        tag = Tag(**payload.model_dump())
        return self.repo.create_tag(session, tag)
