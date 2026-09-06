const SIZES = {
  sm: "text-lg",
  md: "text-2xl",
  lg: "text-4xl sm:text-5xl",
} as const;

/**
 * Pure type-treatment wordmark. No logo image, no icon: "KingB Kits" set
 * as one unified mark in the brand display face, with "Kits" carrying a
 * yellow highlighter underline instead of sitting apart as its own chip.
 */
export function Badge({ size = "md" }: { size?: keyof typeof SIZES }) {
  return (
    <span className={`wordmark text-ink ${SIZES[size]}`} aria-label="KingB Kits">
      KingB&nbsp;<span className="wordmark__kits">Kits</span>
    </span>
  );
}
