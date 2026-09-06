import Image from "next/image";
import Link from "next/link";
import { Container } from "@/components/Container";
import { Reveal } from "@/components/Reveal";
import { getAllGuides } from "@/lib/guides";
import { pageMetadata } from "@/lib/metadata";

export const metadata = pageMetadata({
  title: "Guides",
  description:
    "Reference guides on cigars, tequila and mezcal, and candy pairings with whisky, plus party-planning logistics: how much to buy, how to set up a tasting, and how to run the night.",
  path: "/guides",
});

export default function GuidesIndexPage() {
  const guides = getAllGuides();
  const topics = Array.from(new Set(guides.map((g) => g.topic)));

  return (
    <Container className="max-w-[70ch] py-16">
      <Reveal>
        <p className="text-lg leading-relaxed text-ink-2">
          The primers built into every kit&apos;s PDF, plus the party-planning logistics that come
          before you even open one: how much to buy, how to set the table, and how to run the
          night. No fluff, nothing dated, just the reference material.
        </p>
      </Reveal>

      <div className="mt-14 flex flex-col">
        {topics.map((topic, ti) => (
          <Reveal key={topic} delay={ti * 60}>
            <div className="border-t border-rule py-8 first:border-t-0">
              <div className="mb-6 text-xs font-bold uppercase tracking-[0.08em] text-ink-faint">{topic}</div>
              <div className="flex flex-col gap-8">
                {guides
                  .filter((g) => g.topic === topic)
                  .map((guide) => (
                    <Link
                      key={guide.slug}
                      href={`/guides/${guide.slug}`}
                      className="group flex gap-5"
                    >
                      {guide.image && (
                        <div className="relative aspect-square w-24 flex-none overflow-hidden rounded-card sm:w-28">
                          <Image
                            src={guide.image}
                            alt={guide.imageAlt ?? ""}
                            fill
                            sizes="112px"
                            className="object-cover transition-transform duration-200 group-hover:scale-105"
                          />
                        </div>
                      )}
                      <div>
                        <h2 className="font-display text-xl text-ink">{guide.title}</h2>
                        <p className="mt-1 text-ink-2">{guide.description}</p>
                        <span className="mt-2 inline-block text-sm font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4">
                          Read the guide →
                        </span>
                      </div>
                    </Link>
                  ))}
              </div>
            </div>
          </Reveal>
        ))}
      </div>
    </Container>
  );
}
