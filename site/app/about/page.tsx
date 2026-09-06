import { Container } from "@/components/Container";
import { EtsyButton } from "@/components/EtsyButton";
import { Reveal } from "@/components/Reveal";
import { pageMetadata } from "@/lib/metadata";

export const metadata = pageMetadata({
  title: "About",
  description: "The idea behind KingBKits: printable tasting-party kits built around three real budget tiers.",
  path: "/about",
});

export default function AboutPage() {
  return (
    <>
      <Container className="max-w-[65ch] py-16 sm:py-20">
      <Reveal>
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.08em] text-ink-faint">About</p>
          <h1 className="mt-3 font-display text-3xl italic leading-snug text-ink sm:text-4xl">
            Party planning is the part people skip.
          </h1>
          <p className="mt-6 text-lg leading-relaxed text-ink-2">
            KingBKits started from a simple frustration: pairing nights are fun to host and miserable
            to plan. What do you actually buy? How much? What do you say to a table of six people who
            don&apos;t know a Speyside from a Highland pour?
          </p>
        </div>
      </Reveal>

      <Reveal>
        <div>
          <h2 className="mt-14 font-display text-2xl text-ink">What we do</h2>
          <div className="prose-guide mt-4">
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
        </div>
      </Reveal>

      <Reveal>
        <div>
          <h2 className="mt-14 font-display text-2xl text-ink">What we don&apos;t do</h2>
          <ul className="prose-guide mt-4 list-disc pl-5">
            <li>Recommend a bottle we haven&apos;t actually priced and checked against the tier it&apos;s in.</li>
            <li>Pad a kit with filler pages to make the page count look bigger.</li>
            <li>Pretend a printable PDF is something it isn&apos;t: nothing here ships, and nothing here is a substitute for reading the label on what you pour.</li>
            <li>Sell a physical product, run a subscription, or upsell inside the PDF itself.</li>
          </ul>
        </div>
      </Reveal>

      <Reveal>
        <div>
          <h2 className="mt-14 font-display text-2xl text-ink">How we build it</h2>
          <div className="prose-guide mt-4">
            <p>
              Every pairing has a stated reason, not a vibe. Coconut candy against bourbon works
              because coconut carries the same lactone compounds American oak donates to the barrel.
              Caramel and whisky share a browning reaction. That kind of reasoning shows up in every
              kit&apos;s primer, not just the flavor wheel, so a Newbie-tier guest can repeat the logic
              back by the second pairing.
            </p>
            <p>
              Bottle and budget recommendations get checked against real, current pricing at three
              tiers before a kit ships, not pulled from a generic &ldquo;top shelf vs. bottom
              shelf&rdquo; assumption.
            </p>
          </div>
        </div>
      </Reveal>

      <Reveal>
        <div>
          <h2 className="mt-14 font-display text-2xl text-ink">How we make money</h2>
          <div className="prose-guide mt-4">
            <p>
              Every kit is sold once, on Etsy, as an instant digital download. No affiliate links, no
              subscription, no ads inside the PDF. If a kit recommends a bottle, it&apos;s because the
              bottle earned the spot, not because a link pays a commission.
            </p>
          </div>
        </div>
      </Reveal>

      <Reveal>
        <div>
          <h2 className="mt-14 font-display text-2xl text-ink">Who&apos;s behind it</h2>
          <div className="mt-4 flex items-start gap-4">
            <div className="flex h-12 w-12 flex-none items-center justify-center rounded-full bg-ink font-display text-lg text-paper">
              WB
            </div>
            <div className="prose-guide">
              <p>
                KingBKits is run by <strong>William Blacklock</strong>, a designer and creative
                technologist based in Austin, TX. His design and brand work lives at{" "}
                <a
                  href="https://wblacklock.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4"
                >
                  wblacklock.com
                </a>
                . He also builds{" "}
                <a
                  href="https://trailsteadguide.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4"
                >
                  Trailstead Guide
                </a>
                , a structured camping planner built on the same idea as this shop: most people
                don&apos;t need more reading, they need a plan they can run tonight.
              </p>
            </div>
          </div>
        </div>
      </Reveal>
      </Container>

      <Reveal>
        <section className="bg-accent py-16 sm:py-20">
          <Container className="flex flex-col items-center gap-5 text-center">
            <h2 className="font-display text-3xl text-accent-ink sm:text-4xl">Ready to host?</h2>
            <p className="max-w-md text-accent-ink/80">
              Every kit is an instant download on Etsy, invitation template included.
            </p>
            <EtsyButton campaign="about_page" content="bottom_cta">
              Shop all kits on Etsy
            </EtsyButton>
          </Container>
        </section>
      </Reveal>
    </>
  );
}
