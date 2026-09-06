import Image from "next/image";
import { Container } from "@/components/Container";
import { KitCard } from "@/components/KitCard";
import { EtsyButton } from "@/components/EtsyButton";
import { KITS } from "@/data/kits";

export default function HomePage() {
  const [cigar, mezcal, candy, advent] = KITS;

  return (
    <>
      {/* H2 Split Diptych hero. Left: eyebrow + display headline + lede + CTAs.
          Right: a hand-built aria-hidden shape cluster (Tier A pure CSS art) -
          no stock photography, no product screenshot duplicating the gallery below. */}
      <section className="border-b border-rule bg-paper-2">
        <Container className="grid grid-cols-1 items-center gap-10 py-20 sm:grid-cols-2 sm:gap-6 sm:py-28">
          <div className="max-w-xl">
            <p className="font-mono text-xs uppercase tracking-[0.14em] text-accent">
              Printable party kits
            </p>
            <h1 className="mt-4 font-display text-4xl leading-[1.05] text-ink sm:text-5xl">
              Pick a tier. Buy the bottles. Run the night.
            </h1>
            <p className="mt-5 text-lg text-ink-2">
              Party kits that pair a spirit with something else: cigars, agave, Halloween candy,
              or a whisky advent calendar. Three budget tiers, real named products, ready to
              print tonight.
            </p>
            <div className="mt-8 flex flex-wrap items-center gap-3">
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
          </div>
          <figure className="hero-play mx-auto" aria-hidden="true">
            <span className="hero-play__blob" />
            <span className="hero-play__ring" />
            <span className="hero-play__pill" />
            <Image
              src="/logo.png"
              alt=""
              width={200}
              height={200}
              className="hero-play__badge"
            />
            <span className="hero-play__dot" />
          </figure>
        </Container>
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
