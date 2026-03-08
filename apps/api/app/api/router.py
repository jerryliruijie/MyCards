from fastapi import APIRouter

from app.api.routes import cards, portfolio, pricing, purchases, storage, tags

api_router = APIRouter()
api_router.include_router(cards.router, prefix="/cards", tags=["cards"])
api_router.include_router(purchases.router, prefix="/purchase-lots", tags=["purchase-lots"])
api_router.include_router(storage.router, prefix="/storage", tags=["storage"])
api_router.include_router(pricing.router, prefix="/pricing", tags=["pricing"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
