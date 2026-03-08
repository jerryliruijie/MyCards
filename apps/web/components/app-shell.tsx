"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ReactNode } from "react";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/cards", label: "Cards" },
  { href: "/cards/new", label: "Add Card" },
  { href: "/storage", label: "Storage" },
];

export function AppShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1 className="text-lg font-bold">MyCards Vault</h1>
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
