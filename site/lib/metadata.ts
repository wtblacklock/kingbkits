import type { Metadata } from "next";
import { SITE } from "@/data/site";

/**
 * Keeps og:* and twitter:* in sync for a page. Next.js does not fall back to
 * openGraph.title/description for twitter, so setting them separately here
 * is what previously caused shared links to show the generic site title.
 */
export function pageMetadata({
  title,
  description,
  path,
  image,
  type = "website",
}: {
  title: string;
  description: string;
  path: string;
  image?: string;
  type?: "website" | "article";
}): Metadata {
  const socialTitle = `${title} · ${SITE.name}`;
  const images = [{ url: image ?? SITE.ogImage }];
  return {
    title,
    description,
    alternates: { canonical: path },
    openGraph: { type, url: path, title: socialTitle, description, images },
    twitter: { card: "summary_large_image", title: socialTitle, description, images },
  };
}
