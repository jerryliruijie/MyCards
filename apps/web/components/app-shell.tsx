"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ReactNode } from "react";

const links = [
  { href: "/", label: "仪表盘" },
  { href: "/cards", label: "卡片列表" },
  { href: "/cards/new", label: "新增卡片" },
  { href: "/storage", label: "存储管理" },
];

export function AppShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1 className="text-lg font-bold">MyCards 个人卡库</h1>
        <nav className="mt-4 space-y-2">
          {links.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className={`block rounded px-2 py-1 text-sm ${
                pathname === link.href ? "bg-slate-200 font-semibold" : "hover:bg-slate-100"
              }`}
            >
              {link.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="main">{children}</main>
    </div>
  );
}
