const TAGLINE = "PICK A TIER · BUY THE BOTTLES · RUN THE NIGHT";

export function MarqueeBar() {
  const track = `${TAGLINE} · `.repeat(4);
  return (
    <div className="foot-marquee overflow-hidden border-b-2 border-ink bg-ink py-2">
      <div className="foot-marquee__track" aria-hidden="true">
        <span className="font-wordmark text-sm tracking-[0.08em] text-paper">{track}</span>
        <span className="font-wordmark text-sm tracking-[0.08em] text-paper">{track}</span>
      </div>
      <p className="sr-only">KingBKits. Pick a tier, buy the bottles, run the night.</p>
    </div>
  );
}
