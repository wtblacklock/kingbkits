import Link from "next/link";
import { Badge } from "./Badge";
import { Container } from "./Container";
import { EtsyButton } from "./EtsyButton";

const NAV = [
  { href: "/", label: "Home" },
  { href: "/#kits", label: "Kits" },
  { href: "/guides", label: "Guides" },
  { href: "/about", label: "About" },
];

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-20 border-b border-rule bg-cover/95 backdrop-blur">
      <Container className="flex items-center gap-6 py-3">
        <Link href="/" className="flex items-center gap-3">
          <Badge size="sm" />
        </Link>
        <nav className="hidden flex-1 items-center gap-1 sm:flex">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="rounded-full border border-transparent px-3 py-1.5 text-sm font-medium text-ink-body hover:border-rule hover:text-ink"
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="ml-auto">
          <EtsyButton campaign="header_nav" content="shop_button">
            Shop on Etsy
          </EtsyButton>
        </div>
      </Container>
    </header>
  );
}
