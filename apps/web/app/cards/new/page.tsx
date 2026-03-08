"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

import { api } from "@/lib/api-client";

export default function NewCardPage() {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [year, setYear] = useState("");
  const [cardNumber, setCardNumber] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [buyPrice, setBuyPrice] = useState("");
  const [marketPrice, setMarketPrice] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);

    try {
      const card = await api.createCard({
        title,
        year: year ? Number(year) : null,
        card_number: cardNumber || null,
      });

      if (imageUrl.trim()) {
        await api.addCardImage(card.id, {
          storage_key: imageUrl.trim(),
          content_type: "image/url",
          is_primary: true,
          sort_order: 0,
        });
      }

      if (buyPrice && Number(buyPrice) > 0) {
        await api.createPurchaseLot({
          card_id: card.id,
          purchased_at: new Date().toISOString(),
          quantity: 1,
          unit_price: Number(buyPrice),
          fees: 0,
          tax: 0,
          shipping: 0,
          seller: "手动录入",
        });
      }

      if (marketPrice && Number(marketPrice) > 0) {
        await api.createManualSnapshot({
          card_id: card.id,
          value: Number(marketPrice),
          currency: "USD",
          captured_at: new Date().toISOString(),
          note: "手动录入市场价",
        });
      }

      router.push(`/cards/${card.id}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : "创建失败，请稍后重试");
    }
  }

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">新增卡片</h2>
        <p className="text-sm text-slate-600">核心信息：标题、图片、买入价、当前市场价（手动）。</p>
      </header>

      <form className="panel max-w-xl space-y-3" onSubmit={onSubmit}>
        <div>
          <label className="mb-1 block text-sm font-medium">标题（自定义）</label>
          <input
            required
            className="w-full rounded border p-2 text-sm"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="例如：2023 Topps Series 1 #99"
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium">图片 URL</label>
          <input
            className="w-full rounded border p-2 text-sm"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="https://..."
          />
        </div>

        <div className="grid gap-3 md:grid-cols-2">
          <div>
            <label className="mb-1 block text-sm font-medium">买入价格（USD）</label>
            <input
              type="number"
              step="0.01"
              className="w-full rounded border p-2 text-sm"
              value={buyPrice}
              onChange={(e) => setBuyPrice(e.target.value)}
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium">当前市场价（USD，手动）</label>
            <input
              type="number"
              step="0.01"
              className="w-full rounded border p-2 text-sm"
              value={marketPrice}
              onChange={(e) => setMarketPrice(e.target.value)}
            />
          </div>
        </div>

        <div className="grid gap-3 md:grid-cols-2">
          <div>
            <label className="mb-1 block text-sm font-medium">年份</label>
            <input
              type="number"
              className="w-full rounded border p-2 text-sm"
              value={year}
              onChange={(e) => setYear(e.target.value)}
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium">卡号</label>
            <input
              className="w-full rounded border p-2 text-sm"
              value={cardNumber}
              onChange={(e) => setCardNumber(e.target.value)}
            />
          </div>
        </div>

        {error && <div className="text-sm text-red-700">{error}</div>}

        <button className="rounded bg-slate-800 px-3 py-2 text-sm text-white" type="submit">
          创建卡片
        </button>
      </form>
    </div>
  );
}
