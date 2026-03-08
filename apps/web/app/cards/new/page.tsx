"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

export default function NewCardPage() {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [year, setYear] = useState("");
  const [cardNumber, setCardNumber] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);

    const res = await fetch(`${API_BASE_URL}/cards`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        year: year ? Number(year) : null,
        card_number: cardNumber || null,
      }),
    });

    if (!res.ok) {
      setError(`Could not create card (${res.status})`);
      return;
    }

    const card = await res.json();
    router.push(`/cards/${card.id}`);
  }

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">Add Card</h2>
        <p className="text-sm text-slate-600">Structured metadata first, optional fields later.</p>
      </header>

      <form className="panel max-w-xl space-y-3" onSubmit={onSubmit}>
        <div>
          <label className="mb-1 block text-sm font-medium">Title</label>
          <input
            required
            className="w-full rounded border p-2 text-sm"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="2023 Topps Series 1 Aaron Judge #99"
          />
        </div>
        <div>
          <label className="mb-1 block text-sm font-medium">Year</label>
          <input
            type="number"
            className="w-full rounded border p-2 text-sm"
            value={year}
            onChange={(e) => setYear(e.target.value)}
          />
        </div>
        <div>
          <label className="mb-1 block text-sm font-medium">Card Number</label>
          <input
            className="w-full rounded border p-2 text-sm"
            value={cardNumber}
            onChange={(e) => setCardNumber(e.target.value)}
          />
        </div>

        {error && <div className="text-sm text-red-700">{error}</div>}

        <button className="rounded bg-slate-800 px-3 py-2 text-sm text-white" type="submit">
          Create card
        </button>
      </form>
    </div>
  );
}
