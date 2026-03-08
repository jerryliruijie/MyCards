import Link from "next/link";

import { api } from "@/lib/api-client";

export default async function CardsPage() {
  const cards = await api.listCards().catch(() => []);

  return (
    <div className="space-y-4">
      <header className="panel flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold">卡片库存</h2>
          <p className="text-sm text-slate-600">信息密集型列表，优先管理效率。</p>
        </div>
        <Link href="/cards/new" className="rounded bg-slate-800 px-3 py-2 text-sm text-white">
          新增卡片
        </Link>
      </header>

      <section className="panel">
        <div className="mb-3 grid gap-2 md:grid-cols-5">
          <input className="rounded border p-2 text-sm" placeholder="搜索标题" disabled />
          <input className="rounded border p-2 text-sm" placeholder="运动类型" disabled />
          <input className="rounded border p-2 text-sm" placeholder="球员" disabled />
          <input className="rounded border p-2 text-sm" placeholder="系列" disabled />
          <input className="rounded border p-2 text-sm" placeholder="标签" disabled />
        </div>

        <table className="table">
          <thead>
            <tr>
              <th>标题</th>
              <th>年份</th>
              <th>卡号</th>
              <th>评级</th>
              <th>更新时间</th>
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
                  暂无卡片数据。
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </section>
    </div>
  );
}
