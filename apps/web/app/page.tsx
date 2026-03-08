import Link from "next/link";

import { api } from "@/lib/api-client";

export default async function DashboardPage() {
  let summary = null;
  try {
    summary = await api.summary();
  } catch {
    summary = {
      card_count: 0,
      total_cost_basis: 0,
      total_latest_value: 0,
      unrealized_pnl: 0,
      unrealized_pnl_pct: 0,
    };
  }

  const pnlClass = summary.unrealized_pnl >= 0 ? "text-gain" : "text-loss";

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">Portfolio Dashboard</h2>
        <p className="text-sm text-slate-600">Wireframe-level v1 dashboard for review.</p>
      </header>

      <section className="grid gap-3 md:grid-cols-4">
        <div className="panel">
          <div className="text-sm text-slate-500">Cards</div>
          <div className="text-2xl font-bold">{summary.card_count}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">Cost Basis</div>
          <div className="text-2xl font-bold">${summary.total_cost_basis.toFixed(2)}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">Latest Value</div>
          <div className="text-2xl font-bold">${summary.total_latest_value.toFixed(2)}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">Unrealized PnL</div>
          <div className={`text-2xl font-bold ${pnlClass}`}>
            ${summary.unrealized_pnl.toFixed(2)} ({summary.unrealized_pnl_pct.toFixed(2)}%)
          </div>
        </div>
      </section>

      <section className="grid gap-3 md:grid-cols-2">
        <div className="panel h-48">
          <h3 className="font-semibold">Valuation Trend (Placeholder)</h3>
        </div>
        <div className="panel h-48">
          <h3 className="font-semibold">Recent Activity (Placeholder)</h3>
        </div>
      </section>

      <section>
        <Link href="/cards" className="rounded bg-slate-800 px-3 py-2 text-sm text-white">
          Open card list
        </Link>
      </section>
    </div>
  );
}
