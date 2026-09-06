import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { MDXRemote } from "next-mdx-remote/rsc";
import { Container } from "@/components/Container";
import { Reveal } from "@/components/Reveal";
import { withUtm } from "@/lib/utm";
import { getGuide, getGuideSlugs } from "@/lib/guides";
import { getKit } from "@/data/kits";
import { SITE } from "@/data/site";

export function generateStaticParams() {
  return getGuideSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  try {
    const { slug } = await params;
    const guide = getGuide(slug);
    return {
      title: guide.title,
      description: guide.description,
      alternates: { canonical: `/guides/${slug}` },
    };
  } catch {
    return {};
  }
}

const mdxComponents = {
  img: (props: React.ImgHTMLAttributes<HTMLImageElement>) => (
    // eslint-disable-next-line @next/next/no-img-element
    <img {...props} className="w-full rounded-card border border-rule" alt={props.alt ?? ""} />
  ),
};

export default async function GuidePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  let guide;
  try {
    guide = getGuide(slug);
  } catch {
    notFound();
  }

  const relatedKit = guide.relatedKit ? getKit(guide.relatedKit) : undefined;

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: guide.title,
    description: guide.description,
    articleSection: guide.topic,
  };

  return (
    <Container className="max-w-[65ch] py-16">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      <Link href="/guides" className="text-sm font-semibold text-ink-faint hover:text-ink">
        ← All guides
      </Link>

      <Reveal>
        <div>
          <div className="mt-6 text-xs font-bold uppercase tracking-[0.08em] text-ink-faint">{guide.topic}</div>
          <h1 className="mt-2 font-display text-3xl text-ink sm:text-4xl">{guide.title}</h1>

          {guide.image && (
            <div className="relative mt-8 aspect-[16/9] w-full overflow-hidden rounded-card">
              <Image src={guide.image} alt={guide.imageAlt ?? ""} fill sizes="65ch" className="object-cover" priority />
            </div>
          )}
        </div>
      </Reveal>

      <Reveal>
        <article className="prose-guide mt-10">
          <MDXRemote source={guide.content} components={mdxComponents} />
        </article>
      </Reveal>

      {relatedKit && (
        <Reveal>
          <p className="mt-14 border-t border-rule pt-8 text-ink-2">
            Our <Link href={`/kits/${relatedKit.slug}`} className="font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4">{relatedKit.name}</Link> kit
            builds this into a full pairing chart, flavor wheels, and tasting cards.{" "}
            <a
              href={withUtm(relatedKit.etsyUrl ?? SITE.etsyShopUrl, { campaign: `guide_${guide.slug}`, content: "related_kit" })}
              target="_blank"
              rel="noopener noreferrer"
              className="font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4"
            >
              Buy it on Etsy →
            </a>
          </p>
        </Reveal>
      )}
    </Container>
  );
}
