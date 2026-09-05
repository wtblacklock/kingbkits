import type { Metadata } from "next";
import Link from "next/link";
import { Container } from "@/components/Container";
import { getAllGuides } from "@/lib/guides";

export const metadata: Metadata = {
  title: "Guides",
  description: "Reference guides on cigars, tequila & mezcal, and candy pairings with whisky — the same primers built into every KingBKits PDF.",
};

export default function GuidesIndexPage() {
  const guides = getAllGuides();
  const topics = Array.from(new Set(guides.map((g) => g.topic)));

  return (
    <Container className="py-16">
      <span className="text-xs font-bold uppercase tracking-wide text-ink-faint">Reference</span>
      <h1 className="mt-2 text-4xl font-light text-ink">Pairing Guides</h1>
      <p className="mt-4 max-w-2xl text-lg text-ink-body">
        The same primers built into every kit&apos;s PDF, in one place — how the spirit is made, how to
        read a label, and what actually pairs with what. No fluff, nothing dated, just the reference
        material.
      </p>

      <div className="mt-12 space-y-12">
        {topics.map((topic) => (
          <div key={topic}>
            <h2 className="mb-4 border-b border-rule pb-2 text-sm font-bold uppercase tracking-wide text-ink-faint">
              {topic}
            </h2>
            <div className="grid gap-6 sm:grid-cols-2">
              {guides
                .filter((g) => g.topic === topic)
                .map((guide) => (
                  <Link
                    key={guide.slug}
                    href={`/guides/${guide.slug}`}
                    className="block rounded-xl border border-rule bg-paper p-6 transition-shadow hover:shadow-lg"
                  >
                    <h3 className="text-lg font-semibold text-ink">{guide.title}</h3>
                    <p className="mt-2 text-sm text-ink-body">{guide.description}</p>
                    <span className="mt-4 inline-block text-sm font-semibold text-ink underline decoration-gold decoration-2 underline-offset-4">
                      Read the guide →
                    </span>
                  </Link>
                ))}
            </div>
          </div>
        ))}
      </div>
    </Container>
  );
}
