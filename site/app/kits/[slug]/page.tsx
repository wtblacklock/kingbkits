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
    alternates: { canonical: `/kits/${slug}` },
    openGraph: {
      title: `${kit.name}. ${kit.subtitle}.`,
      description: kit.shortDescription,
      images: [{ url: kit.images.card }],
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
    image: `${SITE.url}${kit.images.card}`,
    brand: { "@type": "Brand", name: SITE.name },
    offers: {
      "@type": "Offer",
      url: kit.etsyUrl ?? SITE.etsyShopUrl,
      availability: "https://schema.org/InStock",
      price: kit.price.toFixed(2),
      priceCurrency: "USD",
      // Instant digital download: nothing ships, so handling/transit time is zero.
      shippingDetails: {
        "@type": "OfferShippingDetails",
        shippingRate: { "@type": "MonetaryAmount", value: "0", currency: "USD" },
        shippingDestination: { "@type": "DefinedRegion", addressCountry: "US" },
        deliveryTime: {
          "@type": "ShippingDeliveryTime",
          handlingTime: { "@type": "QuantitativeValue", minValue: 0, maxValue: 0, unitCode: "DAY" },
          transitTime: { "@type": "QuantitativeValue", minValue: 0, maxValue: 0, unitCode: "DAY" },
        },
      },
      // Matches the shop's actual policy: instant-download items don't accept returns.
      hasMerchantReturnPolicy: {
        "@type": "MerchantReturnPolicy",
        returnPolicyCategory: "https://schema.org/MerchantReturnNotPermitted",
      },
    },
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      {/* Hero: headline/CTA on light paper, the real Etsy listing image shown
          whole (no crop) since it's already a fully-designed product shot. */}
      <section className="border-b border-rule bg-paper-2">
        <Container className="grid grid-cols-1 items-center gap-10 py-12 sm:py-16 lg:grid-cols-2 lg:gap-16 lg:py-20">
          <div className="order-2 lg:order-1">
            <div className="text-xs font-bold uppercase tracking-[0.1em] text-ink-faint">{kit.subtitle}</div>
            <h1 className="mt-3 font-display text-3xl leading-[1.08] text-ink sm:text-5xl">{kit.name}</h1>
            <p className="mt-4 max-w-xl text-lg text-ink-2">{kit.shortDescription}</p>
            <div className="mt-7 flex flex-wrap items-center gap-4">
              <EtsyButton href={kit.etsyUrl} campaign={`kit_${kit.slug}`} content="hero_cta">
                Buy on Etsy
              </EtsyButton>
              <span className="text-sm font-semibold text-ink-faint">
                {kit.pageCount} PDF pages &middot; Instant download
              </span>
            </div>
          </div>
          <div className="relative order-1 aspect-square w-full overflow-hidden rounded-3xl shadow-sm lg:order-2">
            <Image
              src={kit.images.card}
              alt={kit.name}
              fill
              priority
              sizes="(min-width: 1024px) 50vw, 100vw"
              className="object-contain"
            />
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
