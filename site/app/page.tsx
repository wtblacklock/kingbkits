import { Container } from "@/components/Container";
import { KitCard } from "@/components/KitCard";
import { EtsyButton } from "@/components/EtsyButton";
import { KITS } from "@/data/kits";

export default function HomePage() {
  const [cigar, mezcal, candy, advent] = KITS;

  return (
    <>
      {/* Bento Grid macrostructure. F1 Bento knobs: tiles=4, spans=irregular, accent=corner-only. */}
      <section className="flex min-h-[70vh] flex-col items-center justify-center border-b border-rule bg-paper-2 px-6 py-20 text-center">
        <h1 className="max-w-3xl font-display text-4xl leading-tight text-ink sm:text-5xl">
          Pick a tier. Buy the bottles. Run the night.
        </h1>
        <p className="mt-6 max-w-xl text-lg text-ink-2">
          Printable party kits that pair a spirit with something else: cigars, agave, Halloween
          candy, or a whisky advent calendar. Three budget tiers, real named products, ready to
          print tonight.
        </p>
        <div className="mt-8 flex flex-wrap justify-center gap-3">
          <EtsyButton campaign="home_hero" content="primary_cta">
            Buy on Etsy
          </EtsyButton>
          <a
            href="#kits"
            className="inline-flex items-center justify-center rounded-full border-2 border-ink px-6 py-3 text-sm font-bold uppercase tracking-[0.04em] text-ink hover:bg-ink hover:text-paper"
          >
            See the kits
          </a>
        </div>
      </section>

      <section id="kits" className="py-16">
        <Container>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-4 sm:auto-rows-[16rem]">
            <div className="sm:col-span-2 sm:row-span-2">
              <KitCard kit={cigar} featured />
            </div>
            <KitCard kit={mezcal} />
            <KitCard kit={candy} />
            <div className="sm:col-span-2">
              <KitCard kit={advent} contain />
            </div>
          </div>
        </Container>
      </section>

      <section className="border-t border-rule bg-paper-2 py-16">
        <Container className="grid gap-10 tabular-nums sm:grid-cols-3">
          <div>
            <div className="font-display text-3xl text-ink">3</div>
            <p className="mt-1 text-sm text-ink-2">
              budget tiers in every kit: Newbie, Casual, Aficionado, so the shopping list matches
              what you actually want to spend.
            </p>
          </div>
          <div>
            <div className="font-display text-3xl text-ink">100%</div>
            <p className="mt-1 text-sm text-ink-2">
              instant digital download. Print at home or a shop, nothing physical ever ships.
            </p>
          </div>
          <div>
            <div className="font-display text-3xl text-ink">Real</div>
            <p className="mt-1 text-sm text-ink-2">
              named products at every price point, not vague style suggestions, so shopping takes
              minutes, not research.
            </p>
          </div>
        </Container>
      </section>

      <section className="py-20">
        <Container className="flex flex-col items-center gap-4 rounded-card border border-rule bg-paper-2 px-8 py-14 text-center">
          <h2 className="font-display text-2xl text-ink sm:text-3xl">Ready to host?</h2>
          <p className="max-w-md text-ink-2">
            Every kit is on Etsy as an instant download, invitation template included.
          </p>
          <EtsyButton campaign="home_bottom_cta">Buy on Etsy</EtsyButton>
        </Container>
      </section>
    </>
  );
}
