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
      title: `${kit.name} — ${kit.subtitle}`,
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

      <section className="border-b border-rule bg-cover py-16">
        <Container className="grid gap-10 md:grid-cols-2 md:items-center">
          <div className="flex flex-col gap-5">
            <span className="text-xs font-bold uppercase tracking-wide text-ink-faint">{kit.subtitle}</span>
            <h1 className="text-4xl font-light leading-tight text-ink">{kit.name}</h1>
            <p className="text-lg text-ink-body">{kit.shortDescription}</p>
            <div className="flex flex-wrap gap-3 pt-2">
              <EtsyButton href={kit.etsyUrl} campaign={`kit_${kit.slug}`} content="hero_cta">
                Buy on Etsy
              </EtsyButton>
              <span className="inline-flex items-center text-sm text-ink-faint">
                {kit.pageCount} PDF pages · Instant download
              </span>
            </div>
          </div>
          <div className="relative aspect-square overflow-hidden rounded-2xl border border-rule bg-paper">
            <Image src={kit.images.hero} alt={kit.name} fill sizes="(min-width: 768px) 40vw, 90vw" className="object-cover" />
          </div>
        </Container>
      </section>

      <section className="py-16">
        <Container className="grid gap-10 md:grid-cols-[1.2fr_0.8fr]">
          <div>
            <h2 className="text-2xl font-light text-ink">{kit.heroHeadline}</h2>
            <p className="mt-4 text-ink-body">{kit.heroBody}</p>
            {kit.seasonalNote && (
              <p className="mt-4 border-l-2 border-ink-faint pl-4 text-sm text-ink-faint">{kit.seasonalNote}</p>
            )}
          </div>
          <div className="flex flex-col justify-center gap-6 rounded-xl border border-rule bg-zone p-6">
            {kit.stats.map((stat) => (
              <div key={stat.label}>
                <div className="text-3xl font-semibold text-ink">{stat.value}</div>
                <div className="text-sm text-ink-body">{stat.label}</div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-t border-rule bg-paper py-16">
        <Container>
          <h2 className="mb-8 text-2xl font-light text-ink">What&apos;s inside</h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {kit.included.map((item) => (
              <div key={item.number} className="flex gap-4 border-b border-rule pb-4">
                <div className="w-14 flex-none font-display text-lg text-gold">{item.number}</div>
                <div>
                  <div className="font-semibold text-ink">{item.title}</div>
                  <div className="text-sm text-ink-body">{item.description}</div>
                </div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      {kit.tiers && (
        <section className="py-16">
          <Container>
            <h2 className="mb-2 text-2xl font-light text-ink">Pick your tier</h2>
            <p className="mb-6 max-w-2xl text-ink-body">
              Every tier names real, specific bottles at that price point — buy exactly what&apos;s
              listed and you&apos;re ready.
            </p>
            <TierTable kit={kit} />
          </Container>
        </section>
      )}

      {kit.compatibleWith && (
        <section className="py-16">
          <Container>
            <h2 className="mb-6 text-2xl font-light text-ink">Works with any standard calendar</h2>
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              {kit.compatibleWith.map((name) => (
                <div key={name} className="rounded-lg border border-rule bg-zone px-4 py-3 text-center text-sm font-semibold text-ink">
                  {name}
                </div>
              ))}
            </div>
          </Container>
        </section>
      )}

      <section className="border-t border-rule bg-paper py-16">
        <Container>
          <h2 className="mb-8 text-2xl font-light text-ink">Inside the PDF</h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {kit.images.gallery.map((img) => (
              <figure key={img.src} className="overflow-hidden rounded-xl border border-rule bg-cover">
                <div className="relative aspect-[4/5]">
                  <Image src={img.src} alt={img.label} fill sizes="(min-width: 1024px) 33vw, 50vw" className="object-cover" />
                </div>
                <figcaption className="px-4 py-2 text-sm text-ink-body">{img.label}</figcaption>
              </figure>
            ))}
          </div>
        </Container>
      </section>

      <section className="py-16">
        <Container>
          <h2 className="mb-8 text-2xl font-light text-ink">How it works</h2>
          <div className="grid gap-6 sm:grid-cols-2">
            {kit.howItWorks.map((step, i) => (
              <div key={step.title} className="flex gap-4">
                <div className="font-display text-2xl text-gold">{String(i + 1).padStart(2, "0")}</div>
                <div>
                  <div className="font-semibold text-ink">{step.title}</div>
                  <div className="text-sm text-ink-body">{step.description}</div>
                </div>
              </div>
            ))}
          </div>
          <p className="mt-8 text-xs text-ink-faint">
            This is an all-digital product. No physical items are shipped.
          </p>
        </Container>
      </section>

      <section className="border-t border-rule bg-cover py-16">
        <Container className="flex flex-col items-center gap-4 text-center">
          <h2 className="text-2xl font-light text-ink">Ready to host {kit.name}?</h2>
          <EtsyButton href={kit.etsyUrl} campaign={`kit_${kit.slug}`} content="bottom_cta">
            Buy on Etsy
          </EtsyButton>
        </Container>
      </section>
    </>
  );
}
