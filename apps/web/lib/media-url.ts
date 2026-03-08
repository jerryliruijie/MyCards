const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

function apiOrigin(): string {
  try {
    return new URL(API_BASE_URL).origin;
  } catch {
    return "http://localhost:8000";
  }
}

export function resolveImageUrl(storageKey?: string | null): string | null {
  if (!storageKey) return null;
  if (storageKey.startsWith("http://") || storageKey.startsWith("https://")) return storageKey;
  if (storageKey.startsWith("/media/")) return `${apiOrigin()}${storageKey}`;
  return storageKey;
}
