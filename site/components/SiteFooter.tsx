import Link from "next/link";
import { Container } from "./Container";
import { Badge } from "./Badge";
import { KITS } from "@/data/kits";

const TAGLINE = "PICK A TIER · BUY THE BOTTLES · RUN THE NIGHT";

export function SiteFooter() {
  const track = `${TAGLINE} · `.repeat(4);
  return (
    <footer className="mt-24">
      <div className="foot-marquee overflow-hidden border-y-2 border-ink bg-ink py-4">
        <div className="foot-marquee__track" aria-hidden="true">
          <span className="font-display text-lg tracking-[0.08em] text-paper sm:text-xl">{track}</span>
          <span className="font-display text-lg tracking-[0.08em] text-paper sm:text-xl">{track}</span>
        </div>
        <p className="sr-only">KingBKits. Pick a tier, buy the bottles, run the night.</p>
      </div>

      <Container className="flex flex-col gap-8 py-12 sm:flex-row sm:items-start sm:justify-between">
        <div className="flex flex-col gap-3">
          <Badge size="sm" />
          <p className="max-w-xs text-sm text-ink-faint">
            Instant-download PDFs. No physical items ship.
          </p>
        </div>
        <nav aria-label="Footer" className="flex flex-wrap gap-x-8 gap-y-3 text-sm">
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
