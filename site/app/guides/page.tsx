import type { Metadata } from "next";
import Link from "next/link";
import { Container } from "@/components/Container";
import { getAllGuides } from "@/lib/guides";

export const metadata: Metadata = {
  title: "Guides",
  description:
    "Reference guides on cigars, tequila and mezcal, and candy pairings with whisky, plus party-planning logistics: how much to buy, how to set up a tasting, and how to run the night.",
  alternates: { canonical: "/guides" },
};

export default function GuidesIndexPage() {
  const guides = getAllGuides();
  const topics = Array.from(new Set(guides.map((g) => g.topic)));

  return (
    <Container className="max-w-[65ch] py-16">
      <p className="text-lg leading-relaxed text-ink-2">
        The primers built into every kit&apos;s PDF, plus the party-planning logistics that come
        before you even open one: how much to buy, how to set the table, and how to run the
        night. No fluff, nothing dated, just the reference material.
      </p>

      <div className="mt-14 flex flex-col">
        {topics.map((topic) => (
          <div key={topic} className="border-t border-rule py-8 first:border-t-0">
            <div className="mb-4 text-xs font-bold uppercase tracking-[0.08em] text-ink-faint">{topic}</div>
            <div className="flex flex-col gap-6">
              {guides
                .filter((g) => g.topic === topic)
                .map((guide) => (
                  <div key={guide.slug}>
                    <h2 className="font-display text-xl text-ink">{guide.title}</h2>
                    <p className="mt-1 text-ink-2">{guide.description}</p>
                    <Link
                      href={`/guides/${guide.slug}`}
                      className="mt-2 inline-block text-sm font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4"
                    >
                      Read the guide →
                    </Link>
                  </div>
                ))}
            </div>
          </div>
        ))}
      </div>
    </Container>
  );
}
