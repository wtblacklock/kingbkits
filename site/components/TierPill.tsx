const CLASSES: Record<string, string> = {
  newbie: "bg-tier-newbie",
  casual: "bg-tier-casual",
  aficionado: "bg-tier-aficionado",
};

export function TierPill({ tier, tierClass }: { tier: string; tierClass: string }) {
  return (
    <span
      className={`inline-block rounded-full px-3 py-1 text-xs font-bold text-black ${CLASSES[tierClass] ?? "bg-chip"}`}
    >
      {tier}
    </span>
  );
}
