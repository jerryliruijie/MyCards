import { Card, CardCore, CardImage, PortfolioSummary, StoragePosition } from "@/types/api";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const isFormData = init?.body instanceof FormData;
  const headers: Record<string, string> = {
    ...(init?.headers as Record<string, string> | undefined),
  };

  if (!isFormData) {
    headers["Content-Type"] = "application/json";
  }

  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers,
    cache: "no-store",
  });

  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`API error ${res.status}: ${detail}`);
  }

  if (res.status === 204) {
    return undefined as T;
  }

  return (await res.json()) as T;
}

export const api = {
  listCards: () => apiFetch<Card[]>("/cards"),
  listCardCores: () => apiFetch<CardCore[]>("/cards/core/list"),
  getCard: (id: string) => apiFetch<Card>(`/cards/${id}`),
  getCardCore: (id: string) => apiFetch<CardCore>(`/cards/${id}/core`),
  createCard: (payload: Record<string, unknown>) =>
    apiFetch<Card>("/cards", { method: "POST", body: JSON.stringify(payload) }),
  updateCard: (id: string, payload: Record<string, unknown>) =>
    apiFetch<Card>(`/cards/${id}`, { method: "PATCH", body: JSON.stringify(payload) }),
  listCardImages: (cardId: string) => apiFetch<CardImage[]>(`/cards/${cardId}/images`),
  addCardImage: (cardId: string, payload: Record<string, unknown>) =>
    apiFetch<CardImage>(`/cards/${cardId}/images`, { method: "POST", body: JSON.stringify(payload) }),
  uploadCardImage: (
    cardId: string,
    file: File,
    options?: {
      isPrimary?: boolean;
      sortOrder?: number;
    },
  ) => {
    const form = new FormData();
    form.append("file", file);
    const isPrimary = options?.isPrimary ?? true;
    const sortOrder = options?.sortOrder ?? 0;
    return apiFetch<CardImage>(
      `/cards/${cardId}/images/upload?is_primary=${isPrimary}&sort_order=${sortOrder}`,
      { method: "POST", body: form },
    );
  },
  setCardImagePrimary: (imageId: string) =>
    apiFetch<CardImage>("/cards/images/set-primary", {
      method: "PATCH",
      body: JSON.stringify({ image_id: imageId }),
    }),
  reorderCardImages: (cardId: string, imageIds: string[]) =>
    apiFetch<void>(`/cards/${cardId}/images/reorder`, {
      method: "PATCH",
      body: JSON.stringify({ image_ids: imageIds }),
    }),
  deleteCardImage: (imageId: string) => apiFetch<void>(`/cards/images/${imageId}`, { method: "DELETE" }),
  createPurchaseLot: (payload: Record<string, unknown>) =>
    apiFetch("/purchase-lots", { method: "POST", body: JSON.stringify(payload) }),
  createManualSnapshot: (payload: Record<string, unknown>) =>
    apiFetch("/pricing/manual-snapshots", { method: "POST", body: JSON.stringify(payload) }),
  summary: () => apiFetch<PortfolioSummary>("/portfolio/summary"),
  listStorage: () => apiFetch<StoragePosition[]>("/storage/positions?all_positions=true"),
};
