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
    <header className="sticky top-0 z-20 border-b-2 border-ink bg-paper">
      <Container className="flex items-center gap-6 py-3">
        <Link href="/" className="flex items-center gap-3">
          <Badge size="sm" />
        </Link>
        <nav aria-label="Primary" className="hidden flex-1 items-center gap-6 sm:flex">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-semibold uppercase tracking-[0.08em] text-ink-2 hover:text-ink"
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <a
          href={shopUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="ml-auto inline-flex items-center justify-center bg-ink px-4 py-2.5 text-xs font-bold uppercase tracking-[0.1em] text-paper transition-colors hover:bg-accent hover:text-ink"
        >
          Shop
        </a>
      </Container>
    </header>
  );
}
