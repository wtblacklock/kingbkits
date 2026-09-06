import Image from "next/image";
import { Container } from "@/components/Container";
import { KitCard } from "@/components/KitCard";
import { EtsyButton } from "@/components/EtsyButton";
import { Reveal } from "@/components/Reveal";
import { KITS } from "@/data/kits";

const VALUE_PROPS = [
  {
    value: "3",
    label: "budget tiers in every kit",
    detail: "Newbie, Casual, Aficionado, so the shopping list matches what you actually want to spend.",
  },
  {
    value: "100%",
    label: "instant digital download",
    detail: "Print at home or a shop. Nothing physical ships, so there's no waiting on the mail.",
  },
  {
    value: "Real",
    label: "named products, not vibes",
    detail: "Actual bottles and brands at every price point, so shopping takes minutes, not research.",
  },
];

const FAQS = [
  {
    q: "Is this a physical product that ships to me?",
    a: "No. Every kit is an instant-download PDF. You buy it on Etsy, download it right away, and print it at home or at a shop like FedEx or Staples. Nothing physical ever ships.",
  },
  {
    q: "What do I actually need to buy besides the kit?",
    a: "Just the ingredients: the bottles, candy, or cigars named in the kit's own shopping chart. Each kit gives you real, specific products at three budget tiers, so you know exactly what to grab and roughly what it'll cost.",
  },
  {
    q: "Do I need a fancy printer or special paper?",
    a: "No. Every kit is designed for standard US Letter paper on a normal home printer. No bleed, no cardstock required, though cardstock makes the tasting cards feel nicer if you have it.",
  },
  {
    q: "Can I use a kit if I don't know much about whisky, tequila, or cigars?",
    a: "That's exactly who the Newbie tier is for. Every kit starts with a primer that explains the basics in plain language, then hands you a shopping list so you don't have to guess.",
  },
  {
    q: "How many people does one kit cover?",
    a: "Most kits are built around one bottle per tier, which comfortably covers 6 guests at tasting-size pours. The party guide in each kit spells out exact quantities.",
  },
];

const faqJsonLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: FAQS.map((f) => ({
    "@type": "Question",
    name: f.q,
    acceptedAnswer: { "@type": "Answer", text: f.a },
  })),
};

export default function HomePage() {
  const [cigar, mezcal, candy, advent] = KITS;

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }} />

      {/* Hero: photo right (Unsplash), benefit-first copy left. Stacks on mobile. */}
      <Reveal>
        <section className="border-b border-rule bg-paper-2">
          <Container className="grid grid-cols-1 items-center gap-10 py-12 sm:py-16 lg:grid-cols-2 lg:gap-16 lg:py-24">
            <div className="order-2 lg:order-1">
              <p className="inline-flex items-center rounded-full bg-accent px-3 py-1 text-xs font-bold uppercase tracking-[0.06em] text-accent-ink">
                Printable party kits
              </p>
              <h1 className="mt-5 font-display text-[2.25rem] leading-[1.08] text-ink sm:text-5xl lg:text-[3.25rem]">
                The party kit that tells you exactly what to buy.
              </h1>
              <p className="mt-5 max-w-lg text-lg text-ink-2">
                No more Googling &ldquo;what pairs with what&rdquo; the night before. Every kit names
                the real bottles, candy, or cigars to buy at three budget tiers, plus the cards and
                guide that run the night for you.
              </p>
              <div className="mt-8 flex flex-wrap items-center gap-3">
                <EtsyButton campaign="home_hero" content="primary_cta">
                  Shop all kits on Etsy
                </EtsyButton>
                <a
                  href="#kits"
                  className="inline-flex items-center justify-center rounded-full border-2 border-ink px-6 py-3 text-sm font-bold uppercase tracking-[0.04em] text-ink hover:bg-ink hover:text-paper"
                >
                  See the kits
                </a>
              </div>
              <p className="mt-6 text-sm font-semibold text-ink-faint">
                Instant download &middot; Print at home &middot; No physical items ship
              </p>
            </div>
            <div className="relative order-1 aspect-[4/3] w-full overflow-hidden rounded-3xl sm:aspect-[16/10] lg:order-2">
              <Image
                src="https://images.unsplash.com/photo-1581954548122-4dff8989c0f7?w=1600&q=80&auto=format&fit=crop"
                alt="Friends gathered around a table for a tasting night"
                fill
                priority
                sizes="(min-width: 1024px) 50vw, 100vw"
                className="object-cover"
              />
            </div>
          </Container>
        </section>
      </Reveal>

      {/* Value props: editorial row, typographic rather than boxed cards */}
      <section className="py-16 sm:py-20">
        <Container className="grid gap-10 sm:grid-cols-3 sm:gap-8">
          {VALUE_PROPS.map((v, i) => (
            <Reveal key={v.label} delay={i * 100} className="tabular-nums">
              <div
                className={`sm:pl-8 ${i > 0 ? "border-t border-rule pt-6 sm:border-l sm:border-t-0 sm:pt-0" : ""}`}
              >
                <div className="font-display text-4xl italic text-ink">{v.value}</div>
                <p className="mt-2 font-bold text-ink">{v.label}</p>
                <p className="mt-1 text-sm text-ink-2">{v.detail}</p>
              </div>
            </Reveal>
          ))}
        </Container>
      </section>

      {/* Pull quote - real, existing brand copy, editorial statement break */}
      <Reveal>
        <section className="border-y border-rule bg-paper-2 py-16 sm:py-20">
          <Container className="max-w-3xl">
            <blockquote className="font-display text-2xl italic leading-snug text-ink sm:text-3xl">
              &ldquo;Party planning is the part people skip.&rdquo;
            </blockquote>
            <p className="mt-4 text-ink-2">
              Every kit exists to answer the two questions that actually stall a night before it
              starts: what do I buy, and how much. Named products, three budget tiers, printed and
              ready before your guests arrive.
            </p>
          </Container>
        </section>
      </Reveal>

      {/* Kit gallery - kept as the layout the user likes */}
      <section id="kits" className="py-14 sm:py-16">
        <Container>
          <Reveal>
            <div className="mb-8 max-w-xl">
              <h2 className="font-display text-2xl text-ink sm:text-3xl">Pick your night</h2>
              <p className="mt-2 text-ink-2">
                One format for every kit: a printable guide, a shopping chart at three budget tiers,
                and tasting cards to run the night.
              </p>
            </div>
          </Reveal>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-4 sm:auto-rows-[16rem]">
            <Reveal delay={0} className="sm:col-span-2 sm:row-span-2">
              <KitCard kit={cigar} featured />
            </Reveal>
            <Reveal delay={80}>
              <KitCard kit={mezcal} />
            </Reveal>
            <Reveal delay={160}>
              <KitCard kit={candy} />
            </Reveal>
            <Reveal delay={240} className="sm:col-span-2">
              <KitCard kit={advent} />
            </Reveal>
          </div>
        </Container>
      </section>

      {/* FAQ - real objections, real answers. Also feeds FAQPage schema above. */}
      <Reveal>
        <section className="border-t border-rule py-16 sm:py-20">
          <Container className="mx-auto max-w-2xl">
            <h2 className="font-display text-2xl text-ink sm:text-3xl">Questions before you buy</h2>
            <div className="mt-6 divide-y divide-rule">
              {FAQS.map((f) => (
                <details key={f.q} className="faq-item group py-4">
                  <summary className="flex items-center justify-between gap-4 text-left font-bold text-ink">
                    {f.q}
                    <span
                      aria-hidden="true"
                      className="faq-item__icon flex h-6 w-6 flex-none items-center justify-center rounded-full bg-paper-2 text-lg leading-none text-ink transition-transform"
                    >
                      +
                    </span>
                  </summary>
                  <p className="mt-3 text-ink-2">{f.a}</p>
                </details>
              ))}
            </div>
          </Container>
        </section>
      </Reveal>

      {/* Final CTA: full-bleed accent band, real conversion action, no boxed card */}
      <Reveal>
        <section className="bg-accent py-16 sm:py-20">
          <Container className="flex flex-col items-center gap-5 text-center">
            <h2 className="font-display text-3xl text-accent-ink sm:text-4xl">
              Skip the planning. Start the night.
            </h2>
            <p className="max-w-md text-accent-ink/80">
              Every kit is an instant download on Etsy, invitation template included.
            </p>
            <EtsyButton campaign="home_final_cta" content="bottom_cta">
              Shop all kits on Etsy
            </EtsyButton>
          </Container>
        </section>
      </Reveal>
    </>
  );
}
