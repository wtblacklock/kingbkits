import type { Metadata } from "next";
import { Container } from "@/components/Container";
import { EtsyButton } from "@/components/EtsyButton";

export const metadata: Metadata = {
  title: "About",
  description: "The idea behind KingBKits — printable tasting-party kits built around three real budget tiers.",
};

export default function AboutPage() {
  return (
    <Container className="prose-guide py-16">
      <span className="text-xs font-bold uppercase tracking-wide text-ink-faint">About</span>
      <h1 className="mt-2 text-4xl font-light text-ink">Party planning is the part people skip.</h1>
      <div className="mt-6 max-w-2xl text-lg text-ink-body">
        <p>
          KingBKits started from a simple frustration: pairing nights are fun to host and miserable
          to plan. What do you actually buy? How much? What do you say to a table of six people who
          don&apos;t know a Speyside from a Highland pour?
        </p>
        <p>
          Every kit answers those questions with real, named products at three budget tiers —
          Newbie, Casual, Aficionado — so shopping takes minutes instead of research. Print the
          8-page guide, hand out the tasting cards, and the night runs itself.
        </p>
        <p>
          Everything is an instant-download PDF, plus an editable Canva invitation and a
          ready-to-copy Google Form for RSVPs. Nothing physical ships, and nothing about the setup
          requires you to already know what you&apos;re doing.
        </p>
      </div>
      <div className="mt-10">
        <EtsyButton campaign="about_page">Shop the Kits on Etsy</EtsyButton>
      </div>
    </Container>
  );
}
