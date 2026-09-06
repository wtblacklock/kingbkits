const SIZES = {
  sm: "text-lg",
  md: "text-2xl",
  lg: "text-4xl sm:text-5xl",
} as const;

/**
 * Pure type-treatment wordmark, "KingBKits" as one solid word. "Kits"
 * carries an animated yellow highlighter underline instead of sitting
 * apart as its own chip, so it reads as one mark, not two.
 */
export function Badge({ size = "md" }: { size?: keyof typeof SIZES }) {
  return (
    <span className={`wordmark text-ink ${SIZES[size]}`} aria-label="KingBKits">
      KingB<span className="wordmark__kits">Kits</span>
    </span>
  );
}
