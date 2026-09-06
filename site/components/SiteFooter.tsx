import Link from "next/link";
import { Container } from "./Container";
import { Badge } from "./Badge";
import { KITS } from "@/data/kits";
import { withUtm } from "@/lib/utm";
import { SITE } from "@/data/site";

export function SiteFooter() {
  const shopUrl = withUtm(SITE.etsyShopUrl, { campaign: "footer", content: "shop_link" });
  return (
    <footer className="mt-24 border-t border-rule">
      <Container className="flex flex-col gap-10 py-12 sm:flex-row sm:items-start sm:justify-between">
        <div className="flex flex-col gap-3">
          <Badge size="sm" />
          <p className="max-w-xs text-sm text-ink-faint">
            Instant-download PDFs. No physical items ship.
          </p>
          <a
            href={shopUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="mt-1 inline-flex w-fit items-center gap-1 text-sm font-bold text-ink underline decoration-accent decoration-2 underline-offset-4"
          >
            Visit the Etsy shop →
          </a>
        </div>
        <nav aria-label="Footer" className="grid grid-cols-2 gap-x-8 gap-y-3 text-sm font-semibold sm:flex sm:flex-wrap">
          {KITS.map((kit) => (
            <Link key={kit.slug} href={`/kits/${kit.slug}`} className="text-ink-2 hover:text-ink">
              {kit.name}
            </Link>
          ))}
          <Link href="/guides" className="text-ink-2 hover:text-ink">
            Guides
          </Link>
          <Link href="/about" className="text-ink-2 hover:text-ink">
            About
          </Link>
        </nav>
      </Container>
      <Container className="border-t border-rule py-6 text-xs text-ink-faint">
        © {new Date().getFullYear()} KingBKits.
      </Container>
    </footer>
  );
}
