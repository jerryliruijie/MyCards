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
        <h2 className="text-xl font-semibold">资产仪表盘</h2>
        <p className="text-sm text-slate-600">当前为 v1 线框版本，用于信息结构评审。</p>
      </header>

      <section className="grid gap-3 md:grid-cols-4">
        <div className="panel">
          <div className="text-sm text-slate-500">卡片总数</div>
          <div className="text-2xl font-bold">{summary.card_count}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">总成本</div>
          <div className="text-2xl font-bold">${summary.total_cost_basis.toFixed(2)}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">最新估值</div>
          <div className="text-2xl font-bold">${summary.total_latest_value.toFixed(2)}</div>
        </div>
        <div className="panel">
          <div className="text-sm text-slate-500">未实现盈亏</div>
          <div className={`text-2xl font-bold ${pnlClass}`}>
            ${summary.unrealized_pnl.toFixed(2)} ({summary.unrealized_pnl_pct.toFixed(2)}%)
          </div>
        </div>
      </section>

      <section className="grid gap-3 md:grid-cols-2">
        <div className="panel h-48">
          <h3 className="font-semibold">估值趋势（占位）</h3>
        </div>
        <div className="panel h-48">
          <h3 className="font-semibold">最近活动（占位）</h3>
        </div>
      </section>

      <section>
        <Link href="/cards" className="rounded bg-slate-800 px-3 py-2 text-sm text-white">
          打开卡片列表
        </Link>
      </section>
    </div>
  );
}
