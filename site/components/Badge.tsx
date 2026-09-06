const SIZES = {
  sm: { text: "text-lg", crown: 14 },
  md: { text: "text-2xl", crown: 20 },
  lg: { text: "text-4xl sm:text-5xl", crown: 34 },
} as const;

function Crown({ size }: { size: number }) {
  return (
    <svg
      aria-hidden="true"
      width={size}
      height={size * 0.72}
      viewBox="0 0 24 17"
      fill="none"
      className="wordmark__crown"
    >
      <path
        d="M1 16 L1.8 6.5 L7 11 L12 2 L17 11 L22.2 6.5 L23 16 Z"
        fill="currentColor"
        className="text-accent"
        stroke="currentColor"
        strokeWidth="1"
        strokeLinejoin="round"
      />
    </svg>
  );
}

/**
 * Pure type-treatment wordmark. No logo image: bold display face, a small
 * hand-drawn crown accent standing in for the mascot, "Kits" on a yellow
 * highlighter chip for a bit of party energy.
 */
export function Badge({ size = "md" }: { size?: keyof typeof SIZES }) {
  const s = SIZES[size];
  return (
    <span className={`wordmark text-ink ${s.text}`} aria-label="KingB Kits">
      <Crown size={s.crown} />
      KingB
      <span className="ml-1 -rotate-2 rounded bg-accent px-1.5 text-accent-ink">Kits</span>
    </span>
  );
}
