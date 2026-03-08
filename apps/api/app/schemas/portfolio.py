from pydantic import BaseModel


class PortfolioSummary(BaseModel):
    card_count: int
    total_cost_basis: float
    total_latest_value: float
    unrealized_pnl: float
    unrealized_pnl_pct: float
