import Link from "next/link";

import { api } from "@/lib/api-client";
import { resolveImageUrl } from "@/lib/media-url";

export default async function CardsPage() {
  const cards = await api.listCards().catch(() => []);
  const cores = await api.listCardCores().catch(() => []);
  const coreMap = new Map(cores.map((c) => [c.card_id, c]));

  return (
    <div className="space-y-4">
      <header className="panel flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold">卡片库存</h2>
          <p className="text-sm text-slate-600">核心信息：标题、图片、买入价、当前市场价。</p>
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
              <th>图片</th>
              <th>标题</th>
              <th>买入价</th>
              <th>市场价</th>
              <th>更新时间</th>
            </tr>
          </thead>
          <tbody>
            {cards.map((card) => {
              const core = coreMap.get(card.id);
              const imageSrc = resolveImageUrl(core?.primary_image_key);
              return (
                <tr key={card.id}>
                  <td>
                    {imageSrc ? (
                      <img
                        src={imageSrc}
                        alt={card.title}
                        className="h-12 w-12 rounded border object-cover"
                      />
                    ) : (
                      <div className="h-12 w-12 rounded border bg-slate-100" />
                    )}
                  </td>
                  <td>
                    <Link className="text-blue-700 hover:underline" href={`/cards/${card.id}`}>
                      {card.title}
                    </Link>
                  </td>
                  <td>{core?.buy_price != null ? `¥${core.buy_price.toFixed(2)}` : "-"}</td>
                  <td>{core?.market_price != null ? `¥${core.market_price.toFixed(2)}` : "-"}</td>
                  <td>{new Date(card.updated_at).toLocaleDateString()}</td>
                </tr>
              );
            })}
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
