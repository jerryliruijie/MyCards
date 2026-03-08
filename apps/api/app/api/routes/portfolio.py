from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.portfolio import PortfolioSummary
from app.services.portfolio import PortfolioService

router = APIRouter()
service = PortfolioService()


@router.get("/summary", response_model=PortfolioSummary)
def get_summary(session: Session = Depends(get_session)):
    totals = service.summarize(session)
    return PortfolioSummary(**totals.__dict__)
