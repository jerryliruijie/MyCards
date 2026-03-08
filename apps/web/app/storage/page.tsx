import { api } from "@/lib/api-client";

export default async function StoragePage() {
  const positions = await api.listStorage().catch(() => []);

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">存储管理</h2>
        <p className="text-sm text-slate-600">树形位置 + 分配列表（当前为线框阶段）。</p>
      </header>

      <section className="grid gap-3 md:grid-cols-2">
        <div className="panel">
          <h3 className="mb-2 font-semibold">层级结构</h3>
          <ul className="space-y-1 text-sm">
            {positions.map((p) => (
              <li key={p.id}>
                {p.parent_id ? "↳ " : ""}
                {p.name}
              </li>
            ))}
            {positions.length === 0 && <li className="text-slate-500">暂无存储位置</li>}
          </ul>
        </div>
        <div className="panel h-64">
          <h3 className="mb-2 font-semibold">卡片分配</h3>
          <p className="text-sm text-slate-600">当前选中位置的卡片分配列表（占位）。</p>
        </div>
      </section>
    </div>
  );
}
