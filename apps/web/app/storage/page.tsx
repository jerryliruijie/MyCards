import { api } from "@/lib/api-client";

export default async function StoragePage() {
  const positions = await api.listStorage().catch(() => []);

  return (
    <div className="space-y-4">
      <header className="panel">
        <h2 className="text-xl font-semibold">Storage Manager</h2>
        <p className="text-sm text-slate-600">Tree/table split workflow (wireframe stage).</p>
      </header>

      <section className="grid gap-3 md:grid-cols-2">
        <div className="panel">
          <h3 className="mb-2 font-semibold">Hierarchy</h3>
          <ul className="space-y-1 text-sm">
            {positions.map((p) => (
              <li key={p.id}>
                {p.parent_id ? "↳ " : ""}
                {p.name}
              </li>
            ))}
            {positions.length === 0 && <li className="text-slate-500">No positions yet</li>}
          </ul>
        </div>
        <div className="panel h-64">
          <h3 className="mb-2 font-semibold">Assignments</h3>
          <p className="text-sm text-slate-600">Selected-position card assignments placeholder.</p>
        </div>
      </section>
    </div>
  );
}
