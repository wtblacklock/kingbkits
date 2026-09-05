import { Container } from "@/components/Container";
import { KitCard } from "@/components/KitCard";
import { EtsyButton } from "@/components/EtsyButton";
import { KITS } from "@/data/kits";
import { SITE } from "@/data/site";

export default function HomePage() {
  return (
    <>
      <section className="border-b border-rule bg-cover py-20">
        <Container className="flex flex-col items-start gap-6">
          <span className="text-sm font-semibold uppercase tracking-wide text-ink-faint">
            Printable Tasting-Party Kits
          </span>
          <h1 className="max-w-2xl text-4xl font-light leading-tight text-ink sm:text-5xl">
            Pick a tier. Buy the bottles. <span className="font-semibold">Run the night.</span>
          </h1>
          <p className="max-w-xl text-lg text-ink-body">{SITE.description}</p>
          <div className="flex flex-wrap gap-3">
            <EtsyButton campaign="home_hero" content="primary_cta">
              Shop the Kits on Etsy
            </EtsyButton>
            <a
              href="#kits"
              className="inline-flex items-center justify-center rounded-full border border-ink px-6 py-3 text-sm font-semibold text-ink hover:bg-ink hover:text-white"
            >
              See the Kits
            </a>
          </div>
        </Container>
      </section>

      <section id="kits" className="py-20">
        <Container>
          <div className="mb-10 flex flex-col gap-2">
            <span className="text-xs font-bold uppercase tracking-wide text-ink-faint">The Lineup</span>
            <h2 className="text-3xl font-light text-ink">Four kits, one system</h2>
            <p className="max-w-2xl text-ink-body">
              Every kit follows the same structure — a party guide, a primer, a real-bottle pairing
              chart across three budget tiers, flavor wheels, and tasting cards — so once you&apos;ve run
              one, you already know how to run them all.
            </p>
          </div>
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {KITS.map((kit) => (
              <KitCard key={kit.slug} kit={kit} />
            ))}
          </div>
        </Container>
      </section>

      <section className="border-t border-rule bg-paper py-20">
        <Container className="grid gap-10 sm:grid-cols-3">
          <div>
            <div className="text-3xl font-semibold text-ink">3</div>
            <p className="mt-1 text-sm text-ink-body">
              budget tiers in every kit — Newbie, Casual, Aficionado — so the shopping list matches
              what you actually want to spend.
            </p>
          </div>
          <div>
            <div className="text-3xl font-semibold text-ink">100%</div>
            <p className="mt-1 text-sm text-ink-body">
              instant digital download. Print at home or a shop — nothing physical ever ships.
            </p>
          </div>
          <div>
            <div className="text-3xl font-semibold text-ink">Real</div>
            <p className="mt-1 text-sm text-ink-body">
              named products at every price point, not vague style suggestions — so shopping takes
              minutes, not research.
            </p>
          </div>
        </Container>
      </section>

      <section className="py-20">
        <Container className="flex flex-col items-center gap-4 rounded-2xl border border-rule bg-cover px-8 py-14 text-center">
          <h2 className="text-2xl font-light text-ink sm:text-3xl">Ready to host?</h2>
          <p className="max-w-md text-ink-body">
            Every kit is on Etsy as an instant download, invitation template included.
          </p>
          <EtsyButton campaign="home_bottom_cta">Shop on Etsy</EtsyButton>
        </Container>
      </section>
    </>
  );
}
