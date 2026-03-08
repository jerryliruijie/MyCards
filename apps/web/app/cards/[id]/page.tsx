import Link from "next/link";

import { api } from "@/lib/api-client";

export default async function CardDetailPage({ params }: { params: { id: string } }) {
  const card = await api.getCard(params.id).catch(() => null);

  if (!card) {
    return <div className="panel">未找到该卡片。</div>;
  }

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">{card.title}</h2>
        <p className="text-sm text-slate-600">卡片详情线框（后续补充图片、购入批次、价格历史等）。</p>
      </header>

      <section className="grid gap-3 md:grid-cols-3">
        <div className="panel h-48">图片区域（占位）</div>
        <div className="panel">
          <h3 className="mb-2 font-semibold">元数据</h3>
          <dl className="grid grid-cols-2 gap-y-1 text-sm">
            <dt>年份</dt>
            <dd>{card.year ?? "-"}</dd>
            <dt>卡号</dt>
            <dd>{card.card_number ?? "-"}</dd>
            <dt>评级</dt>
            <dd>{card.grade ?? "-"}</dd>
          </dl>
        </div>
        <div className="panel">
          <h3 className="mb-2 font-semibold">估值</h3>
          <p className="text-sm text-slate-600">估值摘要区域（占位）</p>
        </div>
      </section>

      <Link href="/cards" className="text-sm text-blue-700 hover:underline">
        返回卡片列表
      </Link>
    </div>
  );
}
