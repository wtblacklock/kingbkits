"use client";

import { useState } from "react";
import Link from "next/link";
import { Badge } from "./Badge";
import { Container } from "./Container";
import { withUtm } from "@/lib/utm";
import { SITE } from "@/data/site";

const NAV = [
  { href: "/#kits", label: "Kits" },
  { href: "/guides", label: "Guides" },
  { href: "/about", label: "About" },
];

export function SiteHeader() {
  const [open, setOpen] = useState(false);
  const shopUrl = withUtm(SITE.etsyShopUrl, { campaign: "header_nav", content: "shop_button" });

  return (
    <header className="sticky top-0 z-30 border-b border-rule bg-paper/95 backdrop-blur">
      <Container className="flex items-center gap-4 py-3">
        <Link href="/" className="flex items-center gap-3" onClick={() => setOpen(false)}>
          <Badge size="sm" />
        </Link>

        <nav aria-label="Primary" className="hidden flex-1 items-center gap-7 sm:flex">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-bold uppercase tracking-[0.04em] text-ink-2 hover:text-ink"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <a
          href={shopUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="ml-auto hidden items-center justify-center rounded-full bg-accent px-5 py-2.5 text-sm font-bold uppercase tracking-[0.02em] text-accent-ink transition-transform hover:-translate-y-0.5 sm:inline-flex"
        >
          Shop on Etsy
        </a>

        <button
          type="button"
          aria-label={open ? "Close menu" : "Open menu"}
          aria-expanded={open}
          onClick={() => setOpen((v) => !v)}
          className="ml-auto flex h-10 w-10 flex-none items-center justify-center rounded-full border border-rule sm:hidden"
        >
          <svg width="18" height="14" viewBox="0 0 18 14" fill="none" aria-hidden="true">
            {open ? (
              <path
                d="M1 1 L17 13 M17 1 L1 13"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
              />
            ) : (
              <path
                d="M0 1 H18 M0 7 H18 M0 13 H18"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
              />
            )}
          </svg>
        </button>
      </Container>

      {open && (
        <div className="border-t border-rule bg-paper sm:hidden">
          <Container className="flex flex-col gap-1 py-3">
            {NAV.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => setOpen(false)}
                className="rounded-lg px-2 py-3 text-base font-bold uppercase tracking-[0.02em] text-ink-2 hover:bg-paper-2 hover:text-ink"
              >
                {item.label}
              </Link>
            ))}
            <a
              href={shopUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-flex items-center justify-center rounded-full bg-accent px-5 py-3 text-sm font-bold uppercase tracking-[0.02em] text-accent-ink"
            >
              Shop on Etsy
            </a>
          </Container>
        </div>
      )}
    </header>
  );
}
