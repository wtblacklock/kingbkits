import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { MDXRemote } from "next-mdx-remote/rsc";
import { Container } from "@/components/Container";
import { EtsyButton } from "@/components/EtsyButton";
import { getGuide, getGuideSlugs } from "@/lib/guides";
import { getKit } from "@/data/kits";

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
    return { title: guide.title, description: guide.description };
  } catch {
    return {};
  }
}

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
    <Container className="py-16">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      <Link href="/guides" className="text-sm font-semibold text-ink-faint hover:text-ink">
        ← All Guides
      </Link>
      <span className="mt-6 block text-xs font-bold uppercase tracking-wide text-ink-faint">{guide.topic}</span>
      <h1 className="mt-2 max-w-2xl text-4xl font-light text-ink">{guide.title}</h1>

      <article className="prose-guide mt-10 max-w-2xl">
        <MDXRemote source={guide.content} />
      </article>

      {relatedKit && (
        <div className="mt-14 flex max-w-2xl flex-col items-start gap-4 rounded-xl border border-rule bg-cover p-6">
          <div>
            <div className="text-xs font-bold uppercase tracking-wide text-ink-faint">Related Kit</div>
            <div className="text-lg font-semibold text-ink">{relatedKit.name}</div>
            <p className="mt-1 text-sm text-ink-body">{relatedKit.shortDescription}</p>
          </div>
          <EtsyButton href={relatedKit.etsyUrl} campaign={`guide_${guide.slug}`} content="related_kit">
            Buy on Etsy
          </EtsyButton>
        </div>
      )}
    </Container>
  );
}
