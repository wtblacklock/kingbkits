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
  const shopUrl = withUtm(SITE.etsyShopUrl, { campaign: "header_nav", content: "shop_button" });
  return (
    <header className="sticky top-0 z-20 border-b border-rule bg-paper/90 backdrop-blur">
      <Container className="flex items-center gap-6 py-3">
        <Link href="/" className="flex items-center gap-3">
          <Badge size="sm" />
        </Link>
        <nav aria-label="Primary" className="hidden flex-1 items-center gap-6 sm:flex">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="font-mono text-xs uppercase tracking-[0.1em] text-ink-2 hover:text-ink"
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <a
          href={shopUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="ml-auto inline-flex items-center justify-center rounded-full bg-accent px-4 py-2.5 font-mono text-xs font-bold uppercase tracking-[0.1em] text-accent-ink transition-colors hover:opacity-90"
        >
          Shop
        </a>
      </Container>
    </header>
  );
}
