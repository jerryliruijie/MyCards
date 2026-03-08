from sqlmodel import Session, select

from app.models.reference import Tag


class TagRepository:
    def list_tags(self, session: Session) -> list[Tag]:
        return list(session.exec(select(Tag).order_by(Tag.name.asc())))

    def create_tag(self, session: Session, tag: Tag) -> Tag:
        session.add(tag)
        session.commit()
        session.refresh(tag)
        return tag
