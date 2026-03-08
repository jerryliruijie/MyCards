import Link from "next/link";

import { api } from "@/lib/api-client";

export default async function CardDetailPage({ params }: { params: { id: string } }) {
  const card = await api.getCard(params.id).catch(() => null);

  if (!card) {
    return <div className="panel">Card not found.</div>;
  }

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">{card.title}</h2>
        <p className="text-sm text-slate-600">Card detail wireframe (images, lots, pricing tabs next).</p>
      </header>

      <section className="grid gap-3 md:grid-cols-3">
        <div className="panel h-48">Image gallery placeholder</div>
        <div className="panel">
          <h3 className="mb-2 font-semibold">Metadata</h3>
          <dl className="grid grid-cols-2 gap-y-1 text-sm">
            <dt>Year</dt>
            <dd>{card.year ?? "-"}</dd>
            <dt>Card #</dt>
            <dd>{card.card_number ?? "-"}</dd>
            <dt>Grade</dt>
            <dd>{card.grade ?? "-"}</dd>
          </dl>
        </div>
        <div className="panel">
          <h3 className="mb-2 font-semibold">Valuation</h3>
          <p className="text-sm text-slate-600">Pricing summary panel placeholder</p>
        </div>
      </section>

      <Link href="/cards" className="text-sm text-blue-700 hover:underline">
        Back to cards
      </Link>
    </div>
  );
}
