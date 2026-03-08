export type Card = {
  id: string;
  title: string;
  year?: number | null;
  card_number?: string | null;
  grade?: string | null;
  created_at: string;
  updated_at: string;
};

export type CardCore = {
  card_id: string;
  title: string;
  primary_image_key?: string | null;
  buy_price?: number | null;
  market_price?: number | null;
  currency: string;
};

export type PortfolioSummary = {
  card_count: number;
  total_cost_basis: number;
  total_latest_value: number;
  unrealized_pnl: number;
  unrealized_pnl_pct: number;
};

export type StoragePosition = {
  id: string;
  name: string;
  parent_id?: string | null;
  position_type?: string | null;
};
