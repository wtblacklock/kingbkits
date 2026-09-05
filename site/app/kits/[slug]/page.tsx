import type { Metadata } from "next";
import Image from "next/image";
import { notFound } from "next/navigation";
import { Container } from "@/components/Container";
import { EtsyButton } from "@/components/EtsyButton";
import { TierTable } from "@/components/TierTable";
import { getKit, KITS } from "@/data/kits";
import { SITE } from "@/data/site";

export function generateStaticParams() {
  return KITS.map((kit) => ({ slug: kit.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const kit = getKit(slug);
  if (!kit) return {};
  return {
    title: kit.name,
    description: kit.shortDescription,
    openGraph: {
      title: `${kit.name}. ${kit.subtitle}.`,
      description: kit.shortDescription,
      images: [{ url: kit.images.hero }],
    },
  };
}

export default async function KitPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const kit = getKit(slug);
  if (!kit) notFound();

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: kit.name,
    description: kit.shortDescription,
    image: `${SITE.url}${kit.images.hero}`,
    brand: { "@type": "Brand", name: SITE.name },
    offers: {
      "@type": "Offer",
      url: kit.etsyUrl ?? SITE.etsyShopUrl,
      availability: "https://schema.org/InStock",
    },
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      {/* H6 Photographic Fold hero. Real owned product photography, full-bleed.
          Kits without a hero GIF ship a designed cover graphic instead of a photographic
          scene, so that one asset is shown whole (contain) rather than cropped (cover). */}
      <section className="relative h-[60vh] min-h-[420px] w-full overflow-hidden bg-ink">
        <Image
          src={kit.images.hero}
          alt={kit.name}
          fill
          priority
          sizes="100vw"
          className={kit.images.heroGif ? "object-cover" : "object-contain"}
        />
        <div className="absolute inset-0 bg-gradient-to-t from-ink/90 via-ink/20 to-transparent" />
        <Container className="absolute inset-x-0 bottom-0 flex flex-col gap-4 pb-10">
          <div className="text-xs font-bold uppercase tracking-[0.1em] text-paper/80">{kit.subtitle}</div>
          <h1 className="max-w-2xl font-display text-3xl text-paper sm:text-5xl">{kit.name}</h1>
          <p className="max-w-xl text-paper/90">{kit.shortDescription}</p>
          <div className="flex flex-wrap items-center gap-4 pt-2">
            <EtsyButton href={kit.etsyUrl} campaign={`kit_${kit.slug}`} content="hero_cta">
              Buy on Etsy
            </EtsyButton>
            <span className="text-sm text-paper/80">{kit.pageCount} PDF pages. Instant download.</span>
          </div>
        </Container>
      </section>

      {/* F1 Bento grid: pitch, stats, and included items as mixed-span tiles. */}
      <section className="py-16">
        <Container>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-4 sm:auto-rows-[10rem]">
            <div className="flex flex-col justify-center gap-3 rounded-card border border-rule bg-paper-2 p-6 sm:col-span-2 sm:row-span-2">
              <h2 className="font-display text-xl text-ink">{kit.heroHeadline}</h2>
              <p className="text-sm text-ink-2">{kit.heroBody}</p>
              {kit.seasonalNote && (
                <p className="border-l-2 border-accent pl-3 text-xs text-ink-faint">{kit.seasonalNote}</p>
              )}
            </div>
            {kit.stats.map((stat) => (
              <div
                key={stat.label}
                className="flex flex-col justify-center gap-1 rounded-card border border-rule p-5"
              >
                <div className="font-display text-2xl text-ink">{stat.value}</div>
                <div className="text-xs text-ink-2">{stat.label}</div>
              </div>
            ))}
            {kit.included.map((item) => (
              <div
                key={item.number}
                className="flex flex-col justify-center gap-1 rounded-card border border-rule p-5"
              >
                <div className="text-xs font-bold text-ink-faint">{item.number}</div>
                <div className="font-semibold text-ink">{item.title}</div>
                <div className="text-xs text-ink-2">{item.description}</div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      {/* F3 Tabular spec sheet: the tier chart. */}
      {kit.tiers && (
        <section className="border-t border-rule bg-paper-2 py-16">
          <Container>
            <h2 className="mb-2 font-display text-2xl text-ink">Pick your tier</h2>
            <p className="mb-6 max-w-2xl text-ink-2">
              Every tier names real, specific bottles at that price point. Buy exactly what is
              listed and you are ready.
            </p>
            <TierTable kit={kit} />
          </Container>
        </section>
      )}

      {kit.compatibleWith && (
        <section className="py-16">
          <Container>
            <h2 className="mb-6 font-display text-2xl text-ink">Works with any standard calendar</h2>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              {kit.compatibleWith.map((name) => (
                <div key={name} className="rounded-card border border-rule bg-paper-2 px-4 py-3 text-center text-sm font-semibold text-ink">
                  {name}
                </div>
              ))}
            </div>
          </Container>
        </section>
      )}

      <section className="border-t border-rule bg-paper-2 py-16">
        <Container>
          <h2 className="mb-8 font-display text-2xl text-ink">Inside the PDF</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {kit.images.gallery.map((img) => (
              <figure key={img.src} className="overflow-hidden rounded-card border border-rule bg-paper">
                <div className="relative aspect-[4/5]">
                  <Image src={img.src} alt={img.label} fill sizes="(min-width: 1024px) 33vw, 50vw" className="object-cover" />
                </div>
                <figcaption className="px-4 py-2 text-sm text-ink-2">{img.label}</figcaption>
              </figure>
            ))}
          </div>
        </Container>
      </section>

      {/* F4 Step sequence: how it works. */}
      <section className="py-16">
        <Container>
          <h2 className="mb-8 font-display text-2xl text-ink">How it works</h2>
          <div className="grid gap-6 sm:grid-cols-2">
            {kit.howItWorks.map((step, i) => (
              <div key={step.title} className="flex gap-4">
                <div className="font-display text-2xl text-accent">{String(i + 1).padStart(2, "0")}</div>
                <div>
                  <div className="font-semibold text-ink">{step.title}</div>
                  <div className="text-sm text-ink-2">{step.description}</div>
                </div>
              </div>
            ))}
          </div>
          <p className="mt-8 text-xs text-ink-faint">
            This is an all-digital product. No physical items are shipped.
          </p>
        </Container>
      </section>

      <section className="border-t border-rule bg-paper-2 py-16">
        <Container className="flex flex-col items-center gap-4 text-center">
          <h2 className="font-display text-2xl text-ink">Ready to host {kit.name}?</h2>
          <EtsyButton href={kit.etsyUrl} campaign={`kit_${kit.slug}`} content="bottom_cta">
            Buy on Etsy
          </EtsyButton>
        </Container>
      </section>
    </>
  );
}
