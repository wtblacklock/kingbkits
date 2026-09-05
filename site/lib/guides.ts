import fs from "fs";
import path from "path";
import matter from "gray-matter";

const GUIDES_DIR = path.join(process.cwd(), "content/guides");

export interface GuideFrontmatter {
  title: string;
  description: string;
  topic: string;
  relatedKit?: string;
}

export interface GuideSummary extends GuideFrontmatter {
  slug: string;
}

export function getGuideSlugs(): string[] {
  return fs
    .readdirSync(GUIDES_DIR)
    .filter((f) => f.endsWith(".mdx"))
    .map((f) => f.replace(/\.mdx$/, ""));
}

export function getGuide(slug: string): GuideSummary & { content: string } {
  const file = fs.readFileSync(path.join(GUIDES_DIR, `${slug}.mdx`), "utf8");
  const { data, content } = matter(file);
  return { slug, content, ...(data as GuideFrontmatter) };
}

export function getAllGuides(): GuideSummary[] {
  return getGuideSlugs()
    .map((slug) => {
      const { content, ...rest } = getGuide(slug);
      void content;
      return rest;
    })
    .sort((a, b) => a.topic.localeCompare(b.topic));
}
