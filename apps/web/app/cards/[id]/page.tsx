import Link from "next/link";

import { CardImageManager } from "@/components/card-image-manager";
import { api } from "@/lib/api-client";
import { resolveImageUrl } from "@/lib/media-url";

export default async function CardDetailPage({ params }: { params: { id: string } }) {
  const card = await api.getCard(params.id).catch(() => null);
  const core = await api.getCardCore(params.id).catch(() => null);
  const images = await api.listCardImages(params.id).catch(() => []);

  if (!card) {
    return <div className="panel">未找到该卡片。</div>;
  }

  const imageSrc = resolveImageUrl(core?.primary_image_key);

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">{card.title}</h2>
        <p className="text-sm text-slate-600">核心信息：标题、图片、买入价、当前市场价。</p>
      </header>

      <section className="grid gap-3 md:grid-cols-3">
        <div className="panel h-56">
          {imageSrc ? (
            <img src={imageSrc} alt={card.title} className="h-full w-full rounded object-cover" />
          ) : (
            <div className="flex h-full items-center justify-center text-sm text-slate-500">暂无图片</div>
          )}
        </div>

        <div className="panel">
          <h3 className="mb-2 font-semibold">基础信息</h3>
          <dl className="grid grid-cols-2 gap-y-1 text-sm">
            <dt>标题</dt>
            <dd>{card.title}</dd>
            <dt>年份</dt>
            <dd>{card.year ?? "-"}</dd>
            <dt>卡号</dt>
            <dd>{card.card_number ?? "-"}</dd>
            <dt>评级</dt>
            <dd>{card.grade ?? "-"}</dd>
          </dl>
        </div>

        <div className="panel">
          <h3 className="mb-2 font-semibold">价格信息</h3>
          <dl className="grid grid-cols-2 gap-y-1 text-sm">
            <dt>买入价</dt>
            <dd>{core?.buy_price != null ? `￥${core.buy_price.toFixed(2)}` : "-"}</dd>
            <dt>市场价</dt>
            <dd>{core?.market_price != null ? `￥${core.market_price.toFixed(2)}` : "-"}</dd>
          </dl>
        </div>
      </section>

      <CardImageManager cardId={card.id} initialImages={images} />

      <Link href="/cards" className="text-sm text-blue-700 hover:underline">
        返回卡片列表
      </Link>
    </div>
  );
}
