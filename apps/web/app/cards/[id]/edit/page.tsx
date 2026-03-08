"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api/v1";

export default function EditCardPage({ params }: { params: { id: string } }) {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);

    const res = await fetch(`${API_BASE_URL}/cards/${params.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });

    if (!res.ok) {
      setError(`更新失败（${res.status}）`);
      return;
    }

    router.push(`/cards/${params.id}`);
  }

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">编辑卡片</h2>
      </header>
      <form className="panel max-w-xl space-y-3" onSubmit={onSubmit}>
        <div>
          <label className="mb-1 block text-sm font-medium">标题</label>
          <input
            className="w-full rounded border p-2 text-sm"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="请输入新标题"
          />
        </div>
        {error && <div className="text-sm text-red-700">{error}</div>}
        <button className="rounded bg-slate-800 px-3 py-2 text-sm text-white" type="submit">
          保存
        </button>
      </form>
    </div>
  );
}
