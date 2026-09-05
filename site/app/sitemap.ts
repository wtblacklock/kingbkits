import type { MetadataRoute } from "next";
import { KITS } from "@/data/kits";
import { getGuideSlugs } from "@/lib/guides";
import { SITE } from "@/data/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const staticRoutes = ["", "/about", "/guides"].map((route) => ({
    url: `${SITE.url}${route}`,
    changeFrequency: "monthly" as const,
    priority: route === "" ? 1 : 0.6,
  }));

  const kitRoutes = KITS.map((kit) => ({
    url: `${SITE.url}/kits/${kit.slug}`,
    changeFrequency: "monthly" as const,
    priority: 0.9,
  }));

  const guideRoutes = getGuideSlugs().map((slug) => ({
    url: `${SITE.url}/guides/${slug}`,
    changeFrequency: "yearly" as const,
    priority: 0.5,
  }));

  return [...staticRoutes, ...kitRoutes, ...guideRoutes];
}
