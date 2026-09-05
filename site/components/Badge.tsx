const SIZES = {
  sm: {
    wrap: "px-2 py-1 rounded-md gap-0",
    l1: "text-[0.68rem]",
    l2: "text-[0.5rem]",
  },
  md: {
    wrap: "px-3 py-2 rounded-lg gap-0",
    l1: "text-base",
    l2: "text-xs",
  },
  lg: {
    wrap: "px-5 py-4 rounded-xl gap-0",
    l1: "text-3xl",
    l2: "text-lg",
  },
} as const;

export function Badge({ size = "md" }: { size?: keyof typeof SIZES }) {
  const s = SIZES[size];
  return (
    <span
      className={`inline-flex w-fit flex-none flex-col items-center justify-center bg-black font-display leading-[0.92] ${s.wrap}`}
      aria-label="KingBKits"
    >
      <span className={`text-gold tracking-tight ${s.l1}`}>KINGB</span>
      <span className={`mt-px text-white tracking-wide ${s.l2}`}>KITS</span>
    </span>
  );
}
