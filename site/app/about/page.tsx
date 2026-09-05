import type { Metadata } from "next";
import { Container } from "@/components/Container";
import { EtsyButton } from "@/components/EtsyButton";

export const metadata: Metadata = {
  title: "About",
  description: "The idea behind KingBKits: printable tasting-party kits built around three real budget tiers.",
  alternates: { canonical: "/about" },
};

export default function AboutPage() {
  return (
    <Container className="max-w-[65ch] py-16">
      <p className="text-lg leading-relaxed text-ink-2">
        Party planning is the part people skip. KingBKits started from a simple frustration:
        pairing nights are fun to host and miserable to plan. What do you actually buy? How much?
        What do you say to a table of six people who don&apos;t know a Speyside from a Highland
        pour?
      </p>

      <div className="prose-guide mt-8">
        <p>
          Every kit answers those questions with real, named products at three budget tiers:
          Newbie, Casual, Aficionado, so shopping takes minutes instead of research. Print the
          guide, hand out the tasting cards, and the night runs itself.
        </p>
        <p>
          Everything is an instant-download PDF, plus an editable Canva invitation and a
          ready-to-copy Google Form for RSVPs. Nothing physical ships, and nothing about the setup
          requires you to already know what you&apos;re doing.
        </p>
      </div>

      <p className="mt-10 border-t border-rule pt-8">
        <EtsyButton campaign="about_page">Shop the kits on Etsy</EtsyButton>
      </p>
    </Container>
  );
}
