import Link from "next/link";

import { api } from "@/lib/api-client";

export default async function CardsPage() {
  const cards = await api.listCards().catch(() => []);

  return (
    <div className="space-y-4">
      <header className="panel flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold">Card Inventory</h2>
          <p className="text-sm text-slate-600">Information-dense list optimized for management.</p>
        </div>
        <Link href="/cards/new" className="rounded bg-slate-800 px-3 py-2 text-sm text-white">
          Add card
        </Link>
      </header>

      <section className="panel">
        <div className="mb-3 grid gap-2 md:grid-cols-5">
          <input className="rounded border p-2 text-sm" placeholder="Search title" disabled />
          <input className="rounded border p-2 text-sm" placeholder="Sport" disabled />
          <input className="rounded border p-2 text-sm" placeholder="Player" disabled />
          <input className="rounded border p-2 text-sm" placeholder="Set" disabled />
          <input className="rounded border p-2 text-sm" placeholder="Tag" disabled />
        </div>

        <table className="table">
          <thead>
            <tr>
              <th>Title</th>
              <th>Year</th>
              <th>Card #</th>
              <th>Grade</th>
              <th>Updated</th>
            </tr>
          </thead>
          <tbody>
            {cards.map((card) => (
              <tr key={card.id}>
                <td>
                  <Link className="text-blue-700 hover:underline" href={`/cards/${card.id}`}>
                    {card.title}
                  </Link>
                </td>
                <td>{card.year ?? "-"}</td>
                <td>{card.card_number ?? "-"}</td>
                <td>{card.grade ?? "-"}</td>
                <td>{new Date(card.updated_at).toLocaleDateString()}</td>
              </tr>
            ))}
            {cards.length === 0 && (
              <tr>
                <td colSpan={5} className="text-slate-500">
                  No cards yet.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </section>
    </div>
  );
}
