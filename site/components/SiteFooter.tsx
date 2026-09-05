import Link from "next/link";
import { Badge } from "./Badge";
import { Container } from "./Container";
import { KITS } from "@/data/kits";

export function SiteFooter() {
  return (
    <footer className="mt-24 border-t border-rule bg-paper py-14">
      <Container className="grid gap-10 sm:grid-cols-3">
        <div>
          <Badge size="sm" />
          <p className="mt-4 max-w-xs text-sm text-ink-faint">
            Printable tasting-party kits. Pick a tier, buy the bottles, run the night.
          </p>
        </div>
        <div>
          <div className="mb-3 text-xs font-bold uppercase tracking-wide text-ink-faint">Kits</div>
          <ul className="space-y-2 text-sm">
            {KITS.map((kit) => (
              <li key={kit.slug}>
                <Link href={`/kits/${kit.slug}`} className="text-ink-body hover:text-ink">
                  {kit.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <div className="mb-3 text-xs font-bold uppercase tracking-wide text-ink-faint">More</div>
          <ul className="space-y-2 text-sm">
            <li>
              <Link href="/guides" className="text-ink-body hover:text-ink">
                Guides
              </Link>
            </li>
            <li>
              <Link href="/about" className="text-ink-body hover:text-ink">
                About KingBKits
              </Link>
            </li>
          </ul>
        </div>
      </Container>
      <Container className="mt-10 border-t border-rule pt-6 text-xs text-ink-faint">
        © {new Date().getFullYear()} KingBKits. All kits are instant-download PDFs — no physical items ship.
      </Container>
    </footer>
  );
}
