import type { MetadataRoute } from "next";
import { headers } from "next/headers";
import { SITE } from "@/data/site";

const CANONICAL_HOSTS = new Set([SITE.domain, `www.${SITE.domain}`]);

export default async function robots(): Promise<MetadataRoute.Robots> {
  const host = (await headers()).get("host") ?? "";

  if (!CANONICAL_HOSTS.has(host)) {
    return { rules: { userAgent: "*", disallow: "/" } };
  }

  return {
    rules: { userAgent: "*", allow: "/" },
    sitemap: `${SITE.url}/sitemap.xml`,
  };
}
