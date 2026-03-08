import { Card, PortfolioSummary, StoragePosition } from "@/types/api";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers || {}),
    },
    cache: "no-store",
  });

  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`API error ${res.status}: ${detail}`);
  }

  return (await res.json()) as T;
}

export const api = {
  listCards: () => apiFetch<Card[]>("/cards"),
  getCard: (id: string) => apiFetch<Card>(`/cards/${id}`),
  createCard: (payload: Record<string, unknown>) =>
    apiFetch<Card>("/cards", { method: "POST", body: JSON.stringify(payload) }),
  updateCard: (id: string, payload: Record<string, unknown>) =>
    apiFetch<Card>(`/cards/${id}`, { method: "PATCH", body: JSON.stringify(payload) }),
  summary: () => apiFetch<PortfolioSummary>("/portfolio/summary"),
  listStorage: () => apiFetch<StoragePosition[]>("/storage/positions?all_positions=true"),
};
